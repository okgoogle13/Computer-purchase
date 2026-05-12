#!/usr/bin/env python3
"""Pipeline integrity checks for Phase 2->5 artifacts.

Checks:
- Phase 3a enriched CSV contains pricing metadata columns.
- Ranked CSV contains MCDA + policy/risk output columns.
- Policy_Status / Policy_Blockers are populated.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

PRICING_COLUMNS = {
    "source_platform",
    "seller_class",
    "seller_risk_score",
    "current_best_price_aud",
    "current_best_retailer",
    "current_best_url",
    "in_stock_now",
    "student_discount_possible",
    "cashback_possible",
    "cashback_source",
    "stackable_coupons_confirmed",
    "price_match_possible",
    "price_beat_possible",
    "effective_best_price_aud",
    "promo_notes",
    "pricing_checked_at",
    "warranty_months_confirmed",
    "acl_covered",
}

RANKING_COLUMNS = {
    "Performance_Headroom",
    "Price_Value",
    "Future_Proof",
    "Portability",
    "Track2_Avoidance",
    "MCDA_Total",
    "Policy_Status",
    "Policy_Blockers",
    "Seller_Risk_Multiplier",
    "Source_Platform_Penalty",
    "Risk_Adjustment",
    "Adjusted_MCDA_Total",
}


def read_headers(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError(f"CSV has no headers: {path}")
        return reader.fieldnames


def main() -> None:
    parser = argparse.ArgumentParser(description="Run deterministic integrity checks on pricing + ranked CSV outputs")
    parser.add_argument("--enriched", required=True, help="Path to *_pricing_enriched.csv or *_pricing_enriched_live.csv")
    parser.add_argument("--ranked", required=True, help="Path to *_ranked*.csv")
    args = parser.parse_args()

    enriched = Path(args.enriched)
    ranked = Path(args.ranked)
    if not enriched.exists() or not ranked.exists():
        sys.exit("One or more input CSV files do not exist.")

    errors: list[str] = []

    enriched_headers = set(read_headers(enriched))
    missing_pricing = sorted(PRICING_COLUMNS - enriched_headers)
    if missing_pricing:
        errors.append(f"Missing pricing metadata columns in {enriched}: {', '.join(missing_pricing)}")

    ranked_headers = set(read_headers(ranked))
    missing_ranking = sorted(RANKING_COLUMNS - ranked_headers)
    if missing_ranking:
        errors.append(f"Missing ranking columns in {ranked}: {', '.join(missing_ranking)}")

    with ranked.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        errors.append(f"Ranked CSV has no rows: {ranked}")
    else:
        if not any((row.get("Policy_Status") or "").strip() for row in rows):
            errors.append("Policy_Status is empty for all ranked rows")
        if not any((row.get("Policy_Blockers") or "").strip() for row in rows):
            errors.append("Policy_Blockers is empty for all ranked rows")

    if errors:
        print("Pipeline integrity check FAILED")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)

    print("Pipeline integrity check PASSED")


if __name__ == "__main__":
    main()
