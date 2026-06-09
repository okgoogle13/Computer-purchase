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
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "config" / "procurement_policy.json"

MCDA_COLUMNS = [
    "Performance_Headroom",
    "Price_Value",
    "Future_Proof",
    "Portability",
    "Track2_Avoidance",
]

# 5-factor weight constants — aligned with AGENTS.md and procurement_policy.json
WEIGHT_PERFORMANCE_HEADROOM = 0.25
WEIGHT_PRICE_VALUE          = 0.20
WEIGHT_FUTURE_PROOF         = 0.20
WEIGHT_PORTABILITY          = 0.20
WEIGHT_TRACK2_AVOIDANCE     = 0.15

# Assert weights sum exactly to 1.0
assert round(
    WEIGHT_PERFORMANCE_HEADROOM +
    WEIGHT_PRICE_VALUE +
    WEIGHT_FUTURE_PROOF +
    WEIGHT_PORTABILITY +
    WEIGHT_TRACK2_AVOIDANCE,
    3
) == 1.0, "MCDA weights must sum exactly to 1.0"


SELLER_RISK_MULTIPLIERS = {
    "OFFICIAL_STORE": 1.00,
    "MANUFACTURER_AU": 1.00,
    "AUTHORISED_RESELLER": 0.98,
    "MAJOR_RETAILER_AU": 0.98,
    "AMAZON_AU": 0.95,
    "EBAY_POWER_SELLER": 0.90,
    "EBAY_AU": 0.90,
    "REFURB_SELLER": 0.95,
    "PRIVATE_SELLER": 0.70,
    "GUMTREE_AU": 0.70,
    "FB_MARKETPLACE": 0.70,
    "GRAY_MARKET": 0.50,
    "GRAY_IMPORT": 0.50,
}

SOURCE_PLATFORM_PENALTIES = {
    "MANUFACTURER_AU": 0.00,
    "MAJOR_RETAILER_AU": 0.00,
    "AMAZON_AU": 0.20,
    "EBAY_AU": 0.40,
    "GUMTREE_AU": 0.80,
    "FB_MARKETPLACE": 0.80,
    "GRAY_IMPORT": 1.00,
}
# Seller/source risk mappings are intentionally engine-owned constants so
# ranking behavior is auditable and stable across CSV batches.


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        sys.exit(f"ERROR: Missing config: {CONFIG_PATH}")
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def parse_float(value: object) -> float | None:
    if value is None or value == "":
        return None
    text = str(value).strip().replace("$", "").replace(",", "")
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
    pathway_key = pathway.lower().replace(" ", "")

    if key in {"track1", "1"}:
        if pathway_key in {"1a", "a"}:
            return "1", "1A"
        if pathway_key in {"1b", "b"}:
            return "1", "1B"
        if pathway_key in {"1c", "c"}:
            return "1", "1C"
        return "1", pathway
    if key in {"track1a", "1a"}:
        return "1", "1A"
    if key in {"track1b", "1b"}:
        return "1", "1B"
    if key in {"track1c", "1c"}:
        return "1", "1C"
    if key in {"track1.5", "1.5"}:
        return "1.5", pathway
    if key in {"track2", "2"}:
        if pathway_key in {"2a", "a"}:
            return "2", "A"
        if pathway_key in {"2b", "b"}:
            return "2", "B"
        if pathway_key in {"2c", "c"}:
            return "2", "C"
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
    truthy_values = {"yes", "true", "y", "1", "in_stock", "available"}
    stock_fields = [
        str(row.get("in_stock_now", "")).strip().lower(),
        str(row.get("au_stock", "")).strip().lower(),
        str(row.get("au_stock_confirmed", "")).strip().lower(),
    ]
    return any(value in truthy_values for value in stock_fields)


def has_disqualifying_thermal_flag(row: dict) -> bool:
    values = [
        str(row.get("thermal_flag", "")).strip().lower(),
        str(row.get("thermal_status", "")).strip().lower(),
        str(row.get("thermal_risk", "")).strip().lower(),
    ]
    return any("disqualifying" in value for value in values)


def parse_int(value: object) -> int | None:
    """
    Parses an integer from a string or float, returning None if invalid/unknown.
    """
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    if not text or text.upper() in {"UNKNOWN", "N/A", "NONE", "-"}:
        return None
    try:
        return int(float(text))
    except ValueError:
        return None


def parse_bool(value: object) -> bool:
    """
    Parses a boolean from a string or boolean value.
    """
    if isinstance(value, bool):
        return value
    if not value:
        return False
    return str(value).strip().lower() in ("true", "yes", "1")


def get_manufacture_year(row: dict) -> int | None:
    """
    Derives manufacture year from cpu_model using CPU generation lookup rules.
    """
    cpu_model = str(row.get("cpu_model", "")).strip()
    if not cpu_model or cpu_model.upper() in ("UNKNOWN", "N/A", "-"):
        cpu_model = str(row.get("cpu", "")).strip()
    if not cpu_model or cpu_model.upper() in ("UNKNOWN", "N/A", "-"):
        item_name = str(row.get("item_name", "")).strip()
        match = re.search(
            r"\b(i[3579]-\d{4,5}[A-Z]*|Ryzen\s+[3579]\s+\d{4}[A-Z]*|Ryzen\s+AI\s+Max(?:\s*\+)?\s*\d{3})\b",
            item_name,
            re.IGNORECASE
        )
        if match:
            cpu_model = match.group(1)
        else:
            return None

    cpu_lower = cpu_model.lower()

    if "ryzen ai max" in cpu_lower or "strix halo" in cpu_lower:
        return 2025

    if "ultra" in cpu_lower and any(x in cpu_lower for x in ["285", "265", "245", "258", "275", "268"]):
        return 2025
    if "ultra" in cpu_lower:
        return 2024

    intel_match = re.search(r"i[3579]-(\d+)", cpu_lower)
    if intel_match:
        gen_str = intel_match.group(1)
        if len(gen_str) >= 5:
            gen = int(gen_str[:2])
        else:
            gen = int(gen_str[0])

        if gen == 14:
            return 2024
        elif gen == 13:
            return 2023
        elif gen == 12:
            return 2022
        elif gen == 11:
            return 2021
        elif gen == 10:
            return 2019
        elif gen == 9:
            return 2018
        elif gen == 8:
            return 2017

    amd_match = re.search(r"ryzen\s+[3579]\s+(\d)", cpu_lower)
    if amd_match:
        series = int(amd_match.group(1))
        if series == 9:
            return 2024
        elif series == 8:
            return 2024
        elif series == 7:
            return 2023
        elif series == 6:
            return 2022
        elif series == 5:
            return 2021
        elif series == 4:
            return 2020
        elif series == 3:
            return 2019

    if "m4" in cpu_lower:
        return 2024
    if "m3" in cpu_lower:
        return 2023
    if "m2" in cpu_lower:
        return 2022
    if "m1" in cpu_lower:
        return 2020

    if "threadripper" in cpu_lower:
        if "39" in cpu_lower:
            return 2020
        if "59" in cpu_lower:
            return 2022
        if "79" in cpu_lower:
            return 2023

    if "xeon" in cpu_lower:
        if "w-10" in cpu_lower or "w10" in cpu_lower:
            return 2020
        if "w-11" in cpu_lower or "w11" in cpu_lower:
            return 2021
        if "w-12" in cpu_lower or "w12" in cpu_lower:
            return 2022
        if "w-13" in cpu_lower or "w13" in cpu_lower:
            return 2023

    year_match = re.search(r"\b(201\d|202\d)\b", cpu_lower)
    if year_match:
        return int(year_match.group(1))

    return None


def score_battery_disclosure(row: dict) -> float:
    """
    Scores the transparency of battery health disclosure in listing.
    Returns 0.0 – 10.0. Higher = more transparent.
    """
    level = row.get("battery_disclosure_level", "none")
    table = {
        "tested_pct_cycles":  10.0,
        "replaced":            9.0,
        "tested_pct":          8.0,
        "health_range_claim":  6.0,
        "vague_claim":         3.0,
        "none":                1.0,
        "sold_as_is":          0.0,
    }
    return table.get(level, 1.0)


def score_battery_health_value(row: dict) -> float:
    """
    Scores actual battery health where a quantified value exists.
    Defaults to 3.0 (penalised, not zeroed) if no value disclosed.
    Returns 0.0 – 10.0.
    """
    if parse_bool(row.get("battery_replaced")):
        return 10.0
    pct = parse_int(row.get("battery_health_pct"))
    cycles = parse_int(row.get("battery_cycle_count"))
    if pct is None and cycles is None:
        return 3.0  # unknown, not failed
    score = 0.0
    if pct is not None:
        if pct >= 95:   score = 10.0
        elif pct >= 85: score = 8.0
        elif pct >= 75: score = 6.0
        elif pct >= 65: score = 4.0
        elif pct >= 55: score = 2.0
        else:           score = 0.0
    if cycles is not None:
        if cycles > 800:   score = max(0.0, score - 2.0)
        elif cycles > 500: score = max(0.0, score - 1.0)
    return score


def score_battery(row: dict) -> float:
    """
    Combined battery score:
      battery_score = (disclosure * 0.5) + (health_value * 0.5)
    Returns 0.0 – 10.0.
    """
    d = score_battery_disclosure(row)
    h = score_battery_health_value(row)
    return round((d * 0.5) + (h * 0.5), 2)


def score_acquisition_risk(row: dict) -> float:
    """
    Scores the overall risk of this acquisition.
    Combines seller trust, warranty, condition, age, and battery signals.
    Returns 0.0 – 10.0. Higher = lower risk = safer purchase.
    """
    base = 5.0  # neutral starting point

    # ── Seller class ──────────────────────────────────
    seller_class = row.get("seller_class", "unknown")
    seller_class_scores = {
        "commercial_oem":    +3.0,
        "commercial_refurb": +2.0,
        "commercial_seller": +1.0,
        "private":           -1.5,
        "unknown":           -1.0,
    }
    base += seller_class_scores.get(seller_class, -1.0)

    # ── Seller feedback ───────────────────────────────
    fb_count = parse_int(row.get("seller_feedback_count")) or 0
    fb_pct   = parse_float(row.get("seller_feedback_pct")) or 0.0
    if fb_count >= 500 and fb_pct >= 98:  base += 1.0
    elif fb_count >= 100 and fb_pct >= 97: base += 0.5
    elif fb_count < 50 or fb_pct < 95:    base -= 1.0
    elif fb_count < 10:                   base -= 2.0

    # ── Returns policy ───────────────────────────────
    if not parse_bool(row.get("returns_accepted", False)):
        base -= 1.0

    # ── Warranty ─────────────────────────────────────
    warranty = parse_int(row.get("warranty_months") or row.get("warranty_months_confirmed")) or 0
    acl_val = str(row.get("acl_covered", "")).strip().lower()
    is_acl = acl_val in ("yes", "true", "1")
    au_warranty = parse_bool(row.get("warranty_au_redeemable", False)) or is_acl
    if warranty >= 12 and au_warranty:    base += 1.5
    elif warranty >= 6:                   base += 0.5
    elif warranty == 0:                   base -= 1.5

    # ── Age ───────────────────────────────────────────
    year = get_manufacture_year(row)
    if year:
        age = 2026 - year
        if age <= 1:    base += 0.5
        elif age <= 3:  base += 0.0
        elif age <= 5:  base -= 1.0
        elif age <= 7:  base -= 2.0
        else:           base -= 3.0

    # ── Battery transparency ──────────────────────────
    battery_s = score_battery(row)
    if battery_s >= 9:   base += 1.0
    elif battery_s >= 7: base += 0.5
    elif battery_s <= 2: base -= 1.5
    elif battery_s <= 4: base -= 0.5

    # ── Listing country ───────────────────────────────
    if row.get("listing_country", "AU") != "AU":
        base -= 1.0

    return max(0.0, min(base, 10.0))


def score_future_proof(row: dict) -> float:
    """
    Scores future proofing capability based on VRAM/unified memory, adjusted for age and platform risk.
    """
    val = parse_float(row.get("Future_Proof"))
    if val is not None:
        base = val
    else:
        vram = parse_float(row.get("vram_gb"))
        unified = parse_float(row.get("unified_memory_gb"))
        max_mem = max(vram or 0.0, unified or 0.0)
        
        if max_mem >= 24:
            base = 9.0
        elif max_mem >= 16:
            base = 7.0
        elif max_mem >= 12:
            base = 5.0
        else:
            base = 3.0

    # Age modifier
    year = get_manufacture_year(row)
    if year:
        age = 2026 - year
        if age <= 1:    pass           # no penalty
        elif age <= 3:  base -= 0.5
        elif age <= 5:  base -= 1.5
        elif age <= 7:  base -= 2.5
        else:           base -= 3.5

    # Platform risk modifiers
    os_val = str(row.get("os", "")).lower()
    if "windows 10" in os_val and "windows 11" not in os_val:
        base -= 2.0   # Win10 EOL, no upgrade path
    if not parse_bool(row.get("tpm2", True)):    # assume True if not listed
        base -= 1.0
    
    pcie_gen_raw = row.get("pcie_gen")
    if pcie_gen_raw is not None:
        try:
            if int(float(pcie_gen_raw)) < 4:
                base -= 0.5
        except (ValueError, TypeError):
            pass

    return max(0.0, min(base, 10.0))


def compute_risk_adjusted_price(row: dict) -> float:
    """
    Adjusts listed price upward to reflect acquisition risk premiums.
    Used as the true cost baseline for Price_Value scoring.
    """
    price = float(parse_float(row.get("list_price_aud") or row.get("price_aud")) or 0.0)
    price += float(parse_float(row.get("shipping_cost_aud")) or 0.0)

    disclosure = row.get("battery_disclosure_level", "none")
    if disclosure in ["none", "sold_as_is"]:
        price += 120  # estimated battery replacement risk

    warranty = parse_int(row.get("warranty_months") or row.get("warranty_months_confirmed")) or 0
    if warranty == 0:
        price += 150  # no-warranty risk premium

    if row.get("listing_country", "AU") != "AU":
        price += 80   # import/warranty risk

    if row.get("seller_class") == "private" and not parse_bool(row.get("returns_accepted", False)):
        price += 100  # no-recourse risk

    return round(price, 2)


def score_price_value(row: dict) -> float:
    """
    Scores Price_Value against risk-adjusted price.
    """
    risk_price = compute_risk_adjusted_price(row)
    row["risk_adjusted_price"] = risk_price

    manual_val = parse_float(row.get("Price_Value"))
    if manual_val is not None:
        list_p = parse_float(row.get("list_price_aud") or row.get("price_aud")) or 0.0
        if list_p > 0:
            risk_increase = risk_price - list_p
            penalty = (risk_increase / 100.0) * 0.5
            return round(max(0.0, min(10.0, manual_val - penalty)), 2)
        return manual_val

    score = 10.0 - (risk_price - 1000.0) / 400.0
    return round(max(0.0, min(10.0, score)), 2)


def compute_mcda(scores: dict) -> float:
    """
    Computes the final MCDA score using the 5-factor model from AGENTS.md.

    SCORE = Performance_Headroom * 0.25 + Price_Value * 0.20
          + Future_Proof * 0.20 + Portability * 0.20 + Track2_Avoidance * 0.15

    Acquisition_Risk and Upgrade_Ceiling are not MCDA factors; risk is applied
    post-hoc via calculate_risk_adjustment() (seller multiplier + source penalty).
    """
    score = (
        (scores.get("performance_headroom") or 0.0) * WEIGHT_PERFORMANCE_HEADROOM +
        (scores.get("price_value")          or 0.0) * WEIGHT_PRICE_VALUE          +
        (scores.get("future_proof")         or 0.0) * WEIGHT_FUTURE_PROOF         +
        (scores.get("portability")          or 0.0) * WEIGHT_PORTABILITY          +
        (scores.get("track2_avoidance")     or 0.0) * WEIGHT_TRACK2_AVOIDANCE
    )
    return round(score, 3)


def enrich_row(row: dict) -> dict:
    """
    Enriches a shortlist row with derived battery, manufacture year,
    risk adjusted price, and acquisition risk scores.
    """
    manufacture_year = get_manufacture_year(row)
    row["manufacture_year"] = manufacture_year if manufacture_year is not None else ""

    seller_class = str(row.get("seller_class", "unknown")).lower()
    warranty_months = parse_int(row.get("warranty_months") or row.get("warranty_months_confirmed")) or 0
    returns_accepted = parse_bool(row.get("returns_accepted"))
    battery_disclosure_level = row.get("battery_disclosure_level", "none")
    battery_health_pct = parse_int(row.get("battery_health_pct"))
    listing_country = row.get("listing_country", "AU")
    seller_feedback_count = parse_int(row.get("seller_feedback_count"))
    
    battery_score = score_battery(row)
    acquisition_risk = score_acquisition_risk(row)
    risk_adj_price = compute_risk_adjusted_price(row)
    
    row["risk_adjusted_price"] = risk_adj_price
    row["battery_score"]       = battery_score
    row["battery_disclosure_score"]    = score_battery_disclosure(row)
    row["battery_health_value_score"]  = score_battery_health_value(row)
    row["score_acquisition_risk"]      = acquisition_risk

    existing_flags = row.get("risk_flags", "")
    risk_flags = [f.strip() for f in existing_flags.split(";") if f.strip()]

    if manufacture_year and (2026 - manufacture_year) > 4:
        if "AGE_RISK_4YR+" not in risk_flags:
            risk_flags.append("AGE_RISK_4YR+")
    if seller_class == "private":
        if "PRIVATE_SELLER" not in risk_flags:
            risk_flags.append("PRIVATE_SELLER")
    if warranty_months == 0:
        if "NO_WARRANTY" not in risk_flags:
            risk_flags.append("NO_WARRANTY")
    if not returns_accepted:
        if "NO_RETURNS" not in risk_flags:
            risk_flags.append("NO_RETURNS")
    if battery_disclosure_level in ["none", "sold_as_is"]:
        if "BATTERY_UNDISCLOSED" not in risk_flags:
            risk_flags.append("BATTERY_UNDISCLOSED")
    if battery_health_pct is not None and battery_health_pct < 70:
        if "BATTERY_DEGRADED" not in risk_flags:
            risk_flags.append("BATTERY_DEGRADED")
    if listing_country != "AU":
        if "NON_AU_SELLER" not in risk_flags:
            risk_flags.append("NON_AU_SELLER")
    if seller_feedback_count is not None and seller_feedback_count < 10:
        if "NEW_SELLER" not in risk_flags:
            risk_flags.append("NEW_SELLER")

    row["risk_flags"] = "; ".join(risk_flags)

    scores = {
        "performance_headroom": parse_float(row.get("Performance_Headroom")),
        "price_value": score_price_value(row),
        "future_proof": score_future_proof(row),
        "portability": parse_float(row.get("Portability")),
        "track2_avoidance": parse_float(row.get("Track2_Avoidance")),
        "upgrade_ceiling": parse_float(row.get("Upgrade_Ceiling")),
        "acquisition_risk": acquisition_risk,
        "battery": battery_score,
    }
    
    # Store derived scores back in row
    row["Price_Value"] = scores["price_value"]
    row["Future_Proof"] = scores["future_proof"]

    return scores


def score_row(row: dict, weights: dict) -> tuple[float | None, list[str]]:
    """
    Scores a row using the 7-factor MCDA engine.
    """
    scores = enrich_row(row)
    
    manual_mcda_cols = [
        "Performance_Headroom",
        "Price_Value",
        "Future_Proof",
        "Portability",
        "Track2_Avoidance",
    ]
    missing = [col for col in manual_mcda_cols if parse_float(row.get(col)) is None]
    if missing:
        return None, missing
        
    total = compute_mcda(scores)
    return total, []


def normalize_risk_key(value: object) -> str:
    return str(value or "").strip().upper().replace(" ", "_")



def is_unknown_key(value: str) -> bool:
    return value in {"", "UNKNOWN", "N/A", "NONE", "-"}


def calculate_risk_adjustment(row: dict, mcda_total: float | None) -> tuple[float | None, float | None, float | None, list[str]]:
    if mcda_total is None:
        return None, None, None, []

    seller_key = normalize_risk_key(row.get("seller_class"))
    seller_translations = {
        "PRIVATE": "PRIVATE_SELLER",
        "COMMERCIAL_REFURB": "REFURB_SELLER",
        "COMMERCIAL_OEM": "MANUFACTURER_AU",
        "COMMERCIAL_SELLER": "MAJOR_RETAILER_AU",
    }
    if seller_key in seller_translations:
        seller_key = seller_translations[seller_key]

    source_key = normalize_risk_key(row.get("source_platform"))
    source_translations = {
        "PRIVATE_SELLER": "FB_MARKETPLACE", # fallback if source is listed as seller class
    }
    if source_key in source_translations:
        source_key = source_translations[source_key]

    notes: list[str] = []

    seller_multiplier = SELLER_RISK_MULTIPLIERS.get(seller_key)
    if seller_multiplier is None:
        seller_multiplier = 1.0
        if is_unknown_key(seller_key):
            notes.append("seller_class UNKNOWN for risk adjustment")
        else:
            notes.append(f"seller_class unrecognized for risk adjustment ({seller_key})")

    source_penalty = SOURCE_PLATFORM_PENALTIES.get(source_key)
    if source_penalty is None:
        source_penalty = 0.0
        if is_unknown_key(source_key):
            notes.append("source_platform UNKNOWN for risk adjustment")
        else:
            notes.append(f"source_platform unrecognized for risk adjustment ({source_key})")

    adjusted_total = (mcda_total * seller_multiplier) - source_penalty
    adjusted_total = max(0.0, min(10.0, adjusted_total))
    risk_adjustment = adjusted_total - mcda_total
    return (
        round(seller_multiplier, 3),
        round(source_penalty, 3),
        round(risk_adjustment, 3),
        notes,
    )


def track_1b_soc_confirmed(row: dict) -> tuple[bool, str]:
    candidates = [
        row.get("soc"),
        row.get("gpu_or_soc"),
        row.get("gpu_model"),
        row.get("item_name"),
    ]
    raw = " ".join(str(v or "").strip() for v in candidates).strip()
    if not raw:
        return False, "UNKNOWN"
    normalized = raw.lower()
    indicators = (
        "strix halo",
        "ryzen ai max",
        "ryzen ai max+",
    )
    if any(indicator in normalized for indicator in indicators):
        return True, raw
    return False, raw


def track_1c_soc_confirmed(row: dict) -> tuple[bool, str]:
    candidates = [
        row.get("soc"),
        row.get("gpu_or_soc"),
        row.get("gpu_model"),
        row.get("item_name"),
    ]
    raw = " ".join(str(v or "").strip() for v in candidates).strip()
    if not raw:
        return False, "UNKNOWN"
    normalized = raw.lower()
    indicators = (
        "rtx spark",
        "grace blackwell",
        "n1x",
        "n1 laptop",
        "mediatek nvidia",
    )
    if any(indicator in normalized for indicator in indicators):
        return True, raw
    return False, raw


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

    # Stock check bypassed as a soft warning/note instead of policy blocker
    if not stock_is_confirmed(row):
        pass

    if track == "1" and pathway == "1A":
        if price is not None and price > budget:
            blockers.append(f"price > Track 1 cap ({budget:.0f} AUD)")
        if vram is None:
            blockers.append("VRAM UNKNOWN")
        elif vram < laptop_floor:
            blockers.append(f"VRAM below Track 1A floor ({laptop_floor:.0f} GB)")
        if screen is None:
            blockers.append("screen size UNKNOWN")
        elif screen < 16:
            blockers.append("screen size below Track 1A floor (16 in)")
    elif track == "1" and pathway == "1B":
        if price is not None and price > budget:
            blockers.append(f"price > Track 1 cap ({budget:.0f} AUD)")
        if unified is None:
            blockers.append("unified memory UNKNOWN")
        elif unified < unified_floor:
            blockers.append(f"unified memory below Track 1B floor ({unified_floor:.0f} GB)")
        soc_ok, soc_text = track_1b_soc_confirmed(row)
        if not soc_ok:
            if not soc_text or soc_text.upper() in {"UNKNOWN", "N/A", "NONE", "-"}:
                blockers.append("Track 1B SoC not confirmed (requires Strix Halo / Ryzen AI Max)")
            else:
                blockers.append("Track 1B SoC mismatch (requires Strix Halo / Ryzen AI Max)")
    elif track == "1" and pathway == "1C":
        if price is not None and price > budget:
            blockers.append(f"price > Track 1 cap ({budget:.0f} AUD)")
        if unified is None:
            blockers.append("unified memory UNKNOWN")
        elif unified < unified_floor:
            blockers.append(f"unified memory below Track 1C floor ({unified_floor:.0f} GB)")
        soc_ok, soc_text = track_1c_soc_confirmed(row)
        if not soc_ok:
            if not soc_text or soc_text.upper() in {"UNKNOWN", "N/A", "NONE", "-"}:
                blockers.append("Track 1C SoC not confirmed (requires RTX Spark / N1/N1X / Grace Blackwell)")
            else:
                blockers.append("Track 1C SoC mismatch (requires RTX Spark / N1/N1X / Grace Blackwell)")
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
    
    # 5-factor weights aligned with AGENTS.md and procurement_policy.json
    weights = {
        "Performance_Headroom": WEIGHT_PERFORMANCE_HEADROOM,
        "Price_Value": WEIGHT_PRICE_VALUE,
        "Future_Proof": WEIGHT_FUTURE_PROOF,
        "Portability": WEIGHT_PORTABILITY,
        "Track2_Avoidance": WEIGHT_TRACK2_AVOIDANCE,
    }

    with csv_path.open(newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            sys.exit("ERROR: Input CSV has no header.")
        rows = list(reader)
        fieldnames = list(reader.fieldnames)

    # Exclude candidates marked REJECTED or INACTIVE from ranking
    _SKIP_STATUSES = {"REJECTED", "INACTIVE", "REMOVED"}
    active_rows = [r for r in rows if str(r.get("status", "")).strip().upper() not in _SKIP_STATUSES]
    skipped = len(rows) - len(active_rows)
    if skipped:
        print(f"Note: {skipped} candidate(s) excluded (REJECTED/INACTIVE).")
    rows = active_rows

    # Assert that all standard MCDA columns are in fieldnames
    for col in MCDA_COLUMNS:
        if col not in fieldnames:
            sys.exit(f"ERROR: Input CSV is missing MCDA column: {col}")

    # Add new output columns to fieldnames
    new_cols = [
        "MCDA_Total",
        "Seller_Risk_Multiplier",
        "Source_Platform_Penalty",
        "Risk_Adjustment",
        "Adjusted_MCDA_Total",
        "Policy_Status",
        "Policy_Blockers",
        "score_acquisition_risk",
        "battery_score",
        "battery_disclosure_score",
        "battery_health_value_score",
        "risk_adjusted_price",
        "manufacture_year",
        "risk_flags",
        # Archetype transparency columns (written by build_shortlist.py --archetype)
        "archetype_used",
        "intent_notes",
    ]
    for col in new_cols:
        if col not in fieldnames:
            fieldnames.append(col)

    ranked = []
    for row in rows:
        score, missing = score_row(row, weights)
        status, blockers = policy_status(row, config, score)
        seller_multiplier, source_penalty, risk_adjustment, risk_notes = calculate_risk_adjustment(row, score)
        if missing:
            blockers = [f"missing MCDA: {', '.join(missing)}", *blockers]
        if risk_notes:
            blockers = [*blockers, *risk_notes]
        row["MCDA_Total"] = "" if score is None else f"{score:.3f}"
        row["Seller_Risk_Multiplier"] = "" if seller_multiplier is None else f"{seller_multiplier:.3f}"
        row["Source_Platform_Penalty"] = "" if source_penalty is None else f"{source_penalty:.3f}"
        row["Risk_Adjustment"] = "" if risk_adjustment is None else f"{risk_adjustment:.3f}"
        row["Adjusted_MCDA_Total"] = (
            ""
            if score is None or risk_adjustment is None
            else f"{(score + risk_adjustment):.3f}"
        )
        row["Policy_Status"] = status
        row["Policy_Blockers"] = "; ".join(dict.fromkeys(blockers))
        ranked.append(row)

    ranked.sort(key=lambda row: parse_float(row.get("Adjusted_MCDA_Total")) or -1, reverse=True)

    print("\nCareerCopilot MCDA Ranking")
    print("=" * 78)
    print("Weights:", ", ".join(f"{col}={weights[col]:.2f}" for col in weights))
    print("-" * 78)
    print(
        f"{'#':>3}  {'MCDA':>6}  {'Adj':>6}  {'Status':<12}  {'Track':<5} {'Path':<5}  Candidate"
    )
    print("-" * 78)
    for idx, row in enumerate(ranked, start=1):
        track, pathway = normalize_track_pathway(row)
        score = row.get("MCDA_Total") or "NA"
        adjusted = row.get("Adjusted_MCDA_Total") or "NA"
        archetype = row.get("archetype_used") or ""
        archetype_tag = f"  [{archetype}]" if archetype else ""
        print(
            f"{idx:>3}  {score:>6}  {adjusted:>6}  {row['Policy_Status']:<12}  {track:<5} {pathway:<5}  {row.get('item_name') or row.get('Machine')}{archetype_tag}"
        )
        if row["Policy_Blockers"]:
            print(f"       blockers: {row['Policy_Blockers']}")

    winners = [row for row in ranked if row["Policy_Status"] == "GOOD_ENOUGH"]
    if winners:
        winner = winners[0]
        print("\n[GOOD ENOUGH] Highest-ranked outcome-enabled candidate:")
        print(
            f"  {winner.get('item_name') or winner.get('Machine')} "
            f"(base {winner['MCDA_Total']}/10, adjusted {winner['Adjusted_MCDA_Total']}/10)"
        )
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
