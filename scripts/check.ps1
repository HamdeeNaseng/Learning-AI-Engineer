# Priority: P1
# Purpose: Local CI-equivalent quality gate.

$ErrorActionPreference = "Stop"

Write-Host "=== Ruff ==="
uv run ruff check .

Write-Host "=== Ruff Format ==="
uv run ruff format --check .

Write-Host "=== Mypy ==="
uv run mypy src tests

Write-Host "=== Pytest ==="
uv run pytest

Write-Host "=== Docker Compose Validation ==="
docker compose config --quiet

Write-Host "=== Docker Build ==="
docker compose build

Write-Host ""
Write-Host "All checks passed."