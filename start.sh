#!/usr/bin/env bash
# start.sh — starts backend (port 9000) and frontend (port 5173) together.
# Usage: ./start.sh

set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  AI-Powered Research Assistant${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# ── Preflight checks ─────────────────────────────────────────────────────────
if [ ! -f "$ROOT/.venv/bin/python" ]; then
  echo "ERROR: Python venv not found at .venv/"
  echo "Run:  python3 -m venv .venv --without-pip && curl -sS https://bootstrap.pypa.io/get-pip.py | .venv/bin/python"
  echo "      .venv/bin/pip install -r backend/requirements.txt"
  exit 1
fi

if [ ! -f "$ROOT/backend/.env" ]; then
  echo "ERROR: backend/.env not found."
  echo "Run:  cp backend/.env.example backend/.env  then add your GOOGLE_API_KEY"
  exit 1
fi

if [ ! -d "$ROOT/frontend/node_modules" ]; then
  echo -e "${YELLOW}node_modules not found — running npm install...${NC}"
  (cd "$ROOT/frontend" && npm install)
fi

# ── Start backend ─────────────────────────────────────────────────────────────
echo -e "\n${GREEN}[1/2] Starting backend on http://localhost:9000${NC}"
"$ROOT/.venv/bin/python" -m uvicorn app.main:app \
  --port 9000 \
  --app-dir "$ROOT/backend" \
  --reload \
  2>&1 | sed 's/^/[backend] /' &
BACKEND_PID=$!

# Wait until backend is healthy (max 10s)
echo -n "      Waiting for backend..."
for i in $(seq 1 20); do
  if curl -s http://localhost:9000/health >/dev/null 2>&1; then
    echo -e " ${GREEN}ready${NC}"
    break
  fi
  sleep 0.5
done

# ── Start frontend ────────────────────────────────────────────────────────────
echo -e "${GREEN}[2/2] Starting frontend on http://localhost:5173${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "  Backend:   http://localhost:9000"
echo -e "  Frontend:  http://localhost:5173"
echo -e "  API docs:  http://localhost:9000/docs"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "  Press ${YELLOW}Ctrl+C${NC} to stop both servers.\n"

(cd "$ROOT/frontend" && npm run dev) &
FRONTEND_PID=$!

# ── Cleanup on Ctrl+C ─────────────────────────────────────────────────────────
cleanup() {
  echo -e "\n${YELLOW}Shutting down...${NC}"
  kill "$BACKEND_PID"  2>/dev/null
  kill "$FRONTEND_PID" 2>/dev/null
  wait "$BACKEND_PID"  2>/dev/null
  wait "$FRONTEND_PID" 2>/dev/null
  echo -e "${GREEN}Done.${NC}"
  exit 0
}
trap cleanup INT TERM

wait
