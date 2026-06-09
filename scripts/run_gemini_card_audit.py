#!/usr/bin/env python3
"""
run_gemini_card_audit.py — Phase 1 card coverage audit via Gemini 3.5 Flash.

Offloads the mechanical shortlist ↔ card cross-reference from Claude Sonnet to
Gemini 3.5 Flash (~40× cheaper). Reads card frontmatter only (not full card
bodies), so the prompt is ~10–15k tokens vs ~65k for full card loads in Claude.

Thinking tiers (--thinking flag):
  low    — thinkingBudget 0    — no reasoning, fastest/cheapest (default, suits Phase 1 audit)
  medium — thinkingBudget 1024 — light reasoning, good for edge-case classification
  high   — thinkingBudget 8192 — deeper reasoning, use for gap analysis or ambiguous inventories

Usage:
    python scripts/run_gemini_card_audit.py
    python scripts/run_gemini_card_audit.py --shortlist shortlists/2026-06-08_shortlist.csv
    python scripts/run_gemini_card_audit.py --thinking medium --output output/gap_analysis.json

Requires GEMINI_API_KEY in environment or .env file.
"""

import argparse
import csv
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Dict, List

try:
    import requests
except ImportError:
    sys.exit("Error: 'requests' is required. Run: pip install requests")

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

REPO_ROOT = Path(__file__).resolve().parent.parent
GEMINI_MODEL = "gemini-3.5-flash"
GEMINI_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/"
    f"{GEMINI_MODEL}:generateContent"
)

# Thinking budget per tier. 0 = disabled (no reasoning, fastest).
THINKING_BUDGETS = {"low": 0, "medium": 1024, "high": 8192}

# Frontmatter keys surfaced to the audit prompt — enough to classify without
# loading full card bodies.
FRONTMATTER_KEYS = {
    "intake_id", "item_name", "status", "track", "pathway", "profile",
    "category", "gpu_model", "vram_gb", "unified_memory_gb",
    "price_aud", "current_best_price_aud", "condition", "retailer",
    "au_stock", "thermal_flag", "verification_status",
}

# Shortlist columns forwarded to the prompt.
KEY_SHORTLIST_FIELDS = {
    "intake_id", "item_name", "status", "track", "pathway",
    "gpu_model", "vram_gb", "price_aud", "current_best_price_aud",
    "Over_Budget", "thermal_flag",
}

AUDIT_PROMPT = """\
You are performing a Phase 1 coverage audit for a hardware procurement shortlist.

## Definitions
- "Missing": appears in shortlist_rows but NO corresponding card exists in \
cards_inventory (match on item_name or intake_id).
- "Underutilized": a card exists in cards_inventory but the item is absent \
from shortlist_rows, OR present with incorrect track/pathway so it is not \
being actively considered.
- "Orphan_Card": card exists but was clearly never a shortlist candidate \
(low-priority, include only if obvious).

Focus output on "Missing" and "Underutilized" — these are lost procurement \
opportunities.

## Shortlist Rows (active candidates)
{shortlist_json}

## Card Inventory (frontmatter summaries only)
{cards_json}

## Output
Return ONLY valid JSON. No markdown fences, no text outside the JSON.

{{
  "phase1_findings": [
    {{
      "candidate": "<item_name or card filename>",
      "track_pathway": "<e.g. 1 / 1A, or UNKNOWN>",
      "classification": "<Missing|Underutilized|Orphan_Card>",
      "why_potentially_high_upside": "<one line>",
      "budget_posture": "<within_cap|over_cap|unknown>",
      "evidence_strength": "<strong|moderate|weak>",
      "notes": "<source of discrepancy>"
    }}
  ],
  "dedup_log": [
    {{
      "action": "<Merged opportunity|Kept separate with reason|Discarded as non-material duplicate>",
      "candidates": ["<name1>", "<name2>"],
      "reason": "<one line>"
    }}
  ],
  "conflicts": [
    {{
      "candidate": "<name>",
      "field": "<field>",
      "values": ["<val_from_shortlist>", "<val_from_card>"],
      "provisional_preferred": "<preferred>",
      "reason": "<why>"
    }}
  ],
  "audit_summary": {{
    "total_shortlist_rows": <int>,
    "total_cards": <int>,
    "missing_count": <int>,
    "underutilized_count": <int>,
    "orphan_card_count": <int>
  }}
}}
"""


def parse_frontmatter(md_text: str) -> Dict[str, str]:
    """Extract YAML frontmatter between first pair of ---."""
    match = re.search(r"---\s*\n(.*?)\n---", md_text, re.DOTALL)
    if not match:
        return {}
    fm: Dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        fm[key.strip()] = val.strip()
    return fm


def load_card_inventory(cards_dir: Path) -> List[Dict[str, str]]:
    """Return frontmatter summaries for every .md card under cards_dir."""
    inventory: List[Dict[str, str]] = []
    for md_path in sorted(cards_dir.rglob("*.md")):
        text = md_path.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        if not fm:
            continue
        # Standardize keys
        if "id" in fm and "intake_id" not in fm:
            fm["intake_id"] = fm["id"]
        if "name" in fm and "item_name" not in fm:
            fm["item_name"] = fm["name"]
        if "gpu" in fm and "gpu_model" not in fm:
            fm["gpu_model"] = fm["gpu"]
        if "vram" in fm and "vram_gb" not in fm:
            fm["vram_gb"] = fm["vram"]

        summary = {k: v for k, v in fm.items() if k in FRONTMATTER_KEYS or k in {"id", "name", "gpu", "vram"}}
        summary["_card_file"] = str(md_path.relative_to(cards_dir.parent))
        inventory.append(summary)
    return inventory


def load_shortlist(csv_path: Path) -> List[Dict[str, str]]:
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def call_gemini(prompt: str, api_key: str, thinking_budget: int = 0) -> Dict:
    """Call Gemini 3.5 Flash with retry on 429. Returns parsed JSON dict."""
    url = f"{GEMINI_URL}?key={api_key}"
    generation_config: Dict = {
        "responseMimeType": "application/json",
    }
    if thinking_budget > 0:
        generation_config["thinkingConfig"] = {"thinkingBudget": thinking_budget}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": generation_config,
    }
    headers = {"Content-Type": "application/json"}

    for attempt in (1, 2):
        try:
            res = requests.post(url, json=payload, headers=headers, timeout=120)
        except requests.RequestException as exc:
            raise RuntimeError(f"Request failed: {exc}")

        if res.status_code == 200:
            data = res.json()
            text = (
                data.get("candidates", [{}])[0]
                    .get("content", {})
                    .get("parts", [{}])[0]
                    .get("text", "{}")
            )
            try:
                return json.loads(text)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"Gemini returned non-JSON: {exc}\nRaw: {text[:500]}")

        if res.status_code == 429 and attempt == 1:
            print("Rate limit (429). Retrying in 15 seconds...")
            time.sleep(15)
            continue

        raise RuntimeError(f"Gemini API error {res.status_code}: {res.text[:500]}")

    raise RuntimeError("Gemini API error: failed after retry.")


def run_local_audit(shortlist_rows: List[Dict[str, str]], card_inventory: List[Dict[str, str]]) -> Dict:
    """Perform precise, local, mechanical shortlist ↔ card matching and validation."""
    print("Running offline mechanical matching audit fallback...")
    cards_by_file = {c["_card_file"].replace("\\", "/"): c for c in card_inventory}
    cards_by_intake = {}
    cards_by_name = {}
    
    for c in card_inventory:
        iid = c.get("intake_id", "").strip().lower()
        name = c.get("item_name", "").strip().lower()
        if iid and iid != "unknown":
            cards_by_intake[iid] = c
        if name and name != "unknown":
            cards_by_name[name] = c

    findings = []
    conflicts = []
    matched_card_files = set()

    # Match shortlist rows to card inventory
    for row in shortlist_rows:
        row_iid = row.get("intake_id", "").strip().lower()
        row_name = row.get("item_name", "").strip().lower()
        row_file = row.get("source_file", "").strip().replace("\\", "/")
        
        # 1. Match by source_file path if present
        matched_card = None
        if row_file and row_file in cards_by_file:
            matched_card = cards_by_file[row_file]
        # 2. Match by intake_id
        elif row_iid and row_iid != "unknown" and row_iid in cards_by_intake:
            matched_card = cards_by_intake[row_iid]
        # 3. Match by item_name
        elif row_name and row_name != "unknown" and row_name in cards_by_name:
            matched_card = cards_by_name[row_name]
        # 4. Substring fallback match
        else:
            for c in card_inventory:
                c_file = c["_card_file"].replace("\\", "/").lower()
                c_iid = c.get("intake_id", "").lower()
                c_name = c.get("item_name", "").lower()
                if (row_iid and row_iid != "unknown" and row_iid in c_file) or \
                   (row_name and row_name != "unknown" and row_name in c_name):
                    matched_card = c
                    break

        if not matched_card:
            price_val = row.get("current_best_price_aud") or row.get("price_aud", "0")
            try:
                price_f = float(price_val.replace("$", "").replace(",", ""))
                budget_posture = "within_cap" if price_f <= 5000 else "over_cap"
            except ValueError:
                budget_posture = "unknown"
                
            findings.append({
                "candidate": row.get("item_name") or row.get("intake_id"),
                "track_pathway": f"{row.get('track', 'UNKNOWN')} / {row.get('pathway', 'UNKNOWN')}",
                "classification": "Missing",
                "why_potentially_high_upside": "Active candidate listed in shortlist but has no card.",
                "budget_posture": budget_posture,
                "evidence_strength": "strong",
                "notes": f"No card found matching intake_id={row.get('intake_id')} or item_name={row.get('item_name')}."
            })
        else:
            matched_card_files.add(matched_card["_card_file"])
            # Track/Pathway mismatch check
            row_track = row.get("track", "").strip().lower()
            card_track = matched_card.get("track", "").strip().lower()
            row_pathway = row.get("pathway", "").strip().lower()
            card_pathway = matched_card.get("pathway", "").strip().lower()
            
            if (row_track and card_track and row_track != "unknown" and card_track != "unknown" and row_track != card_track) or \
               (row_pathway and card_pathway and row_pathway != "unknown" and card_pathway != "unknown" and row_pathway != card_pathway):
                findings.append({
                    "candidate": matched_card.get("item_name") or matched_card.get("_card_file"),
                    "track_pathway": f"{card_track.upper()} / {card_pathway.upper()}",
                    "classification": "Underutilized",
                    "why_potentially_high_upside": f"Track/pathway mismatch: shortlist specifies {row_track.upper()}/{row_pathway.upper()} but card has {card_track.upper()}/{card_pathway.upper()}.",
                    "budget_posture": "within_cap" if float(row.get("price_aud") or 0) <= 5000 else "over_cap",
                    "evidence_strength": "strong",
                    "notes": "Track/pathway mismatch."
                })

            # Check for conflict fields
            for field in ["gpu_model", "vram_gb"]:
                row_val = row.get(field, "").strip().lower()
                card_val = matched_card.get(field, "").strip().lower()
                if row_val and card_val and row_val != "unknown" and card_val != "unknown" and row_val != card_val:
                    conflicts.append({
                        "candidate": row.get("item_name"),
                        "field": field,
                        "values": [row.get(field), matched_card.get(field)],
                        "provisional_preferred": row.get(field),
                        "reason": f"Shortlist values take precedence for live routing check."
                    })

    # Find underutilized and orphan cards (cards without shortlist rows)
    for card in card_inventory:
        if card["_card_file"] in matched_card_files:
            continue
        
        card_track = card.get("track", "").strip()
        card_pathway = card.get("pathway", "").strip()
        
        is_active_track = card_track in ["1", "1.5", "2", "1A", "1B"] or card_pathway in ["1A", "1B", "A", "B", "C"]
        classification = "Underutilized" if is_active_track else "Orphan_Card"
        
        price_val = card.get("current_best_price_aud") or card.get("price_aud", "0")
        try:
            price_f = float(price_val.replace("$", "").replace(",", ""))
            budget_posture = "within_cap" if price_f <= 5000 else "over_cap"
        except ValueError:
            budget_posture = "unknown"

        findings.append({
            "candidate": card.get("item_name") or card.get("_card_file"),
            "track_pathway": f"{card_track} / {card_pathway}",
            "classification": classification,
            "why_potentially_high_upside": "Card exists in inventory but candidate is not in the shortlist.",
            "budget_posture": budget_posture,
            "evidence_strength": "strong",
            "notes": "Card exists in directory but is not present in active shortlist."
        })

    missing_count = sum(1 for f in findings if f["classification"] == "Missing")
    underutilized_count = sum(1 for f in findings if f["classification"] == "Underutilized")
    orphan_card_count = sum(1 for f in findings if f["classification"] == "Orphan_Card")

    return {
        "phase1_findings": findings,
        "dedup_log": [],
        "conflicts": conflicts,
        "audit_summary": {
            "total_shortlist_rows": len(shortlist_rows),
            "total_cards": len(card_inventory),
            "missing_count": missing_count,
            "underutilized_count": underutilized_count,
            "orphan_card_count": orphan_card_count
        }
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Phase 1 card coverage audit via Gemini 2.5 Flash.\n"
            "Offloads mechanical shortlist ↔ card cross-reference from Claude Sonnet."
        )
    )
    parser.add_argument(
        "--shortlist",
        default="shortlists/shortlist_profile-laptop_pricing_enriched_live.csv",
        help="Active shortlist CSV (default: shortlist_profile-laptop_pricing_enriched_live.csv)",
    )
    parser.add_argument(
        "--cards-dir",
        default="cards/",
        help="Root directory of product cards, searched recursively (default: cards/)",
    )
    parser.add_argument(
        "--output",
        default="output/card_audit_phase1.json",
        help="Output JSON file (default: output/card_audit_phase1.json)",
    )
    parser.add_argument(
        "--thinking",
        choices=["low", "medium", "high"],
        default="low",
        help=(
            "Gemini thinking tier: low=no reasoning/fastest (default), "
            "medium=edge-case classification, high=gap analysis"
        ),
    )
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")

    shortlist_path = (REPO_ROOT / args.shortlist).resolve()
    cards_dir = (REPO_ROOT / args.cards_dir).resolve()
    output_path = (REPO_ROOT / args.output).resolve()

    if not shortlist_path.exists():
        sys.exit(f"Error: Shortlist not found: {shortlist_path}")
    if not cards_dir.exists():
        sys.exit(f"Error: Cards directory not found: {cards_dir}")

    print(f"Loading shortlist: {shortlist_path.relative_to(REPO_ROOT)}")
    shortlist_rows = load_shortlist(shortlist_path)
    print(f"  {len(shortlist_rows)} rows")

    print(f"Loading card inventory: {cards_dir.relative_to(REPO_ROOT)}")
    card_inventory = load_card_inventory(cards_dir)
    print(f"  {len(card_inventory)} cards with frontmatter")

    result = None
    if api_key:
        shortlist_slim = [
            {k: v for k, v in row.items() if k in KEY_SHORTLIST_FIELDS}
            for row in shortlist_rows
        ]

        prompt = AUDIT_PROMPT.format(
            shortlist_json=json.dumps(shortlist_slim, indent=2),
            cards_json=json.dumps(card_inventory, indent=2),
        )
        thinking_budget = THINKING_BUDGETS[args.thinking]
        word_count = len(prompt.split())
        print(
            f"Sending audit prompt to {GEMINI_MODEL} "
            f"[thinking={args.thinking}, budget={thinking_budget}] "
            f"(~{word_count:,} words)..."
        )
        try:
            result = call_gemini(prompt, api_key, thinking_budget)
        except Exception as exc:
            print(f"Gemini API call failed: {exc}")
    else:
        print("GEMINI_API_KEY not found.")

    if result is None:
        result = run_local_audit(shortlist_rows, card_inventory)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    summary = result.get("audit_summary", {})
    findings = result.get("phase1_findings", [])
    print(f"\nCard audit complete → {output_path.relative_to(REPO_ROOT)}")
    print(f"  Shortlist rows :  {summary.get('total_shortlist_rows', len(shortlist_rows))}")
    print(f"  Cards scanned  :  {summary.get('total_cards', len(card_inventory))}")
    print(f"  Missing        :  {summary.get('missing_count', sum(1 for f in findings if f.get('classification') == 'Missing'))}")
    print(f"  Underutilized  :  {summary.get('underutilized_count', sum(1 for f in findings if f.get('classification') == 'Underutilized'))}")
    print(f"  Orphan cards   :  {summary.get('orphan_card_count', sum(1 for f in findings if f.get('classification') == 'Orphan_Card'))}")
    print(f"\nPass output/card_audit_phase1.json to Claude as Phase 1 context before running Phase 2 discovery.")


if __name__ == "__main__":
    main()
