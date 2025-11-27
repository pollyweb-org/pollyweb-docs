"""Replacement helpers for mention-style tokens."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Iterable, List, Optional

import yaml

from broken_links.common import method_folder_markers, normalize_string
from .context import get_existing_files, get_project_dir
from .patterns import (
    build_project_link_index,
    extract_curly_at_tokens,
    extract_curly_upper_tokens,
    extract_links_text_href,
    pick_matching_link_upper,
)


def _dynamic_normalized_candidates(token: str) -> List[str]:
    candidates: List[str] = []

    parts = token.split("@", 1)
    textual_variants: List[str] = []
    if len(parts) == 2:
        textual_variants.extend(parts[::-1])
    textual_variants.append(token)

    for variant in textual_variants:
        normalized = normalize_string(variant)
        if normalized not in candidates:
            candidates.append(normalized)
        wrapped = normalize_string(f"{{{variant}}}")
        if wrapped not in candidates:
            candidates.append(wrapped)

    if token.endswith("s") and len(token) > 1:
        singular = normalize_string(token[:-1])
        if singular not in candidates:
            candidates.append(singular)

    return candidates


def _score_dynamic_candidate(token: str, name_without_md: str, path: Path) -> tuple[int, int, int, int, str]:
    normalized_token = normalize_string(token)
    normalized_name = normalize_string(name_without_md)
    mismatch_flag = 0 if normalized_token == normalized_name else 1

    preferred_chars = set("._`ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    leading_char = name_without_md[:1]
    leading_penalty = 0 if leading_char and leading_char in preferred_chars else 1

    length_penalty = len(name_without_md)
    depth_penalty = len(path.parts)

    return (
        mismatch_flag,
        leading_penalty,
        length_penalty,
        depth_penalty,
        str(path),
    )


def _select_dynamic_candidate(token: str, candidates: List[tuple[str, str]]) -> Optional[Path]:
    best_path: Optional[Path] = None
    best_score: Optional[tuple[int, int, int, int, str]] = None

    for name_without_md, path_str in candidates:
        path = Path(path_str)
        score = _score_dynamic_candidate(token, name_without_md, path)
        if best_score is None or score < best_score:
            best_score = score
            best_path = path

    return best_path


def find_dynamic_target(token: str, file_dict: dict[str, List[tuple[str, str]]]) -> Optional[Path]:
    normalized_candidates = _dynamic_normalized_candidates(token)
    aggregate: List[tuple[str, str]] = []

    for normalized in normalized_candidates:
        entries = file_dict.get(normalized)
        if entries:
            aggregate.extend(entries)

    if not aggregate:
        # If no direct matches, try common suffix fallbacks. This lets tokens
        # like "TalkerHolders" resolve to "TalkerHolders table" when a
        # dedicated table file exists but the token was used without the
        # "table" suffix.
        for suffix in (" table", " flow", " script", " handler"):
            augmented = token + suffix
            normalized_candidates = _dynamic_normalized_candidates(augmented)
            aggregate_alt: List[tuple[str, str]] = []
            for normalized in normalized_candidates:
                entries = file_dict.get(normalized)
                if entries:
                    aggregate_alt.extend(entries)
            if aggregate_alt:
                return _select_dynamic_candidate(augmented, aggregate_alt)

        return None

    return _select_dynamic_candidate(token, aggregate)


def format_dynamic_link_text(token: str, *, triple_brace: bool = False) -> str:
    if token.lower().endswith(" table"):
        core = token[: -len(" table")].strip()
        if core:
            return f"`{core}` 🪣 table"
    if token.lower().endswith(" flow"):
        core = token[: -len(" flow")].strip()
        if core:
            return f"`{core}` ⏩ flow"
    if token.lower().endswith(" script"):
        core = token[: -len(" script")].strip()
        if core:
            return f"`{core}` 📃 script"
    if token.lower().endswith(" handler"):
        core = token[: -len(" handler")].strip()
        if core:
            return f"`{core}` 📃 handler"
    if token.lower().endswith(" holders"):
        core = token[: -len(" holders")].strip()
        if core:
            return f"{core} 🧠 holders"
    if token.lower().startswith("item "):
        suffix = token[5:].strip()
        if suffix:
            return f"Item 🛢 {suffix}"

    display = f"{{{token}}}" if triple_brace else token
    return f"`{display}`"


def replace_curly_at_mentions(md_files: Iterable[str]) -> int:
    """Replace tokens like ``{{Prompt@Broker}}`` with markdown links."""
    yaml_path = Path(__file__).resolve().parent.parent / "links.yaml"
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    # Normalize Failed Tests keys by stripping surrounding braces so they match
    # the token strings returned by extract_curly_at_tokens (which omit braces).
    failed = {}
    for test in data.get("Failed Tests", []):
        if "WrongFile" in test and "Given" in test:
            given = test["Given"]
            # strip outer braces if present
            key = given.strip()
            if key.startswith("{{") and key.endswith("}}"):
                key = key.strip("{}")
            failed[key] = test["WrongFile"]

    total_replacements = 0
    project_index = build_project_link_index(md_files)
    existing_files = list(get_existing_files()) or list(md_files)

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        tokens = extract_curly_at_tokens(content)
        if not tokens:
            continue

        links_here = extract_links_text_href(content)
        changed = False

        for token in tokens:
            if "@" not in token:
                continue

            before, after = token.split("@", 1)
            normalized_before = normalize_string(before)
            markers = method_folder_markers(after)
            if not markers:
                continue

            found_href: str | None = None
            link_label = "🅰️ method"

            # Collect candidates that match stem equality or start-with semantics
            candidates: List[tuple[Path, int]] = []
            for candidate in existing_files:
                candidate_path = Path(candidate)
                if candidate_path.suffix.lower() != ".md":
                    continue
                stem_norm = normalize_string(candidate_path.stem)
                # accept exact stem matches or stems that start with the token
                if stem_norm != normalized_before and not stem_norm.startswith(normalized_before):
                    continue
                folder_path = normalize_string(str(candidate_path.parent))
                if not any(marker in folder_path for marker in markers):
                    continue

                # scoring: prefer request/msg/reply, deprioritize handler
                score = 0
                if 'request' in stem_norm:
                    score += 100
                if stem_norm.endswith('request'):
                    score += 50
                if 'msg' in stem_norm:
                    score += 80
                if 'reply' in stem_norm:
                    score += 60
                if 'handler' in stem_norm:
                    score += 10

                candidates.append((candidate_path, score))

            if candidates:
                # deterministic selection: highest score, tie-break on path string
                candidates.sort(key=lambda t: (t[1], str(t[0])), reverse=True)
                best_path = candidates[0][0]
                found_href = os.path.relpath(best_path, path.parent)
                if any(normalize_string(part).endswith('events') for part in best_path.parts):
                    link_label = '🔔 event'

            if not found_href:
                continue

            if token in failed and Path(found_href).name == failed[token]:
                raise ValueError(
                    f"Generated wrong file link for {token}: {Path(found_href).name}"
                )

            markdown = f"[`{token}` {link_label}](<{found_href}>)"
            updated = content.replace(f"{{{{{token}}}}}", markdown)
            if updated != content:
                content = updated
                changed = True
                total_replacements += 1

        if changed:
            try:
                path.write_text(content, encoding="utf-8")
            except Exception:
                continue

    return total_replacements


def find_uppercase_token_target(token: str, md_files: Iterable[str]) -> Path | None:
    """Locate a markdown file that likely documents the uppercase token."""

    normalized_token = normalize_string(token)
    candidates: list[Path] = []
    token_word_re = re.compile(rf"(^|[^A-Z0-9]){re.escape(token)}([^A-Z0-9]|$)")

    for candidate in md_files:
        path = Path(candidate)
        if path.suffix.lower() != ".md":
            continue
        normalized_name = normalize_string(path.stem)
        if normalized_name == normalized_token:
            candidates.append(path)
            continue

        base_upper = path.stem.upper()
        if token_word_re.search(base_upper):
            candidates.append(path)

    if not candidates:
        return None

    def priority(path: Path) -> tuple[int, int, int, int, int, str]:
        parts = tuple(path.parts)
        talker_cmd_idx = next((idx for idx, part in enumerate(parts) if "Talker cmds" in part), None)
        scripts_idx = next((idx for idx, part in enumerate(parts) if "Talker scripts" in part), None)
        contains_cmds_folder = any("cmds" in normalize_string(part) for part in parts)
        contains_scripts_folder = any("scripts" in normalize_string(part) for part in parts)
        disallowed_emoji = 1 if any(emoji in path.name for emoji in ("🧪", "📃")) else 0
        script_rank = 0
        if scripts_idx is not None:
            script_rank = 1
            for part in parts:
                if "scripts" in part.lower():
                    for exit_emoji in ("📃", "script"):
                        if exit_emoji in part:
                            script_rank = 0
                            break
                    break
        # Prefer talker command definitions, then scripts, then anything else.
        if talker_cmd_idx is not None:
            bucket = 0
            depth = talker_cmd_idx
        elif scripts_idx is not None:
            bucket = 1
            depth = scripts_idx
        else:
            bucket = 2
            depth = len(parts)
        base_contains_name = normalize_string(path.stem).startswith(normalized_token)
        cmds_penalty = 0 if contains_cmds_folder else 1
        scripts_penalty = 0 if contains_scripts_folder else 1
        return (
            disallowed_emoji,
            bucket,
            cmds_penalty,
            scripts_penalty,
            script_rank,
            0 if base_contains_name else 1,
            str(path),
        )

    best = min(candidates, key=priority)
    return best


def replace_curly_upper_mentions(md_files: Iterable[str]) -> int:
    """Replace all-uppercase tokens like ``{{TOKEN}}`` with existing links."""
    total_replacements = 0
    project_index = build_project_link_index(md_files)
    project_dir = get_project_dir()

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        tokens = extract_curly_upper_tokens(content)
        if not tokens:
            continue

        links_here = extract_links_text_href(content)
        changed = False

        for token in tokens:
            href, base = pick_matching_link_upper(token, links_here)
            if not href:
                href, base = pick_matching_link_upper(token, project_index)

            if not href and token.isupper() and project_dir:
                assumed = Path(project_dir) / "4 ⚙️ Solution" / "35 💬 Chats" / "😃 Talkers" / "😃⚙️ Talker cmds" / "for control" / f"{token} ⤴️.md"
                if assumed.exists():
                    href = os.path.relpath(assumed, path.parent)
                    base = None

            if not href:
                guessed = find_uppercase_token_target(token, md_files)
                if guessed:
                    href = os.path.relpath(guessed, path.parent)
                    base = None

            if not href:
                continue

            final_href = href
            try:
                if base and base != md_file and not href.startswith(("http://", "https://", "mailto:")):
                    absolute_target = Path(base).parent / href
                    final_href = os.path.relpath(absolute_target, path.parent)
            except Exception:
                final_href = href

            markdown = f"[`{token}`](<{final_href}>)"
            updated = content.replace(f"{{{{{token}}}}}", markdown)
            if updated != content:
                content = updated
                changed = True
                total_replacements += 1

        if changed:
            try:
                path.write_text(content, encoding="utf-8")
            except Exception:
                continue

    return total_replacements


def replace_prompt_broker_tokens(md_files: Iterable[str]) -> int:
    """Replace ``{{Prompt@Broker}}`` tokens with a link to the prompt helper."""
    target_file = None
    for candidate in md_files:
        if Path(candidate).name == "🤗🐌🤵 Prompt.md":
            target_file = Path(candidate)
            break

    if not target_file:
        return 0

    total = 0
    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        if "{{Prompt@Broker}}" not in content:
            continue

        rel_path = os.path.relpath(target_file, path.parent)
        replacement = f"[`Prompt@Broker` 🅰️ method](<{rel_path}>)"
        updated = content.replace("{{Prompt@Broker}}", replacement)
        if updated != content:
            try:
                path.write_text(updated, encoding="utf-8")
            except Exception:
                continue
            total += 1

    return total


def replace_dynamic_tokens(
    md_files: Iterable[str],
    file_dict: dict[str, List[tuple[str, str]]],
    hardcoded_handlers: dict[str, dict[str, object]] | None = None,
) -> int:
    """Replace any remaining ``{{...}}`` tokens using normalized filenames.

    Hardcoded handlers keep the highest priority (MAX_POINTS). When the
    hardcoded pass fails to rewrite a token, this fallback re-uses the
    hardcoded link text but recomputes the correct relative path before
    applying a low-priority replacement (MIN_POINTS)."""

    MAX_POINTS = 10_000
    MIN_POINTS = -10_000

    if hardcoded_handlers:
        # Store normalized key -> handler metadata for quick lookup.
        normalized_hardcoded: dict[str, dict[str, object]] = {
            normalize_string(key): meta for key, meta in hardcoded_handlers.items()
        }
    else:
        normalized_hardcoded = {}

    # Cache basenames to absolute paths for computing relative links.
    basename_index: dict[str, Path] = {os.path.basename(path): Path(path) for path in md_files}

    def replacer(match, current_file: Path):
        token = match.group(1)
        normalized_token = normalize_string(token)

        handler_meta = normalized_hardcoded.get(normalized_token)
        if handler_meta:
            token_priority = MAX_POINTS
        else:
            token_priority = MIN_POINTS

        if token_priority == MAX_POINTS:
            replacement = handler_meta.get("replacement", "") if handler_meta else ""
            link_text = None
            target_path = None

            if isinstance(replacement, str):
                m = re.match(r"\[(.+?)\]\(<([^>]+)>\)", replacement)
                if m:
                    link_text = m.group(1)
                    target_basename = os.path.basename(m.group(2))
                    target_path = basename_index.get(target_basename)

            if link_text and target_path:
                try:
                    rel_path = os.path.relpath(target_path, current_file.parent)
                except Exception:
                    rel_path = str(target_path)
                return f"[{link_text}](<{rel_path}>)"

            # Fall back to the registered replacement if we cannot compute a rel path.
            if isinstance(replacement, str) and replacement:
                return replacement

            return match.group(0)

        if token.startswith('$.'):
            return match.group(0)

        target = find_dynamic_target(token, file_dict)
        if target:
            try:
                rel_path = os.path.relpath(target, current_file.parent)
            except Exception:
                rel_path = str(target)
            link_text = format_dynamic_link_text(token)
            return f"[{link_text}](<{rel_path}>)"
        return match.group(0)

    total = 0
    pattern = re.compile(r"\{\{([^}]+)\}\}", re.IGNORECASE)

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        replacements_for_file = 0

        def counting_replacer(m):
            nonlocal replacements_for_file
            original = m.group(0)
            replaced = replacer(m, path)
            if replaced != original:
                replacements_for_file += 1
            return replaced

        new_content = pattern.sub(counting_replacer, content)

        # Only write when there were actual textual replacements
        if replacements_for_file > 0:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception as exc:
                # Raise an explicit error so the caller can see why replacements didn't persist
                raise RuntimeError(f"Failed writing replacements to {path}: {exc}")

            # Verify the write persisted and no token patterns remain. If tokens are still
            # present after write, raise an error so we can diagnose persistent replacement loops.
            try:
                verified = path.read_text(encoding="utf-8")
            except Exception as exc:
                raise RuntimeError(f"Wrote replacements to {path} but cannot re-open file for verification: {exc}")

            if pattern.search(verified):
                raise RuntimeError(f"Replacements written to {path} but token patterns still present afterwards (possible write/encoding/FS issue)")

            total += replacements_for_file

    return total


__all__ = [
    "replace_curly_at_mentions",
    "replace_curly_upper_mentions",
    "replace_dynamic_tokens",
    "replace_prompt_broker_tokens",
    "find_uppercase_token_target",
    "find_dynamic_target",
    "format_dynamic_link_text",
]
