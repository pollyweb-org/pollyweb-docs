#!/usr/bin/env bash
set -euo pipefail

SECRET_REGEX='(ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{20,}|AIza[0-9A-Za-z_-]{20,}|sk-[A-Za-z0-9_-]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|-----BEGIN (RSA|EC|OPENSSH|DSA|PRIVATE) KEY-----|[[:<:]](api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|oauth[_-]?(token|secret))[[:space:]]*[:=][[:space:]]*[\"'\'']?[A-Za-z0-9_./+=:-]{12,})'

is_blocked_secret_path() {
  local p="$1"
  case "$p" in
    .tools/youtube-oauth-token.json|.tools/youtube/tokens.yaml|tokens.yaml|*.pem|*.key|*.p12|*.pfx|*.jks|*.kdbx)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

check_paths_for_blocked_files() {
  local files=("$@")
  local blocked=()
  local f
  for f in "${files[@]}"; do
    if is_blocked_secret_path "$f"; then
      blocked+=("$f")
    fi
  done

  if (( ${#blocked[@]} > 0 )); then
    echo "❌ Secret guard: blocked file path(s) detected:"
    printf ' - %s\n' "${blocked[@]}"
    echo "Add these files to .gitignore and keep secrets outside the repository."
    return 1
  fi

  return 0
}

check_patch_for_secret_patterns() {
  local patch_text="$1"

  if printf '%s\n' "$patch_text" | grep -E -i -- "$SECRET_REGEX" >/dev/null; then
    echo "❌ Secret guard: detected potential secret pattern in staged/pushed content."
    echo "Review token/key/secret changes before committing or pushing."
    printf '%s\n' "$patch_text" | grep -E -i -- "$SECRET_REGEX" | head -n 5 | sed 's/^/  > /'
    return 1
  fi

  return 0
}
