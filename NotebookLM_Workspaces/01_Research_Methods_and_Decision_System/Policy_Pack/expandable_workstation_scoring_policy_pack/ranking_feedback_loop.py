#!/usr/bin/env python3
"""
ranking_feedback_loop.py

Lightweight sanity check for scored MCDA CSVs.

Use this after filling the five MCDA columns and running
rubric_weighting_engine.py. It highlights incomplete scores and close calls
that need human review.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


MCDA_COLUMNS = [
    "Performance_Headroom",
    "Price_Value",
    "Future_Proof",
    "Portability",
    "Track2_Avoidance",
]


def parse_float(value: object) -> float | None:
    text = str(value or "").strip()
    if not text or text.upper() in {"UNKNOWN", "N/A", "NONE", "-"}:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def load_rows(csv_path: Path) -> list[dict]:
    with csv_path.open(newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def candidate_name(row: dict) -> str:
    return row.get("item_name") or row.get("Machine") or row.get("intake_id") or "UNKNOWN"


def run_feedback_loop(csv_path: Path) -> int:
    rows = load_rows(csv_path)
    if not rows:
        print(f"No rows found in {csv_path}")
        return 1

    missing_by_row = []
    scored = []
    for row in rows:
        missing = [col for col in MCDA_COLUMNS if parse_float(row.get(col)) is None]
        if missing:
            missing_by_row.append((candidate_name(row), missing))
        total = parse_float(row.get("MCDA_Total"))
        if total is not None:
            scored.append((total, row))

    print("\nMCDA feedback loop")
    print("=" * 72)

    if missing_by_row:
        print("\nIncomplete MCDA rows:")
        for name, missing in missing_by_row[:20]:
            print(f"  - {name}: {', '.join(missing)}")
        if len(missing_by_row) > 20:
            print(f"  ... {len(missing_by_row) - 20} more")

    if not scored:
        print("\nNo computed MCDA_Total values found. Run rubric_weighting_engine.py first.")
        return 1

    scored.sort(reverse=True, key=lambda item: item[0])
    print("\nTop candidates:")
    for rank, (score, row) in enumerate(scored[:5], start=1):
        status = row.get("Policy_Status", "UNKNOWN")
        print(f"  {rank}. {score:.3f} [{status}] {candidate_name(row)}")

    if len(scored) >= 2 and scored[0][0] - scored[1][0] <= 0.5:
        print("\nClose call: top two candidates are within 0.5 points.")
        print("Review source evidence for thermals, warranty, stock certainty, and Q4 feature headroom.")

    if not any(row.get("Policy_Status") == "GOOD_ENOUGH" for _, row in scored):
        print("\nNo GOOD_ENOUGH candidate found. Apply the Track Escalation Rule in AGENTS.md.")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Review MCDA scoring completeness and close calls.")
    parser.add_argument("--csv", required=True, help="Ranked CSV from rubric_weighting_engine.py")
    args = parser.parse_args()
    return run_feedback_loop(Path(args.csv))


if __name__ == "__main__":
    raise SystemExit(main())
