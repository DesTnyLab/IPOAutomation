#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

: "${POSTGRES_HOST:=postgres}"
: "${POSTGRES_PORT:=5432}"
: "${PG_WAIT_TIMEOUT:=60}"              # seconds to wait for Postgres
: "${CELERY_CONCURRENCY:=4}"            # override via env
: "${CELERY_LOGLEVEL:=info}"            # override via env
: "${CELERY_APP:=core}"                 # your celery app (celery -A $CELERY_APP)

wait_for_postgres() {
  local timeout=$1
  local start
  start=$(date +%s)

  # Prefer pg_isready if available
  if command -v pg_isready >/dev/null 2>&1; then
    until pg_isready -h "${POSTGRES_HOST}" -p "${POSTGRES_PORT}" >/dev/null 2>&1; do
      echo "Waiting for Postgres (pg_isready)..."
      sleep 2
      if [ $(( $(date +%s) - start )) -ge "$timeout" ]; then
        echo "Timed out waiting for Postgres after ${timeout}s" >&2
        return 1
      fi
    done
    return 0
  fi

  # Fallback to nc
  if command -v nc >/dev/null 2>&1; then
    until nc -z "${POSTGRES_HOST}" "${POSTGRES_PORT}"; do
      echo "Waiting for Postgres (nc)..."
      sleep 2
      if [ $(( $(date +%s) - start )) -ge "$timeout" ]; then
        echo "Timed out waiting for Postgres after ${timeout}s" >&2
        return 1
      fi
    done
    return 0
  fi

  echo "Neither pg_isready nor nc found; skipping Postgres wait." >&2
  return 0
}

echo "Starting entrypoint for Celery worker..."
if ! wait_for_postgres "${PG_WAIT_TIMEOUT}"; then
  echo "Postgres did not become available - exiting" >&2
  exit 2
fi

echo "Postgres is available. Starting Celery worker..."
# Replace shell with celery process so signals are forwarded correctly
exec celery -A "${CELERY_APP}" worker \
  --concurrency="${CELERY_CONCURRENCY}" \
  --loglevel="${CELERY_LOGLEVEL}"
