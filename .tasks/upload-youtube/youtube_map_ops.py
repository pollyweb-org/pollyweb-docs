#!/usr/bin/env python3
"""Upload missing mapped videos and rename mapped YouTube titles from .tasks/upload-youtube/video-index.yaml."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Iterable

import yaml
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

PROJECT_ROOT = Path(__file__).resolve().parents[2]
YOUTUBE_TOOLS_DIR = Path(__file__).resolve().parent
TOKENS_PATH = YOUTUBE_TOOLS_DIR / "tokens.yaml"
INDEX_PATH = YOUTUBE_TOOLS_DIR / "video-index.yaml"
MAP_PATH = YOUTUBE_TOOLS_DIR / "youtube-upload-map.csv"
OAUTH_TOKEN_PATH = YOUTUBE_TOOLS_DIR / "youtube-oauth-token.json"
VIDEO_ROOT = PROJECT_ROOT / ".videos" / "done"
SCOPES = ["https://www.googleapis.com/auth/youtube"]
URL_RE = re.compile(r"(?:v=|youtu\.be/|/shorts/)([A-Za-z0-9_-]{11})")
UUID_RE = re.compile(
    r"([0-9a-fA-F]{8})[^0-9a-fA-F]+([0-9a-fA-F]{4})[^0-9a-fA-F]+([0-9a-fA-F]{4})[^0-9a-fA-F]+([0-9a-fA-F]{4})[^0-9a-fA-F]+([0-9a-fA-F]{12})"
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Operate YouTube videos based on map/index")
    p.add_argument("--apply", action="store_true", help="apply changes (default dry-run)")
    p.add_argument("--do-upload", action="store_true", help="upload missing map entries")
    p.add_argument("--do-rename", action="store_true", help="rename mapped videos to original_title")
    p.add_argument("--publish-new", action="store_true", help="set uploaded videos privacy to public")
    p.add_argument("--youtube-profile", default="testing", help="tokens.yaml youtube profile")
    p.add_argument("--limit", type=int, default=0, help="limit per operation, 0=unlimited")
    return p.parse_args()


def load_client(tokens_path: Path, profile: str) -> tuple[str, str]:
    data = yaml.safe_load(tokens_path.read_text(encoding="utf-8")) or {}
    yt = data.get("youtube")
    if not isinstance(yt, dict):
        raise RuntimeError("tokens.yaml missing youtube section")
    source = yt.get(profile) if profile else yt
    if not isinstance(source, dict):
        source = yt
    cid = str(source.get("client_id", "")).strip()
    sec = str(source.get("client_secret", "")).strip()
    if not cid or not sec:
        raise RuntimeError("Missing youtube client_id/client_secret")
    return cid, sec


def load_service(token_path: Path) -> object:
    creds = Credentials.from_authorized_user_info(
        json.loads(token_path.read_text(encoding="utf-8")),
        SCOPES,
    )
    return build("youtube", "v3", credentials=creds)


def iter_chunks(values: list[str], size: int) -> Iterable[list[str]]:
    for i in range(0, len(values), size):
        yield values[i : i + size]


def parse_video_id(url: str) -> str | None:
    m = URL_RE.search(url)
    return m.group(1) if m else None


def parse_asset_id_from_title(title: str) -> str | None:
    m = UUID_RE.search(title)
    if not m:
        return None
    return "-".join(g.lower() for g in m.groups())


def load_index_titles(path: Path) -> dict[str, str]:
    videos = (yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get("videos", [])
    out: dict[str, str] = {}
    for v in videos:
        if not isinstance(v, dict):
            continue
        aid = str(v.get("github_asset_url", "")).rsplit("/", 1)[-1].lower()
        if not aid:
            continue
        title = str(v.get("original_title", "")).strip()
        if not title:
            title = Path(str(v.get("filename", ""))).stem
        out[aid] = title[:100]
    return out


def find_local_file(upload_filename: str) -> Path | None:
    direct = VIDEO_ROOT / upload_filename
    if direct.exists():
        return direct
    matches = list(VIDEO_ROOT.rglob(upload_filename))
    if matches:
        return matches[0]
    return None


def fetch_mine_videos(youtube: object) -> dict[str, dict[str, str]]:
    ids: list[str] = []
    token = None
    while True:
        resp = (
            youtube.search()
            .list(part="id", forMine=True, type="video", maxResults=50, pageToken=token)
            .execute()
        )
        ids.extend(it["id"]["videoId"] for it in resp.get("items", []))
        token = resp.get("nextPageToken")
        if not token:
            break
    ids = list(dict.fromkeys(ids))

    out: dict[str, dict[str, str]] = {}
    for chunk in iter_chunks(ids, 50):
        resp = youtube.videos().list(part="snippet,status", id=",".join(chunk), maxResults=50).execute()
        for it in resp.get("items", []):
            out[it["id"]] = {
                "title": it.get("snippet", {}).get("title", ""),
                "privacy": it.get("status", {}).get("privacyStatus", ""),
            }
    return out


def main() -> int:
    args = parse_args()
    _cid, _sec = load_client(TOKENS_PATH, args.youtube_profile)
    youtube = load_service(OAUTH_TOKEN_PATH)
    title_by_asset = load_index_titles(INDEX_PATH)

    with MAP_PATH.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys())

    mine = fetch_mine_videos(youtube)
    by_asset_channel: dict[str, str] = {}
    for vid, meta in mine.items():
        aid = parse_asset_id_from_title(meta["title"])
        if aid and aid not in by_asset_channel:
            by_asset_channel[aid] = vid

    uploads_done = 0
    rename_done = 0
    touched = False

    if args.do_upload:
        for row in rows:
            if args.limit and uploads_done >= args.limit:
                break
            aid = (row.get("asset_id") or "").lower().strip()
            if not aid:
                continue
            # already mapped
            if parse_video_id((row.get("youtube_url") or "").strip()):
                continue
            # exists in channel, just map it
            existing = by_asset_channel.get(aid)
            if existing:
                row["youtube_url"] = f"https://www.youtube.com/watch?v={existing}"
                touched = True
                continue
            upload_name = (row.get("upload_filename") or "").strip()
            if not upload_name:
                continue
            path = find_local_file(upload_name)
            if not path:
                continue
            desired_title = title_by_asset.get(aid, Path(upload_name).stem)[:100]
            privacy = "public" if args.publish_new else "private"
            print(f"UPLOAD {path.name} -> {desired_title} ({privacy})")
            if not args.apply:
                uploads_done += 1
                continue
            try:
                req = youtube.videos().insert(
                    part="snippet,status",
                    body={
                        "snippet": {"title": desired_title},
                        "status": {"privacyStatus": privacy},
                    },
                    media_body=MediaFileUpload(str(path), resumable=True),
                )
                resp = req.execute()
                vid = resp["id"]
                row["youtube_url"] = f"https://www.youtube.com/watch?v={vid}"
                by_asset_channel[aid] = vid
                uploads_done += 1
                touched = True
                print(f"UPLOADED {vid}")
            except HttpError as e:
                print(f"UPLOAD_ERROR {aid}: {e}")
                if "quotaExceeded" in str(e):
                    break

    if args.do_rename:
        rename_count = 0
        for row in rows:
            if args.limit and rename_done >= args.limit:
                break
            aid = (row.get("asset_id") or "").lower().strip()
            desired = (title_by_asset.get(aid) or "").strip()
            if not desired:
                continue
            vid = parse_video_id((row.get("youtube_url") or "").strip())
            if not vid:
                continue
            meta = mine.get(vid)
            if not meta:
                continue
            current = meta["title"]
            if current == desired:
                continue
            print(f"RENAME {vid}: {current} -> {desired}")
            if not args.apply:
                rename_done += 1
                continue
            try:
                full = youtube.videos().list(part="snippet", id=vid).execute()
                items = full.get("items", [])
                if not items:
                    continue
                snippet = items[0].get("snippet", {})
                snippet["title"] = desired[:100]
                youtube.videos().update(part="snippet", body={"id": vid, "snippet": snippet}).execute()
                rename_done += 1
                rename_count += 1
            except HttpError as e:
                print(f"RENAME_ERROR {vid}: {e}")
                if "quotaExceeded" in str(e):
                    break
        if args.apply:
            print(f"RENAMED_TOTAL {rename_count}")

    if touched:
        with MAP_PATH.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)

    print(f"SUMMARY uploads={uploads_done} renames={rename_done} apply={args.apply}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
