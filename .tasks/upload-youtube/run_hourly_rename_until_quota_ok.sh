#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
PY="$ROOT_DIR/.venv/bin/python3.14"
TASK="$ROOT_DIR/.tasks/upload-youtube/youtube_map_ops.py"
LOG="$ROOT_DIR/.tasks/upload-youtube/hourly_rename.log"
LOCK_DIR="$ROOT_DIR/.tasks/upload-youtube/.runner.lock"
LAST_RUN_FILE="$ROOT_DIR/.tasks/upload-youtube/.last_runner_attempt_epoch"

# Guardrails:
# - Never run more than once per hour even if an external scheduler restarts this.
# - Limit rename operations per run to cap quota spend.
MIN_SECONDS_BETWEEN_ATTEMPTS="${MIN_SECONDS_BETWEEN_ATTEMPTS:-3600}"
RENAME_LIMIT_PER_RUN="${RENAME_LIMIT_PER_RUN:-10}"

TS_NOW="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
NOW_EPOCH="$(date +%s)"

if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  echo "[$TS_NOW] skip: runner lock exists (another invocation active)" >> "$LOG"
  exit 0
fi
cleanup() {
  rmdir "$LOCK_DIR" 2>/dev/null || true
}
trap cleanup EXIT

if [ -f "$LAST_RUN_FILE" ]; then
  LAST_EPOCH="$(cat "$LAST_RUN_FILE" 2>/dev/null || echo 0)"
  if [[ "$LAST_EPOCH" =~ ^[0-9]+$ ]]; then
    DELTA=$((NOW_EPOCH - LAST_EPOCH))
    if [ "$DELTA" -lt "$MIN_SECONDS_BETWEEN_ATTEMPTS" ]; then
      echo "[$TS_NOW] skip: cooldown active (${DELTA}s < ${MIN_SECONDS_BETWEEN_ATTEMPTS}s)" >> "$LOG"
      exit 0
    fi
  fi
fi
printf '%s' "$NOW_EPOCH" > "$LAST_RUN_FILE"

echo "[$TS_NOW] starting guarded rename runner (limit=${RENAME_LIMIT_PER_RUN})" >> "$LOG"
echo "[$TS_NOW] attempt: rename apply" >> "$LOG"

OUT="$("$PY" "$TASK" --do-rename --apply --limit "$RENAME_LIMIT_PER_RUN" 2>&1 || true)"
echo "$OUT" >> "$LOG"

if grep -q "quotaExceeded" <<<"$OUT"; then
  echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] quota exceeded; deferring to next scheduled run" >> "$LOG"
  exit 0
fi

echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] completed without quotaExceeded; waiting for next scheduled run" >> "$LOG"
exit 0
