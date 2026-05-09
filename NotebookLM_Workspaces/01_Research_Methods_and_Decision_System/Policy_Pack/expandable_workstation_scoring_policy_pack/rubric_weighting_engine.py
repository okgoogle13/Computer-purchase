#!/usr/bin/env python3
"""
rubric_weighting_engine.py

CareerCopilot hardware MCDA ranking engine.

Ranks shortlist CSVs using the simplified 5-factor policy in AGENTS.md:

  SCORE =
    Performance_Headroom * 0.25 +
    Price_Value          * 0.20 +
    Future_Proof         * 0.20 +
    Portability          * 0.20 +
    Track2_Avoidance     * 0.15

Input rows should come from scripts/build_shortlist.py after live pricing
verification and manual 0-10 MCDA scoring.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
CONFIG_PATH = REPO_ROOT / "config" / "procurement_policy.json"

MCDA_COLUMNS = [
    "Performance_Headroom",
    "Price_Value",
    "Future_Proof",
    "Portability",
    "Track2_Avoidance",
]


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        sys.exit(f"ERROR: Missing config: {CONFIG_PATH}")
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def parse_float(value: object) -> float | None:
    text = str(value or "").strip().replace("$", "").replace(",", "")
    if not text or text.upper() in {"UNKNOWN", "N/A", "NONE", "-"}:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def normalize_track_pathway(row: dict) -> tuple[str, str]:
    track = str(row.get("track", "UNKNOWN")).strip()
    pathway = str(row.get("pathway", "UNKNOWN")).strip()
    key = track.lower().replace(" ", "")

    if key in {"track1", "1"}:
        return "1", pathway
    if key in {"track1a", "1a"}:
        return "1", "1A"
    if key in {"track1b", "1b"}:
        return "1", "1B"
    if key in {"track1.5", "1.5"}:
        return "1.5", pathway
    if key in {"track2", "2"}:
        return "2", pathway
    if key in {"track2a", "2a"}:
        return "2", "A"
    if key in {"track2b", "2b"}:
        return "2", "B"
    if key in {"track2c", "2c"}:
        return "2", "C"
    return track, pathway


def effective_price(row: dict) -> float | None:
    return parse_float(row.get("effective_best_price_aud")) or parse_float(row.get("price_aud"))


def stock_is_confirmed(row: dict) -> bool:
    stock_fields = [
        str(row.get("in_stock_now", "")).strip().lower(),
        str(row.get("au_stock", "")).strip().lower(),
        str(row.get("au_stock_confirmed", "")).strip().lower(),
    ]
    return any(value == "yes" for value in stock_fields)


def has_disqualifying_thermal_flag(row: dict) -> bool:
    values = [
        str(row.get("thermal_flag", "")).strip().lower(),
        str(row.get("thermal_status", "")).strip().lower(),
        str(row.get("thermal_risk", "")).strip().lower(),
    ]
    return any("disqualifying" in value for value in values)


def score_row(row: dict, weights: dict) -> tuple[float | None, list[str]]:
    missing = [col for col in MCDA_COLUMNS if parse_float(row.get(col)) is None]
    if missing:
        return None, missing
    total = sum(parse_float(row[col]) * weights[col] for col in MCDA_COLUMNS)
    return round(total, 3), []


def policy_status(row: dict, config: dict, score: float | None) -> tuple[str, list[str]]:
    track, pathway = normalize_track_pathway(row)
    price = effective_price(row)
    vram = parse_float(row.get("vram_gb"))
    unified = parse_float(row.get("unified_memory_gb"))
    screen = parse_float(row.get("screen_size_in"))
    budget = float(config.get("budget_cap_aud", 5000.0))
    laptop_floor = float(config.get("laptop_discrete_minimum_vram_gb", 16.0))
    unified_floor = float(config.get("laptop_unified_minimum_vram_gb", 16.0))
    desktop_floor = float(config.get("desktop_minimum_vram_gb", 16.0))
    track2_caps = config.get("track2_budget_caps_aud", {})

    blockers: list[str] = []

    if price is None:
        blockers.append("price UNKNOWN")

    if not stock_is_confirmed(row):
        blockers.append("AU stock not confirmed")

    if has_disqualifying_thermal_flag(row):
        blockers.append("disqualifying thermal flag")

    if track == "1" and pathway == "1A":
        if price is not None and price > budget:
            blockers.append(f"price > Track 1 cap ({budget:.0f} AUD)")
        if vram is None:
            blockers.append(f"VRAM below Track 1A floor ({laptop_floor:.0f} GB)")
        elif vram < laptop_floor:
            blockers.append(f"VRAM below Track 1A floor ({laptop_floor:.0f} GB)")
        if screen is None:
            blockers.append("screen size UNKNOWN")
        elif screen < 16:
            blockers.append("screen size below Track 1A floor (16 in)")
    elif track == "1" and pathway == "1B":
        if price is not None and price > budget:
            blockers.append(f"price > Track 1 cap ({budget:.0f} AUD)")
        if unified is None or unified < unified_floor:
            blockers.append(f"unified memory below Track 1B floor ({unified_floor:.0f} GB)")
    elif track == "1.5":
        if vram is None or vram < desktop_floor:
            blockers.append(f"VRAM below Track 1.5 floor ({desktop_floor:.0f} GB)")
    elif track == "2":
        cap = parse_float(track2_caps.get(pathway))
        if cap is not None and price is not None and price > cap:
            blockers.append(f"price > Track 2 {pathway} cap ({cap:.0f} AUD)")
    else:
        blockers.append("track/pathway unresolved")

    if score is None:
        blockers.append("MCDA score incomplete")

    if blockers:
        return "NEEDS_REVIEW", blockers
    return "GOOD_ENOUGH", []


def rank(csv_path: Path, output_csv: Path | None = None) -> int:
    config = load_config()
    weights = config.get("mcda_weights", {})
    missing_weights = [col for col in MCDA_COLUMNS if col not in weights]
    if missing_weights:
        sys.exit(f"ERROR: Missing MCDA weights in config: {', '.join(missing_weights)}")

    with csv_path.open(newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            sys.exit("ERROR: Input CSV has no header.")
        rows = list(reader)
        fieldnames = list(reader.fieldnames)

    for col in MCDA_COLUMNS:
        if col not in fieldnames:
            sys.exit(f"ERROR: Input CSV is missing MCDA column: {col}")
    for col in ["MCDA_Total", "Policy_Status", "Policy_Blockers"]:
        if col not in fieldnames:
            fieldnames.append(col)

    ranked = []
    for row in rows:
        score, missing = score_row(row, weights)
        status, blockers = policy_status(row, config, score)
        if missing:
            blockers = [f"missing MCDA: {', '.join(missing)}", *blockers]
        row["MCDA_Total"] = "" if score is None else f"{score:.3f}"
        row["Policy_Status"] = status
        row["Policy_Blockers"] = "; ".join(dict.fromkeys(blockers))
        ranked.append(row)

    ranked.sort(key=lambda row: parse_float(row.get("MCDA_Total")) or -1, reverse=True)

    print("\nCareerCopilot MCDA Ranking")
    print("=" * 78)
    print("Weights:", ", ".join(f"{col}={weights[col]:.2f}" for col in MCDA_COLUMNS))
    print("-" * 78)
    print(f"{'#':>3}  {'MCDA':>6}  {'Status':<12}  {'Track':<5} {'Path':<5}  Candidate")
    print("-" * 78)
    for idx, row in enumerate(ranked, start=1):
        track, pathway = normalize_track_pathway(row)
        score = row.get("MCDA_Total") or "NA"
        print(f"{idx:>3}  {score:>6}  {row['Policy_Status']:<12}  {track:<5} {pathway:<5}  {row.get('item_name') or row.get('Machine')}")
        if row["Policy_Blockers"]:
            print(f"       blockers: {row['Policy_Blockers']}")

    winners = [row for row in ranked if row["Policy_Status"] == "GOOD_ENOUGH"]
    if winners:
        winner = winners[0]
        print("\n[GOOD ENOUGH] Highest-ranked outcome-enabled candidate:")
        print(f"  {winner.get('item_name') or winner.get('Machine')} ({winner['MCDA_Total']}/10)")
    else:
        print("\nNo candidate currently clears GOOD_ENOUGH. Apply Track Escalation Rule.")

    if output_csv:
        with output_csv.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(ranked)
        print(f"\nRanked CSV written: {output_csv}")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Rank hardware candidates using CareerCopilot MCDA scoring.")
    parser.add_argument("--csv", required=True, help="Path to scored shortlist CSV")
    parser.add_argument("--output-csv", default=None, help="Optional path to write ranked CSV")
    parser.add_argument("--profile", default="merged", help="Accepted for compatibility; MCDA scoring is profile-independent")
    args = parser.parse_args()
    return rank(Path(args.csv), Path(args.output_csv) if args.output_csv else None)


if __name__ == "__main__":
    raise SystemExit(main())
