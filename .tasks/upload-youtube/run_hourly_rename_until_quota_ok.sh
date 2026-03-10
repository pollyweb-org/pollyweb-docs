#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
PY="$ROOT_DIR/.venv/bin/python3.14"
TASK="$ROOT_DIR/.tasks/upload-youtube/youtube_map_ops.py"
LOG="$ROOT_DIR/.tasks/upload-youtube/hourly_rename.log"

echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] starting hourly rename runner" >> "$LOG"

while true; do
  TS="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo "[$TS] attempt: rename apply" >> "$LOG"

  OUT="$("$PY" "$TASK" --do-rename --apply 2>&1 || true)"
  echo "$OUT" >> "$LOG"

  if grep -q "quotaExceeded" <<<"$OUT"; then
    echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] quota exceeded, sleeping 3600s" >> "$LOG"
    sleep 3600
    continue
  fi

  echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] completed without quotaExceeded, stopping runner" >> "$LOG"
  exit 0
done

