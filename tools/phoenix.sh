#!/bin/zsh
set -euo pipefail

LOG_FILE="$HOME/.local/share/opencode/log/phoenix.log"
PID_FILE="$HOME/.local/share/opencode/log/phoenix.pid"
PYTHON_BIN="$HOME/anaconda3/envs/ai-builder/bin/python"
CONFIG_FILE="$HOME/.config/opencode/opencode.json"
PLUGIN_MODULE="./plugins/phoenix-otel.ts"

mkdir -p "$HOME/.local/share/opencode/log"

listener_pids() {
  lsof -tiTCP:6006 -sTCP:LISTEN || true
}

wait_for_listeners() {
  local expected="$1"
  local tries=20

  while (( tries > 0 )); do
    local pids
    pids=$(listener_pids)

    if [[ "$expected" == "up" && -n "$pids" ]]; then
      return 0
    fi

    if [[ "$expected" == "down" && -z "$pids" ]]; then
      return 0
    fi

    sleep 0.5
    ((tries--))
  done

  return 1
}

trace_status() {
  node - "$CONFIG_FILE" "$PLUGIN_MODULE" <<'EOF'
const fs = require("fs")

const [configPath, pluginModule] = process.argv.slice(2)
const config = JSON.parse(fs.readFileSync(configPath, "utf8"))
const enabled = config.experimental?.openTelemetry === true
const plugins = Array.isArray(config.plugin) ? config.plugin : []
const pluginEnabled = plugins.some((item) => (Array.isArray(item) ? item[0] : item) === pluginModule)

console.log(`OpenCode trace: ${enabled && pluginEnabled ? "enabled" : "disabled"}`)
EOF
}

update_trace_config() {
  local mode="$1"
  node - "$CONFIG_FILE" "$mode" "$PLUGIN_MODULE" <<'EOF'
const fs = require("fs")

const [configPath, mode, pluginModule] = process.argv.slice(2)
const config = JSON.parse(fs.readFileSync(configPath, "utf8"))

config.experimental ||= {}
config.experimental.openTelemetry = mode === "enable"

const currentPlugins = Array.isArray(config.plugin) ? config.plugin : []
const filteredPlugins = currentPlugins.filter((item) => (Array.isArray(item) ? item[0] : item) !== pluginModule)

if (mode === "enable") {
  filteredPlugins.push(pluginModule)
  config.plugin = filteredPlugins
} else if (filteredPlugins.length > 0) {
  config.plugin = filteredPlugins
} else {
  delete config.plugin
}

fs.writeFileSync(configPath, `${JSON.stringify(config, null, 2)}\n`)
EOF
}

status() {
  trace_status

  local pids
  pids=$(listener_pids)

  if [[ -n "$pids" ]]; then
    local pid
    pid=$(printf '%s\n' "$pids" | head -n 1)
    echo "Phoenix running: pid=$pid"
  elif [[ -f "$PID_FILE" ]]; then
    local pid
    pid=$(<"$PID_FILE")
    echo "Phoenix pid file exists but listener is down: pid=$pid"
  else
    echo "Phoenix not running"
  fi

  lsof -nP -iTCP:6006 -sTCP:LISTEN || true
  lsof -nP -iTCP:4317 -sTCP:LISTEN || true
}

start() {
  if [[ -f "$PID_FILE" ]]; then
    local pid
    pid=$(<"$PID_FILE")
    if kill -0 "$pid" 2>/dev/null; then
      echo "Phoenix already running: pid=$pid"
      exit 0
    fi
  fi

  nohup env PYTHONNOUSERSITE=1 "$PYTHON_BIN" -s -m phoenix.server.main serve > "$LOG_FILE" 2>&1 &
  echo $! > "$PID_FILE"
  local pid
  pid=$(<"$PID_FILE")

  if wait_for_listeners up; then
    echo "Phoenix started: pid=$pid"
  else
    echo "Phoenix start timed out. Check $LOG_FILE"
    exit 1
  fi
}

stop() {
  local pids
  pids=$(listener_pids)

  if [[ ! -f "$PID_FILE" ]]; then
    if [[ -z "$pids" ]]; then
      echo "Phoenix is not running"
      exit 0
    fi
  fi

  if [[ -f "$PID_FILE" ]]; then
    local pid
    pid=$(<"$PID_FILE")
    if kill -0 "$pid" 2>/dev/null; then
      kill "$pid" || true
      echo "Phoenix stopped: pid=$pid"
    else
      echo "Phoenix process already gone: pid=$pid"
    fi
  fi

  pids=$(listener_pids)
  if [[ -n "$pids" ]]; then
    for pid in ${(f)pids}; do
      kill "$pid" || true
      echo "Phoenix stopped listener: pid=$pid"
    done
  fi

  if wait_for_listeners down; then
    :
  else
    echo "Phoenix stop timed out. Check listeners manually."
    exit 1
  fi

  rm -f "$PID_FILE"
}

on() {
  update_trace_config enable
  echo "OpenCode trace enabled"
  start
}

off() {
  update_trace_config disable
  echo "OpenCode trace disabled"
  stop
}

case "${1:-}" in
  on)
    on
    ;;
  off)
    off
    ;;
  start)
    start
    ;;
  stop)
    stop
    ;;
  status)
    status
    ;;
  restart)
    stop || true
    start
    ;;
  *)
    echo "Usage: ./tools/phoenix.sh {on|off|start|stop|status|restart}"
    exit 1
    ;;
esac
