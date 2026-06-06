#!/usr/bin/env python3
"""
fill_mcda_gaps.py

Fills the following gaps in the shortlist CSV before re-running the scoring engine:

  1. Upgrade_Ceiling  — derived from vram_gb / unified_memory_gb / gpu_model / profile.
  2. track / pathway  — inferred from profile + category for rows where both are UNKNOWN.
  3. in_stock_now     — backfilled from au_stock where missing.
  4. Performance_Headroom, Future_Proof, Price_Value, Portability, Track2_Avoidance
     — computed where still blank using spec-driven rubric rules from AGENTS.md.

Output: shortlists/<date>_shortlist_mcda_filled.csv
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from datetime import date

REPO_ROOT = Path(__file__).resolve().parent.parent
BUDGET_CAP = 5000.0


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def pf(val: object) -> float | None:
    """Parse float from messy string."""
    text = str(val or "").strip().replace("$", "").replace(",", "")
    if not text or text.upper() in {"UNKNOWN", "N/A", "NONE", "-"}:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def clamp(v: float, lo: float = 0.0, hi: float = 10.0) -> float:
    return max(lo, min(hi, v))


def is_empty(val: object) -> bool:
    return str(val or "").strip() in ("", "UNKNOWN", "N/A", "NONE", "-")


# ---------------------------------------------------------------------------
# Upgrade_Ceiling derivation
# ---------------------------------------------------------------------------

WORKSTATION_KEYWORDS = ["RTX PRO", "RTX 6000", "RTX 5000 ADA", "A6000", "A5000",
                        "A4500", "A4000", "QUADRO", "RADEON PRO W", "ARC PRO"]

def derive_upgrade_ceiling(row: dict) -> float:
    """
    Upgrade_Ceiling: how much GPU upgrade headroom exists in this platform?
    Scale 0–10.

    Laptop       → low ceiling (soldered GPU in most cases)
    Desktop/WS   → high ceiling (swappable GPU)
    Component GPU → not applicable (score as platform-agnostic future value)
    Strix Halo   → moderate (unified, no discrete upgrade path)
    """
    profile = str(row.get("profile", "")).strip()
    cat_group = str(row.get("Category_Group", "")).strip()
    gpu_model = str(row.get("gpu_model", "")).upper()
    item_name = str(row.get("item_name", "")).upper()
    vram = pf(row.get("vram_gb")) or 0.0
    unified = pf(row.get("unified_memory_gb")) or 0.0
    max_mem = max(vram, unified)

    # Component GPUs — score on raw performance potential, not upgrade path
    if cat_group in ("Standalone_GPU", "Workstation_GPU"):
        if max_mem >= 48:
            return 10.0
        if max_mem >= 32:
            return 9.0
        if max_mem >= 24:
            return 8.0
        if max_mem >= 16:
            return 6.0
        return 4.0

    # Strix Halo / unified memory laptops — no discrete GPU upgrade path
    strix_signals = ["STRIX HALO", "RYZEN AI MAX", "RADEON 890M", "RADEON 8060S",
                     "HN6306", "PROART PX13", "HP Z2 MINI G1A", "OMEN MAX 16",
                     "TUF GAMING A14", "TUF A14", "TUF A16 STRIX"]
    is_strix = any(sig in gpu_model or sig in item_name for sig in strix_signals)
    if unified >= 32 or is_strix:
        # Strix Halo: upgrade ceiling is moderate — can't swap GPU
        if unified >= 128:
            return 6.0
        if unified >= 64:
            return 5.0
        if unified >= 32:
            return 4.0
        return 3.0

    # Laptops with discrete GPU — essentially no upgrade path
    if profile in ("Laptop", "Mini PC"):
        # Score purely on current VRAM tier (future sufficiency)
        if vram >= 24:
            return 4.0   # good now, but no upgrade path
        if vram >= 16:
            return 3.0
        if vram >= 12:
            return 2.0
        return 1.0

    # Desktops — real upgrade ceiling
    if profile == "Desktop":
        # Workstation-class chassis: excellent upgrade path
        workstation_signals = ["THINKSTATION", "PRECISION", "Z4", "Z8", "XEON",
                               "ZBOOK", "HP Z", "DELL T", "POWER EDGE"]
        is_ws = any(sig in item_name for sig in workstation_signals)
        if is_ws:
            return 9.0   # can slot any GPU, PCIe x16, high-wattage PSU
        # Standard desktop / gaming tower
        if vram >= 24:
            return 8.0
        if vram >= 16:
            return 7.0
        if vram >= 12:
            return 6.0
        return 5.0

    # Fallback
    if max_mem >= 24:
        return 5.0
    if max_mem >= 16:
        return 4.0
    return 3.0


# ---------------------------------------------------------------------------
# Track / Pathway inference
# ---------------------------------------------------------------------------

def infer_track_pathway(row: dict) -> tuple[str, str]:
    """Return (track, pathway) inferred from profile/category/specs."""
    profile = str(row.get("profile", "")).strip()
    category = str(row.get("category", "")).lower()
    gpu_model = str(row.get("gpu_model", "")).upper()
    cat_group = str(row.get("Category_Group", "")).strip()
    item_name = str(row.get("item_name", "")).upper()
    vram = pf(row.get("vram_gb")) or 0.0
    unified = pf(row.get("unified_memory_gb")) or 0.0

    # Already set — return as-is after normalizing
    t = str(row.get("track", "")).strip()
    p = str(row.get("pathway", "")).strip()
    if not is_empty(t) and not is_empty(p):
        return t, p

    # Component GPUs → Track 2B (add-in card to a workstation)
    if cat_group in ("Standalone_GPU", "Workstation_GPU"):
        return "2", "B"

    # Strix Halo laptops → Track 1B
    strix_signals = ["STRIX HALO", "RYZEN AI MAX", "RADEON 890M", "RADEON 8060S",
                     "PROART PX13", "HP Z2 MINI G1A", "OMEN MAX 16",
                     "TUF GAMING A14", "TUF A14", "ASUS TUF A16"]
    is_strix = any(sig in gpu_model or sig in item_name for sig in strix_signals)
    if profile in ("Laptop", "Mini PC") and (unified >= 32 or is_strix):
        return "1", "1B"

    # Standard discrete GPU laptop → Track 1A
    if profile in ("Laptop",):
        return "1", "1A"

    # Mini PC with unified → 1B or 2C depending on unified memory
    if profile == "Mini PC":
        if unified >= 32:
            return "2", "C"
        return "1", "1B"

    # Desktop / workstation systems
    if profile == "Desktop":
        # Refurbished enterprise workstation signals → Track 2B
        ws_signals = ["THINKSTATION", "PRECISION", "HP Z4", "HP Z8", "XEON",
                      "RECOMPUTE", "ACT DELL", "AURORA"]
        if any(sig in item_name for sig in ws_signals):
            return "2", "B"
        # Track 1.5 — refurb single GPU desktop
        refurb_signals = ["REFURB", "REFURBISH", "USED", "EX-DEMO", "EXDEMO"]
        if any(sig in item_name for sig in refurb_signals):
            return "1.5", "UNKNOWN"
        # New custom/prebuilt desktop
        if vram >= 16:
            return "1.5", "UNKNOWN"
        return "2", "B"

    # Fallback
    return "UNKNOWN", "UNKNOWN"


# ---------------------------------------------------------------------------
# Spec-driven MCDA scores (only applied when column is blank)
# ---------------------------------------------------------------------------

def derive_performance_headroom(row: dict) -> float:
    """AGENTS.md Performance_Headroom scale, capped at 7 for Strix Halo."""
    vram = pf(row.get("vram_gb")) or 0.0
    unified = pf(row.get("unified_memory_gb")) or 0.0
    gpu = str(row.get("gpu_model", "")).upper()
    item = str(row.get("item_name", "")).upper()

    strix_signals = ["STRIX HALO", "RYZEN AI MAX", "RADEON 8060S", "RADEON 890M",
                     "PROART PX13", "TUF A14", "TUF GAMING A14", "OMEN MAX"]

    is_strix = any(sig in gpu or sig in item for sig in strix_signals)

    max_mem = max(vram, unified)

    if max_mem >= 48:
        score = 10.0
    elif max_mem >= 32:
        score = 9.0
    elif max_mem >= 24:
        score = 9.0
    elif max_mem >= 16:
        score = 7.0
    elif max_mem >= 12:
        score = 5.0
    elif max_mem >= 8:
        score = 3.0
    else:
        score = 1.0

    # Strix Halo cap per AGENTS.md: <= 7 unless benchmark evidence shows more
    if is_strix:
        score = min(score, 7.0)

    return clamp(score)


def derive_future_proof(row: dict) -> float:
    """AGENTS.md Future_Proof scale."""
    vram = pf(row.get("vram_gb")) or 0.0
    unified = pf(row.get("unified_memory_gb")) or 0.0
    max_mem = max(vram, unified)
    if max_mem >= 32:
        return 9.0
    if max_mem >= 24:
        return 9.0
    if max_mem >= 16:
        return 7.0
    if max_mem >= 12:
        return 5.0
    if max_mem >= 8:
        return 3.0
    return 2.0


def derive_price_value(row: dict) -> float:
    """Score Price_Value based on price relative to VRAM tier and budget cap."""
    price = pf(row.get("price_aud")) or pf(row.get("current_best_price_aud")) or 0.0
    vram = pf(row.get("vram_gb")) or 0.0
    unified = pf(row.get("unified_memory_gb")) or 0.0
    max_mem = max(vram, unified)

    if price <= 0:
        return 5.0  # unknown price — neutral

    # Compute rough price/VRAM value
    if max_mem >= 24:
        expected_fair = 3500
    elif max_mem >= 16:
        expected_fair = 4000
    elif max_mem >= 12:
        expected_fair = 3000
    elif max_mem >= 8:
        expected_fair = 2500
    else:
        expected_fair = 2000

    ratio = price / expected_fair
    if ratio <= 0.6:
        score = 10.0
    elif ratio <= 0.8:
        score = 8.0
    elif ratio <= 1.0:
        score = 6.0
    elif ratio <= 1.2:
        score = 4.0
    elif ratio <= 1.5:
        score = 2.0
    else:
        score = 0.0

    # Over budget penalty
    if price > BUDGET_CAP:
        score = max(0.0, score - 2.0)

    return clamp(score)


def derive_portability(row: dict) -> float:
    """AGENTS.md Portability scale."""
    profile = str(row.get("profile", "")).strip()
    item = str(row.get("item_name", "")).upper()
    cat_group = str(row.get("Category_Group", "")).strip()

    if cat_group in ("Standalone_GPU", "Workstation_GPU"):
        return 2.0  # GPU card — not a portable device

    if profile == "Laptop":
        # Large 18" laptops
        screen = pf(row.get("screen_size_in")) or 0.0
        if screen >= 18:
            return 5.0
        if screen >= 16:
            return 7.0
        return 8.0

    if profile == "Mini PC":
        return 7.0

    if profile == "Desktop":
        # Workstation towers are not portable
        ws_signals = ["THINKSTATION", "PRECISION", "HP Z", "XEON", "AURORA",
                      "TOWER", "WORKSTATION"]
        if any(sig in item for sig in ws_signals):
            return 1.0
        return 2.0

    return 3.0


def derive_track2_avoidance(row: dict) -> float:
    """AGENTS.md Track2_Avoidance scale."""
    vram = pf(row.get("vram_gb")) or 0.0
    unified = pf(row.get("unified_memory_gb")) or 0.0
    max_mem = max(vram, unified)
    gpu = str(row.get("gpu_model", "")).upper()
    item = str(row.get("item_name", "")).upper()

    strix_signals = ["STRIX HALO", "RYZEN AI MAX", "RADEON 8060S", "RADEON 890M",
                     "PROART PX13", "TUF A14", "TUF GAMING A14", "OMEN MAX"]
    is_strix = any(sig in gpu or sig in item for sig in strix_signals)

    if max_mem >= 48:
        return 10.0
    if max_mem >= 32:
        # Strix Halo cap at 7 for 64 GB, 8 for 128 GB
        if is_strix:
            return 7.0 if unified <= 64 else 8.0
        return 10.0
    if max_mem >= 24:
        return 9.0
    if max_mem >= 16:
        if is_strix:
            return 5.0
        return 7.0
    if max_mem >= 12:
        return 4.0
    if max_mem >= 8:
        return 2.0
    return 0.0


# ---------------------------------------------------------------------------
# Stock backfill
# ---------------------------------------------------------------------------

def backfill_stock(row: dict) -> str:
    """Set in_stock_now from au_stock if missing."""
    existing = str(row.get("in_stock_now", "")).strip().lower()
    if existing in ("yes", "true", "1", "no", "false", "0"):
        return existing
    au_stock = str(row.get("au_stock", "")).strip().lower()
    if au_stock in ("yes", "in stock", "available", "true", "1"):
        return "yes"
    if au_stock in ("no", "out of stock", "false", "0"):
        return "no"
    return ""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fill MCDA gaps (Upgrade_Ceiling, track/pathway, in_stock_now, spec-derived scores)."
    )
    parser.add_argument("csv_path", help="Input shortlist CSV path")
    parser.add_argument(
        "--output", default=None,
        help="Output CSV path (default: <date>_shortlist_mcda_filled.csv in shortlists/)"
    )
    args = parser.parse_args()

    csv_path = Path(args.csv_path)
    if not csv_path.exists():
        sys.exit(f"ERROR: File not found: {csv_path}")

    with csv_path.open(newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        fieldnames: list[str] = list(reader.fieldnames or [])
        rows = list(reader)

    print(f"Loaded {len(rows)} rows from {csv_path.name}")

    # Ensure Upgrade_Ceiling column exists
    if "Upgrade_Ceiling" not in fieldnames:
        # Insert after Track2_Avoidance
        try:
            idx = fieldnames.index("Track2_Avoidance")
            fieldnames.insert(idx + 1, "Upgrade_Ceiling")
        except ValueError:
            fieldnames.append("Upgrade_Ceiling")

    filled_uc = 0
    filled_track = 0
    filled_stock = 0
    filled_ph = 0
    filled_fp = 0
    filled_pv = 0
    filled_pt = 0
    filled_t2 = 0

    for row in rows:
        # --- Upgrade_Ceiling ---
        if is_empty(row.get("Upgrade_Ceiling")):
            row["Upgrade_Ceiling"] = str(round(derive_upgrade_ceiling(row), 1))
            filled_uc += 1

        # --- Track / Pathway ---
        t = str(row.get("track", "")).strip()
        p = str(row.get("pathway", "")).strip()
        if is_empty(t) or is_empty(p):
            new_t, new_p = infer_track_pathway(row)
            if is_empty(t):
                row["track"] = new_t
            if is_empty(p):
                row["pathway"] = new_p
            filled_track += 1

        # --- in_stock_now ---
        new_stock = backfill_stock(row)
        if is_empty(row.get("in_stock_now")) and new_stock:
            row["in_stock_now"] = new_stock
            filled_stock += 1

        # --- Spec-derived MCDA scores (only fill if blank) ---
        if is_empty(row.get("Performance_Headroom")):
            row["Performance_Headroom"] = str(round(derive_performance_headroom(row), 1))
            filled_ph += 1

        if is_empty(row.get("Future_Proof")):
            row["Future_Proof"] = str(round(derive_future_proof(row), 1))
            filled_fp += 1

        if is_empty(row.get("Price_Value")):
            row["Price_Value"] = str(round(derive_price_value(row), 1))
            filled_pv += 1

        if is_empty(row.get("Portability")):
            row["Portability"] = str(round(derive_portability(row), 1))
            filled_pt += 1

        if is_empty(row.get("Track2_Avoidance")):
            row["Track2_Avoidance"] = str(round(derive_track2_avoidance(row), 1))
            filled_t2 += 1

    out_path = Path(args.output) if args.output else (
        REPO_ROOT / "shortlists" / f"{date.today().isoformat()}_shortlist_mcda_filled.csv"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n✅ Filled CSV written: {out_path}")
    print(f"   Upgrade_Ceiling filled      : {filled_uc}")
    print(f"   Track/Pathway inferred      : {filled_track}")
    print(f"   in_stock_now backfilled     : {filled_stock}")
    print(f"   Performance_Headroom filled : {filled_ph}")
    print(f"   Future_Proof filled         : {filled_fp}")
    print(f"   Price_Value filled          : {filled_pv}")
    print(f"   Portability filled          : {filled_pt}")
    print(f"   Track2_Avoidance filled     : {filled_t2}")
    print(f"\n   Next: python scripts/scoring/rubric_weighting_engine.py")
    print(f"         --csv {out_path}")
    print(f"         --output-csv shortlists/{date.today().isoformat()}_ranked_final.csv")


if __name__ == "__main__":
    main()
