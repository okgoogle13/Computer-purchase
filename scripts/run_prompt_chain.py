#!/usr/bin/env python3
"""Run the CareerCopilot hardware prompt-chain orchestration skeleton.

This executes deterministic script stages and prints prompt-template checkpoints
for agent/human steps.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def run(cmd: list[str]) -> None:
    printable = " ".join(cmd)
    print(f"\n$ {printable}")
    completed = subprocess.run(cmd, cwd=REPO_ROOT)
    if completed.returncode != 0:
        raise RuntimeError(f"Command failed ({completed.returncode}): {printable}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Execute hardware prompt/script chain through ranking stage")
    parser.add_argument("--batch", help="Optional batch filter passed to build_shortlist.py")
    parser.add_argument("--shortlist", help="Use existing shortlist CSV instead of building a new one")
    parser.add_argument("--enriched", help="Use existing enriched CSV instead of generating one")
    parser.add_argument("--ranked-output", help="Output path for ranked CSV")
    args = parser.parse_args()

    # 0) Policy drift check gate
    run([sys.executable, "scripts/policy_drift_check.py"])

    # 1) Phase 2
    shortlist_path = Path(args.shortlist) if args.shortlist else REPO_ROOT / "shortlists" / f"{date.today().isoformat()}_shortlist.csv"
    if not args.shortlist:
        cmd = [sys.executable, "scripts/build_shortlist.py"]
        if args.batch:
            cmd += ["--batch", args.batch]
        run(cmd)

    if not shortlist_path.exists():
        raise RuntimeError(f"Shortlist not found: {shortlist_path}")

    # 2) Phase 3a
    enriched_path = Path(args.enriched) if args.enriched else shortlist_path.parent / f"{shortlist_path.stem}_pricing_enriched.csv"
    if not args.enriched:
        run([sys.executable, "scripts/enrich_shortlist_pricing.py", str(shortlist_path), "--force"])

    if not enriched_path.exists():
        raise RuntimeError(f"Enriched shortlist not found: {enriched_path}")

    print("\nManual/agent checkpoint required before scoring:")
    print("1) Run pre-scoring gate via scripts/prompt_templates/pre_scoring_validation_prompt.md")
    print("2) Populate live AU pricing via scripts/prompt_templates/browser_pricing_lookup.md")
    print("3) Apply sync rules via scripts/prompt_templates/track1_card_shortlist_sync_prompt.md")
    print("4) Fill MCDA factors via scripts/prompt_templates/ai_scoring_execution_prompt.md")

    # 3) Ranking
    ranked_output = Path(args.ranked_output) if args.ranked_output else shortlist_path.parent / f"{shortlist_path.stem}_ranked.csv"
    run([
        sys.executable,
        "scripts/scoring/rubric_weighting_engine.py",
        "--csv",
        str(enriched_path),
        "--output-csv",
        str(ranked_output),
    ])

    print("\nFinal memo checkpoint:")
    print("Use scripts/prompt_templates/final_purchase_justification_prompt.md with ranked CSV + winner card.")
    print(f"Ranked output: {ranked_output}")


if __name__ == "__main__":
    main()
