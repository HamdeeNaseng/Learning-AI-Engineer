#!/usr/bin/env bash
# Priority: P1
# Purpose: Bootstrap development environment.
set -euo pipefail

echo "=== Python Project Setup ==="

echo "Installing project Python..."
uv python install

echo "Synchronizing environment..."
uv sync --locked

echo "Validating Python..."
uv run python --version

echo "Validating uv..."
uv --version

echo "Running basic tests..."
uv run pytest

echo
echo "Environment ready."
