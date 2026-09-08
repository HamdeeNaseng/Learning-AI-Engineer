# Priority: P1
# Purpose: Bootstrap development environment.

$ErrorActionPreference = "Stop"

Write-Host "=== Python Project Setup ==="

Write-Host "Installing project Python..."
uv python install

Write-Host "Synchronizing environment..."
uv sync --locked

Write-Host "Validating Python..."
uv run python --version

Write-Host "Validating uv..."
uv --version

Write-Host "Running basic tests..."
uv run pytest

Write-Host ""
Write-Host "Environment ready."