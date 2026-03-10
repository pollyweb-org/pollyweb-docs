#!/usr/bin/env python3
"""Scan markdown GitHub video assets, build .tasks/upload-youtube/video-index.yaml, and download videos in parallel."""

from __future__ import annotations

import argparse
import concurrent.futures
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = PROJECT_ROOT / ".tasks" / "upload-youtube" / "video-index.yaml"
VIDEO_DIR = PROJECT_ROOT / ".videos"
DONE_DIR = VIDEO_DIR / "done"
CURL_BIN = shutil.which("curl")

ASSET_URL_RE = re.compile(r"https://github\.com/user-attachments/assets/[0-9a-fA-F-]+")
MARKDOWN_LINK_RE = re.compile(
    r"\[(?P<label>[^\]]+)\]\((?P<url>https://github\.com/user-attachments/assets/[0-9a-fA-F-]+)\)"
)
YOUTUBE_RE = re.compile(
    r"https?://(?:www\.)?(?:youtube\.com/watch\?[^\s<)]+|youtu\.be/[^\s<)]+)",
    re.IGNORECASE,
)
VIDEO_EXTS = {".webm", ".mp4", ".mov", ".mkv", ".m4v"}


@dataclass
class Reference:
    markdown_path: str
    line: int
    label: str | None
    asset_url: str
    youtube_url: str | None


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if not path.is_file():
            continue
        if "/.git/" in str(path):
            continue
        if path.parts and path.parts[0] == ".videos":
            continue
        yield path


def sanitize_filename(name: str) -> str:
    clean = name.strip().replace("\\", "/").split("/")[-1].strip()
    clean = re.sub(r"[\x00-\x1f]", "", clean)
    clean = clean.replace(":", "_")
    clean = clean.replace("?", "_")
    clean = clean.replace("*", "_")
    clean = clean.replace('"', "_")
    clean = clean.replace("<", "_").replace(">", "_").replace("|", "_")
    clean = clean.strip(". ")
    return clean or "unnamed.webm"


def pick_youtube(youtube_hits: list[tuple[int, str]], line_no: int) -> str | None:
    if not youtube_hits:
        return None
    return min(youtube_hits, key=lambda item: abs(item[0] - line_no))[1]


def scan_references(root: Path) -> list[Reference]:
    refs: list[Reference] = []

    for md_file in iter_markdown_files(root):
        text = md_file.read_text(encoding="utf-8")
        lines = text.splitlines()
        youtube_hits: list[tuple[int, str]] = []

        for i, line in enumerate(lines, start=1):
            for m in YOUTUBE_RE.finditer(line):
                youtube_hits.append((i, m.group(0)))

        for i, line in enumerate(lines, start=1):
            consumed_spans: list[tuple[int, int]] = []

            for m in MARKDOWN_LINK_RE.finditer(line):
                consumed_spans.append(m.span())
                refs.append(
                    Reference(
                        markdown_path=str(md_file.relative_to(root)),
                        line=i,
                        label=m.group("label"),
                        asset_url=m.group("url"),
                        youtube_url=pick_youtube(youtube_hits, i),
                    )
                )

            for m in ASSET_URL_RE.finditer(line):
                start, end = m.span()
                if any(a <= start and end <= b for a, b in consumed_spans):
                    continue
                refs.append(
                    Reference(
                        markdown_path=str(md_file.relative_to(root)),
                        line=i,
                        label=None,
                        asset_url=m.group(0),
                        youtube_url=pick_youtube(youtube_hits, i),
                    )
                )

    return refs


def derive_filename(ref: Reference) -> tuple[str, str]:
    asset_id = ref.asset_url.rsplit("/", 1)[-1]
    if ref.label:
        label_name = sanitize_filename(ref.label)
        ext = Path(label_name).suffix.lower()
        if ext in VIDEO_EXTS:
            return label_name, "markdown_link_label"
        if ext:
            return f"{label_name}.webm", "markdown_link_label_plus_webm"

    md_stem = sanitize_filename(Path(ref.markdown_path).stem)
    return f"{md_stem}__{asset_id}.webm", "inferred_from_markdown_path"


def build_index(refs: list[Reference]) -> list[dict[str, object]]:
    by_url: dict[str, dict[str, object]] = {}
    used_names: dict[str, str] = {}

    for ref in refs:
        filename, name_source = derive_filename(ref)

        if filename in used_names and used_names[filename] != ref.asset_url:
            stem = Path(filename).stem
            suffix = Path(filename).suffix
            short = ref.asset_url.rsplit("/", 1)[-1][:8]
            filename = f"{stem}__{short}{suffix or '.webm'}"

        used_names[filename] = ref.asset_url

        if ref.asset_url not in by_url:
            by_url[ref.asset_url] = {
                "filename": filename,
                "github_asset_url": ref.asset_url,
                "youtube_source": ref.youtube_url,
                "name_source": name_source,
                "references": [
                    {
                        "markdown_path": ref.markdown_path,
                        "line": ref.line,
                        "label": ref.label,
                    }
                ],
            }
            continue

        current = by_url[ref.asset_url]
        current_refs = current["references"]
        assert isinstance(current_refs, list)
        current_refs.append(
            {"markdown_path": ref.markdown_path, "line": ref.line, "label": ref.label}
        )

        if current.get("youtube_source") is None and ref.youtube_url:
            current["youtube_source"] = ref.youtube_url

        existing_source = current.get("name_source")
        if existing_source and str(existing_source).startswith("inferred") and name_source.startswith(
            "markdown_link_label"
        ):
            current["filename"] = filename
            current["name_source"] = name_source

    return sorted(by_url.values(), key=lambda item: str(item["filename"]).lower())


def yaml_quote(value: str | None) -> str:
    if value is None:
        return "null"
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def write_yaml(index_items: list[dict[str, object]], path: Path) -> None:
    lines = ["videos:"]
    for item in index_items:
        lines.append(f"  - filename: {yaml_quote(str(item['filename']))}")
        lines.append(f"    github_asset_url: {yaml_quote(str(item['github_asset_url']))}")
        lines.append(f"    youtube_source: {yaml_quote(item.get('youtube_source'))}")
        lines.append(f"    name_source: {yaml_quote(str(item.get('name_source', '')))}")
        lines.append("    references:")
        refs = item.get("references", [])
        assert isinstance(refs, list)
        for ref in refs:
            assert isinstance(ref, dict)
            lines.append(f"      - markdown_path: {yaml_quote(str(ref.get('markdown_path', '')))}")
            lines.append(f"        line: {int(ref.get('line', 0))}")
            lines.append(f"        label: {yaml_quote(ref.get('label'))}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def download_one(item: dict[str, object], timeout: int) -> tuple[str, bool, str]:
    filename = str(item["filename"])
    url = str(item["github_asset_url"])
    destination = DONE_DIR / filename
    legacy_destination = VIDEO_DIR / filename

    if destination.exists() and destination.stat().st_size > 0:
        return filename, True, "skipped-existing"
    if legacy_destination.exists() and legacy_destination.stat().st_size > 0:
        DONE_DIR.mkdir(parents=True, exist_ok=True)
        os.replace(legacy_destination, destination)
        return filename, True, "moved-existing"

    DONE_DIR.mkdir(parents=True, exist_ok=True)
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)
    tmp_path = VIDEO_DIR / f"{filename}.part"

    try:
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if CURL_BIN:
            curl_cmd = [
                CURL_BIN,
                "-L",
                "--fail",
                "--silent",
                "--show-error",
                "--connect-timeout",
                "20",
                "--max-time",
                str(timeout),
                "-H",
                "User-Agent: pollyweb-video-sync/1.0",
            ]
            if token:
                curl_cmd.extend(["-H", f"Authorization: Bearer {token}"])
            curl_cmd.extend(["-o", str(tmp_path), url])
            if tmp_path.exists() and tmp_path.stat().st_size > 0:
                curl_cmd.insert(1, "-C")
                curl_cmd.insert(2, "-")

            proc = subprocess.run(
                curl_cmd,
                capture_output=True,
                text=True,
                check=False,
            )
            if proc.returncode != 0:
                msg = proc.stderr.strip() or f"curl exit code {proc.returncode}"
                raise RuntimeError(msg)
        else:
            import urllib.request

            headers = {"User-Agent": "pollyweb-video-sync/1.0"}
            if token:
                headers["Authorization"] = f"Bearer {token}"
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp, tmp_path.open("wb") as out:
                while True:
                    chunk = resp.read(1024 * 1024)
                    if not chunk:
                        break
                    out.write(chunk)

        if not tmp_path.exists() or tmp_path.stat().st_size == 0:
            raise RuntimeError("downloaded file is empty")

        os.replace(tmp_path, destination)
        return filename, True, "downloaded"
    except Exception as exc:  # noqa: BLE001
        if tmp_path.exists():
            tmp_path.unlink(missing_ok=True)
        return filename, False, f"{type(exc).__name__}: {exc}"


def download_all(
    index_items: list[dict[str, object]], workers: int, timeout: int
) -> tuple[int, int, list[tuple[str, str]]]:
    ok_count = 0
    fail_count = 0
    failures: list[tuple[str, str]] = []
    total = len(index_items)
    started_at = time.monotonic()
    last_report_at = started_at

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        pending = {executor.submit(download_one, item, timeout) for item in index_items}
        while pending:
            done, pending = concurrent.futures.wait(
                pending,
                timeout=60,
                return_when=concurrent.futures.FIRST_COMPLETED,
            )

            for future in done:
                filename, ok, info = future.result()
                if ok:
                    ok_count += 1
                else:
                    fail_count += 1
                    failures.append((filename, info))

            now = time.monotonic()
            if now - last_report_at >= 60 and pending:
                finished = ok_count + fail_count
                elapsed = int(now - started_at)
                print(
                    f"Progress: completed={finished}/{total}, success={ok_count}, failed={fail_count}, elapsed={elapsed}s",
                    flush=True,
                )
                last_report_at = now

    return ok_count, fail_count, sorted(failures)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync GitHub user-asset videos to local .videos folder")
    parser.add_argument(
        "--mode",
        choices=["scan", "download", "sync"],
        default="sync",
        help="scan: only build index, download: use fresh scan and download, sync: scan + index + download",
    )
    parser.add_argument("--workers", type=int, default=12, help="parallel download workers")
    parser.add_argument("--timeout", type=int, default=600, help="per-download timeout in seconds")
    parser.add_argument(
        "--allow-missing-404",
        action="store_true",
        help="treat 404 download failures as non-fatal (report-only)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    refs = scan_references(PROJECT_ROOT)
    index_items = build_index(refs)

    write_yaml(index_items, INDEX_PATH)

    inferred = sum(1 for item in index_items if str(item.get("name_source", "")).startswith("inferred"))
    print(f"Indexed {len(index_items)} unique GitHub asset videos")
    print(f"Index file: {INDEX_PATH}")
    print(f"Entries with inferred filename (no markdown filename): {inferred}")

    if args.mode == "scan":
        return 0

    VIDEO_DIR.mkdir(parents=True, exist_ok=True)
    DONE_DIR.mkdir(parents=True, exist_ok=True)
    ok_count, fail_count, failures = download_all(index_items, max(1, args.workers), max(30, args.timeout))
    print(f"Download results: success={ok_count}, failed={fail_count}, target_dir={VIDEO_DIR}")

    if failures:
        missing_404: list[tuple[str, str]] = []
        hard_failures: list[tuple[str, str]] = []
        for filename, reason in failures:
            if "404" in reason:
                missing_404.append((filename, reason))
            else:
                hard_failures.append((filename, reason))

        if missing_404:
            print("Missing assets (404):")
            for filename, reason in missing_404:
                print(f"- {filename}: {reason}")

        if hard_failures:
            print("Failures:")
            for filename, reason in hard_failures:
                print(f"- {filename}: {reason}")
            return 2

        if args.allow_missing_404:
            print(f"Ignored {len(missing_404)} missing 404 assets due to --allow-missing-404")
            return 0

        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
