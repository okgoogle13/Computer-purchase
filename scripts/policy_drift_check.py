#!/usr/bin/env python3
"""Check/Sync AGENTS.md policy constants against config/procurement_policy.json.

This is a lightweight guardrail for ranking-time drift detection and syncing.
"""

from __future__ import annotations

import argparse
import json
import sys
import difflib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AGENTS_PATH = REPO_ROOT / "AGENTS.md"
CONFIG_PATH = REPO_ROOT / "config" / "procurement_policy.json"
DEFAULT_LOG_PATH = REPO_ROOT / "logs" / "policy_drift_check_latest.json"

def generate_policy_markdown(config: dict) -> str:
    budget_cap = config.get("budget_cap_aud", 5000.0)
    laptop_discrete_vram = config.get("laptop_discrete_minimum_vram_gb", 8.0)
    laptop_unified_memory = config.get("laptop_unified_minimum_vram_gb", 16.0)
    desktop_vram = config.get("desktop_minimum_vram_gb", 16.0)
    track2_caps = config.get("track2_budget_caps_aud", {})
    cap_a = track2_caps.get("A", 5000.0)
    cap_b = track2_caps.get("B", 4000.0)
    cap_c = track2_caps.get("C", 3500.0)

    markdown = f"""- **Track 1 (Laptop Core)**: Active choice path. Proceed immediately upon locating a baseline validation match. Target budget: ≤ {budget_cap:,.0f} AUD.
  - **Track 1A (Discrete GPU Laptop)**: Discrete VRAM is at least {laptop_discrete_vram:.0f} GB. Screen size is at least 16 inches (or 14–16 inches if touchscreen).
  - **Track 1B (Unified Memory Laptop)**: Unified memory is at least {laptop_unified_memory:.0f} GB (32 GB+ preferred, 48GB/64GB+ strong for Q4). Includes Apple Silicon and other Unified Memory Architectures (UMAs) with advanced VRAM BIOS configuration options.
- **Track 1.5 (Desktop Swap)**: Enabled exclusively under Exception A parameters (Zero valid laptop configurations discovered within pricing parameters).
  - **Track 1.5 Minimum VRAM**: GPU VRAM is at least {desktop_vram:.0f} GB.
- **Track 2 (Secondary/Alternative Tracks)**:
  - **Pathway A**: Total cost is at most {cap_a:,.0f} AUD.
  - **Pathway B**: Total cost is at most {cap_b:,.0f} AUD.
  - **Pathway C**: Total cost is at most {cap_c:,.0f} AUD."""
    return markdown

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check or sync policy drift between AGENTS.md and config/procurement_policy.json"
    )
    parser.add_argument(
        "--sync",
        action="store_true",
        help="Update the AGENTS.md policy section in place"
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_LOG_PATH),
        help="Write JSON report to this file"
    )
    args = parser.parse_args()

    if not AGENTS_PATH.exists() or not CONFIG_PATH.exists():
        sys.exit("Error: Missing AGENTS.md or config/procurement_policy.json")

    try:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        sys.exit(f"Error: Failed to parse {CONFIG_PATH}: {e}")

    agents_text = AGENTS_PATH.read_text(encoding="utf-8")
    start_tag = "<!-- POLICY_START -->"
    end_tag = "<!-- POLICY_END -->"

    if start_tag not in agents_text or end_tag not in agents_text:
        sys.exit(f"Error: Could not find markers {start_tag} and {end_tag} in AGENTS.md")

    parts = agents_text.split(start_tag)
    before_policy = parts[0]
    after_start = parts[1]
    parts2 = after_start.split(end_tag)
    existing_policy_raw = parts2[0]
    after_policy = parts2[1]

    existing_policy = existing_policy_raw.strip()
    generated_policy = generate_policy_markdown(config).strip()

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if args.sync:
        if existing_policy == generated_policy:
            print("AGENTS.md policy section is already in sync.")
        else:
            new_agents_text = f"{before_policy}{start_tag}\n{generated_policy}\n{end_tag}{after_policy}"
            AGENTS_PATH.write_text(new_agents_text, encoding="utf-8")
            print("AGENTS.md successfully synced with config/procurement_policy.json.")
        
        # Write success log
        summary = {
            "status": "PASS",
            "message": "Synced successfully.",
        }
        out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        sys.exit(0)

    # Check mode
    if existing_policy == generated_policy:
        print("Policy drift check: PASS")
        summary = {
            "status": "PASS",
            "message": "No numeric policy drift detected."
        }
        out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        sys.exit(0)
    else:
        print("Policy drift check: FAIL (Mismatches detected)")
        diff = difflib.unified_diff(
            existing_policy.splitlines(),
            generated_policy.splitlines(),
            fromfile="AGENTS.md (current)",
            tofile="procurement_policy.json (expected)",
            lineterm=""
        )
        print("\n".join(diff))
        
        summary = {
            "status": "FAIL",
            "message": "Policy drift detected between AGENTS.md and config/procurement_policy.json. Run --sync to align."
        }
        out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        sys.exit(2)

if __name__ == "__main__":
    main()
