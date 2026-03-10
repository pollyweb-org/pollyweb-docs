#!/usr/bin/env python3
"""Publish YouTube videos listed in .tasks/upload-youtube/youtube-upload-map.csv.

Reads OAuth client credentials from .tasks/upload-youtube/tokens.yaml:
  youtube.client_id
  youtube.client_secret

Performs a safe dry run by default. Use --apply to actually update privacy.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from urllib.parse import parse_qs, urlparse
from pathlib import Path
from typing import Iterable

import yaml
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

PROJECT_ROOT = Path(__file__).resolve().parents[2]
YOUTUBE_TOOLS_DIR = Path(__file__).resolve().parent
TOKENS_PATH = YOUTUBE_TOOLS_DIR / "tokens.yaml"
MAP_PATH = YOUTUBE_TOOLS_DIR / "youtube-upload-map.csv"
OAUTH_TOKEN_PATH = YOUTUBE_TOOLS_DIR / "youtube-oauth-token.json"
SCOPES = ["https://www.googleapis.com/auth/youtube"]
WATCH_URL_RE = re.compile(r"(?:v=|youtu\.be/|/shorts/)([A-Za-z0-9_-]{11})")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish mapped YouTube videos in bulk")
    parser.add_argument("--map", type=Path, default=MAP_PATH, help="CSV map path")
    parser.add_argument("--token-file", type=Path, default=OAUTH_TOKEN_PATH, help="OAuth user token file")
    parser.add_argument(
        "--youtube-profile",
        default="testing",
        help="tokens.yaml youtube profile key (e.g. testing, not-working). Empty uses youtube.client_id/client_secret",
    )
    parser.add_argument(
        "--privacy-status",
        choices=["public", "unlisted", "private"],
        default="public",
        help="target privacy status when applying",
    )
    parser.add_argument(
        "--auth-mode",
        choices=["console", "local"],
        default="console",
        help="OAuth flow mode: console shows URL/code prompt; local opens browser callback server",
    )
    parser.add_argument("--apply", action="store_true", help="apply updates (default is dry-run)")
    return parser.parse_args()


def load_client_config(tokens_path: Path, profile: str) -> dict[str, object]:
    data = yaml.safe_load(tokens_path.read_text(encoding="utf-8")) or {}
    youtube = data.get("youtube")
    if not isinstance(youtube, dict):
        raise RuntimeError("tokens.yaml missing youtube section")
    source = youtube
    if profile:
        prof = youtube.get(profile)
        if isinstance(prof, dict):
            source = prof
    client_id = str(source.get("client_id", "")).strip()
    client_secret = str(source.get("client_secret", "")).strip()
    if not client_id or not client_secret:
        raise RuntimeError("tokens.yaml missing youtube.client_id or youtube.client_secret")

    return {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "redirect_uris": ["http://localhost"],
        }
    }


def load_or_authenticate(
    token_file: Path, client_config: dict[str, object], auth_mode: str
) -> Credentials:
    creds: Credentials | None = None
    if token_file.exists():
        creds = Credentials.from_authorized_user_info(
            json.loads(token_file.read_text(encoding="utf-8")),
            SCOPES,
        )

    if creds and creds.valid:
        return creds

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
        if auth_mode == "console":
            flow.redirect_uri = "http://localhost:8080/"
            auth_url, _state = flow.authorization_url(
                access_type="offline",
                include_granted_scopes="true",
                prompt="consent",
            )
            print("Open this URL in your browser, then paste the returned code:")
            print(auth_url)
            code_input = input("Authorization code (or full callback URL): ").strip()
            code = code_input
            if code_input.startswith("http"):
                parsed = urlparse(code_input)
                code = parse_qs(parsed.query).get("code", [""])[0]
            if not code:
                raise RuntimeError("No authorization code found in input")
            flow.fetch_token(code=code)
            creds = flow.credentials
        else:
            creds = flow.run_local_server(port=0, open_browser=True)

    token_file.parent.mkdir(parents=True, exist_ok=True)
    token_file.write_text(creds.to_json(), encoding="utf-8")
    return creds


def iter_video_ids_from_map(map_path: Path) -> Iterable[str]:
    with map_path.open(newline="", encoding="utf-8") as f:
        rows = csv.DictReader(f)
        seen: set[str] = set()
        for row in rows:
            url = (row.get("youtube_url") or "").strip()
            if not url:
                continue
            match = WATCH_URL_RE.search(url)
            if not match:
                continue
            video_id = match.group(1)
            if video_id in seen:
                continue
            seen.add(video_id)
            yield video_id


def chunked(values: list[str], size: int) -> Iterable[list[str]]:
    for i in range(0, len(values), size):
        yield values[i : i + size]


def main() -> int:
    args = parse_args()
    client_config = load_client_config(TOKENS_PATH, args.youtube_profile)
    creds = load_or_authenticate(args.token_file, client_config, args.auth_mode)
    youtube = build("youtube", "v3", credentials=creds)

    video_ids = list(iter_video_ids_from_map(args.map))
    if not video_ids:
        print(f"No youtube_url entries found in {args.map}")
        return 0

    print(f"Found {len(video_ids)} mapped YouTube videos in CSV")
    to_update: list[tuple[str, str]] = []
    status_counts = {"public": 0, "unlisted": 0, "private": 0, "other": 0}

    for ids in chunked(video_ids, 50):
        resp = (
            youtube.videos()
            .list(part="status,snippet", id=",".join(ids), maxResults=50)
            .execute()
        )
        for item in resp.get("items", []):
            video_id = item["id"]
            title = item.get("snippet", {}).get("title", "")
            current = item.get("status", {}).get("privacyStatus", "")
            if current in status_counts:
                status_counts[current] += 1
            else:
                status_counts["other"] += 1
            if current == args.privacy_status:
                continue
            to_update.append((video_id, title))
            print(f"PLAN {video_id} :: {current} -> {args.privacy_status} :: {title}")

    print(
        "Current status counts:"
        f" public={status_counts['public']},"
        f" unlisted={status_counts['unlisted']},"
        f" drafts(private)={status_counts['private']},"
        f" other={status_counts['other']}"
    )

    if not to_update:
        print("Nothing to update.")
        return 0

    if not args.apply:
        print(f"Dry-run only. Would update {len(to_update)} videos.")
        print("Re-run with --apply to perform updates.")
        return 0

    updated = 0
    for video_id, title in to_update:
        body = {"id": video_id, "status": {"privacyStatus": args.privacy_status}}
        youtube.videos().update(part="status", body=body).execute()
        updated += 1
        print(f"UPDATED {video_id} -> {args.privacy_status} :: {title}")

    print(f"Done. Updated {updated} videos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
