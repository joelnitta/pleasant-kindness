#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

# Use SQLite locally so no Postgres connection is needed
export PGDATABASE=""
export PGUSER=""
export PGPASSWORD=""
export PGHOST=""
export PGPORT=""

echo "Starting local dev server at http://127.0.0.1:8000"
echo "Press Ctrl-C to stop."
echo ""

python manage.py runserver
