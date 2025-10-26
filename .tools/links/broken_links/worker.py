"""Worker routines that scan markdown files for link issues."""

from collections import OrderedDict
from concurrent.futures import ProcessPoolExecutor
import os
import urllib.parse

from .common import (
    count_end_match,
    count_mismatch_chars,
    possible_emoji_insertions,
    remove_numbers,
)
from .patterns import extract_links_with_malformed_detection

_EXISTING_FILES: set[str] | None = None
_PROJECT_DIR: str | None = None


def _init_worker(existing_files: set[str], project_dir: str) -> None:
    global _EXISTING_FILES, _PROJECT_DIR
    _EXISTING_FILES = existing_files
    _PROJECT_DIR = project_dir


def _process_single_md_file(md_file: str):
    """Process a single markdown file and return link diagnostics."""
    broken_list: list[tuple[str, str, int, str, str | None]] = []
    malformed_list: list[tuple[str, int]] = []
    replacement_hits: list[tuple[int, str]] = []
    count = 0

    try:
        with open(md_file, "r", encoding="utf-8") as handle:
            content = handle.read()
    except FileNotFoundError:
        # File may have been moved or removed; skip gracefully.
        return (md_file, [], [], [], 0)

    if "\ufffd" in content or "�" in content:
        for line_no, line in enumerate(content.splitlines(), 1):
            if ("\ufffd" in line) or ("�" in line):
                replacement_hits.append((line_no, line))

    links_with_lines, malformed_links_with_lines = extract_links_with_malformed_detection(content)

    existing_files = _EXISTING_FILES or set()
    project_directory = _PROJECT_DIR or ""

    for link, line_num in links_with_lines:
        full_link = os.path.normpath(os.path.join(os.path.dirname(md_file), link))
        full_link = urllib.parse.unquote(full_link)

        if full_link in existing_files:
            continue

        suggestion = "!!!"
        tip: str | None = None

        if suggestion == "!!!":
            target_name = os.path.basename(full_link)
            for file_path in existing_files:
                if os.path.dirname(full_link) == os.path.dirname(file_path):
                    other_name = os.path.basename(file_path)
                    if remove_numbers(other_name).endswith(remove_numbers(target_name)):
                        suggestion = os.path.basename(suggestion)
                        tip = "File in the same folder?"
                        break

        if suggestion == "!!!":
            for file_path in existing_files:
                if remove_numbers(full_link).lower() == remove_numbers(file_path).lower():
                    relative = file_path.replace(project_directory, "")
                    suggestion = os.path.relpath(relative, os.path.dirname(md_file))
                    tip = "Case mismatch?"
                    break

        if suggestion == "!!!" and existing_files:
            closest_match = max(
                existing_files,
                key=lambda candidate: count_end_match(
                    candidate.replace(" ", "%20"), full_link.replace(" ", "%20")
                ),
            )
            resolved = os.path.normpath(closest_match)
            names_equal = remove_numbers(os.path.basename(resolved)) == remove_numbers(os.path.basename(full_link))
            near_match = count_mismatch_chars(os.path.basename(resolved), os.path.basename(full_link)) <= 1
            if names_equal or near_match:
                suggestion = os.path.relpath(resolved, os.path.dirname(md_file))
                tip = "Closest match?"

        if suggestion == "!!!":
            target_name = os.path.basename(full_link)
            for file_path in existing_files:
                other_name = os.path.basename(file_path)
                if remove_numbers(other_name) == remove_numbers(target_name):
                    relative = file_path.replace(project_directory, "")
                    suggestion = os.path.relpath(relative, full_link)
                    tip = "File name match?"
                    break

        if suggestion == "!!!" and project_directory:
            emoji_char = "⏳"
            rel_link_path = os.path.relpath(full_link, project_directory)
            for alt_path in possible_emoji_insertions(rel_link_path, emoji=emoji_char):
                abs_path = os.path.normpath(os.path.join(project_directory, alt_path))
                if abs_path in existing_files:
                    suggestion = os.path.relpath(abs_path, os.path.dirname(md_file))
                    tip = f"Fix by adding '{emoji_char}' emoji"
                    break

        if link == suggestion:
            suggestion = "found same"

        if "https://" in link:
            continue

        entry = (link, full_link, line_num, suggestion, tip)
        if entry not in broken_list:
            broken_list.append(entry)
            count += 1

    if malformed_links_with_lines:
        malformed_list = malformed_links_with_lines

    return (md_file, broken_list, malformed_list, replacement_hits, count)


def check_broken_links(md_files: list[str], png_files: list[str], project_directory: str):
    """Scan project markdown files using a worker pool."""
    broken_links: OrderedDict[str, list[tuple[str, str, int, str, str | None]]] = OrderedDict()
    malformed_links: OrderedDict[str, list[tuple[str, int]]] = OrderedDict()
    replacement_char_hits: OrderedDict[str, list[tuple[int, str]]] = OrderedDict()

    existing_files = set(md_files + png_files)
    max_workers = os.cpu_count() or 1

    with ProcessPoolExecutor(
        max_workers=max_workers,
        initializer=_init_worker,
        initargs=(existing_files, project_directory),
    ) as executor:
        results_iter = executor.map(_process_single_md_file, md_files)

        total_count = 0
        finished = True
        for md_file, broken_list, malformed_list, replacement_hits, count in results_iter:
            if broken_list:
                broken_links[md_file] = broken_list
                total_count += len(broken_list)
            if malformed_list:
                malformed_links[md_file] = malformed_list
            if replacement_hits:
                replacement_char_hits[md_file] = replacement_hits

            if total_count > 1000 and finished:
                print(f"Checking {total_count} times, stopping for performance reasons.")
                finished = False
                break

    return broken_links, malformed_links, replacement_char_hits, finished


__all__ = [
    "check_broken_links",
]
