#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
TASK_DIR="$ROOT_DIR/.tasks/upload-youtube"
RUNNER_LOG="$TASK_DIR/hourly_rename.log"
MONITOR_LOG="$TASK_DIR/hourly_progress.log"
PID_FILE="$TASK_DIR/hourly_rename.pid"

snapshot() {
  local ts pid status summary_line rename_events upload_events quota_events
  ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  pid="none"
  status="not-running"
  if [ -f "$PID_FILE" ]; then
    pid="$(cat "$PID_FILE" 2>/dev/null || true)"
    if [ -n "$pid" ] && ps -p "$pid" >/dev/null 2>&1; then
      status="running"
    fi
  fi
  summary_line="$(grep -E "PENDING uploads=|SUMMARY uploads=|RENAMED_TOTAL|PUBLISHED_TOTAL|finished: no more upload/rename/publish work found|completed without quotaExceeded|quota exceeded" "$RUNNER_LOG" 2>/dev/null | tail -n 1 || true)"
  rename_events="$(grep -c "^RENAME " "$RUNNER_LOG" 2>/dev/null || true)"
  upload_events="$(grep -c "^UPLOADED " "$RUNNER_LOG" 2>/dev/null || true)"
  quota_events="$(grep -c "quotaExceeded" "$RUNNER_LOG" 2>/dev/null || true)"
  printf '[%s] pid=%s status=%s rename_events=%s upload_events=%s quota_mentions=%s\n' "$ts" "$pid" "$status" "$rename_events" "$upload_events" "$quota_events" >> "$MONITOR_LOG"
  if [ -n "$summary_line" ]; then
    printf '[%s] last_status: %s\n' "$ts" "$summary_line" >> "$MONITOR_LOG"
  fi
}

snapshot
while true; do
  sleep 3600
  snapshot
done
