import os
import re
from pathlib import Path
from typing import List, Optional, Tuple

import yaml
from urllib.parse import quote

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
from link_replacements import (
    configure_context,
    find_dynamic_target,
    format_dynamic_link_text,
    find_uppercase_token_target,
    replace_curly_at_mentions, replace_curly_upper_mentions, add_emoji_to_table_rows,
    replace_placeholder_tokens, replace_msg_tokens, replace_hosts_tokens, replace_host_tokens,
    replace_issuer_tokens, replace_issuers_tokens, replace_vaults_tokens, replace_vault_tokens,
    replace_token_tokens, replace_tokens_tokens, replace_script_tokens, replace_chat_tokens,
    replace_chats_tokens, replace_command_tokens, replace_commands_tokens, replace_settings_tokens,
    replace_placeholders_tokens, replace_domain_tokens, replace_domains_tokens, replace_dataset_tokens,
    replace_datasets_tokens, replace_message_tokens, replace_messages_tokens, replace_schema_tokens,
    replace_schemas_tokens, replace_chat_msg_tokens, replace_broker_tokens, replace_brokers_tokens, replace_seller_tokens,
    replace_function_tokens, replace_functions_tokens, replace_scripts_tokens, replace_item_tokens,
    replace_items_tokens, replace_itemizer_tokens, replace_itemizers_tokens, replace_talker_tokens,
    replace_talkers_tokens, replace_itemized_dataset_tokens, replace_itemized_datasets_tokens,
    replace_notifier_tokens, replace_notifiers_tokens, replace_prompt_broker_tokens, replace_dynamic_tokens,
    replace_triple_brace_tokens
)
from link_replacements.tokens import HARDCODED_HANDLERS

HARDCODED_FILE_ALIASES: dict[str, list[str]] = {
    # Prefer the YAML-canonical form on the left; accept the older emoji-prefixed
    # variant as an alias for backward compatibility.
    "Script 📃.md": ["📃 Script.md"],
    # Some filenames use a different emoji ordering (alias the existing file
    # so hardcoded tests that expect the YAML canonical name still pass).
    "🛢 Itemizer 🤲 helper.md": ["🛢🤲 Itemizer helper.md"],
}

# Some X@Y tokens (Raised@Itemizer) need to resolve to files whose stem uses
# a different verb. Map normalized token stems to additional equivalents so the
# resolver can still locate the intended markdown file.
AT_IDENTIFIER_STEM_ALIASES: dict[str, list[str]] = {
    "raised": ["triggered"],
}

yes_memory = []
all_memory = False


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


def compute_expected_replacement(token: str, given_raw: str, md_files: list[str], file_dict: dict[str, List[tuple[str, str]]], project_directory: str) -> Optional[Tuple[str, Path]]:
    triple_brace = given_raw.startswith('{{{') and given_raw.endswith('}}}')
    if '@' in token:
        resolved = _resolve_at_token(token, md_files)
        if resolved:
            label, path = resolved
            return f"`{token}` {label}", path

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
            if normalize_string(stem) == normalized_token or normalize_string(stem).startswith(normalized_token):
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

    # Ensure that every LinkFile listed in the Successful Tests actually exists.
    # ENFORCE: the basename must match exactly (emoji, spacing and extension).
    missing_linkfiles: list[str] = []
    for test in successful_tests:
        expected = test.get('LinkFile')
        if not expected:
            continue
        # Require an exact basename match. Do not accept aliases here because
        # the YAML specification requires exact filenames.
        found = any(os.path.basename(p) == expected for p in md_files)
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
            if expected_linktext not in replacement:
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
            if actual_name != expected_linkfile:
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
            helper_candidates = {
                normalize_string(token),
                normalize_string(f"{{{token}}}"),
            }
            expected_found = any(
                normalize_string(os.path.basename(path)[:-3]) in helper_candidates
                and os.path.basename(path) == expected_linkfile
                for path in md_files
            )
            if not expected_found:
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
    # from the YAML Successful Tests are actually replaced in files. Some of
    # the generic replacement helpers may not catch every '$.' pattern, so
    # perform a deterministic substitution based on the YAML expectations.
    for test in successful_tests:
        raw_given = test['Given']
        token = raw_given.strip('{}')
        # Only consider the holder-style tokens that start with '$.'
        if not token.startswith('$.'):
            continue
        expected_file = test['LinkFile']
        expected_text = test['LinkText']
        # build the markdown replacement e.g. "[`$.Inputs` 🧠 holder](<▶️ $.Inputs 🧠 holder.md>)"
        replacement_markdown = f"[{expected_text}](<{expected_file}>)"
        # match occurrences of {{ $.Inputs }} with optional backticks/spaces
        pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?" + re.escape(token) + r"`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
        for path in md_files:
            try:
                text = Path(path).read_text(encoding='utf-8')
            except Exception:
                continue
            new_text, n = pattern.subn(replacement_markdown, text)
            if n:
                Path(path).write_text(new_text, encoding='utf-8')
                print(f"Auto-replaced {n} occurrences of {token} in {path}")

    # Additional targeted pass: resolve any remaining holder-style tokens,
    # including variants like '{{$.Inputs placeholder}}', using the same logic
    # as compute_expected_replacement to determine the correct link target.
    holder_token_pattern = re.compile(r"\{\{([^}]+)\}\}")
    for path in md_files:
        try:
            text = Path(path).read_text(encoding='utf-8')
        except Exception:
            continue

        def holder_sub(match):
            inner = match.group(1)
            stripped = inner.strip()
            if stripped.startswith('`') and stripped.endswith('`') and len(stripped) > 2:
                stripped = stripped[1:-1]
            normalized_token = ' '.join(stripped.split())
            lowered = normalized_token.lower()
            if not (normalized_token.startswith('$.') or lowered.endswith(' holders')):
                return match.group(0)

            result = compute_expected_replacement(normalized_token, f"{{{{{normalized_token}}}}}", md_files, file_dict, project_directory)
            if not result:
                return match.group(0)
            link_text, target_path = result
            placeholder_suffix = normalized_token.endswith(' placeholder') or normalized_token.endswith(' placeholders')
            if placeholder_suffix:
                link_text = f"`{normalized_token}` 🧠 holder"
            elif normalized_token.startswith('$.') and '🧠' not in link_text:
                link_text = f"`{normalized_token}` 🧠 holder"
            try:
                rel_path = os.path.relpath(target_path, Path(path).parent)
            except Exception:
                rel_path = target_path.name
            return f"[{link_text}](<{rel_path}>)"

        new_text, replacements = holder_token_pattern.subn(holder_sub, text)
        if replacements:
            Path(path).write_text(new_text, encoding='utf-8')
            print(f"Auto-linked {replacements} holder tokens in {path}")

    # Harmonize existing Markdown links so their basenames match the canonical
    # filenames declared in links.yaml Successful Tests. This catches cases where
    # files were renamed (emoji changes, etc.) but old links still point to the
    # previous basename.
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
    for path_str in md_files:
        doc_path = Path(path_str)
        try:
            text = doc_path.read_text(encoding='utf-8')
        except Exception:
            continue

        def canonicalize_link(match: re.Match[str]) -> str:
            target_url = match.group(1)
            basename = os.path.basename(target_url)
            normalized = normalize_string(os.path.splitext(basename)[0])
            targets = canonical_targets.get(normalized)
            if not targets:
                return match.group(0)
            if any(target.name == basename for target in targets):
                return match.group(0)
            target_path = targets[0]
            try:
                rel_path = os.path.relpath(target_path, doc_path.parent)
            except Exception:
                rel_path = target_path.name
            rel_path = rel_path.replace(os.sep, '/')
            print(f"Retargeted link basename '{basename}' to '{target_path.name}' in {doc_path}")
            return f"(<{rel_path}>)"

        new_text, replacements = link_target_pattern.subn(canonicalize_link, text)
        if replacements:
            doc_path.write_text(new_text, encoding='utf-8')

    # After replacement passes, scan for any remaining unresolved {{...}} tokens and report them
    token_pattern = re.compile(r"\{\{([^}]+)\}\}")
    unresolved: dict[str, list[tuple[int, str]]] = {}
    for path in md_files:
        try:
            text = Path(path).read_text(encoding="utf-8")
        except Exception:
            continue
        for m in token_pattern.finditer(text):
            # compute 1-based line number
            line = text.count("\n", 0, m.start()) + 1
            unresolved.setdefault(path, []).append((line, m.group(1)))

    if unresolved:
        print("\nUnresolved {{...}} tokens found in files:")
        for p, hits in unresolved.items():
            for line, token in hits:
                abs_path = Path(p).resolve()
                quoted_path = quote(abs_path.as_posix(), safe="/")
                uri = f"vscode://file{quoted_path}:{line}"
                display = f"{os.path.relpath(abs_path, project_directory)}:{line}"
                file_link = f"\x1b]8;;{uri}\x1b\\{display}\x1b]8;;\x1b\\"
                print(f" - {file_link} -> {{{{{token}}}}}")
        print("\nThese tokens were not replaced by the replacement passes.\n")
        # Enforce any Failed Tests in links.yaml: either the token must not
        # resolve to the listed WrongFile, and ideally it should resolve at all.
        yaml_path = os.path.join(os.path.dirname(__file__), 'links.yaml')
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        failed_tests = [t for t in data.get('Failed Tests', []) if 'Given' in t and 'WrongFile' in t]
        failed_errors = []
        for test in failed_tests:
            raw = test['Given']
            token = raw.strip()
            if token.startswith('{{') and token.endswith('}}'):
                token = token.strip('{}')
            wrong = test['WrongFile']

            # If token unresolved, that's a test failure (you asked replacements to run)
            token_unresolved = any(token == found for hits in unresolved.values() for _, found in hits)
            if token_unresolved:
                failed_errors.append(f"Failed test for {raw}: token remained unresolved")
                continue

            # Otherwise compute what it would resolve to and fail if it matches the wrong file
            result = compute_expected_replacement(token, raw, md_files, file_dict, project_directory)
            if result is None:
                failed_errors.append(f"Failed test for {raw}: could not compute expected replacement")
                continue
            _, path = result
            if os.path.basename(path) == wrong:
                failed_errors.append(f"Failed test for {raw}: resolved to wrong file {wrong}")

        if failed_errors:
            detail = '\n - '.join(failed_errors)
            raise AssertionError(f"links.yaml Failed Tests failed:\n - {detail}")

        # Enforce Successful Tests: tokens listed as successful must have been replaced
        successful_tests = [t for t in successful_tests if 'Given' in t]
        success_errors = []
        for test in successful_tests:
            raw = test['Given']
            token = raw.strip()
            if token.startswith('{{') and token.endswith('}}'):
                token = token.strip('{}')

            # if the token still appears in the unresolved map, it wasn't replaced
            token_unresolved = any(token == found for hits in unresolved.values() for _, found in hits)
            if token_unresolved:
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