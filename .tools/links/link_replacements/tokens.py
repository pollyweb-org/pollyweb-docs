"""Straightforward token replacement helpers."""

from __future__ import annotations

import os
import re
from pathlib import Path
from threading import RLock
from typing import Callable, Dict, Iterable, Optional

import yaml

from broken_links.common import normalize_string
from .mentions import find_dynamic_target, format_dynamic_link_text


HARDCODED_HANDLERS: Dict[str, Dict[str, object]] = {}
TRIPLE_BRACE_PATTERN = re.compile(r"\{\{\{([^{}]+)\}\}\}")

def _find_basename(md_files: Iterable[str], basename: str) -> Optional[Path]:
    """Return the first markdown file whose basename matches the provided name."""

    for candidate in md_files:
        if os.path.basename(candidate) == basename:
            return Path(candidate)
    return None

_SIMPLE_CONTENT_CACHE: Dict[str, Dict[str, object]] = {}
_SIMPLE_CACHE_LOCK = RLock()
LINK_PATTERN = re.compile(r"\[[^\]]+?\]\(<[^>]+?>\)", re.DOTALL)
PATTERN_NEEDLES: Dict[int, str] = {}
TOKEN_LITERAL_EXTRACT = re.compile(r"`\??([^`]+)`\??")


def _build_dot_function_index(md_files: Iterable[str]) -> Dict[str, Path]:
    """Map normalized dot-function tokens (e.g. '.UUID') to canonical files."""

    index: Dict[str, Path] = {}

    def maybe_store(key: str, path: Path) -> None:
        if not key:
            return

        existing = index.get(key)
        if existing is None:
            index[key] = path
            return

        existing_score = (len(existing.parts), str(existing))
        candidate_score = (len(path.parts), str(path))
        if candidate_score < existing_score:
            index[key] = path

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

        token_left = normalize_string(left)
        token_right = normalize_string(right)
        if not token_left:
            continue

        maybe_store(token_left, path)
        if token_right:
            maybe_store(f"{token_left}{token_right}", path)
    return index


def _register_literal_pattern(pattern: re.Pattern[str], token_literal: str) -> re.Pattern[str]:
    PATTERN_NEEDLES[id(pattern)] = token_literal
    return pattern


def clear_simple_replacer_cache() -> None:
    """Reset cached file contents used by simple token replacers."""

    with _SIMPLE_CACHE_LOCK:
        _SIMPLE_CONTENT_CACHE.clear()


def register_hardcoded(
    token_key: str,
    *,
    replacement: str,
    token_label: str,
) -> Callable[[Callable[[Iterable[str]], int]], Callable[[Iterable[str]], int]]:
    """Register a token replacer that is backed by a static replacement string."""

    def decorator(func: Callable[[Iterable[str]], int]) -> Callable[[Iterable[str]], int]:
        HARDCODED_HANDLERS[token_key] = {
            "replacement": replacement,
            "token_label": token_label,
            "func": func,
        }
        return func

    return decorator


def _get_cached_entry(path: Path) -> Optional[Dict[str, object]]:
    key = str(path)
    with _SIMPLE_CACHE_LOCK:
        entry = _SIMPLE_CONTENT_CACHE.get(key)
    if entry is not None:
        return entry

    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None

    entry = {"content": text, "link_spans": None, "lower": None}
    with _SIMPLE_CACHE_LOCK:
        _SIMPLE_CONTENT_CACHE[key] = entry
    return entry


def _replace_simple(
    md_files: Iterable[str],
    pattern: re.Pattern[str],
    replacement: str,
    *,
    needle: Optional[str] = None,
) -> int:
    """Replace occurrences of pattern with replacement while respecting existing links."""

    total = 0
    for md_file in md_files:
        path = Path(md_file)
        entry = _get_cached_entry(path)
        if entry is None:
            continue

        content = entry.get("content")
        if not isinstance(content, str) or "{{" not in content:
            continue

        if needle is None:
            needle = PATTERN_NEEDLES.get(id(pattern))
            if needle is None:
                match = TOKEN_LITERAL_EXTRACT.search(pattern.pattern)
                if match:
                    candidate = match.group(1)
                    needle = re.sub(r"\\(.)", r"\1", candidate)
                    PATTERN_NEEDLES[id(pattern)] = needle

        if needle:
            if needle in content:
                pass
            else:
                lower = entry.get("lower")
                if lower is None:
                    lower = content.lower()
                    entry["lower"] = lower
                if needle.lower() not in lower:
                    continue

        if not pattern.search(content):
            continue

        link_spans = entry.get("link_spans")
        if link_spans is None:
            link_spans = [m.span() for m in LINK_PATTERN.finditer(content)]
            entry["link_spans"] = link_spans

        changes = 0

        if link_spans:
            spans = tuple(link_spans)

            def _repl(m: re.Match[str]) -> str:
                nonlocal changes
                pos = m.start()
                for a, b in spans:
                    if a <= pos < b:
                        return m.group(0)
                changes += 1
                return replacement
        else:
            def _repl(m: re.Match[str]) -> str:
                nonlocal changes
                changes += 1
                return replacement

        new_content = pattern.sub(_repl, content)
        if not changes:
            continue

        try:
            path.write_text(new_content, encoding="utf-8")
        except Exception:
            continue

        entry["content"] = new_content
        entry["link_spans"] = None
        entry["lower"] = None
        total += changes

    return total


def _replace_literal_variants(
    md_files: Iterable[str],
    pattern: re.Pattern[str],
    replacements: Dict[str, str],
    normalized_map: Dict[str, str],
    needles: Iterable[str],
) -> int:
    """Replace tokens while honoring case-specific replacements."""

    total = 0
    needle_list = list(needles)

    for md_file in md_files:
        path = Path(md_file)
        entry = _get_cached_entry(path)
        if entry is None:
            continue

        content = entry.get("content")
        if not isinstance(content, str) or "{{" not in content:
            continue

        if needle_list:
            if not any(needle in content for needle in needle_list):
                lower = entry.get("lower")
                if lower is None:
                    lower = content.lower()
                    entry["lower"] = lower
                if not any(needle.lower() in lower for needle in needle_list):
                    continue

        if not pattern.search(content):
            continue

        link_spans = entry.get("link_spans")
        if link_spans is None:
            link_spans = [m.span() for m in LINK_PATTERN.finditer(content)]
            entry["link_spans"] = link_spans

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            pos = match.start()
            if inside_link(pos):
                return match.group(0)

            literal = match.group(1)
            replacement = replacements.get(literal)
            if replacement is None:
                replacement = normalized_map.get(normalize_string(literal))
            if replacement is None:
                return match.group(0)

            changes += 1
            return replacement

        new_content = pattern.sub(_repl, content)
        if not changes:
            continue

        try:
            path.write_text(new_content, encoding="utf-8")
        except Exception:
            continue

        entry["content"] = new_content
        entry["link_spans"] = None
        entry["lower"] = None
        total += changes

    return total


def _simple_pattern_for(token_literal: str) -> re.Pattern[str]:
    """Build a simple regex pattern matching {{ `Token` }} variants for a token literal."""

    pattern = rf"\{{\{{[\s\u00A0\u200B\u200C\u200D]*`?{re.escape(token_literal)}`?[\s\u00A0\u200B\u200C\u200D]*\}}\}}"
    compiled = re.compile(pattern, re.IGNORECASE)
    PATTERN_NEEDLES[id(compiled)] = token_literal
    return compiled


def _make_hardcoded_replacer(func_name: str, token_literal: str, token_key: str, replacement: str, token_label: str):
    """Dynamically create and register a simple hardcoded replacer.

    The created function will be available in module globals under `func_name`
    and also registered in HARDCODED_HANDLERS under `token_key`.
    """

    pattern = _simple_pattern_for(token_literal)

    def replacer(md_files: Iterable[str]) -> int:
        return _replace_simple(md_files, pattern, replacement, needle=token_literal)

    replacer.__name__ = func_name
    globals()[func_name] = replacer
    HARDCODED_HANDLERS[token_key] = {"func": replacer, "replacement": replacement, "token_label": token_label}
    return replacer


_DOT_FUNCTION_PATTERN = re.compile(
    r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?\.(\w+(?:[\s\u00A0\u200B\u200C\u200D]+\w+)*)`?[\s\u00A0\u200B\u200C\u200D]*\}\}"
)


def replace_msg_tokens(md_files):
    pattern = _simple_pattern_for("$.Msg")
    # Use the holder file for $.Msg (emoji then token then '🧠 holder')
    replacement = "[`$.Msg` 🧠 holder](<📨 $.Msg 🧠 holder.md>)"
    return _replace_simple(md_files, pattern, replacement, needle="$.Msg")

# Hardcoded Map token with case-sensitive link text handling
_MAP_PATTERN = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Mm]ap)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")


def replace_function_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Function`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    # Link text shows the function placeholder with braces, but the target file
    # is named without braces (e.g. "Function 🐍.md"). Keep link text as-is
    # but point to the correct existing file.
    return _replace_simple(md_files, pattern, "[{Function} 🐍](<Function 🐍.md>)")


def replace_functions_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Functions`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    # Similar to single-function case; target file is "Function 🐍.md"
    return _replace_simple(md_files, pattern, "[{Functions} 🐍](<Function 🐍.md>)")


def replace_dot_function_tokens(md_files: Iterable[str]) -> int:
    """Replace tokens like ``{{.UUID}}`` with links to their ⓕ function docs."""

    function_index = _build_dot_function_index(md_files)
    if not function_index:
        return 0

    total = 0

    for md_file in md_files:
        path = Path(md_file)
        entry = _get_cached_entry(path)
        if not entry:
            continue

        content = entry["content"]
        if "{{." not in content:
            continue

        link_spans = entry.get("link_spans")
        if link_spans is None:
            spans = [m.span() for m in LINK_PATTERN.finditer(content)]
            entry["link_spans"] = spans
            link_spans = spans

        spans_tuple = tuple(link_spans)

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in spans_tuple)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_name = match.group(1)
            normalized_token = normalize_string(token_name)
            target_path = function_index.get(normalized_token)
            if not target_path:
                return match.group(0)

            try:
                rel_path = os.path.relpath(target_path, path.parent)
            except Exception:
                rel_path = target_path.name

            changes += 1
            return f"[`.{token_name}`](<{rel_path}>)"

        new_content = _DOT_FUNCTION_PATTERN.sub(_repl, content)
        if not changes:
            continue

        try:
            path.write_text(new_content, encoding="utf-8")
        except Exception:
            continue

        entry["content"] = new_content
        entry["link_spans"] = None
        entry["lower"] = None
        total += changes

    return total
def replace_item_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Item`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Item 🛢](<Itemized 🛢 dataset.md>)")


def replace_items_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Items`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[`Items` 🛢](<Itemized 🛢 dataset.md>)")


def replace_itemizer_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Itemizer`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    replacement = "[Itemizer 🛢 helper domain](<../../🛢🤲 Itemizer helper.md>)"
    return _replace_simple(md_files, pattern, replacement)


def replace_itemizers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Itemizers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    replacement = "[Itemizer 🛢 helper domains](<../../🛢🤲 Itemizer helper.md>)"
    return _replace_simple(md_files, pattern, replacement)


def replace_talker_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Talker`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Talker 😃 domain](<😃 Talker role.md>)")


def replace_talkers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Talkers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Talker 😃 domains](<😃 Talker role.md>)")

def replace_itemized_datasets_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Itemized datasets`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Itemized 🪣 datasets](<Itemized 🛢 dataset.md>)")

def replace_triple_brace_tokens(md_files: Iterable[str], file_dict: dict[str, list[tuple[str, str]]]) -> int:
    """Replace helper tokens using triple braces with markdown links."""

    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        def replacer(match: re.Match[str]) -> str:
            token = match.group(1).strip()
            target = find_dynamic_target(token, file_dict)
            if not target:
                return match.group(0)

            try:
                rel_path = os.path.relpath(target, path.parent)
            except Exception:
                rel_path = str(target)

            link_text = format_dynamic_link_text(token, triple_brace=True)
            return f"[{link_text}](<{rel_path}>)"

        new_content, count = TRIPLE_BRACE_PATTERN.subn(replacer, content)
        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


def _register_yaml_hardcoded_handlers() -> None:
    """Auto-register hardcoded replacements defined in links.yaml."""

    yaml_path = Path(__file__).resolve().parent.parent / "links.yaml"
    try:
        data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    except Exception:
        return

    raw_successful = data.get("Successful Tests", [])

    def _iter_successful_tests(raw) -> Iterable[dict]:
        if isinstance(raw, dict):
            for section, value in raw.items():
                if isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            entry = dict(item)
                            entry["_section"] = section
                            yield entry
                elif isinstance(value, dict):
                    entry = dict(value)
                    entry["_section"] = section
                    yield entry
        elif isinstance(raw, list):
            for item in raw:
                if isinstance(item, dict):
                    yield dict(item)

    tests = list(_iter_successful_tests(raw_successful))

    grouped: Dict[str, Dict[str, object]] = {}

    for test in tests:
        section = normalize_string(str(test.get("_section", "")))
        test.pop("_section", None)
        reasons = (test.get("Reasons") or "").lower()
        if section != "hardcoded" and "hardcoded" not in reasons:
            continue

        given = test.get("Given")
        link_text = test.get("LinkText")
        link_file = test.get("LinkFile")
        if not (given and link_text and link_file):
            continue

        token_literal = given.strip()
        if token_literal.startswith("{{") and token_literal.endswith("}}"):  # strip braces
            token_literal = token_literal[2:-2]
        token_literal = token_literal.strip()
        if not token_literal:
            continue

        token_key = normalize_string(token_literal)
        if token_key in HARDCODED_HANDLERS:
            continue

        bucket = grouped.setdefault(token_key, {"order": [], "variants": {}})
        order = bucket["order"]  # type: ignore[assignment]
        variants = bucket["variants"]  # type: ignore[assignment]
        if token_literal not in variants:
            order.append(token_literal)
        variants[token_literal] = (link_text, link_file)

    for token_key, payload in grouped.items():
        order = payload["order"]  # type: ignore[index]
        variants = payload["variants"]  # type: ignore[index]
        if not order:
            continue

        if len(order) == 1:
            literal = order[0]
            link_text, link_file = variants[literal]
            replacement = f"[{link_text}](<{link_file}>)"
            pattern = _simple_pattern_for(literal)

            def _make_single(pat: re.Pattern[str], needle: str, repl: str):
                def _replacer(md_files: Iterable[str]) -> int:
                    return _replace_simple(md_files, pat, repl, needle=needle)

                return _replacer

            replacer = _make_single(pattern, literal, replacement)
            func_name = f"replace_{token_key}_tokens_from_yaml"
            replacer.__name__ = func_name
            globals()[func_name] = replacer
            HARDCODED_HANDLERS[token_key] = {
                "func": replacer,
                "replacement": replacement,
                "token_label": literal,
            }
            continue

        replacements: Dict[str, str] = {}
        normalized_map: Dict[str, str] = {}
        needles: list[str] = []

        # Sort by length (desc) then literal to stabilize regex order
        ordered_literals = sorted(order, key=lambda item: (-len(item), item))
        for literal in ordered_literals:
            link_text, link_file = variants[literal]
            replacement = f"[{link_text}](<{link_file}>)"
            replacements[literal] = replacement
            normalized_map[normalize_string(literal)] = replacement
            needles.append(literal)

        alternation = "|".join(re.escape(lit) for lit in ordered_literals)
        pattern = re.compile(
            rf"\{{\{{[\s\u00A0\u200B\u200C\u200D]*`?({alternation})`?[\s\u00A0\u200B\u200C\u200D]*\}}\}}"
        )

        def _make_multi(pat: re.Pattern[str], reps: Dict[str, str], norm_map: Dict[str, str], hints: Iterable[str]):
            def _replacer(md_files: Iterable[str]) -> int:
                return _replace_literal_variants(md_files, pat, reps, norm_map, hints)

            return _replacer

        replacer = _make_multi(pattern, replacements, normalized_map, needles)
        func_name = f"replace_{token_key}_tokens_from_yaml_variants"
        replacer.__name__ = func_name
        globals()[func_name] = replacer

        combined_replacement = " | ".join(replacements[literal] for literal in order)
        HARDCODED_HANDLERS[token_key] = {
            "func": replacer,
            "replacement": combined_replacement,
            "token_label": "/".join(order),
        }


_register_yaml_hardcoded_handlers()


__all__ = [
    "HARDCODED_HANDLERS",
    "clear_simple_replacer_cache",
    "register_hardcoded",
    "replace_msg_tokens",
    "replace_function_tokens",
    "replace_functions_tokens",
    "replace_dot_function_tokens",
    "replace_item_tokens",
    "replace_items_tokens",
    "replace_itemizer_tokens",
    "replace_itemizers_tokens",
    "replace_talker_tokens",
    "replace_talkers_tokens",
    "replace_itemized_datasets_tokens",
    "replace_triple_brace_tokens",
]
