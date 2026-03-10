#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
AGENT_SRC_DIR="$ROOT_DIR/.tasks/upload-youtube/launchd"
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"

labels=(
  "com.pollyweb.youtube.hourly-rename"
  "com.pollyweb.youtube.notify-progress"
  "com.pollyweb.youtube.terminal-digest"
)

usage() {
  cat <<USAGE
Usage: $0 <install|uninstall|restart|status>

install   Copy plists to ~/Library/LaunchAgents and bootstrap/start them
uninstall Bootout agents and remove plists from ~/Library/LaunchAgents
restart   Kickstart all installed agents
status    Show launchctl and process status for all agents
USAGE
}

ensure_dirs() {
  mkdir -p "$LAUNCH_AGENTS_DIR"
}

install_agents() {
  ensure_dirs
  for label in "${labels[@]}"; do
    cp "$AGENT_SRC_DIR/$label.plist" "$LAUNCH_AGENTS_DIR/$label.plist"
    launchctl bootout "gui/$(id -u)/$label" >/dev/null 2>&1 || true
    launchctl bootstrap "gui/$(id -u)" "$LAUNCH_AGENTS_DIR/$label.plist"
    launchctl kickstart -k "gui/$(id -u)/$label"
    echo "installed: $label"
  done
}

uninstall_agents() {
  for label in "${labels[@]}"; do
    launchctl bootout "gui/$(id -u)/$label" >/dev/null 2>&1 || true
    rm -f "$LAUNCH_AGENTS_DIR/$label.plist"
    echo "removed: $label"
  done
}

restart_agents() {
  for label in "${labels[@]}"; do
    launchctl kickstart -k "gui/$(id -u)/$label"
    echo "restarted: $label"
  done
}

status_agents() {
  for label in "${labels[@]}"; do
    echo "--- $label ---"
    launchctl print "gui/$(id -u)/$label" | rg -n "state =|pid =|last exit code =" || true
  done
}

case "${1:-}" in
  install) install_agents ;;
  uninstall) uninstall_agents ;;
  restart) restart_agents ;;
  status) status_agents ;;
  *) usage; exit 1 ;;
esac
