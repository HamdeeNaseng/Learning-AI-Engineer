"""P0 - Smoke test verifying the environment matches project requirements."""

import sys


def test_python_version_matches_requirement() -> None:
    assert (sys.version_info.major, sys.version_info.minor) == (3, 12)
