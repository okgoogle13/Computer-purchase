#!/usr/bin/env python3
"""
fill_shortlist_live_pricing.py — Phase 3 live pricing fill step.

Reads a *_pricing_enriched.csv file and fills pricing fields for candidates in the
verification queue.

Verification queue predicate:
- Candidate is queued if any core live-pricing field is blank or UNKNOWN:
  current_best_price_aud, current_best_retailer, current_best_url,
  in_stock_now, pricing_checked_at.
- This keeps re-runs idempotent for already verified rows while allowing
  partially-complete rows to be retried.

The lookup is delegated to browser_agent_lookup(row), currently a placeholder that
returns an empty dict. Integrate your browser agent there.

Optional secondary confirmation (for example ScraperAPI) should be implemented in
scraper_confirm_lookup() and explicitly wired by a future integration pass. It is
intentionally unused by default in this scaffolded orchestrator.
"""

import argparse
import csv
import sys
from pathlib import Path
from typing import Dict, Iterable, List

PRICING_COLUMNS = [
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
]

BROWSER_AGENT_RESPONSE_FIELDS = [
    "candidate_id",
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
]

QUEUE_FIELDS = [
    "current_best_price_aud",
    "current_best_retailer",
    "current_best_url",
    "in_stock_now",
    "pricing_checked_at",
]

UNRESOLVED_TOKENS = {"unknown", "n/a", "none", "-"}


def normalize_value(value: str) -> str:
    return (value or "").strip()


def is_unknown_or_blank(value: str) -> bool:
    v = normalize_value(value).lower()
    return v == "" or v in UNRESOLVED_TOKENS


def in_verification_queue(row: Dict[str, str]) -> bool:
    return any(is_unknown_or_blank(row.get(field, "")) for field in QUEUE_FIELDS)


def browser_agent_lookup(row: Dict[str, str]) -> Dict[str, str]:
    """
    Browser-agent integration using Gemini API and Browserless.
    """
    import os
    import json
    import requests
    from dotenv import load_dotenv
    from pathlib import Path
    
    load_dotenv()
    gemini_key = os.environ.get("GEMINI_API_KEY")
    browserless_key = os.environ.get("BROWSERLESS_API_KEY")
    
    if not gemini_key:
        print("Warning: No GEMINI_API_KEY found.")
        return {}

    candidate_id = get_row_identifier(row)
    item_name = row.get("item_name", candidate_id)
    print(f"Looking up {item_name} via Gemini Browser Agent...")
    
    prompt_path = Path("scripts/prompt_templates/browser_pricing_lookup.md")
    prompt = prompt_path.read_text(encoding="utf-8") if prompt_path.exists() else ""
    prompt = prompt.replace("[INSERT ITEM NAME AND SPECS HERE]", f"Item: {item_name}")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={gemini_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "tools": [{"google_search": {}}],
        "generationConfig": {"temperature": 0.1, "responseMimeType": "application/json"}
    }
    
    try:
        res = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        if res.status_code == 200:
            data = res.json()
            text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "{}")
            result = json.loads(text)
            result["candidate_id"] = candidate_id
            return result
        else:
            print(f"Gemini API Error: {res.text}")
    except Exception as e:
        print(f"Agent lookup failed: {e}")
        
    return {}


def scraper_confirm_lookup(row: Dict[str, str]) -> Dict[str, str]:
    """
    Optional confirmation hook for a secondary pricing source.
    Intentionally returns empty data and is not called by default.
    """
    return {}


def validate_agent_response(data: Dict[str, str]) -> Dict[str, str]:
    if not isinstance(data, dict):
        raise ValueError("browser_agent_lookup() must return a dict.")
    unknown_keys = [k for k in data.keys() if k not in BROWSER_AGENT_RESPONSE_FIELDS]
    if unknown_keys:
        raise ValueError(f"Unexpected browser-agent keys: {', '.join(sorted(unknown_keys))}")
    return data


def get_row_identifier(row: Dict[str, str]) -> str:
    return normalize_value(row.get("intake_id", "")) or normalize_value(row.get("id", ""))


def validate_candidate_identity(row: Dict[str, str], agent_data: Dict[str, str]) -> None:
    agent_candidate_id = normalize_value(str(agent_data.get("candidate_id", "")))
    if not agent_candidate_id:
        return
    row_identifier = get_row_identifier(row)
    if not row_identifier:
        raise ValueError("Row has no intake_id/id for candidate identity validation.")
    if agent_candidate_id != row_identifier:
        raise ValueError(
            f"candidate_id mismatch: agent={agent_candidate_id} row={row_identifier}"
        )


def merge_agent_data(row: Dict[str, str], agent_data: Dict[str, str]) -> None:
    for key, value in agent_data.items():
        if key == "candidate_id":
            continue
        if key in PRICING_COLUMNS:
            row[key] = "" if value is None else str(value)


def ensure_pricing_columns(fieldnames: Iterable[str]) -> List[str]:
    names = list(fieldnames)
    for col in PRICING_COLUMNS:
        if col not in names:
            names.append(col)
    return names


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Fill live pricing fields for verification-queue rows in a *_pricing_enriched.csv "
            "file using a browser-agent lookup placeholder."
        )
    )
    parser.add_argument("csv_path", type=str, help="Path to an enriched shortlist CSV")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the output file if it already exists.",
    )
    args = parser.parse_args()

    input_path = Path(args.csv_path)
    if not input_path.exists():
        sys.exit(f"Error: Input file {input_path} does not exist.")

    output_path = input_path.parent / f"{input_path.stem}_live.csv"
    if output_path.exists() and not args.force:
        sys.exit(
            f"Error: Output file {output_path} already exists. "
            "Use --force to overwrite intentionally."
        )

    with open(input_path, "r", encoding="utf-8") as fin:
        reader = csv.DictReader(fin)
        if not reader.fieldnames:
            sys.exit("Error: Input CSV has no headers.")
        fieldnames = ensure_pricing_columns(reader.fieldnames)
        rows = list(reader)

    attempted = 0
    updated = 0
    failed = 0
    failed_ids: List[str] = []
    for row in rows:
        for col in PRICING_COLUMNS:
            if col not in row:
                row[col] = ""
        if not in_verification_queue(row):
            continue
        attempted += 1
        row_identifier = get_row_identifier(row) or "<unknown-row-id>"
        try:
            response = browser_agent_lookup(row)
            response = validate_agent_response(response)
            validate_candidate_identity(row, response)
            merge_agent_data(row, response)
            updated += 1
        except Exception as exc:
            failed += 1
            failed_ids.append(row_identifier)
            print(f"Row failed [{row_identifier}]: {exc}")

    with open(output_path, "w", newline="", encoding="utf-8") as fout:
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Live pricing fill completed: {output_path}")
    print("Lookup mode: placeholder browser_agent_lookup (no live integration by default)")
    print(f"Rows attempted: {attempted}")
    print(f"Rows updated: {updated}")
    print(f"Rows failed: {failed}")
    if failed_ids:
        print(f"Failed identifiers: {', '.join(failed_ids)}")


if __name__ == "__main__":
    main()
