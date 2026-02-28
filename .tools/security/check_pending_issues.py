#!/usr/bin/env python3
"""Fail when there are unresolved security issues in the local registry."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


PENDING_STATUSES = {"pending", "open", "in_progress", "unresolved"}


def _repo_root() -> Path:
    return Path(os.getcwd())


def _issues_path(root: Path) -> Path:
    configured = os.environ.get("POLLYWEB_SECURITY_PENDING_FILE")
    if configured:
        path = Path(configured)
        return path if path.is_absolute() else root / path
    return root / ".security" / "pending-issues.json"


def _load_payload(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"security-check: invalid JSON in {path}: {exc}")
        raise SystemExit(2) from exc


def _pending_issues(payload: dict) -> list[dict]:
    issues = payload.get("issues")
    if issues is None:
        return []
    if not isinstance(issues, list):
        print("security-check: expected 'issues' to be a list")
        raise SystemExit(2)

    pending: list[dict] = []
    for issue in issues:
        if not isinstance(issue, dict):
            continue
        status = str(issue.get("status", "")).strip().lower()
        if status in PENDING_STATUSES:
            pending.append(issue)
    return pending


def main() -> int:
    root = _repo_root()
    pending_file = _issues_path(root)

    if not pending_file.exists():
        print(f"security-check: no pending issue file at {pending_file}; skipping")
        return 0

    payload = _load_payload(pending_file)
    pending = _pending_issues(payload)

    if not pending:
        print("security-check: no pending security issues")
        return 0

    print("security-check: pending security issues found:")
    for issue in pending:
        issue_id = issue.get("id", "NO-ID")
        title = issue.get("title", "Untitled issue")
        status = str(issue.get("status", "pending")).lower()
        print(f"- {issue_id} [{status}] {title}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
