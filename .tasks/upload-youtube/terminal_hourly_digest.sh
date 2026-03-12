#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
TASK_DIR="$ROOT_DIR/.tasks/upload-youtube"
RUNNER_LOG="$TASK_DIR/hourly_rename.log"
DIGEST_LOG="$TASK_DIR/terminal_progress.log"
PID_FILE="$TASK_DIR/hourly_rename.pid"

emit() {
  ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  pid="none"
  status="stopped"
  if [ -f "$PID_FILE" ]; then
    pid="$(cat "$PID_FILE" 2>/dev/null || true)"
    if [ -n "$pid" ] && ps -p "$pid" >/dev/null 2>&1; then
      status="running"
    fi
  fi
  last="$(grep -E "PENDING uploads=|RENAMED_TOTAL|PUBLISHED_TOTAL|SUMMARY uploads=|finished: no more upload/rename/publish work found|completed without quotaExceeded|quota exceeded|UPLOAD_ERROR|RENAME_ERROR|PUBLISH_ERROR" "$RUNNER_LOG" 2>/dev/null | tail -n 1 || true)"
  printf '[%s] runner=%s pid=%s\n' "$ts" "$status" "$pid" >> "$DIGEST_LOG"
  if [ -n "$last" ]; then
    printf '[%s] last: %s\n' "$ts" "$last" >> "$DIGEST_LOG"
  fi
}

emit
while true; do
  sleep 3600
  emit
done
