#!/usr/bin/env python3
"""
Update or create product card markdown files from a scored shortlist CSV.

Requirements:
  pip install pyyaml

Usage:
  python scripts/cards/update_cards_from_scored_shortlist.py \\
    --input shortlists/shortlist_2026-06-06_ranked.csv \\
    --cards-dir cards/laptops \\
    [--slug-field item_name] \\
    [--dry-run]

  --slug-field: CSV column to use as the card filename slug.
                Defaults to product_name slugification.
                Use 'item_name' or 'machine' to match existing card naming conventions.
                DO NOT use vendor_item_id (numeric) for existing card libraries.

  --dry-run: Preview changes without writing to disk.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required. Install with: pip install pyyaml") from exc

DEFAULT_NEW_BODY = """## Summary

## Key Specs

## Upgrade Path

## Battery Health

## Acquisition Risk

## Risk Flags

## Policy Check

## Price History

## Manual Notes
"""

FRONTMATTER_FIELDS = [
    "vendor_item_id", "product_name", "product_url", "source_label", "source_platform",
    "source_tier", "seller_risk_score", "list_price_aud", "risk_adjusted_price",
    "condition", "seller_name", "seller_class",
    "seller_feedback_count", "seller_feedback_pct", "shipping_cost_aud", "stock_status",
    "price_collected_at", "gpu_model", "vram_gb", "ram_gb", "weight_kg",
    "battery_disclosure_level", "battery_health_pct", "battery_cycle_count",
    "battery_replaced", "battery_score", "battery_disclosure_score",
    "battery_health_value_score", "has_thunderbolt_5", "has_thunderbolt_4",
    "egpu_confirmed", "pcie_slot_available", "gpu_user_swappable", "ram_upgradeable",
    "spare_m2_slot", "score_performance_headroom", "score_price_value",
    "score_future_proof", "score_portability", "score_track2_avoidance",
    "score_upgrade_ceiling", "score_acquisition_risk", "penalty_performance",
    "penalty_portability", "penalty_future_proof", "penalty_upgrade_ceiling",
    "score_total", "rank", "policy_status", "policy_flags", "risk_flags",
    "upgrade_path_summary", "warranty_months", "warranty_au_redeemable",
    "returns_accepted", "manufacture_year", "listing_date", "listing_status",
    "last_updated",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Update or create product card markdown files from a scored shortlist CSV."
    )
    parser.add_argument("--input", required=True, help="Path to scored shortlist CSV")
    parser.add_argument("--cards-dir", required=True, help="Directory for markdown cards")
    # FIX C5: --slug-field lets users align with existing card naming convention
    parser.add_argument(
        "--slug-field",
        default="",
        help=(
            "CSV column to use as the card filename slug "
            "(e.g. 'item_name', 'machine'). "
            "Defaults to slugified product_name. "
            "Avoid using vendor_item_id for existing card libraries."
        ),
    )
    # FIX M5: dry-run mode
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be created/updated without writing any files.",
    )
    return parser.parse_args()


def normalize_value(value: str) -> Any:
    if value is None:
        return None
    s = str(value).strip()
    if s == "":
        return ""
    lower = s.lower()
    if lower in {"true", "false"}:
        return lower == "true"
    if lower in {"none", "null", "nan"}:
        return ""
    if re.fullmatch(r"-?\d+", s):
        try:
            return int(s)
        except ValueError:
            return s
    if re.fullmatch(r"-?\d+\.\d+", s):
        try:
            return float(s)
        except ValueError:
            return s
    return s


# FIX C6 (frontmatter): flexible \n?--- closing delimiter to prevent data-loss on edge cases
def split_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    # FIX: \n? before closing --- handles files with no trailing newline before ---
    match = re.match(r"^---\n(.*?)\n?---\n?(.*)$", text, flags=re.DOTALL)
    if not match:
        return {}, text
    raw_yaml, body = match.groups()
    try:
        data = yaml.safe_load(raw_yaml) or {}
    except Exception:
        data = {}
    return data, body


def dump_frontmatter(data: Dict[str, Any], body: str) -> str:
    yaml_text = yaml.safe_dump(
        data, sort_keys=False, allow_unicode=True, default_flow_style=False
    ).strip()
    return f"---\n{yaml_text}\n---\n\n{body.lstrip(chr(10))}"


def make_slug(row: Dict[str, str], slug_field: str) -> Optional[str]:
    """
    FIX C5: build slug from explicit --slug-field, then product_name, never raw vendor_item_id.
    Returns None if no usable slug can be formed (row will be skipped).
    """
    # Try explicit slug field first
    if slug_field:
        val = str(row.get(slug_field) or "").strip()
        if val:
            return re.sub(r"[^a-z0-9]+", "-", val.lower()).strip("-")

    # Fall back to slugified product_name
    name = str(row.get("product_name") or "").strip()
    if name:
        return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

    return None


def card_path(cards_dir: Path, row: Dict[str, str], slug_field: str) -> Optional[Path]:
    slug = make_slug(row, slug_field)
    if not slug or len(slug) < 2:
        return None
    return cards_dir / f"{slug}.md"


def build_frontmatter(existing: Dict[str, Any], row: Dict[str, str]) -> Dict[str, Any]:
    out = dict(existing)
    for field in FRONTMATTER_FIELDS:
        if field == "last_updated":
            out[field] = dt.datetime.now().isoformat(timespec="seconds")
        else:
            val = row.get(field)
            if val is not None:
                out[field] = normalize_value(val)
            elif field not in out:
                out[field] = ""
    if "policy_status" not in out or not out["policy_status"]:
        out["policy_status"] = "PENDING_REVIEW"
    return out


def main() -> None:
    args = parse_args()
    input_csv = Path(args.input)
    cards_dir = Path(args.cards_dir)
    dry_run: bool = args.dry_run
    slug_field: str = args.slug_field

    if dry_run:
        print("[dry-run] No files will be written.")

    if not input_csv.exists():
        print(f"[error] Input CSV {input_csv} does not exist.")
        return

    if not dry_run:
        cards_dir.mkdir(parents=True, exist_ok=True)

    with input_csv.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    updated = created = skipped = 0

    for row in rows:
        path = card_path(cards_dir, row, slug_field)

        # FIX H3: increment skipped for rows without a usable slug
        if path is None:
            skipped += 1
            name = row.get("product_name") or row.get("vendor_item_id") or "?"
            print(f"[warn] Skipping row — no usable slug: {name!r}")
            continue

        if path.exists():
            text = path.read_text(encoding="utf-8")
            existing_frontmatter, body = split_frontmatter(text)
            if not body.strip():
                body = DEFAULT_NEW_BODY
            new_frontmatter = build_frontmatter(existing_frontmatter, row)
            if dry_run:
                print(f"[dry-run] Would UPDATE: {path}")
            else:
                path.write_text(dump_frontmatter(new_frontmatter, body), encoding="utf-8")
            updated += 1
        else:
            new_frontmatter = build_frontmatter({}, row)
            if not new_frontmatter.get("policy_status"):
                new_frontmatter["policy_status"] = "PENDING_REVIEW"
            if dry_run:
                print(f"[dry-run] Would CREATE: {path}")
            else:
                path.write_text(
                    dump_frontmatter(new_frontmatter, DEFAULT_NEW_BODY), encoding="utf-8"
                )
            created += 1

    prefix = "[dry-run] " if dry_run else ""
    print(f"{prefix}cards updated={updated} created={created} skipped={skipped}")


if __name__ == "__main__":
    main()
