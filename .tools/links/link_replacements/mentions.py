"""Replacement helpers for mention-style tokens."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Iterable

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


def replace_curly_at_mentions(md_files: Iterable[str]) -> int:
    """Replace tokens like ``{{Prompt@Broker}}`` with markdown links."""
    yaml_path = Path(__file__).resolve().parent.parent / "links.yaml"
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    failed = {
        test["Given"]: test["WrongFile"]
        for test in data.get("Failed Tests", [])
        if "WrongFile" in test
    }

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
            for candidate in existing_files:
                candidate_path = Path(candidate)
                if candidate_path.suffix.lower() != ".md":
                    continue
                if normalize_string(candidate_path.stem) != normalized_before:
                    continue
                folder_path = normalize_string(str(candidate_path.parent))
                if any(marker in folder_path for marker in markers):
                    found_href = os.path.relpath(candidate_path, path.parent)
                    break

            if not found_href:
                continue

            if token in failed and Path(found_href).name == failed[token]:
                raise ValueError(
                    f"Generated wrong file link for {token}: {Path(found_href).name}"
                )

            markdown = f"[`{token}` 🅰️ method](<{found_href}>)"
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


def replace_dynamic_tokens(md_files: Iterable[str], file_dict: dict[str, tuple[str, str]]) -> int:
    """Replace any remaining ``{{...}}`` tokens using normalized filenames."""

    def replacer(match, current_file: Path):
        token = match.group(1)
        parts = token.split("@", 1)

        candidates = []
        if len(parts) == 2:
            candidates.extend(parts[::-1])  # after, before
        candidates.append(token)

        for candidate in candidates:
            normalized = normalize_string(candidate)
            if normalized in file_dict:
                _, target_path = file_dict[normalized]
                rel_path = os.path.relpath(target_path, current_file.parent)
                return f"[`{token}`](<{rel_path}>)"
        return match.group(0)

    total = 0
    pattern = re.compile(r"\{\{([^}]+)\}\}", re.IGNORECASE)

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        new_content, count = pattern.subn(lambda m: replacer(m, path), content)
        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


__all__ = [
    "replace_curly_at_mentions",
    "replace_curly_upper_mentions",
    "replace_dynamic_tokens",
    "replace_prompt_broker_tokens",
]
