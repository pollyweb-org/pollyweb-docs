"""Regular expression patterns used for link extraction."""

import re

_LINK_PATTERNS = [
    re.compile(r"\[.*?\]\(([^)]+\.md)\)"),
    re.compile(r"\[.*?\]\(<?([^)>]+\.md)>?\)"),
    re.compile(r"\[.*?\]\(([^)]+\.png)\)"),
    re.compile(r"\[.*?\]\(<?([^)>]+\.png)>?\)"),
    re.compile(r"\[.*?\]\(([^)]+\.jpg)\)"),
    re.compile(r"\[.*?\]\(<?([^)>]+\.jpg)>?\)"),
    re.compile(r"\[.*?\]\(([^)]+\.pdf)\)"),
    re.compile(r"\[.*?\]\(<?([^)>]+\.pdf)>?\)"),
    re.compile(r"!\[\]\(([^)]+?\.(?:png|pdf))\)"),
]

_GENERIC_LINK_RE = re.compile(r"(?<!!)\[.*?\]\(<?([^)>#]+)>?\)")
_GENERIC_EXT_RE = re.compile(r"\.(md|png|jpg|pdf)$", re.IGNORECASE)

_MALFORMED_PATTERNS = [
    re.compile(r"\[[^\]]+\]\([^)\n]*\.md(?![^)]*\))"),
    re.compile(r"\[[^\]]+\][^ \[<]+\..+?\)\>?"),
    re.compile(r"\[.*?\]\(<?([^)>]+\.md)>(?!\))"),
    re.compile(r"\[[^\]]*\.[^\]]*\>\)"),
    re.compile(r"!\[.*?\]\([^)\n]+$"),
]

_SUSPICIOUS_TAIL_PATTERNS = [
    # Detect tokens where a markdown-like extension has accidental trailing characters (e.g., "Command.mdds")
    re.compile(r"\b[^\s\[\]()<>]+\.(?:md|png|jpg|pdf)[A-Za-z0-9]+", re.IGNORECASE),
    # Detect leftover `.md` paths immediately followed by a closing bracket and new link opener (missing `[`).
    re.compile(r"[^\s\[\]()<>]+\.(?:md|png|jpg|pdf)[^\s()\[\]<>]*\]\(", re.IGNORECASE),
    # Detect extension immediately followed by word characters without whitespace (e.g. ".mdConverse").
    re.compile(r"\.(?:md|png|jpg|pdf)[A-Za-z0-9]", re.IGNORECASE),
]


def extract_links_with_malformed_detection(content: str):
    """Extract links to markdown assets and log malformed patterns."""
    links_with_lines: list[tuple[str, int]] = []
    malformed_links_with_lines: list[tuple[str, int]] = []

    lines = content.splitlines()
    found_the_line = False
    matched_the_line = False

    for line_no, line in enumerate(lines, 1):
        if "ads-market-share.png" in line:
            found_the_line = True

        for pattern in _LINK_PATTERNS:
            links = pattern.findall(line)
            for link in links:
                links_with_lines.append((link, line_no))
                if False and found_the_line and "ads-market-share.png" in line:
                    raise ValueError(line)
                    matched_the_line = True
                if "](." in line:
                    malformed_links_with_lines.append((line, line_no))

        generic_links = _GENERIC_LINK_RE.findall(line)
        for link in generic_links:
            if _GENERIC_EXT_RE.search(link):
                continue
            if link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if not link.strip():
                continue
            links_with_lines.append((link, line_no))

        for pattern in _MALFORMED_PATTERNS:
            malformed_links = pattern.findall(line)
            for malformed_link in malformed_links:
                if "https://" in malformed_link:
                    links_with_lines.append((malformed_link, line_no))
                    continue
                malformed_links_with_lines.append((malformed_link, line_no))

        for pattern in _SUSPICIOUS_TAIL_PATTERNS:
            for match in pattern.finditer(line):
                fragment = match.group(0)
                entry = (fragment, line_no)
                if fragment and entry not in malformed_links_with_lines:
                    malformed_links_with_lines.append(entry)

    if False and found_the_line:
        if matched_the_line:
            raise ValueError("MATCHED THE LINE")
        raise ValueError("FOUND THE LINE")

    return links_with_lines, malformed_links_with_lines


__all__ = [
    "_GENERIC_EXT_RE",
    "_GENERIC_LINK_RE",
    "_LINK_PATTERNS",
    "_MALFORMED_PATTERNS",
    "extract_links_with_malformed_detection",
]
