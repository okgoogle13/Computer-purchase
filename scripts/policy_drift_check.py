#!/usr/bin/env python3
"""Check AGENTS.md policy constants against config/procurement_policy.json.

This is a lightweight guardrail for ranking-time drift detection.
Human-facing recommendations should follow AGENTS.md when mismatches exist.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AGENTS_PATH = REPO_ROOT / "AGENTS.md"
CONFIG_PATH = REPO_ROOT / "config" / "procurement_policy.json"
DEFAULT_LOG_PATH = REPO_ROOT / "logs" / "policy_drift_check_latest.json"


def parse_agents_constants(text: str) -> dict[str, float]:
    constants: dict[str, float] = {}

    track1_cap = re.search(r"Track 1 budget cap:\s*\*\*(\d[\d,]*)\s*AUD\*\*", text, re.IGNORECASE)
    if track1_cap:
        constants["track1_budget_cap_aud"] = float(track1_cap.group(1).replace(",", ""))

    track1a_vram = re.search(r"Discrete VRAM is at least\s*(\d+)\s*GB", text, re.IGNORECASE)
    if track1a_vram:
        constants["track1a_min_discrete_vram_gb"] = float(track1a_vram.group(1))

    track1b_unified = re.search(r"Unified memory is at least\s*(\d+)\s*GB", text, re.IGNORECASE)
    if track1b_unified:
        constants["track1b_min_unified_memory_gb"] = float(track1b_unified.group(1))

    track15_vram = re.search(r"GPU VRAM is at least\s*(\d+)\s*GB", text, re.IGNORECASE)
    if track15_vram:
        constants["track15_min_vram_gb"] = float(track15_vram.group(1))

    cap_a = re.search(r"Total cost is at most\s*(\d[\d,]*)\s*AUD", text, re.IGNORECASE)
    if cap_a:
        constants["track2_a_cap_aud"] = float(cap_a.group(1).replace(",", ""))

    b_match = re.search(r"Pathway B.*?Total cost is at most\s*(\d[\d,]*)\s*AUD", text, re.IGNORECASE | re.DOTALL)
    if b_match:
        constants["track2_b_cap_aud"] = float(b_match.group(1).replace(",", ""))

    c_match = re.search(r"Pathway C.*?Total cost is at most\s*(\d[\d,]*)\s*AUD", text, re.IGNORECASE | re.DOTALL)
    if c_match:
        constants["track2_c_cap_aud"] = float(c_match.group(1).replace(",", ""))

    return constants


def compare(agents_values: dict[str, float], config: dict) -> list[dict[str, object]]:
    track2_caps = config.get("track2_budget_caps_aud", {})
    comparisons = [
        ("track1_budget_cap_aud", config.get("budget_cap_aud")),
        ("track1a_min_discrete_vram_gb", config.get("laptop_discrete_minimum_vram_gb")),
        ("track1b_min_unified_memory_gb", config.get("laptop_unified_minimum_vram_gb")),
        ("track15_min_vram_gb", config.get("desktop_minimum_vram_gb")),
        ("track2_a_cap_aud", track2_caps.get("A")),
        ("track2_b_cap_aud", track2_caps.get("B")),
        ("track2_c_cap_aud", track2_caps.get("C")),
    ]

    result: list[dict[str, object]] = []
    for key, config_value in comparisons:
        agents_value = agents_values.get(key)
        status = "MATCH"
        if agents_value is None or config_value is None:
            status = "UNRESOLVED"
        elif float(agents_value) != float(config_value):
            status = "MISMATCH"
        result.append(
            {
                "field": key,
                "agents_md": agents_value,
                "config": config_value,
                "status": status,
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Check policy drift between AGENTS.md and config/procurement_policy.json")
    parser.add_argument("--output", default=str(DEFAULT_LOG_PATH), help="Write JSON report to this file")
    args = parser.parse_args()

    if not AGENTS_PATH.exists() or not CONFIG_PATH.exists():
        sys.exit("Missing AGENTS.md or config/procurement_policy.json")

    agents_text = AGENTS_PATH.read_text(encoding="utf-8")
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    agents_values = parse_agents_constants(agents_text)
    checks = compare(agents_values, config)

    mismatches = [r for r in checks if r["status"] == "MISMATCH"]
    unresolved = [r for r in checks if r["status"] == "UNRESOLVED"]

    summary = {
        "status": "PASS" if not mismatches else "FAIL",
        "message": (
            "No numeric policy drift detected."
            if not mismatches
            else "Policy drift detected. Follow AGENTS.md for recommendation language and update config."
        ),
        "checks": checks,
    }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"Policy drift check: {summary['status']}")
    print(summary["message"])
    print(f"Report: {out_path}")

    if unresolved:
        print("Unresolved fields:")
        for row in unresolved:
            print(f"  - {row['field']}")

    if mismatches:
        print("Mismatches:")
        for row in mismatches:
            print(f"  - {row['field']}: AGENTS.md={row['agents_md']} config={row['config']}")
        sys.exit(2)


if __name__ == "__main__":
    main()
