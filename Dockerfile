# Priority: P0
# Purpose: Reproducible container for the AI Research & Engineering Lab.
#
# GPU workloads: swap the base image for a CUDA-enabled Python image
# (e.g. nvidia/cuda:12.4.1-runtime-ubuntu22.04 + deadsnakes) when a lab
# requires GPU execution; keep this slim image as the CPU-only default.

FROM python:3.12-slim

# P0: Install uv (pinned to match [tool.uv].required-version in pyproject.toml).
COPY --from=ghcr.io/astral-sh/uv:0.12.10 /uv /uvx /usr/local/bin/

ENV UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# P1: Install dependencies first so this layer is cached across code changes.
COPY pyproject.toml uv.lock* ./
RUN uv sync --locked --no-install-project || uv sync --no-install-project

COPY . .
RUN uv sync --locked || uv sync

EXPOSE 8888

CMD ["uv", "run", "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
