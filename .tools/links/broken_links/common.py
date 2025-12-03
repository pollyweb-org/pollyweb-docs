"""Shared helpers for link scanning and text normalization."""

import itertools
import os
import re

try:
    import emoji as _emoji_mod  # optional dependency
except Exception:  # pragma: no cover - best effort import
    _emoji_mod = None

_GENERAL_EMOJI_RE = re.compile(
    "[\U0001F1E6-\U0001F1FF\U0001F300-\U0001FAFF\u2190-\u21FF\u2300-\u23FF\u25A0-\u25FF\u2600-\u26FF\u2700-\u27BF\u2B00-\u2BFF]\uFE0F?",
    re.UNICODE,
)


def normalize_string(value: str) -> str:
    """Normalize strings by removing emoji, whitespace, and casing."""
    sanitized = _GENERAL_EMOJI_RE.sub("", value)
    sanitized = re.sub(r"\s+", "", sanitized).lower()
    sanitized = re.sub(r"[\u200B\u200C\u200D\uFE0E\uFE0F]", "", sanitized)
    sanitized = sanitized.replace("$", "")
    return sanitized


def method_folder_markers(identifier: str) -> set[str]:
    """Return normalized folder markers that should contain method- or event-style suffixes."""

    markers: set[str] = set()
    suffixes = ("methods", "events", "msgs", "msg", "messages")

    def add_markers(root: str) -> None:
        for suffix in suffixes:
            normalized = normalize_string(f"{root}{suffix}")
            if normalized:
                markers.add(normalized)

    add_markers(identifier)

    lowered = identifier.lower()
    if lowered.endswith("ed") and len(identifier) > 2:
        add_markers(identifier[:-2])
    if lowered.endswith("es") and len(identifier) > 2:
        add_markers(identifier[:-2])
    if lowered.endswith("s") and len(identifier) > 1:
        add_markers(identifier[:-1])
    if lowered.endswith("ized") and len(identifier) > 4:
        add_markers(f"{identifier[:-2]}er")
    if lowered.endswith("ised") and len(identifier) > 4:
        add_markers(f"{identifier[:-2]}er")

    return markers


def count_mismatch_chars(left: str, right: str) -> int:
    """Return number of non-matching characters for aligned prefixes."""
    mismatch_count = 0
    for char_left, char_right in zip(left, right):
        if char_left != char_right:
            mismatch_count += 1
    return mismatch_count


def count_end_match(left: str, right: str) -> int:
    """Return matching suffix length between two strings."""
    match_length = 0
    for idx in range(1, min(len(left), len(right)) + 1):
        if left[-idx] != right[-idx]:
            break
        match_length += 1
    return match_length


def remove_numbers(value: str) -> str:
    """Strip digits, select symbols, and known emoji from a string."""
    cleaned = re.sub(r"\d+", "", value)
    for token in ("$", "✅", "⏳", " ", "."):
        cleaned = cleaned.replace(token, "")
    # Remove specific emoji occurrences
    for token in ("📺", "🖼️", "🇺🇸", "🇨🇳"):
        cleaned = cleaned.replace(token, "")

    if _emoji_mod and ("✅" in value or "⏳" in value):
        try:
            cleaned = _emoji_mod.replace_emoji(cleaned, replace="")
        except Exception:
            pass
    return cleaned


def possible_emoji_insertions(path: str, emoji: str = "⏳") -> set[str]:
    """Yield path variants inserting emoji across path segments."""
    normalized = path.replace("/", os.sep).replace("\\", os.sep)
    parts = normalized.split(os.sep)
    if not parts:
        return {path}

    combos = []
    for part in parts:
        stripped = part.strip()
        if emoji in stripped:
            combos.append([stripped])
        else:
            combos.append([stripped, f"{emoji} {stripped}"])

    variants = {os.sep.join(option) for option in itertools.product(*combos)}
    return variants


__all__ = [
    "_GENERAL_EMOJI_RE",
    "count_end_match",
    "count_mismatch_chars",
    "method_folder_markers",
    "normalize_string",
    "possible_emoji_insertions",
    "remove_numbers",
]
