"""P1 - Structural validation for Jupyter notebooks.

Does not execute notebooks: some labs need CUDA, large models, or large datasets.
Catches corrupted JSON, missing nbformat, and empty or malformed cells.

Used by both scripts/check.* (local) and .github/workflows/ci.yaml (CI) so that
the local quality gate and CI check exactly the same thing.
"""

import argparse
import json
import sys
from pathlib import Path

VALID_CELL_TYPES = {"markdown", "code", "raw"}


def validate(path: Path) -> list[str]:
    errors: list[str] = []

    try:
        with path.open("r", encoding="utf-8") as file:
            notebook = json.load(file)
    except Exception as exc:  # noqa: BLE001 - report any parse failure, keep scanning
        return [f"{path}: invalid JSON: {exc}"]

    if not isinstance(notebook.get("nbformat"), int):
        errors.append(f"{path}: missing or invalid nbformat")

    cells = notebook.get("cells")
    if not isinstance(cells, list):
        errors.append(f"{path}: missing cells list")
        return errors

    if not cells:
        errors.append(f"{path}: notebook contains no cells")

    for index, cell in enumerate(cells):
        cell_type = cell.get("cell_type")
        if cell_type not in VALID_CELL_TYPES:
            errors.append(f"{path}: cell {index} has invalid type {cell_type!r}")

    print(f"OK  {path}  cells={len(cells)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "roots",
        nargs="*",
        default=["labs"],
        help="directories to scan for .ipynb files (default: labs)",
    )
    args = parser.parse_args()

    notebooks = sorted(notebook for root in args.roots for notebook in Path(root).rglob("*.ipynb"))

    if not notebooks:
        print("No notebooks found.")
        return 0

    errors = [error for path in notebooks for error in validate(path)]

    if errors:
        print("\nNotebook validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"\nValidated {len(notebooks)} notebook(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
