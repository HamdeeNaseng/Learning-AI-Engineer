#!/usr/bin/env bash
# Priority: P1
# Purpose: Local quality gate. Mirrors .github/workflows/ci.yaml, plus mypy.
set -euo pipefail

echo "=== Ruff ==="
uv run ruff check .

echo "=== Ruff Format ==="
uv run ruff format --check .

echo "=== Mypy ==="
# Paths come from [tool.mypy] files in pyproject.toml (shared/src, tests).
uv run mypy

echo "=== Pytest ==="
uv run pytest

echo "=== Notebook Validation ==="
uv run python scripts/validate_notebooks.py labs

echo "=== Dependency Lock ==="
uv lock --check

echo "=== Docker Compose Validation ==="
docker compose config --quiet

echo
echo "All checks passed."
