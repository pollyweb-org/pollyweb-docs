"""Runtime context shared by link replacement helpers."""

from __future__ import annotations

from typing import Iterable, Set

_EXISTING_FILES: Set[str] = set()
_PROJECT_DIR: str = ""


def configure(existing_files: Iterable[str], project_directory: str) -> None:
    """Capture project-wide paths used by replacement routines."""
    global _EXISTING_FILES, _PROJECT_DIR
    _EXISTING_FILES = set(existing_files)
    _PROJECT_DIR = project_directory


def get_existing_files() -> Set[str]:
    """Return the collection of known project files."""
    return _EXISTING_FILES


def get_project_dir() -> str:
    """Return the active project directory root."""
    return _PROJECT_DIR


__all__ = [
    "configure",
    "get_existing_files",
    "get_project_dir",
]
