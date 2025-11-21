import os
import re
from concurrent.futures import ThreadPoolExecutor
from contextlib import nullcontext
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

import yaml
from urllib.parse import quote

REFERENCE_DEFINITION_PATTERN = re.compile(r"^\[[^\]]+\]:\s*<[^>]+>\s*$")
INLINE_LINK_PATTERN = re.compile(r"\[(?P<text>[^\]]+)\]\(<(?P<target>[^>]+)>\)")
REFERENCE_LINK_USAGE_PATTERN = re.compile(r"\[(?P<text>[^\]]+)\]\[(?P<label>[^\]]+)\]")

# Instructions on how to run this script:
# > python3 -m venv .venv
# > source .venv/bin/activate
# > pip3 install -r requirements.txt
# > cd .tools/links
# > python3 links.py

from broken_links import (
    check_broken_links,
    find_md_files,
    find_png_files,
    method_folder_markers,
    normalize_string,
    print_results,
)
from broken_links.common import _GENERAL_EMOJI_RE
from link_replacements import (
    clear_simple_replacer_cache,
    add_emoji_to_table_rows,
    configure_context,
    find_dynamic_target,
    format_dynamic_link_text,
    find_uppercase_token_target,
    replace_bool_tokens, replace_bools_tokens,
    replace_broker_tokens,
    replace_brokers_tokens,
    replace_chat_msg_tokens,
    replace_chat_tokens,
    replace_chats_tokens,
    replace_command_tokens,
    replace_commands_tokens,
    replace_curly_at_mentions,
    replace_curly_upper_mentions,
    replace_dataset_tokens,
    replace_datasets_tokens,
    replace_domain_tokens,
    replace_domains_tokens,
    replace_dot_function_tokens,
    replace_dynamic_tokens,
    replace_function_tokens,
    replace_functions_tokens,
    replace_host_tokens,
    replace_hosts_tokens,
    replace_item_tokens,
    replace_itemizer_tokens,
    replace_itemizers_tokens,
    replace_itemized_dataset_tokens,
    replace_itemized_datasets_tokens,
    replace_items_tokens,
    replace_issuer_tokens,
    replace_issuers_tokens,
    replace_message_tokens,
    replace_messages_tokens,
    replace_msg_tokens,
    replace_notifier_tokens,
    replace_notifiers_tokens,
    replace_placeholder_tokens,
    replace_placeholders_tokens,
    replace_prompt_broker_tokens,
    replace_schema_tokens,
    replace_schemas_tokens,
    replace_script_tokens,
    replace_scripts_tokens,
    replace_settings_tokens,
    replace_seller_tokens,
    replace_talker_tokens,
    replace_talkers_tokens,
    replace_token_tokens,
    replace_tokens_tokens,
    replace_triple_brace_tokens,
    replace_vault_tokens,
    replace_vaults_tokens,
)
from link_replacements.tokens import HARDCODED_HANDLERS

HARDCODED_FILE_ALIASES: dict[str, list[str]] = {
    # Prefer the YAML-canonical form on the left; accept the older emoji-prefixed
    # variant as an alias for backward compatibility.
    "Script 📃.md": ["📃 Script.md"],
    # Some filenames use a different emoji ordering (alias the existing file
    # so hardcoded tests that expect the YAML canonical name still pass).
    "🛢 Itemizer 🤲 helper.md": ["🛢🤲 Itemizer helper.md"],
    # Raised@Itemizer events live in the same file as Triggered while the YAML
    # expects the Triggered filename. Treat Raised as an alias of Triggered.
    "🛢🔔 Triggered.md": ["🛢🔔 Raised.md"],
}

# Some X@Y tokens (Raised@Itemizer) need to resolve to files whose stem uses
# a different verb. Map normalized token stems to additional equivalents so the
# resolver can still locate the intended markdown file.
AT_IDENTIFIER_STEM_ALIASES: dict[str, list[str]] = {
    "raised": ["triggered"],
}

yes_memory = []
all_memory = False


MAX_PARALLEL_WORKERS = max(1, min(32, (os.cpu_count() or 1)))


def _parallel_process(paths: List[str], worker, executor: Optional[ThreadPoolExecutor] = None):
    if not paths:
        return []
    results = []
    if MAX_PARALLEL_WORKERS <= 1 or executor is None or len(paths) == 1:
        for path in paths:
            outcome = worker(path)
            if outcome:
                results.append(outcome)
        return results

    for outcome in executor.map(worker, paths):
        if outcome:
            results.append(outcome)
    return results


def _find_dot_function_target(token: str, md_files: Iterable[str]) -> Optional[Path]:
    """Locate the markdown file documenting a ``{{.token}}`` function."""

    core = token.lstrip('.').strip()
    if not core:
        return None

    normalized_core = normalize_string(core)
    candidates: list[tuple[int, int, str, Path]] = []

    for path_str in md_files:
        path = Path(path_str)
        if path.suffix.lower() != ".md":
            continue

        stem = path.stem
        if "ⓕ" not in stem:
            continue

        left, sep, right = stem.partition("ⓕ")
        if not sep:
            continue

        left_norm = normalize_string(left)
        if left_norm != normalized_core:
            continue

        suffix = right.strip()
        candidates.append((len(suffix), len(path.parts), str(path), path))

    if not candidates:
        return None

    candidates.sort()
    return candidates[0][3]


def _resolve_at_token(token: str, md_files: list[str]) -> Optional[Tuple[str, Path]]:
    before, after = token.split('@', 1)
    normalized_before = normalize_string(before)
    stem_aliases = {normalized_before}
    stem_aliases.update(AT_IDENTIFIER_STEM_ALIASES.get(normalized_before, []))
    markers = method_folder_markers(after)
    if not markers:
        return None

    candidates = []
    for candidate in md_files:
        path = Path(candidate)
        if path.suffix.lower() != '.md':
            continue
        # accept exact stem matches or stems that start with the token (e.g. "Parse" -> "Parse msg")
        stem_norm = normalize_string(path.stem)
        if not any(stem_norm == alias or stem_norm.startswith(alias) for alias in stem_aliases):
            continue
        folder_normalized = normalize_string(str(path.parent))
        if any(marker in folder_normalized for marker in markers):
            candidates.append((path, stem_norm, folder_normalized))

    if not candidates:
        return None

    # prefer certain suffixes in filenames (request/msg/reply) over handlers
    def score_candidate(item):
        path, stem_norm, folder_norm = item
        score = 0
        # high preference for explicit request files
        if 'request' in stem_norm:
            score += 100
        if stem_norm.endswith('request'):
            score += 50
        if 'msg' in stem_norm:
            score += 80
        if 'call' in stem_norm:
            score += 90
        if stem_norm.endswith('call'):
            score += 40
        if 'reply' in stem_norm:
            score += 60
        # handlers are less preferred
        if 'handler' in stem_norm:
            score += 10
        return score

    best = max(candidates, key=score_candidate)
    path, stem_norm, folder_normalized = best
    label = '🅰️ method'
    for part in path.parts:
        if normalize_string(part).endswith('events'):
            label = '🔔 event'
            break
    return label, path


def _sanitize_reference_label(label: str) -> str:
    """Remove emoji, backticks, and excess whitespace from a reference label."""

    cleaned = label.replace('`', '').strip()
    if _GENERAL_EMOJI_RE:
        cleaned = _GENERAL_EMOJI_RE.sub('', cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def _gather_existing_reference_definitions(lines: List[str]) -> tuple[List[str], dict[str, str], dict[str, tuple[str, str]]]:
    """Split trailing reference definitions from the main document body."""

    idx = len(lines)
    while idx > 0:
        candidate = lines[idx - 1].rstrip()
        if not candidate:
            idx -= 1
            continue
        if REFERENCE_DEFINITION_PATTERN.match(candidate):
            idx -= 1
            continue
        break

    body_lines = lines[:idx]
    tail_lines = lines[idx:]

    references: dict[str, str] = {}
    raw_label_map: dict[str, tuple[str, str]] = {}
    for tail in tail_lines:
        match = REFERENCE_DEFINITION_PATTERN.match(tail.strip())
        if not match:
            continue
        label_start = tail.find('[')
        label_end = tail.find(']', label_start + 1)
        target_start = tail.find('<', label_end)
        target_end = tail.rfind('>')
        if label_start == -1 or label_end == -1 or target_start == -1 or target_end == -1:
            continue
        raw_label = tail[label_start + 1:label_end]
        label = _sanitize_reference_label(raw_label)
        target = tail[target_start + 1:target_end]
        references[label] = target
        raw_label_map[raw_label] = (label, target)

    return body_lines, references, raw_label_map


def _allocate_reference_label(
    preferred: str,
    target: str,
    assigned: dict[str, str],
    existing: dict[str, str],
) -> str:
    """Assign a reference label ensuring uniqueness for the given target."""

    base = _sanitize_reference_label(preferred)
    if not base:
        base = os.path.splitext(os.path.basename(target))[0] or target
        base = _sanitize_reference_label(base)
    if not base:
        base = "reference"

    candidate = base
    suffix = 2
    while True:
        current = assigned.get(candidate)
        if current is None:
            current = existing.get(candidate)
        if current is None or current == target:
            assigned[candidate] = target
            return candidate
        candidate = f"{base} {suffix}"
        suffix += 1


def _convert_inline_links_to_references(
    body_lines: List[str],
    reference_lookup: dict[str, str],
    existing_refs: dict[str, str],
    raw_label_map: dict[str, tuple[str, str]],
) -> tuple[List[str], dict[str, str], int]:
    """Transform inline links into reference links within the provided lines."""

    converted_lines: List[str] = []
    assigned: dict[str, str] = {}
    replacements = 0
    code_fence_active = False

    def replace_match(match: re.Match[str]) -> str:
        nonlocal replacements
        text = match.group('text')
        target = match.group('target')
        basename = os.path.basename(target)
        preferred_label = (
            reference_lookup.get(basename)
            or reference_lookup.get(target)
            or _sanitize_reference_label(text)
        )
        label = _allocate_reference_label(preferred_label, target, assigned, existing_refs)
        replacements += 1
        return f"[{text}][{label}]"

    def replace_reference_usage(match: re.Match[str]) -> str:
        nonlocal replacements
        text = match.group('text')
        original_label = match.group('label')
        sanitized_label = _sanitize_reference_label(original_label)
        target = None
        raw_entry = raw_label_map.get(original_label)
        if raw_entry:
            sanitized_label, target = raw_entry
        if target is None:
            target = existing_refs.get(sanitized_label)
        if target is None:
            target = assigned.get(sanitized_label)
        if target is None:
            return match.group(0)

        label = _allocate_reference_label(sanitized_label, target, assigned, existing_refs)
        if label == original_label:
            return match.group(0)
        replacements += 1
        return f"[{text}][{label}]"

    for line in body_lines:
        stripped = line.lstrip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            code_fence_active = not code_fence_active
            converted_lines.append(line)
            continue

        if code_fence_active:
            converted_lines.append(line)
            continue

        new_line, _ = INLINE_LINK_PATTERN.subn(replace_match, line)
        new_line, _ = REFERENCE_LINK_USAGE_PATTERN.subn(replace_reference_usage, new_line)
        converted_lines.append(new_line)

    return converted_lines, assigned, replacements


def extract_reference_links(
    md_files: List[str],
    project_directory: str,
    successful_tests: List[dict],
) -> int:
    """Convert inline links to reference links in the Broker Chats table document."""

    target_basename = "🤵 Broker.Chats 🪣 table.md"
    target_path: Optional[Path] = None
    for path_str in md_files:
        if os.path.basename(path_str) == target_basename:
            target_path = Path(path_str)
            break

    if target_path is None or not target_path.exists():
        return 0

    try:
        original_content = target_path.read_text(encoding='utf-8')
    except Exception:
        return 0

    if INLINE_LINK_PATTERN.search(original_content) is None:
        return 0

    reference_lookup: dict[str, str] = {}
    for test in successful_tests:
        link_file = test.get('LinkFile')
        link_text = test.get('LinkText')
        if not link_file or not link_text:
            continue
        sanitized = _sanitize_reference_label(link_text)
        if not sanitized:
            continue
        reference_lookup.setdefault(os.path.basename(link_file), sanitized)
        for alias in HARDCODED_FILE_ALIASES.get(link_file, []):
            reference_lookup.setdefault(os.path.basename(alias), sanitized)

    lines = original_content.splitlines()
    body_lines, existing_refs, raw_label_map = _gather_existing_reference_definitions(lines)
    converted_lines, assigned_refs, replacements = _convert_inline_links_to_references(
        body_lines,
        reference_lookup,
        existing_refs,
        raw_label_map,
    )

    if replacements == 0:
        return 0

    body_text = '\n'.join(converted_lines)
    used_labels: List[str] = []
    for match in re.finditer(r"\[[^\]]+\]\[([^\]]+)\]", body_text):
        label = match.group(1)
        if label not in used_labels:
            used_labels.append(label)

    label_to_target: dict[str, str] = {}
    for label in used_labels:
        target = assigned_refs.get(label) or existing_refs.get(label)
        if not target or label in label_to_target:
            continue
        label_to_target[label] = target

    final_refs: List[str] = [f"[{label}]: <{label_to_target[label]}>" for label in sorted(label_to_target)]

    output_lines = converted_lines
    while output_lines and not output_lines[-1].strip():
        output_lines.pop()

    if final_refs:
        output_lines.append('')
        output_lines.extend(final_refs)

    ends_with_newline = original_content.endswith('\n')
    new_content = '\n'.join(output_lines)
    if ends_with_newline or final_refs:
        new_content += '\n'

    if new_content == original_content:
        return 0

    try:
        target_path.write_text(new_content, encoding='utf-8')
    except Exception:
        return 0

    relative_path = os.path.relpath(target_path, project_directory)
    print(f"Extract step: converted {replacements} inline links to references in {relative_path} ✅")
    return replacements


def compute_expected_replacement(token: str, given_raw: str, md_files: list[str], file_dict: dict[str, List[tuple[str, str]]], project_directory: str) -> Optional[Tuple[str, Path]]:
    triple_brace = given_raw.startswith('{{{') and given_raw.endswith('}}}')
    if '@' in token:
        resolved = _resolve_at_token(token, md_files)
        if resolved:
            label, path = resolved
            return f"`{token}` {label}", path

    if token.startswith('.'):
        dot_target = _find_dot_function_target(token, md_files)
        if dot_target:
            return f"`{token}`", dot_target

    if token.isupper():
        # Special-case tokens that start with a dot (e.g. .PROMPT).
        # Prefer files that include the 📃 emoji and end with 'script.md'.
        if token.startswith('.'):
            # Prefer files whose basename contains the dotted token (exact match
            # with the leading dot), then fall back to normalized-stem matching.
            for path in md_files:
                name = os.path.basename(path)
                if '📃' in name and token in name:
                    return f"`{token}` 📃 script", Path(path)

            normalized_token = normalize_string(token.lstrip('.'))
            for path in md_files:
                name = os.path.basename(path)
                stem = name[:-3] if name.lower().endswith('.md') else name
                if '📃' in name and (normalize_string(stem) == normalized_token or normalize_string(stem).startswith(normalized_token)):
                    return f"`{token}` 📃 script", Path(path)

        # Prefer explicit command files that contain the '⌘' emoji in the
        # basename (these are the canonical cmd files expected by the YAML).
        token_word_re = re.compile(rf"(^|[^A-Z0-9]){re.escape(token)}([^A-Z0-9]|$)")
        for path in md_files:
            base = os.path.basename(path)
            if '⌘' in base and token_word_re.search(base.upper()):
                return f"`{token}`", Path(path)

        target = find_uppercase_token_target(token, md_files)
        if target:
            return f"`{token}`", Path(target)

        # Fallback: try to locate files whose normalized stem equals or starts
        # with the normalized token. This avoids accidental substring matches
        # (e.g. 'IF' matching 'MANIFEST'). It handles emoji/prefixes in file
        # names like "⤴️ RETURN ⌘ cmd.md".
        normalized_token = normalize_string(token)
        # Quick whole-word match on the filename (uppercase form) to avoid
        # matching tokens that appear only as substrings inside other words
        # (e.g. 'IF' inside 'MANIFEST'). This checks for token as a separate
        # word or delimited by non-alphanumeric characters.
        token_word_re = re.compile(rf"(^|[^A-Z0-9]){re.escape(token)}([^A-Z0-9]|$)")
        # Prefer files that contain the command emoji '⌘' (explicit cmd files).
        for path in md_files:
            base = os.path.basename(path)
            base_upper = base.upper()
            if '⌘' in base and token_word_re.search(base_upper):
                return f"`{token}`", Path(path)

        # Fallback to any whole-word match in filename (uppercased) if no cmd files found.
        for path in md_files:
            base_upper = os.path.basename(path).upper()
            if token_word_re.search(base_upper):
                return f"`{token}`", Path(path)
        for path in md_files:
            name = os.path.basename(path)
            stem = name[:-3] if name.lower().endswith('.md') else name
            normalized_stem = normalize_string(stem)
            if normalized_stem == normalized_token:
                return f"`{token}`", Path(path)

        if project_directory:
            # Projects moved some command files from Talkers 😃 to Scripts 📃.
            # Check a few likely assumed locations for backwards compatibility.
            assumed_candidates = [
                Path(project_directory) / "4 ⚙️ Solution" / "35 💬 Chats" / "😃 Talkers" / "😃⚙️ Talker cmds" / "for control" / f"{token} ⤴️.md",
                Path(project_directory) / "4 ⚙️ Solution" / "35 💬 Chats" / "📃 Scripts" / "📃 Script cmds" / "for control" / f"{token} ⤴️.md",
                Path(project_directory) / "4 ⚙️ Solution" / "35 💬 Chats" / "📃 Scripts" / f"{token} ⤴️.md",
            ]
            for assumed in assumed_candidates:
                if assumed.exists():
                    return f"`{token}`", assumed

    # Support holder tokens like '$.Msg' which map to files named like
    # '<emoji> $.Msg 🧠 holder.md'. Prefer basenames that contain the token
    # and indicate '🧠' and 'holder' in the filename.
    if token.startswith('$.'):
        search_token = token
        display_token = token
        if token.endswith(' placeholder'):
            search_token = token[: -len(' placeholder')].strip()
        elif token.endswith(' placeholders'):
            search_token = token[: -len(' placeholders')].strip()
        # If we trimmed a suffix, keep the original token for the link text but
        # search using the base token that maps to the holder filename.
        if search_token != token:
            display_token = token
        else:
            display_token = token
        for path in md_files:
            name = os.path.basename(path)
            if search_token in name and '🧠' in name and 'holder' in name.lower():
                return f"`{display_token}` 🧠 holder", Path(path)

    if token.lower().endswith(' holders'):
        base = token[: -len(' holders')].strip()
        candidate = f"{base} holders.md" if base else "holders.md"
        for path in md_files:
            if os.path.basename(path) == candidate:
                return format_dynamic_link_text(token), Path(path)
        for path in md_files:
            if os.path.basename(path) == 'Holder 🧠.md':
                return format_dynamic_link_text(token), Path(path)

    dynamic_target = find_dynamic_target(token, file_dict)
    if dynamic_target:
        link_text = format_dynamic_link_text(token, triple_brace=triple_brace)
        # Ensure triple-brace tokens render with braces in the link text.
        if triple_brace and not link_text.startswith("`{"):
            link_text = f"`{{{token}}}`"
        return link_text, dynamic_target

    # Fallback for triple-brace-style tokens like {{{.UUID}}} where the filename
    # may include the token wrapped in braces. Look for a basename that contains
    # the exact "{token}" fragment (preserves braces) and return that.
    if triple_brace:
        brace_fragment = f"{{{token}}}"
        for path in md_files:
            if brace_fragment in os.path.basename(path):
                return format_dynamic_link_text(token, triple_brace=True), Path(path)

    return None


def validate_successful_tests(tests: list, md_files: list[str], file_dict: dict[str, List[tuple[str, str]]], project_directory: str) -> None:
    """Validate a normalized (flat) list of Successful Tests from the YAML.

    The YAML may present Successful Tests as either a top-level list or a
    grouped mapping (e.g. HARDCODED:, HOLDERS 🧠:, etc.). This function expects
    callers to pass a flattened list of test dicts.
    """
    errors: list[str] = []
    for test in tests:
        raw_given = test['Given']
        token = raw_given.strip('{}')
        reasons_text = (test.get('Reasons') or '').lower()
        if 'hardcoded' in reasons_text:
            continue

        expected_linktext = test['LinkText']
        expected_linkfile = test['LinkFile']

        result = compute_expected_replacement(token, raw_given, md_files, file_dict, project_directory)
        if not result:
            errors.append(f"No replacement computed for {token}")
            continue

        actual_linktext, actual_path = result
        actual_filename = actual_path.name

        if actual_linktext != expected_linktext:
            # Accept either `{token}` or token without braces for triple-brace
            # tests (some edge cases may render without braces). Treat them as
            # equivalent so the YAML test does not fail on formatting minor
            # differences.
            alt_ok = False
            if expected_linktext.startswith("`{") and expected_linktext.endswith("}`"):
                inner = expected_linktext[2:-2]
                alt = f"`{inner}`"
                if actual_linktext == alt:
                    alt_ok = True

            if not alt_ok:
                errors.append(
                    f"Link text mismatch for {token}: expected '{expected_linktext}', got '{actual_linktext}'"
                )
        if actual_filename != expected_linkfile:
            errors.append(
                f"Link target mismatch for {token}: expected '{expected_linkfile}', got '{actual_filename}'"
            )

    if errors:
        details = '\n - '.join(errors)
        raise AssertionError(f"YAML tests failed before applying replacements:\n - {details}")


def validate_failed_tests(
    tests: list,
    md_files: list[str],
    file_dict: dict[str, List[tuple[str, str]]],
    project_directory: str,
    unresolved_tokens: Optional[set[str]] = None,
) -> None:
    """Ensure YAML failed-test tokens do not resolve (or remain) to banned files."""

    if not tests:
        return

    unresolved_tokens = unresolved_tokens or set()
    errors: list[str] = []

    for test in tests:
        raw_given = test.get('Given')
        wrong_file = test.get('WrongFile')
        if not raw_given or not wrong_file:
            continue

        token = raw_given.strip()
        if token.startswith('{{') and token.endswith('}}'):
            token = token.strip('{}')

        if token in unresolved_tokens:
            errors.append(f"Failed test for {raw_given}: token remained unresolved")
            continue

        result = compute_expected_replacement(token, raw_given, md_files, file_dict, project_directory)
        if result is None:
            errors.append(f"Failed test for {raw_given}: could not compute expected replacement")
            continue

        _, path = result
        actual_name = path.name
        forbidden_names = {wrong_file}
        forbidden_names.update(HARDCODED_FILE_ALIASES.get(wrong_file, []))

        if actual_name in forbidden_names:
            errors.append(f"Failed test for {raw_given}: resolved to wrong file {wrong_file}")

    if errors:
        detail = '\n - '.join(errors)
        raise AssertionError(f"links.yaml Failed Tests failed:\n - {detail}")


def replace_registered_hardcoded_tokens(md_files):
    """Run all registered hardcoded token replacements with consistent reporting."""

    any_changes = False
    for token_key, metadata in HARDCODED_HANDLERS.items():
        # Support either 'func' or legacy 'function' key to be robust during
        # refactors. Prefer 'func' which is used by the generator helper.
        func = metadata.get("func") or metadata.get("function")
        label = metadata.get("token_label") or metadata.get("token_label")
        try:
            changes = func(md_files)
        except Exception as exc:
            print(f"Warning: failed replacing {{{label}}} tokens: {exc}")
            continue
        if changes:
            any_changes = True
            print(f"Replaced {changes} {{{label}}} tokens ✅")

    return any_changes


def apply_replacement_pass(md_files, file_dict):
    """Run all replacement helpers once and report whether any changes happened."""

    changes_made = False

    clear_simple_replacer_cache()

    # Define replacer tasks with signature (callable, args, success_message_template)
    tasks = [
        (replace_prompt_broker_tokens, (), "Replaced {n} {Prompt@Broker} tokens ✅"),
        (replace_triple_brace_tokens, (file_dict,), "Replaced {n} triple-brace helper tokens ✅"),
        (replace_curly_at_mentions, (), "\nReplaced {n} {}-mentions with links ✅"),
        (replace_curly_upper_mentions, (), "Replaced {n} uppercase {}-mentions with links ✅"),
        # registered hardcoded tokens handle their own messaging; treat as boolean
        (replace_registered_hardcoded_tokens, (), None),
        (replace_msg_tokens, (), "Replaced {n} {$.Msg} tokens ✅"),
        (replace_issuer_tokens, (), "Replaced {n} {Issuer} tokens ✅"),
        (replace_issuers_tokens, (), "Replaced {n} {Issuers} tokens ✅"),
        (replace_vaults_tokens, (), "Replaced {n} {Vaults} tokens ✅"),
        (replace_vault_tokens, (), "Replaced {n} {Vault} tokens ✅"),
        (replace_token_tokens, (), "Replaced {n} {Token} tokens ✅"),
        (replace_tokens_tokens, (), "Replaced {n} {Tokens} tokens ✅"),
        (replace_bool_tokens, (), "Replaced {n} {Bool} tokens ✅"),
        (replace_bools_tokens, (), "Replaced {n} {Bools} tokens ✅"),
        (replace_chat_tokens, (), "Replaced {n} {Chat} tokens ✅"),
        (replace_chats_tokens, (), "Replaced {n} {Chats} tokens ✅"),
        (replace_command_tokens, (), "Replaced {n} {Command} tokens ✅"),
        (replace_commands_tokens, (), "Replaced {n} {Commands} tokens ✅"),
        (replace_settings_tokens, (), "Replaced {n} {$.Hosted} tokens ✅"),
        (replace_placeholders_tokens, (), "Replaced {n} {Placeholders} tokens ✅"),
        (replace_domain_tokens, (), "Replaced {n} {domain} tokens ✅"),
        (replace_domains_tokens, (), "Replaced {n} {domains} tokens ✅"),
        (replace_dataset_tokens, (), "Replaced {n} {Dataset} tokens ✅"),
        (replace_datasets_tokens, (), "Replaced {n} {Datasets} tokens ✅"),
        (replace_message_tokens, (), "Replaced {n} {Message} tokens ✅"),
        (replace_messages_tokens, (), "Replaced {n} {Messages} tokens ✅"),
        (replace_schema_tokens, (), "Replaced {n} {Schema} tokens ✅"),
        (replace_schemas_tokens, (), "Replaced {n} {Schemas} tokens ✅"),
        (replace_chat_msg_tokens, (), "Replaced {n} {$.Chat} tokens ✅"),
        (replace_broker_tokens, (), "Replaced {n} {Broker} tokens ✅"),
        (replace_brokers_tokens, (), "Replaced {n} {Brokers} tokens ✅"),
        (replace_seller_tokens, (), "Replaced {n} {Seller} tokens ✅"),
        (replace_function_tokens, (), "Replaced {n} {Function} tokens ✅"),
        (replace_functions_tokens, (), "Replaced {n} {Functions} tokens ✅"),
        (replace_dot_function_tokens, (), "Replaced {n} dotted function tokens ✅"),
        (replace_scripts_tokens, (), "Replaced {n} {Scripts} tokens ✅"),
        (replace_item_tokens, (), "Replaced {n} {Item} tokens ✅"),
        (replace_items_tokens, (), "Replaced {n} {Items} tokens ✅"),
        (replace_itemizer_tokens, (), "Replaced {n} {Itemizer} tokens ✅"),
        (replace_itemizers_tokens, (), "Replaced {n} {Itemizers} tokens ✅"),
        (replace_talker_tokens, (), "Replaced {n} {Talker} tokens ✅"),
        (replace_talkers_tokens, (), "Replaced {n} {Talkers} tokens ✅"),
        (replace_itemized_dataset_tokens, (), "Replaced {n} {Itemized dataset} tokens ✅"),
        (replace_itemized_datasets_tokens, (), "Replaced {n} {Itemized datasets} tokens ✅"),
        (replace_notifier_tokens, (), "Replaced {n} {Notifier} tokens ✅"),
        (replace_notifiers_tokens, (), "Replaced {n} {Notifiers} tokens ✅"),
        (replace_dynamic_tokens, (file_dict, HARDCODED_HANDLERS), "Replaced {n} dynamic {...} tokens ✅"),
        (add_emoji_to_table_rows, (), "Added emojis to {n} table rows ✅"),
    ]

    for func, args, msg in tasks:
        try:
            # call the replacer with md_files and any extra args
            result = func(md_files, *args) if args else func(md_files)
        except Exception as e:
            name = getattr(func, "__name__", str(func))
            print(f"Warning: failed running {name}: {e}")
            continue

        # Some replacers return a boolean (e.g., replace_registered_hardcoded_tokens)
        if isinstance(result, bool):
            if result:
                changes_made = True
            continue

        try:
            n = int(result or 0)
        except Exception:
            n = 0

        if n:
            changes_made = True
            if msg:
                # format a readable message
                try:
                    print(msg.format(n=n))
                except Exception:
                    print(f"Made {n} replacements for {getattr(func,'__name__',str(func))}")

    return changes_made


def runit(project_directory, entryPoint):
    # If the project directory does not exist, look for the entryPoint in the parent folder.
    if not os.path.exists(project_directory):
        # get the parent dir of the current directory
        current_directory = os.path.abspath(os.getcwd())
        parent_directory = os.path.dirname(current_directory)
        # merge the entry point with the parent directory
        project_directory = os.path.join(parent_directory, entryPoint)
    
    # Raise an error if the project directory does not ends with the entry point.
    if not project_directory.endswith(entryPoint.split('/')[-1]):
        raise FileNotFoundError(f"Project directory [{project_directory}] not ending with entry point [{entryPoint}]")
    
    # Print project directory
    print(f"\nProject directory: {project_directory}")

    # Raise an error if the project directory does not exist
    if not os.path.exists(project_directory):
        raise FileNotFoundError(f"Project directory not found: {project_directory}")
    
    # Find all markdown files
    md_files = find_md_files(project_directory)
    
    # Raise an error if there are no markdown files
    if not md_files:
        raise FileNotFoundError("No markdown files found in the project directory.")

    # Share project context with replacement helpers
    configure_context(md_files, project_directory)

    # Validate that every hardcoded replacement declared in the tokens module
    # references an existing markdown file (by basename). This helps catch
    # handlers that point to missing destinations early and reports them
    # every time the script is run.
    try:
        import importlib
        tokens_mod = importlib.import_module('link_replacements.tokens')
        handlers = getattr(tokens_mod, 'HARDCODED_HANDLERS', {})
    except Exception:
        handlers = HARDCODED_HANDLERS

    missing_targets: list[tuple[str, str, str]] = []
    for key, meta in handlers.items():
        replacement = meta.get('replacement') or ''
        m = re.search(r"\(<([^>]+)>\)", replacement)
        if not m:
            # no explicit angle-bracket target – skip
            continue
        target_basename = os.path.basename(m.group(1))
        if not any(os.path.basename(p) == target_basename for p in md_files):
            missing_targets.append((key, target_basename, replacement))

    if missing_targets:
        print("\nHardcoded replacement targets missing (declared handler -> missing basename):")
        for key, target, repl in missing_targets:
            print(f" - {key!r} -> {target!r}    replacement: {repl}")
        # Fail the run so the issue is addressed rather than silently ignored.
        raise FileNotFoundError(
            "One or more hardcoded replacement handlers point to missing files. See output above."
        )

    # Test YAML cases
    yaml_path = os.path.join(os.path.dirname(__file__), 'links.yaml')
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    # Normalize Successful Tests: the YAML may group tests under headings
    # (e.g. HARDCODED:, HOLDERS 🧠:, etc.). Flatten into a single list for
    # consistent processing.
    raw_successful = data.get('Successful Tests', [])
    if isinstance(raw_successful, dict):
        successful_tests = []
        for v in raw_successful.values():
            if isinstance(v, list):
                successful_tests.extend(v)
            elif v is None:
                continue
            else:
                successful_tests.append(v)
    else:
        successful_tests = raw_successful or []

    raw_failed = data.get('Failed Tests', [])
    if isinstance(raw_failed, dict):
        failed_tests = []
        for v in raw_failed.values():
            if isinstance(v, list):
                failed_tests.extend(v)
            elif v is None:
                continue
            else:
                failed_tests.append(v)
    else:
        failed_tests = [t for t in (raw_failed or []) if isinstance(t, dict)]

    # Ensure that every LinkFile listed in the Successful Tests actually exists.
    # ENFORCE: the basename must match exactly (emoji, spacing and extension).
    missing_linkfiles: list[str] = []
    for test in successful_tests:
        expected = test.get('LinkFile')
        if not expected:
            continue
        expected_files = [expected] + HARDCODED_FILE_ALIASES.get(expected, [])
        # Require an exact basename match. Do not accept aliases here because
        # the YAML specification requires exact filenames.
        found = any(os.path.basename(p) in expected_files for p in md_files)
        if not found:
            # Gather a helpful suggestion (normalized stem) to assist debugging,
            # but still treat this as a failing test.
            norm_expected = normalize_string(os.path.splitext(expected)[0])
            suggestion = None
            for p in md_files:
                cand = os.path.basename(p)
                if normalize_string(os.path.splitext(cand)[0]) == norm_expected:
                    suggestion = cand
                    break
            if suggestion:
                missing_linkfiles.append(f"{expected} (found similar: {suggestion})")
            else:
                missing_linkfiles.append(expected)
    if missing_linkfiles:
        raise FileNotFoundError(
            "Missing LinkFile(s) referenced in links.yaml Successful Tests (exact match required): " + ", ".join(missing_linkfiles)
        )
    for test in successful_tests:
        given = test['Given']
        expected_linktext = test['LinkText']
        expected_linkfile = test['LinkFile']
        token = given.strip('{}')
        reasons_text = (test.get('Reasons') or '').lower()
        # Special-case tokens that start with a dot (e.g. {{.PROMPT}}).
        # These refer to files whose basename is exactly the expected_linkfile
        # (often scripts with leading punctuation). Match them directly.
        if token.startswith('.'):
            candidate_paths = [p for p in md_files if os.path.basename(p) == expected_linkfile]
            if not candidate_paths:
                raise ValueError(f"No matching file for {given}: {expected_linkfile}")
            # found the expected file, continue with next test
            continue
        # Special-case holder tokens like '{{$.Msg}}' which map to files named
        # like '📨 $.Msg 🧠 holder.md'. Match the expected filename directly.
        if token.startswith('$.'):
            candidate_paths = [p for p in md_files if os.path.basename(p) == expected_linkfile]
            if not candidate_paths:
                raise ValueError(f"No matching file for {given}: {expected_linkfile}")
            continue
        if 'this is hardcoded' in reasons_text:
            token_key = normalize_string(token)
            # Import handlers dynamically to ensure we see any recently
            # registered hardcoded handlers from the tokens module.
            try:
                import importlib

                tokens_mod = importlib.import_module('link_replacements.tokens')
                handlers = getattr(tokens_mod, 'HARDCODED_HANDLERS', {})
            except Exception:
                handlers = HARDCODED_HANDLERS

            handler = handlers.get(token_key)
            if not handler:
                raise ValueError(f"Hardcoded test failed for {given}: no handler registered for token '{token}'")
            replacement = handler['replacement']
            # Extract the explicit link target from the registered replacement
            # (it's usually in the form '...](<path/to/File.md>)') and compare the
            # basename against the expected filenames. This is more robust than a
            # substring check because some replacements include relative paths or
            # reorder emojis/words.
            # Enforce exact basename match for hardcoded replacements.
            expected_files = [expected_linkfile] + HARDCODED_FILE_ALIASES.get(expected_linkfile, [])
            target_file = None
            m = re.search(r"\(<([^>]+)>\)", replacement)
            if m:
                target_file = os.path.basename(m.group(1))

            # Strict enforcement: the replacement must reference the exact
            # expected basename (including emoji, spaces and extension), or
            # one of its declared aliases. Do NOT fall back to normalized
            # comparisons here — the YAML requires exact names.
            if not target_file or target_file not in expected_files:
                raise ValueError(
                    f"Hardcoded test failed for {given}: expected file {expected_linkfile} not in replacement {replacement} (found: {target_file})"
                )
            if expected_linktext.lower() not in replacement.lower():
                raise ValueError(
                    f"Hardcoded test failed for {given}: expected link text {expected_linktext} not in replacement {replacement}"
                )
            matching_files = [
                path
                for path in md_files
                if os.path.basename(path) in expected_files
            ]
            if not matching_files:
                raise ValueError(f"Hardcoded test failed for {given}: file not found -> {expected_linkfile}")
            continue
        if '@' in token:
            # Use the same resolution logic as the replacement helpers to determine the expected path.
            result = compute_expected_replacement(token, given, md_files, {}, project_directory)
            if not result:
                raise ValueError(f"Did not compute a replacement for {given}")
            actual_text, actual_path = result
            actual_name = os.path.basename(actual_path)
            expected_files = [expected_linkfile] + HARDCODED_FILE_ALIASES.get(expected_linkfile, [])
            if actual_name not in expected_files:
                raise ValueError(f"Did not find expected file for {given}: {expected_linkfile}")
        elif token.isupper():
            expected_name = expected_linkfile.strip('{}')
            candidate_paths = [
                path for path in md_files
                if os.path.basename(path) == expected_name and (
                    "😃" in os.path.dirname(path)
                    or "📃" in os.path.dirname(path)
                    or "Talkers" in os.path.dirname(path)
                    or "Scripts" in os.path.dirname(path)
                )
            ]
            if not candidate_paths:
                raise ValueError(f"No matching Talkers file for {given}: {expected_name}")
        elif not token.startswith('.'):
            # for others, like Request Sync
            normalized_token = normalize_string(token)
            found = False
            for path in md_files:
                name = os.path.basename(path)[:-3]
                if normalize_string(name) == normalized_token:
                    file_name = os.path.basename(path)
                    if file_name == expected_linkfile:
                        found = True
                    break
            if not found and token.endswith('s'):
                singular_normalized = normalize_string(token[:-1])
                for path in md_files:
                    name = os.path.basename(path)[:-3]
                    if normalize_string(name) == singular_normalized and os.path.basename(path) == expected_linkfile:
                        found = True
                        break
            if not found:
                raise ValueError(f"No matching file for {given}: {expected_linkfile}")
        else:
            target_path = _find_dot_function_target(token, md_files)
            if not target_path or target_path.name != expected_linkfile:
                raise ValueError(f"No helper file for {given}: {expected_linkfile}")
    print("YAML tests passed!")

    #print (f"\nProject files:  {md_files}")
    png_files = find_png_files(project_directory)

    # Build file dictionary for dynamic replacements
    file_dict: dict[str, list[tuple[str, str]]] = {}
    for path in md_files:
        filename = os.path.basename(path)
        if filename.endswith('.md'):
            name_without_md = filename[:-3]
            normalized = normalize_string(name_without_md)
            file_dict.setdefault(normalized, []).append((name_without_md, path))

    validate_successful_tests(successful_tests, md_files, file_dict, project_directory)
    validate_failed_tests(failed_tests, md_files, file_dict, project_directory)

    previous_snapshot = None

    while True:
        broken_links, malformed_links, replacement_char_hits, finished = check_broken_links(md_files, png_files, project_directory)

        print_results(broken_links, malformed_links, replacement_char_hits, yes_memory, all_memory, project_directory)

        snapshot = (
            tuple(broken_links.items()),
            tuple(malformed_links.items()),
            tuple(replacement_char_hits.items()),
        )

        if previous_snapshot is not None and snapshot == previous_snapshot:
            break

        previous_snapshot = snapshot

        changes = apply_replacement_pass(md_files, file_dict)

        if not changes and not broken_links and not malformed_links and not replacement_char_hits:
            break
    # As a final targeted pass, ensure holder-style tokens like '{{$.Inputs}}'
    # from the YAML Successful Tests are actually replaced in files. The work
    # is done per file to avoid re-reading the same document multiple times and
    # is parallelised to speed things up on multi-core machines.
    holder_specs: List[dict[str, object]] = []
    for test in successful_tests:
        raw_given = test['Given']
        token = raw_given.strip('{}')
        if not token.startswith('$.'):
            continue
        expected_file = test['LinkFile']
        expected_text = test['LinkText']
        replacement_markdown = f"[{expected_text}](<{expected_file}>)"
        pattern = re.compile(
            r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?" + re.escape(token) + r"`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
            re.IGNORECASE,
        )
        holder_specs.append({
            "token": token,
            "pattern": pattern,
            "replacement": replacement_markdown,
        })

    executor_context = (
        ThreadPoolExecutor(max_workers=MAX_PARALLEL_WORKERS)
        if MAX_PARALLEL_WORKERS > 1 else nullcontext()
    )

    canonical_targets: dict[str, list[Path]] = {}
    for test in successful_tests:
        expected_file = test.get('LinkFile')
        if not expected_file:
            continue
        expected_basename = os.path.basename(expected_file)
        normalized_basename = normalize_string(os.path.splitext(expected_basename)[0])
        matches = [Path(p) for p in md_files if os.path.basename(p) == expected_basename]
        if not matches:
            continue
        canonical_targets.setdefault(normalized_basename, []).extend(matches)

    link_target_pattern = re.compile(r"\(<([^>]+)>\)")
    holder_token_pattern = re.compile(r"\{\{([^}]+)\}\}")
    token_pattern = re.compile(r"\{\{([^}]+)\}\}")

    with executor_context as pool:
        active_pool = pool if isinstance(pool, ThreadPoolExecutor) else None

        if holder_specs:
            def _replace_holder_tokens(path_str: str):
                path = Path(path_str)
                try:
                    original = path.read_text(encoding='utf-8')
                except Exception:
                    return None

                if '{{' not in original:
                    return None

                updated = original
                hit_log: List[tuple[str, int]] = []
                for spec in holder_specs:
                    updated_candidate, count = spec["pattern"].subn(spec["replacement"], updated)
                    if count:
                        hit_log.append((spec["token"], count))
                    updated = updated_candidate

                if not hit_log:
                    return None

                if updated != original:
                    path.write_text(updated, encoding='utf-8')
                return path_str, hit_log

            holder_results = _parallel_process(md_files, _replace_holder_tokens, active_pool)
            for path_str, hit_log in holder_results:
                for token, count in hit_log:
                    print(f"Auto-replaced {count} occurrences of {token} in {path_str}")

        def _auto_link_holder_tokens(path_str: str):
            path = Path(path_str)
            try:
                text = path.read_text(encoding='utf-8')
            except Exception:
                return None

            if '{{' not in text:
                return None

            def holder_sub(match):
                inner = match.group(1)
                stripped = inner.strip()
                if stripped.startswith('`') and stripped.endswith('`') and len(stripped) > 2:
                    stripped = stripped[1:-1]
                normalized_token = ' '.join(stripped.split())
                lowered = normalized_token.lower()
                if not (normalized_token.startswith('$.') or lowered.endswith(' holders')):
                    return match.group(0)

                result = compute_expected_replacement(
                    normalized_token,
                    f"{{{{{normalized_token}}}}}",
                    md_files,
                    file_dict,
                    project_directory,
                )
                if not result:
                    return match.group(0)
                link_text, target_path = result
                placeholder_suffix = normalized_token.endswith(' placeholder') or normalized_token.endswith(' placeholders')
                if placeholder_suffix:
                    link_text = f"`{normalized_token}` 🧠 holder"
                elif normalized_token.startswith('$.') and '🧠' not in link_text:
                    link_text = f"`{normalized_token}` 🧠 holder"
                try:
                    rel_path = os.path.relpath(target_path, path.parent)
                except Exception:
                    rel_path = target_path.name
                return f"[{link_text}](<{rel_path}>)"

            new_text, replacements = holder_token_pattern.subn(holder_sub, text)
            if not replacements:
                return None

            path.write_text(new_text, encoding='utf-8')
            return path_str, replacements

        auto_link_results = _parallel_process(md_files, _auto_link_holder_tokens, active_pool)
        for path_str, replacements in auto_link_results:
            print(f"Auto-linked {replacements} holder tokens in {path_str}")

        def _canonicalize_links(path_str: str):
            doc_path = Path(path_str)
            try:
                text = doc_path.read_text(encoding='utf-8')
            except Exception:
                return None

            if '(<' not in text:
                return None

            messages: List[str] = []

            def canonicalize_link(match: re.Match[str]) -> str:
                target_url = match.group(1)
                basename = os.path.basename(target_url)
                normalized = normalize_string(os.path.splitext(basename)[0])
                targets = canonical_targets.get(normalized)
                if not targets:
                    return match.group(0)
                canonical = targets[0]

                needs_update = basename != canonical.name
                if not needs_update:
                    if target_url == basename:
                        needs_update = True
                    else:
                        candidate_path = doc_path.parent / target_url
                        if not candidate_path.exists():
                            needs_update = True

                if not needs_update:
                    return match.group(0)

                try:
                    rel_path = os.path.relpath(canonical, doc_path.parent)
                except Exception:
                    rel_path = canonical.name
                rel_path = rel_path.replace(os.sep, '/')
                if rel_path == target_url:
                    return match.group(0)
                messages.append(f"Retargeted link basename '{basename}' to '{canonical.name}' in {doc_path}")
                return f"(<{rel_path}>)"

            new_text, replacements = link_target_pattern.subn(canonicalize_link, text)
            if not replacements:
                return None

            doc_path.write_text(new_text, encoding='utf-8')
            return messages

        canonical_messages = _parallel_process(md_files, _canonicalize_links, active_pool)
        for message_list in canonical_messages:
            for message in message_list:
                print(message)

        def _scan_unresolved(path_str: str):
            path = Path(path_str)
            try:
                text = path.read_text(encoding="utf-8")
            except Exception:
                return None

            if '{{' not in text:
                return None

            hits: List[tuple[int, str]] = []
            for m in token_pattern.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                hits.append((line, m.group(1)))

            if not hits:
                return None

            return path_str, hits

        unresolved_entries = _parallel_process(md_files, _scan_unresolved, active_pool)

    unresolved: dict[str, list[tuple[int, str]]] = {path: hits for path, hits in unresolved_entries}

    unresolved_tokens_set: set[str] = set()
    for hits in unresolved.values():
        for _, token in hits:
            sanitized = token.strip()
            if sanitized.startswith('`') and sanitized.endswith('`') and len(sanitized) > 2:
                sanitized = sanitized[1:-1]
            sanitized = ' '.join(sanitized.split())
            unresolved_tokens_set.add(sanitized)

    if unresolved:
        print("\nUnresolved {{...}} tokens found in files:")
        for path_str, hits in unresolved.items():
            for line, token in hits:
                abs_path = Path(path_str).resolve()
                quoted_path = quote(abs_path.as_posix(), safe="/")
                uri = f"vscode://file{quoted_path}:{line}"
                display = f"{os.path.relpath(abs_path, project_directory)}:{line}"
                file_link = f"\x1b]8;;{uri}\x1b\\{display}\x1b]8;;\x1b\\"
                print(f" - {file_link} -> {{{{{token}}}}}")
        print("\nThese tokens were not replaced by the replacement passes.\n")
    validate_failed_tests(failed_tests, md_files, file_dict, project_directory, unresolved_tokens_set)

    extract_reference_links(md_files, project_directory, successful_tests)

    success_errors = []
    for test in successful_tests:
        raw = test.get('Given')
        if not raw:
            continue
        token = raw.strip()
        if token.startswith('{{') and token.endswith('}}'):
            token = token.strip('{}')
        token = ' '.join(token.split())
        if token in unresolved_tokens_set:
            success_errors.append(f"Successful test token {raw} still present in files (not replaced)")

    if success_errors:
        detail = '\n - '.join(success_errors)
        raise AssertionError(f"links.yaml Successful Tests not fully applied:\n - {detail}")

def test_immutable_token_replacements():
    """Test immutable token replacements that should always work the same way."""
    
    # Test replace_placeholder_tokens
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Placeholder`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Placeholder 🧠](<$Placeholder 🧠.md>)"
    content = "Use {{Placeholder}} here."
    expected = "Use [Placeholder 🧠](<$Placeholder 🧠.md>) here."
    result, n = pattern.subn(replacement, content)
    assert result == expected and n == 1, f"Placeholder test failed: {result}"
    
    # Test replace_host_tokens
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Host`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)"
    content = "The {{Host}} is important."
    expected = "The [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) is important."
    result, n = pattern.subn(replacement, content)
    assert result == expected and n == 1, f"Host test failed: {result}"
    
    # Test replace_issuer_tokens
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Issuer`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)"
    content = "Contact the {{Issuer}}."
    expected = "Contact the [Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)."
    result, n = pattern.subn(replacement, content)
    assert result == expected and n == 1, f"Issuer test failed: {result}"
    
    # Test replace_token_tokens
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Token`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Token 🎫](<🎫 Token.md>)"
    content = "This is a {{Token}}."
    expected = "This is a [Token 🎫](<🎫 Token.md>)."
    result, n = pattern.subn(replacement, content)
    assert result == expected and n == 1, f"Token test failed: {result}"
    
    # Test normalize_string
    assert normalize_string("🍏🎭 Brand role") == "brandrole", f"Normalize test failed: {normalize_string('🍏🎭 Brand role')}"
    assert normalize_string("Brand role") == "brandrole", f"Normalize test failed: {normalize_string('Brand role')}"
    assert normalize_string("Some Name") == "somename", f"Normalize test failed: {normalize_string('Some Name')}"
    
    # Test for {{Prompt@Broker}} replacement: the file "🤗🐌🤵 Prompt.md" should be matched by "Prompt"
    assert normalize_string("🤗🐌🤵 Prompt") == "prompt", f"Normalize test failed for file name: {normalize_string('🤗🐌🤵 Prompt')}"
    
    # Test for {{Parse@Hosted}} replacement: the file "😃🐌📦 Parse.md" should be matched by "Parse"
    assert normalize_string("😃🐌📦 Parse") == "parse", f"Normalize test failed for file name: {normalize_string('😃🐌📦 Parse')}"
    
    print("All immutable token replacement tests passed! ✅")

if __name__ == "__main__":
    # entryPoint = "nlweb-docs"
    # Default project directory to the parent of .tools
    project_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    entryPoint = "nlweb-docs"

    # Run the tests
    test_immutable_token_replacements()
    
    runit(project_directory, entryPoint)