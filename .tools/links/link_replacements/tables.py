"""Helpers for table formatting tweaks."""

from __future__ import annotations

import os
import re
import urllib.parse
from pathlib import Path
from typing import Iterable

from .patterns import _ROW_LEADING_UPPER_LINK_RE, find_first_emoji


def add_emoji_to_table_rows(md_files: Iterable[str]) -> int:
    """Insert emoji prefix into table rows referencing emoji-bearing files."""
    total_changes = 0
    for md_file in md_files:
        path = Path(md_file)
        try:
            lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        except Exception:
            continue

        changed = False
        for index, line in enumerate(lines):
            match = _ROW_LEADING_UPPER_LINK_RE.match(line)
            if not match:
                continue

            href = match.group(2) if match.group(2) is not None else match.group(3)
            if not href or href.startswith(("http://", "https://", "mailto:", "#")):
                continue

            href_decoded = urllib.parse.unquote(href)
            filename = os.path.basename(href_decoded)
            emoji_char = find_first_emoji(filename)
            if not emoji_char:
                continue

            if re.match(r"^\s*\|\s*" + re.escape(emoji_char) + r"\s", line):
                continue

            new_line = re.sub(r"^(\s*\|\s*)", r"\g<1>" + emoji_char + " ", line, count=1)
            if new_line != line:
                lines[index] = new_line
                changed = True
                total_changes += 1

        if changed:
            try:
                path.write_text("".join(lines), encoding="utf-8")
            except Exception:
                continue

    return total_changes


__all__ = [
    "add_emoji_to_table_rows",
]
