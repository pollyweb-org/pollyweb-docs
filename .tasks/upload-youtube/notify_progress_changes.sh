#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
TASK_DIR="$ROOT_DIR/.tasks/upload-youtube"
RUNNER_LOG="$TASK_DIR/hourly_rename.log"
STATE_FILE="$TASK_DIR/.notify_state"
NOTIFY_LOG="$TASK_DIR/notify_progress.log"

last_sig=""
if [ -f "$STATE_FILE" ]; then
  last_sig="$(cat "$STATE_FILE" 2>/dev/null || true)"
fi

while true; do
  latest="$(grep -E "RENAMED_TOTAL|SUMMARY uploads=|completed without quotaExceeded|quota exceeded|UPLOAD_ERROR|RENAME_ERROR" "$RUNNER_LOG" 2>/dev/null | tail -n 1 || true)"
  sig="$(printf '%s' "$latest" | shasum | awk '{print $1}')"
  if [ -n "$latest" ] && [ "$sig" != "$last_sig" ]; then
    ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    printf '[%s] %s\n' "$ts" "$latest" >> "$NOTIFY_LOG"
    osascript -e "display notification \"${latest//\"/\\\"}\" with title \"YouTube Upload Task\""
    printf '%s' "$sig" > "$STATE_FILE"
    last_sig="$sig"
  fi
  sleep 300
done
