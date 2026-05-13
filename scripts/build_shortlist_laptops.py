#!/usr/bin/env python3
"""Wrapper: build shortlist for laptop products."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    cmd = [sys.executable, "scripts/build_shortlist.py", "--profile", "laptop", *sys.argv[1:]]
    return subprocess.run(cmd, cwd=REPO_ROOT).returncode


if __name__ == "__main__":
    raise SystemExit(main())
