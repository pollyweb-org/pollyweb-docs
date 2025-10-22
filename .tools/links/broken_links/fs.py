"""File discovery helpers for link validation."""

import os


def find_md_files(directory: str) -> list[str]:
    """Recursively locate markdown files beneath the given directory."""
    matches: list[str] = []
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".md"):
                matches.append(os.path.join(root, file_name))
    return matches


def find_png_files(directory: str) -> list[str]:
    """Recursively locate supported binary assets beneath the given directory."""
    matches: list[str] = []
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".png") or file_name.endswith(".jpg") or file_name.endswith(".pdf"):
                matches.append(os.path.join(root, file_name))
    return matches


__all__ = ["find_md_files", "find_png_files"]
