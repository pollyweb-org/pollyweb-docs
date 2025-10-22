"""Regex utilities used by link replacement workflows."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

try:
    import emoji as _emoji_mod  # optional dependency
except Exception:  # pragma: no cover - best effort import
    _emoji_mod = None

_LINK_WITH_TEXT_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(<?([^)>#]+)>?\)")
_LINK_WITH_TEXT_ANGLE_RE = re.compile(r"(?<!!)\[([^\]]+)\]<([^>#]+)>")
_ANGLE_AUTOLINK_RE = re.compile(r"(?<!!)<?<([^>#]+)>")

_CURLY_AT_TOKEN_RE = re.compile(r"\{\{([^{}]*@[^{}]*)\}\}")
_CURLY_UPPER_TOKEN_RE = re.compile(r"\{\{([A-Z][A-Z0-9._-]*)\}\}")

_ROW_LEADING_UPPER_LINK_RE = re.compile(
    r"^\s*\|\s*"  # start of row and pipe
    r"\[`([A-Z][A-Z0-9._-]*)`\]"  # link label wrapped in backticks
    r"(?:\(<?([^)>#]+)>?\)|<([^)>#]+)>)"  # either (...<href>...) or <href>",
)

_KEYCAP_EMOJI_RE = re.compile("(?:[0-9#*]\uFE0F?\u20E3)")
_GENERAL_EMOJI_RE = re.compile(
    "[\U0001F1E6-\U0001F1FF\U0001F300-\U0001FAFF\u2190-\u21FF\u2300-\u23FF\u25A0-\u25FF\u2600-\u26FF\u2700-\u27BF\u2B00-\u2BFF]\uFE0F?",
    re.UNICODE,
)

LinkEntry = Tuple[str, str]
IndexedLinkEntry = Tuple[str, str, str]


def extract_links_text_href(content: str) -> List[LinkEntry]:
    """Return list of `(text, href)` tuples for markdown links inside content."""
    results: list[LinkEntry] = []
    seen: set[LinkEntry] = set()

    for text, href in _LINK_WITH_TEXT_RE.findall(content):
        key = (text, href)
        if key not in seen:
            seen.add(key)
            results.append(key)

    for text, href in _LINK_WITH_TEXT_ANGLE_RE.findall(content):
        key = (text, href)
        if key not in seen:
            seen.add(key)
            results.append(key)

    return results


def extract_curly_at_tokens(content: str) -> List[str]:
    """Return tokens found inside `{{...}}` that contain an at-sign."""
    unique = list(dict.fromkeys(_CURLY_AT_TOKEN_RE.findall(content)))
    return unique


def extract_curly_upper_tokens(content: str) -> List[str]:
    """Return uppercase tokens found inside `{{...}}`."""
    unique = list(dict.fromkeys(_CURLY_UPPER_TOKEN_RE.findall(content)))
    return unique


def pick_matching_link(token: str, links: Sequence[IndexedLinkEntry | LinkEntry]):
    """Return `(href, base_path)` pair matching the token, or `(None, None)`."""
    token_lower = token.lower()

    for entry in links:
        if len(entry) == 2:
            text, href = entry  # type: ignore[misc]
            base = None
        else:
            base, text, href = entry  # type: ignore[misc]
        if token in href:
            return href, base

    for entry in links:
        if len(entry) == 2:
            text, href = entry  # type: ignore[misc]
            base = None
        else:
            base, text, href = entry  # type: ignore[misc]
        if token in text:
            return href, base

    for entry in links:
        if len(entry) == 2:
            text, href = entry  # type: ignore[misc]
            base = None
        else:
            base, text, href = entry  # type: ignore[misc]
        if token_lower in href.lower():
            return href, base

    for entry in links:
        if len(entry) == 2:
            text, href = entry  # type: ignore[misc]
            base = None
        else:
            base, text, href = entry  # type: ignore[misc]
        if token_lower in text.lower():
            return href, base

    return None, None


def pick_matching_link_upper(token: str, links: Sequence[IndexedLinkEntry | LinkEntry]):
    """Return `(href, base_path)` where link label is exactly ``TOKEN``."""
    for entry in links:
        if len(entry) == 2:
            text, href = entry  # type: ignore[misc]
            base = None
        else:
            base, text, href = entry  # type: ignore[misc]
        stripped = text.strip()
        if len(stripped) >= 2 and stripped[0] == "`" and stripped[-1] == "`":
            inner = stripped[1:-1]
            if inner == token and inner.upper() == inner:
                return href, base
    return None, None


def build_project_link_index(md_files: Iterable[str]) -> List[IndexedLinkEntry]:
    """Build a project-wide index of `(path, text, href)` triples."""
    index: list[IndexedLinkEntry] = []
    for path in md_files:
        try:
            content = Path(path).read_text(encoding="utf-8")
        except Exception:
            continue

        for text, href in extract_links_text_href(content):
            index.append((path, text, href))

        for href in _ANGLE_AUTOLINK_RE.findall(content):
            index.append((path, "", href))

    return index


def find_first_emoji(value: str) -> str | None:
    """Return first emoji sequence detected within `value`."""
    match = _KEYCAP_EMOJI_RE.search(value)
    if match:
        return match.group(0)

    match = _GENERAL_EMOJI_RE.search(value)
    if match:
        return match.group(0)

    if _emoji_mod:
        try:
            for char in value:
                if hasattr(_emoji_mod, "EMOJI_DATA") and char in getattr(_emoji_mod, "EMOJI_DATA"):
                    return char
        except Exception:
            pass

    return None


__all__ = [
    "_GENERAL_EMOJI_RE",
    "_ROW_LEADING_UPPER_LINK_RE",
    "build_project_link_index",
    "extract_curly_at_tokens",
    "extract_curly_upper_tokens",
    "extract_links_text_href",
    "find_first_emoji",
    "pick_matching_link",
    "pick_matching_link_upper",
]
