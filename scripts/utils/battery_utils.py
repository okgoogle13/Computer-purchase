"""
battery_utils.py — shared battery field extraction logic.

Imported by:
  - scripts/data_collection/gumtree_collect.py
  - scripts/data_collection/facebook_collect.py

Centralising this logic prevents the two scripts from drifting apart (Fix M4).
"""

from __future__ import annotations

import re


def extract_battery_fields(text: str) -> dict:
    """
    Parse battery health metadata from free-text listing description.

    Returns a dict with keys:
      battery_disclosure_level: str  — 'none' | 'replaced' | 'vague_claim' |
                                       'sold_as_is' | 'tested_pct' |
                                       'cycles_only' | 'tested_pct_cycles'
      battery_health_pct:       int | str  — percentage if found, else ''
      battery_cycle_count:      int | str  — cycle count if found, else ''
      battery_replaced:         bool
    """
    s = (text or "").lower()
    result: dict = {
        "battery_disclosure_level": "none",
        "battery_health_pct": "",
        "battery_cycle_count": "",
        "battery_replaced": False,
    }

    if "battery replaced" in s or "new battery" in s:
        result["battery_replaced"] = True
        result["battery_disclosure_level"] = "replaced"

    pct = re.search(r"(\d{2,3})\s*%\s*(?:battery|health|capacity)", s)
    cyc = re.search(r"cycle[s]?\D{0,10}(\d{1,4})", s)

    if pct:
        result["battery_health_pct"] = int(pct.group(1))
        result["battery_disclosure_level"] = "tested_pct"

    if cyc:
        result["battery_cycle_count"] = int(cyc.group(1))
        if result["battery_disclosure_level"] == "tested_pct":
            result["battery_disclosure_level"] = "tested_pct_cycles"
        elif result["battery_disclosure_level"] == "none":
            result["battery_disclosure_level"] = "cycles_only"

    if not pct and not cyc and not result["battery_replaced"]:
        if "holds charge" in s or "good battery" in s:
            result["battery_disclosure_level"] = "vague_claim"
        elif "as is" in s or "not tested" in s:
            result["battery_disclosure_level"] = "sold_as_is"

    return result
