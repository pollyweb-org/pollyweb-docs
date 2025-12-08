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


PLACEHOLDER_REPLACEMENT = "[Placeholder 🧠](<Holder 🧠.md>)"
SUBSCRIBER_REPLACEMENT = "[Subscriber 🔔 domain](<../Subscribers 🔔/🔔🎭 Subscriber role.md>)"
SUBSCRIBERS_REPLACEMENT = "[Subscriber 🔔 domains](<../Subscribers 🔔/🔔🎭 Subscriber role.md>)"


@register_hardcoded("placeholder", replacement=PLACEHOLDER_REPLACEMENT, token_label="Placeholder")
def replace_placeholder_tokens(md_files):
    pattern = _simple_pattern_for("Placeholder")
    return _replace_simple(md_files, pattern, PLACEHOLDER_REPLACEMENT)

def replace_msg_tokens(md_files):
    pattern = _simple_pattern_for("$.Msg")
    # Use the holder file for $.Msg (emoji then token then '🧠 holder')
    replacement = "[`$.Msg` 🧠 holder](<📨 $.Msg 🧠 holder.md>)"
    return _replace_simple(md_files, pattern, replacement, needle="$.Msg")

# Hardcoded Map token with case-sensitive link text handling
_MAP_PATTERN = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Mm]ap)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")


@register_hardcoded("map", replacement="[Map 🧠 holder](<🧠 Map holders.md>)|[map](<🧠 Map holders.md>)", token_label="Map")
def replace_map_tokens(md_files):
    total = 0
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            # Emit lowercase variant without the emoji when the token is fully lowercase
            replacement = "[map](<🧠 Map holders.md>)" if token_value.islower() else "[Map 🧠 holder](<🧠 Map holders.md>)"
            changes += 1
            return replacement

        new_content = _MAP_PATTERN.sub(_repl, content)

        if changes:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += changes

    return total


@register_hardcoded("bool", replacement="[Bool 🧠 holder](<Bool holders.md>)|[bool](<Bool holders.md>)", token_label="Bool")
def replace_bool_tokens(md_files):
    """Replace {{Bool}}/{{bool}} tokens while preserving link text casing."""

    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Bb]ool)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)
    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            replacement = "[bool](<Bool holders.md>)" if token_value.islower() else "[Bool 🧠 holder](<Bool holders.md>)"
            changes += 1
            return replacement

        new_content, count = pattern.subn(_repl, content)

        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


@register_hardcoded("list", replacement="[List 🧠 holder](<🧠 List holders.md>)|[list](<🧠 List holders.md>)", token_label="List")
def replace_list_tokens(md_files):
    """Replace {{List}}/{{list}} tokens while preserving link text casing."""

    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Ll]ist)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)
    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            replacement = "[list](<🧠 List holders.md>)" if token_value.islower() else "[List 🧠 holder](<🧠 List holders.md>)"
            changes += 1
            return replacement

        new_content, count = pattern.subn(_repl, content)

        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


@register_hardcoded(
    "enum",
    replacement="[Enum 🧠 holder](<🧠 Enum holders.md>)|[enum](<Enum holders.md>)|[Enum 🧠 holders](<🧠 Enum holders.md>)",
    token_label="Enum",
)
def replace_enum_tokens(md_files):
    """Replace enum tokens with casing- and plurality-aware links."""

    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Ee]nums?)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)
    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            lower_value = token_value.lower()
            is_plural = lower_value.endswith('s')

            if token_value.islower():
                # Lowercase tokens link to the non-emoji holder specification.
                link_text = lower_value
                link_target = "Enum holders.md"
            else:
                link_text = "Enum 🧠 holders" if is_plural else "Enum 🧠 holder"
                link_target = "🧠 Enum holders.md"

                # Preserve trailing 's' for capitalized plurals while keeping the emoji placement.
                if is_plural and not link_text.endswith('s'):
                    link_text += 's'

            changes += 1
            return f"[{link_text}](<{link_target}>)"

        new_content, count = pattern.subn(_repl, content)

        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


@register_hardcoded("text", replacement="[Text 🧠 holder](<🧠 Text holders.md>)|[text](<🧠 Text holders.md>)", token_label="Text")
def replace_text_tokens(md_files):
    """Replace {{Text}}/{{text}} tokens while preserving link text casing."""

    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Tt]ext)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)
    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            replacement = "[text](<🧠 Text holders.md>)" if token_value.islower() else "[Text 🧠 holder](<🧠 Text holders.md>)"
            changes += 1
            return replacement

        new_content, count = pattern.subn(_repl, content)

        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


@register_hardcoded("set", replacement="[Set 🧠 holder](<🧠 Set holders.md>)|[set](<🧠 Set holders.md>)", token_label="Set")
def replace_set_tokens(md_files):
    """Replace {{Set}}/{{set}} tokens while preserving link text casing."""

    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Ss]et)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)
    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            replacement = "[set](<🧠 Set holders.md>)" if token_value.islower() else "[Set 🧠 holder](<🧠 Set holders.md>)"
            changes += 1
            return replacement

        new_content, count = pattern.subn(_repl, content)

        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


@register_hardcoded("num", replacement="[Num 🧠 holder](<🧠 Num holders.md>)|[num](<🧠 Num holders.md>)", token_label="Num")
def replace_num_tokens(md_files):
    """Replace {{Num}}/{{num}} tokens while preserving link text casing."""

    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Nn]um)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)
    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            replacement = "[num](<🧠 Num holders.md>)" if token_value.islower() else "[Num 🧠 holder](<🧠 Num holders.md>)"
            changes += 1
            return replacement

        new_content, count = pattern.subn(_repl, content)

        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


@register_hardcoded("time", replacement="[Time 🧠 holder](<🧠 Time holders.md>)|[time](<🧠 Time holders.md>)", token_label="Time")
def replace_time_tokens(md_files):
    """Replace {{Time}}/{{time}} tokens while preserving link text casing."""

    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Tt]ime)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)
    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            replacement = "[time](<🧠 Time holders.md>)" if token_value.islower() else "[Time 🧠 holder](<🧠 Time holders.md>)"
            changes += 1
            return replacement

        new_content, count = pattern.subn(_repl, content)

        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total

# Generate common simple replacers to reduce repeated boilerplate. These are
# intentionally created via helper to keep the explicit simple cases compact.
_GEN_BASIC = [
    ("replace_token_tokens", "Token", "token", "[Token 🎫](<🎫 Token.md>)", "Token"),
    ("replace_tokens_tokens", "Tokens", "tokens", "[Tokens 🎫](<🎫 Token.md>)", "Tokens"),
    ("replace_chat_tokens", "Chat", "chat", "[Chat 💬](<💬 Chat.md>)", "Chat"),
    ("replace_chats_tokens", "Chats", "chats", "[Chats 💬](<💬 Chat.md>)", "Chats"),
    ("replace_settings_tokens", "$.Hosted", "$.settings", "[`$.Hosted` 🧠 holder](<📦 $.Hosted 🧠 holder.md>)", "$.Hosted"),
    ("replace_placeholders_tokens", "Placeholders", "placeholders", "[Placeholders 🧠](<Holder 🧠.md>)", "Placeholders"),
    ("replace_domain_tokens", "domain", "domain", "[domain 👥](<👥 Domain.md>)", "domain"),
    ("replace_domains_tokens", "domains", "domains", "[domains 👥](<👥 Domain.md>)", "domains"),
    ("replace_dataset_tokens", "Dataset", "dataset", "[Dataset 🪣](<🪣 Dataset.md>)", "Dataset"),
    ("replace_datasets_tokens", "Datasets", "datasets", "[Datasets 🪣](<🪣 Dataset.md>)", "Datasets"),
    ("replace_message_tokens", "Message", "message", "[Message 📨](<📨 Message.md>)", "Message"),
    ("replace_messages_tokens", "Messages", "messages", "[Messages 📨](<📨 Message.md>)", "Messages"),
    ("replace_schema_tokens", "Schema", "schema", "[Schema Code 🧩](<🧩 Schema Code.md>)", "Schema"),
    ("replace_schemas_tokens", "Schemas", "schemas", "[Schema Codes 🧩](<🧩 Schema Code.md>)", "Schemas"),
    ("replace_chat_msg_tokens", "$.Chat", "$.chat", "[`$.Chat` 🧠 holder](<💬 $.Chat 🧠 holder.md>)", "$.Chat"),
]

for fname, lit, key, repl, label in _GEN_BASIC:
    _make_hardcoded_replacer(fname, lit, key, repl, label)
@register_hardcoded("subscriber", replacement=SUBSCRIBER_REPLACEMENT, token_label="Subscriber")
def replace_subscriber_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Subscriber`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, SUBSCRIBER_REPLACEMENT)


@register_hardcoded("subscribers", replacement=SUBSCRIBERS_REPLACEMENT, token_label="Subscribers")
def replace_subscribers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Subscribers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, SUBSCRIBERS_REPLACEMENT)


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

        replacement = f"[{link_text}](<{link_file}>)"
        pattern = _simple_pattern_for(token_literal)

        def _make_replacer(pat: re.Pattern[str], literal: str, repl: str):
            def _replacer(md_files: Iterable[str]) -> int:
                return _replace_simple(md_files, pat, repl, needle=literal)

            return _replacer

        replacer = _make_replacer(pattern, token_literal, replacement)
        func_name = f"replace_{token_key}_tokens_from_yaml"
        replacer.__name__ = func_name
        globals()[func_name] = replacer
        HARDCODED_HANDLERS[token_key] = {
            "func": replacer,
            "replacement": replacement,
            "token_label": token_literal,
        }


_register_yaml_hardcoded_handlers()


__all__ = [
    "HARDCODED_HANDLERS",
    "replace_placeholder_tokens",
    "replace_msg_tokens",
    "replace_token_tokens",
    "replace_tokens_tokens",
    "replace_chat_tokens",
    "replace_chats_tokens",
    "replace_settings_tokens",
    "replace_placeholders_tokens",
    "replace_domain_tokens",
    "replace_domains_tokens",
    "replace_dataset_tokens",
    "replace_datasets_tokens",
    "replace_message_tokens",
    "replace_messages_tokens",
    "replace_schema_tokens",
    "replace_schemas_tokens",
    "replace_chat_msg_tokens",
    "replace_map_tokens",
    "replace_bool_tokens",
    "replace_list_tokens",
    "replace_enum_tokens",
    "replace_text_tokens",
    "replace_set_tokens",
    "replace_num_tokens",
    "replace_time_tokens",
    "replace_subscriber_tokens",
    "replace_subscribers_tokens",
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
