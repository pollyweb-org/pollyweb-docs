#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
PY="$ROOT_DIR/.venv/bin/python3.14"
TASK="$ROOT_DIR/.tasks/upload-youtube/youtube_map_ops.py"
LOG="$ROOT_DIR/.tasks/upload-youtube/hourly_rename.log"
LOCK_DIR="$ROOT_DIR/.tasks/upload-youtube/.runner.lock"
LOCK_PID_FILE="$LOCK_DIR/pid"
LOCK_CMD_FILE="$LOCK_DIR/cmd"

# Guardrails:
# - Limit upload/rename operations per run to cap quota spend.
RENAME_LIMIT_PER_RUN="${RENAME_LIMIT_PER_RUN:-10}"
UPLOAD_LIMIT_PER_RUN="${UPLOAD_LIMIT_PER_RUN:-3}"
PUBLISH_LIMIT_PER_RUN="${PUBLISH_LIMIT_PER_RUN:-20}"
SLEEP_ON_QUOTA_SECONDS="${SLEEP_ON_QUOTA_SECONDS:-3600}"

TS_NOW="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

is_live_runner_pid() {
  local pid="$1"
  if [ -z "$pid" ] || ! [[ "$pid" =~ ^[0-9]+$ ]]; then
    return 1
  fi
  if ! ps -p "$pid" >/dev/null 2>&1; then
    return 1
  fi
  local cmd
  cmd="$(ps -p "$pid" -o command= 2>/dev/null || true)"
  [[ "$cmd" == *"run_hourly_rename_until_quota_ok.sh"* ]]
}

if [ -d "$LOCK_DIR" ]; then
  LOCK_PID="$(cat "$LOCK_PID_FILE" 2>/dev/null || true)"
  if is_live_runner_pid "$LOCK_PID"; then
    echo "[$TS_NOW] skip: runner lock exists (active pid=$LOCK_PID)" >> "$LOG"
    exit 0
  fi
  echo "[$TS_NOW] stale lock detected (pid=${LOCK_PID:-unknown}); removing stale lock" >> "$LOG"
  rm -rf "$LOCK_DIR"
fi

if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  echo "[$TS_NOW] skip: failed to acquire runner lock" >> "$LOG"
  exit 0
fi
printf '%s' "$$" > "$LOCK_PID_FILE"
printf '%s' "$0" > "$LOCK_CMD_FILE"
cleanup() {
  rmdir "$LOCK_DIR" 2>/dev/null || true
  rm -rf "$LOCK_DIR" 2>/dev/null || true
}
trap cleanup EXIT

echo "[$TS_NOW] starting guarded upload+rename+publish runner (upload_limit=${UPLOAD_LIMIT_PER_RUN}, rename_limit=${RENAME_LIMIT_PER_RUN}, publish_limit=${PUBLISH_LIMIT_PER_RUN})" >> "$LOG"
while true; do
  TS="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo "[$TS] attempt: upload+rename+publish apply" >> "$LOG"

  OUT="$("$PY" "$TASK" --do-upload --do-rename --do-publish --apply --upload-limit "$UPLOAD_LIMIT_PER_RUN" --rename-limit "$RENAME_LIMIT_PER_RUN" --publish-limit "$PUBLISH_LIMIT_PER_RUN" 2>&1 || true)"
  echo "$OUT" >> "$LOG"

  if grep -q "quotaExceeded" <<<"$OUT"; then
    echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] quota exceeded; sleeping ${SLEEP_ON_QUOTA_SECONDS}s before retry" >> "$LOG"
    sleep "$SLEEP_ON_QUOTA_SECONDS"
    continue
  fi

  SUMMARY_LINE="$(grep -E "SUMMARY uploads=[0-9]+ renames=[0-9]+ publishes=[0-9]+" <<<"$OUT" | tail -n 1 || true)"
  UPLOADS="$(sed -nE 's/.*uploads=([0-9]+).*/\1/p' <<<"$SUMMARY_LINE")"
  RENAMES="$(sed -nE 's/.*renames=([0-9]+).*/\1/p' <<<"$SUMMARY_LINE")"
  PUBLISHES="$(sed -nE 's/.*publishes=([0-9]+).*/\1/p' <<<"$SUMMARY_LINE")"
  UPLOADS="${UPLOADS:-0}"
  RENAMES="${RENAMES:-0}"
  PUBLISHES="${PUBLISHES:-0}"

  if [ "$UPLOADS" -eq 0 ] && [ "$RENAMES" -eq 0 ] && [ "$PUBLISHES" -eq 0 ]; then
    echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] finished: no more upload/rename/publish work found" >> "$LOG"
    exit 0
  fi

  echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] progress detected (uploads=${UPLOADS}, renames=${RENAMES}, publishes=${PUBLISHES}); continuing immediately" >> "$LOG"
done
