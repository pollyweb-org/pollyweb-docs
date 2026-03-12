#!/usr/bin/env python3
"""Upload missing mapped videos and rename mapped YouTube titles from .tasks/upload-youtube/video-index.yaml."""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import json
import re
import threading
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
THREAD_LOCAL = threading.local()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Operate YouTube videos based on map/index")
    p.add_argument("--apply", action="store_true", help="apply changes (default dry-run)")
    p.add_argument("--do-upload", action="store_true", help="upload missing map entries")
    p.add_argument("--do-rename", action="store_true", help="rename mapped videos to original_title")
    p.add_argument("--do-publish", action="store_true", help="set mapped videos to public and not made for kids")
    p.add_argument("--publish-new", action="store_true", help="set uploaded videos privacy to public")
    p.add_argument("--youtube-profile", default="testing", help="tokens.yaml youtube profile")
    p.add_argument("--limit", type=int, default=0, help="limit per operation, 0=unlimited")
    p.add_argument("--upload-limit", type=int, default=0, help="limit uploads, overrides --limit when >0")
    p.add_argument("--upload-workers", type=int, default=4, help="parallel upload workers")
    p.add_argument("--rename-limit", type=int, default=0, help="limit renames, overrides --limit when >0")
    p.add_argument("--publish-limit", type=int, default=0, help="limit publish updates, overrides --limit when >0")
    p.add_argument(
        "--source-title-limit",
        type=int,
        default=0,
        help="max source titles to fetch from youtube_source per run, 0=unlimited",
    )
    p.add_argument(
        "--no-sync-source-titles",
        action="store_true",
        help="skip fetching and persisting source_title from video-index youtube_source URLs",
    )
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


def get_thread_service(token_path: Path) -> object:
    svc = getattr(THREAD_LOCAL, "youtube_service", None)
    svc_key = getattr(THREAD_LOCAL, "youtube_service_key", "")
    key = str(token_path)
    if svc is None or svc_key != key:
        svc = load_service(token_path)
        THREAD_LOCAL.youtube_service = svc
        THREAD_LOCAL.youtube_service_key = key
    return svc


def upload_one_video(
    token_path: Path, path: Path, desired_title: str, privacy: str
) -> tuple[bool, str]:
    youtube = get_thread_service(token_path)
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
        return True, str(resp["id"])
    except HttpError as e:
        return False, str(e)
    except Exception as e:  # noqa: BLE001
        return False, f"{type(e).__name__}: {e}"


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


def load_index_doc(path: Path) -> dict[str, object]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        return {"videos": []}
    videos = data.get("videos")
    if not isinstance(videos, list):
        data["videos"] = []
    return data


def load_index_titles(videos: list[dict[str, object]]) -> dict[str, str]:
    out: dict[str, str] = {}
    for v in videos:
        if not isinstance(v, dict):
            continue
        aid = str(v.get("github_asset_url", "")).rsplit("/", 1)[-1].lower()
        if not aid:
            continue
        title = str(v.get("source_title", "")).strip()
        if not title:
            title = str(v.get("original_title", "")).strip()
        if not title:
            title = Path(str(v.get("filename", ""))).stem
        out[aid] = title[:100]
    return out


def sync_source_titles(
    youtube: object, videos: list[dict[str, object]], max_fetch: int
) -> tuple[bool, int]:
    to_fetch_ids: list[str] = []
    idx_by_video_id: dict[str, list[int]] = {}
    for idx, video in enumerate(videos):
        if not isinstance(video, dict):
            continue
        if str(video.get("source_title", "")).strip():
            continue
        src = str(video.get("youtube_source", "")).strip()
        vid = parse_video_id(src)
        if not vid:
            continue
        if max_fetch and len(to_fetch_ids) >= max_fetch and vid not in idx_by_video_id:
            continue
        if vid not in idx_by_video_id:
            to_fetch_ids.append(vid)
            idx_by_video_id[vid] = []
        idx_by_video_id[vid].append(idx)

    if not to_fetch_ids:
        return False, 0

    id_to_title: dict[str, str] = {}
    for chunk in iter_chunks(to_fetch_ids, 50):
        resp = youtube.videos().list(part="snippet", id=",".join(chunk), maxResults=50).execute()
        for item in resp.get("items", []):
            vid = item.get("id", "")
            title = str(item.get("snippet", {}).get("title", "")).strip()
            if vid and title:
                id_to_title[vid] = title[:100]

    changed = False
    updated = 0
    for vid, indices in idx_by_video_id.items():
        title = id_to_title.get(vid)
        if not title:
            continue
        for idx in indices:
            video = videos[idx]
            if str(video.get("source_title", "")).strip() == title:
                continue
            video["source_title"] = title
            changed = True
            updated += 1
    return changed, updated


def find_local_file(upload_filename: str) -> Path | None:
    direct = VIDEO_ROOT / upload_filename
    if direct.exists():
        return direct
    matches = list(VIDEO_ROOT.rglob(upload_filename))
    if matches:
        return matches[0]
    return None


def fetch_mine_videos(youtube: object) -> dict[str, dict[str, str]]:
    channel = youtube.channels().list(part="contentDetails", mine=True, maxResults=1).execute()
    items = channel.get("items", [])
    if not items:
        return {}
    uploads_playlist = (
        items[0].get("contentDetails", {}).get("relatedPlaylists", {}).get("uploads", "")
    )
    if not uploads_playlist:
        return {}

    ids: list[str] = []
    token = None
    while True:
        resp = (
            youtube.playlistItems()
            .list(
                part="contentDetails",
                playlistId=uploads_playlist,
                maxResults=50,
                pageToken=token,
            )
            .execute()
        )
        for it in resp.get("items", []):
            vid = it.get("contentDetails", {}).get("videoId")
            if vid:
                ids.append(vid)
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
                "made_for_kids": bool(it.get("status", {}).get("madeForKids", False)),
                "self_declared_made_for_kids": bool(
                    it.get("status", {}).get("selfDeclaredMadeForKids", False)
                ),
                "snippet": it.get("snippet", {}),
            }
    return out


def main() -> int:
    args = parse_args()
    _cid, _sec = load_client(TOKENS_PATH, args.youtube_profile)
    youtube = load_service(OAUTH_TOKEN_PATH)
    index_doc = load_index_doc(INDEX_PATH)
    videos = index_doc.get("videos", [])
    if not isinstance(videos, list):
        videos = []
        index_doc["videos"] = videos

    index_changed = False
    if not args.no_sync_source_titles:
        synced_changed, synced_count = sync_source_titles(youtube, videos, args.source_title_limit)
        index_changed = index_changed or synced_changed
        if synced_count:
            print(f"SOURCE_TITLE_SYNCED {synced_count}")

    title_by_asset = load_index_titles(videos)

    with MAP_PATH.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys())

    mine = fetch_mine_videos(youtube)
    by_asset_channel: dict[str, str] = {}
    for vid, meta in mine.items():
        aid = parse_asset_id_from_title(meta["title"])
        if aid and aid not in by_asset_channel:
            by_asset_channel[aid] = vid

    pending_uploads = 0
    pending_renames = 0
    pending_publishes = 0
    for row in rows:
        aid = (row.get("asset_id") or "").lower().strip()
        yt_url = (row.get("youtube_url") or "").strip()
        vid = parse_video_id(yt_url)
        desired = (title_by_asset.get(aid) or "").strip()[:100]

        # Pending upload: no mapped URL and not already discoverable in channel map.
        if aid and not vid and aid not in by_asset_channel:
            upload_name = (row.get("upload_filename") or "").strip()
            path = find_local_file(upload_name) if upload_name else None
            if path:
                pending_uploads += 1

        # Pending rename / publish require an existing mapped video with metadata.
        if not vid:
            continue
        meta = mine.get(vid)
        if not meta:
            continue
        if desired and meta.get("title", "") != desired:
            pending_renames += 1
        if meta.get("privacy", "") != "public" or bool(meta.get("self_declared_made_for_kids", False)):
            pending_publishes += 1

    uploads_done = 0
    rename_done = 0
    publish_done = 0
    touched = False
    upload_limit = args.upload_limit if args.upload_limit > 0 else args.limit
    rename_limit = args.rename_limit if args.rename_limit > 0 else args.limit
    publish_limit = args.publish_limit if args.publish_limit > 0 else args.limit

    if args.do_upload:
        upload_candidates: list[tuple[int, str, Path, str, str]] = []
        for idx, row in enumerate(rows):
            if upload_limit and len(upload_candidates) >= upload_limit:
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
            upload_candidates.append((idx, aid, path, desired_title, privacy))

        if not args.apply:
            uploads_done += len(upload_candidates)
        elif upload_candidates:
            workers = max(1, args.upload_workers)
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
                future_map = {
                    executor.submit(upload_one_video, OAUTH_TOKEN_PATH, path, desired_title, privacy): (idx, aid)
                    for idx, aid, path, desired_title, privacy in upload_candidates
                }
                for future in concurrent.futures.as_completed(future_map):
                    idx, aid = future_map[future]
                    ok, payload = future.result()
                    if ok:
                        vid = payload
                        rows[idx]["youtube_url"] = f"https://www.youtube.com/watch?v={vid}"
                        by_asset_channel[aid] = vid
                        uploads_done += 1
                        touched = True
                        print(f"UPLOADED {vid}")
                    else:
                        print(f"UPLOAD_ERROR {aid}: {payload}")

    if args.do_rename:
        rename_count = 0
        for row in rows:
            if rename_limit and rename_done >= rename_limit:
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
                snippet = dict(meta.get("snippet", {}) or {})
                if not snippet:
                    continue
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

    if args.do_publish:
        publish_count = 0
        for row in rows:
            if publish_limit and publish_done >= publish_limit:
                break
            vid = parse_video_id((row.get("youtube_url") or "").strip())
            if not vid:
                continue
            meta = mine.get(vid)
            if not meta:
                continue

            current_privacy = str(meta.get("privacy", ""))
            current_made_for_kids = bool(meta.get("self_declared_made_for_kids", False))
            if current_privacy == "public" and not current_made_for_kids:
                continue

            print(
                f"PUBLISH {vid}: privacy={current_privacy}, selfDeclaredMadeForKids={current_made_for_kids} -> public,false"
            )
            if not args.apply:
                publish_done += 1
                continue
            try:
                youtube.videos().update(
                    part="status",
                    body={
                        "id": vid,
                        "status": {
                            "privacyStatus": "public",
                            "selfDeclaredMadeForKids": False,
                        },
                    },
                ).execute()
                publish_done += 1
                publish_count += 1
            except HttpError as e:
                print(f"PUBLISH_ERROR {vid}: {e}")
                if "quotaExceeded" in str(e):
                    break
        if args.apply:
            print(f"PUBLISHED_TOTAL {publish_count}")

    if touched:
        with MAP_PATH.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)

    if index_changed:
        INDEX_PATH.write_text(
            yaml.safe_dump(index_doc, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )

    pending_uploads_after = max(0, pending_uploads - uploads_done) if args.apply else pending_uploads
    pending_renames_after = max(0, pending_renames - rename_done) if args.apply else pending_renames
    pending_publishes_after = max(0, pending_publishes - publish_done) if args.apply else pending_publishes

    print(
        f"PENDING uploads={pending_uploads_after} renames={pending_renames_after} publishes={pending_publishes_after}"
    )
    print(
        f"SUMMARY uploads={uploads_done} renames={rename_done} publishes={publish_done} "
        f"pending_uploads={pending_uploads_after} pending_renames={pending_renames_after} "
        f"pending_publishes={pending_publishes_after} apply={args.apply}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
