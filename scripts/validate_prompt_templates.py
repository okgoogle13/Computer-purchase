#!/usr/bin/env python3
"""Contract checks for prompt templates used by the hardware prompt chain."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = REPO_ROOT / "scripts" / "prompt_templates"

REQUIRED_PATTERNS = {
    "notebooklm_system_prompt.md": [
        "source of truth",
        "AGENTS.md",
        "config/procurement_policy.json",
    ],
    "audit_checklist_prompt.md": [
        "Output only the exact checklist",
    ],
    "pre_scoring_validation_prompt.md": [
        '"ready_to_score"',
        '"unscoreable"',
        '"orphaned_csv"',
        '"orphaned_cards"',
        '"price_stale"',
    ],
    "browser_pricing_lookup.md": [
        "Required Output Contract",
        '"candidate_id"',
        '"source_platform"',
        '"seller_class"',
        '"pricing_checked_at"',
    ],
    "track1_card_shortlist_sync_prompt.md": [
        "Required Output",
        '"csv_row_updates"',
        '"card_field_updates"',
        '"conflicts"',
        '"unresolved_unknowns"',
    ],
    "ai_scoring_execution_prompt.md": [
        "Output only a CSV block",
        "Leave `MCDA_Total` blank",
    ],
    "final_purchase_justification_prompt.md": [
        "Final Recommendation",
        "Recommendation: PROCEED",
        "Recommendation: PROCEED WITH CONDITIONS",
        "Recommendation: DO NOT PROCEED",
    ],
}


def main() -> None:
    errors: list[str] = []
    for filename, patterns in REQUIRED_PATTERNS.items():
        path = TEMPLATES / filename
        if not path.exists():
            errors.append(f"Missing template: {filename}")
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in patterns:
            if pattern not in text:
                errors.append(f"{filename}: missing pattern `{pattern}`")

    if errors:
        print("Prompt contract validation FAILED")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)

    print("Prompt contract validation PASSED")


if __name__ == "__main__":
    main()
