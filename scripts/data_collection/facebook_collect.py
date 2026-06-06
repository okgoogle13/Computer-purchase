#!/usr/bin/env python3
"""
Parse Facebook Marketplace listings from a user-exported HAR file into canonical CSV.

Requirements:
  No third-party dependencies (stdlib only).

HOW TO CAPTURE A HAR FILE
--------------------------
1. Open Chrome or Firefox and log into Facebook.
2. Navigate to Facebook Marketplace > Computers & Laptops (or your target category).
3. Open DevTools (F12) → Network tab.
4. Browse and scroll through the listings you want to capture.
5. In the Network tab, right-click any request → "Save all as HAR with content".
6. Save the .har file (e.g. data/raw/facebook_marketplace/session_export.har).
7. Run this script against the saved file.

The script looks for GraphQL responses containing marketplace listing data
in the HAR's network entries and extracts all listings found.

Usage:
  python scripts/data_collection/facebook_collect.py \\
    --har data/raw/facebook_marketplace/session_export.har \\
    --output data/processed/facebook_marketplace_2026-06-06.csv
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

# FIX H1: source_platform and seller_risk_score added to canonical FIELDS
FIELDS = [
    "vendor_item_id",
    "product_name",
    "product_url",
    "source_label",
    "source_platform",       # FIX H1
    "source_tier",
    "seller_risk_score",     # FIX H1
    "list_price_aud",
    "currency",
    "condition",
    "seller_name",
    "seller_class",
    "seller_feedback_count",
    "seller_feedback_pct",
    "shipping_cost_aud",
    "listing_country",
    "listing_date",          # FIX H4
    "listing_status",        # FIX H4
    "returns_accepted",
    "warranty_months",
    "battery_disclosure_level",
    "battery_health_pct",
    "battery_cycle_count",
    "battery_replaced",
    "risk_flags",
    "price_collected_at",
    "location_suburb",
    "description_snippet",
]

# FIX C4: Facebook GraphQL condition enum → canonical condition label
CONDITION_MAP: dict[str, str] = {
    "new": "new",
    "used_like_new": "like_new",
    "used_good": "used_good",
    "used_fair": "fair",
    "refurbished": "refurbished",
    "not_specified": "unknown",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Parse Facebook Marketplace HAR export, raw JSON dump, or ParseHub output into canonical CSV."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--har", help="Path to exported HAR file")
    group.add_argument("--json-dump", help="Path to targeted search GraphQL JSON dump")
    group.add_argument("--parsehub", help="Path to ParseHub JSON output")
    parser.add_argument("--output", required=True, help="Output CSV path")
    return parser.parse_args()


def load_har(path: Path) -> Dict[str, Any]:
    # FIX: error handling for malformed/missing HAR
    try:
        with path.open("r", encoding="utf-8", errors="replace") as f:
            return json.load(f)
    except json.JSONDecodeError as exc:
        print(f"[error] HAR file is not valid JSON: {exc}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(f"[error] HAR file not found: {path}", file=sys.stderr)
        sys.exit(1)


def safe_get(obj: Any, *path: Any, default: Any = None) -> Any:
    cur = obj
    for key in path:
        if isinstance(cur, dict):
            cur = cur.get(key, default)
            if cur is default:
                return default
        elif isinstance(cur, list) and isinstance(key, int) and 0 <= key < len(cur):
            cur = cur[key]
        else:
            return default
    return cur


def maybe_json_loads(s: str) -> Optional[Any]:
    try:
        return json.loads(s)
    except Exception:
        return None


def extract_response_json(entry: Dict[str, Any]) -> Optional[Any]:
    text = safe_get(entry, "response", "content", "text", default="")
    if not text:
        return None
    return maybe_json_loads(text)


# FIX: iterative walk to avoid recursion limit on large HAR files
def walk(obj: Any) -> Iterable[Any]:
    """Iterative DFS walk of nested dicts/lists — avoids Python recursion limit."""
    stack = [obj]
    while stack:
        current = stack.pop()
        if isinstance(current, dict):
            yield current
            stack.extend(current.values())
        elif isinstance(current, list):
            stack.extend(current)


def looks_like_listing(node: Dict[str, Any]) -> bool:
    keys = set(node.keys())
    if "listing" in keys and isinstance(node.get("listing"), dict):
        return True
    if {"id", "marketplace_listing_title"}.issubset(keys):
        return True
    if "marketplace_listing_title" in keys or "listing_price" in keys:
        return True
    return False


# FIX M4: battery logic as standalone function (shared pattern with gumtree)
def extract_battery_fields(lower_blob: str) -> dict:
    battery_disclosure_level = "none"
    battery_health_pct: int | str = ""
    battery_cycle_count: int | str = ""
    battery_replaced = False

    pct = re.search(r"(\d{2,3})\s*%\s*(battery|health|capacity)", lower_blob)
    cyc = re.search(r"cycle[s]?\D{0,10}(\d{1,4})", lower_blob)

    if pct:
        battery_health_pct = int(pct.group(1))
        battery_disclosure_level = "tested_pct"
    if cyc:
        battery_cycle_count = int(cyc.group(1))
        battery_disclosure_level = "tested_pct_cycles" if pct else "cycles_only"
    if "new battery" in lower_blob or "battery replaced" in lower_blob:
        battery_replaced = True
        if battery_disclosure_level == "none":
            battery_disclosure_level = "replaced"

    return {
        "battery_disclosure_level": battery_disclosure_level,
        "battery_health_pct": battery_health_pct,
        "battery_cycle_count": battery_cycle_count,
        "battery_replaced": battery_replaced,
    }


def extract_listing_candidate(node: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    listing = node.get("listing") if isinstance(node.get("listing"), dict) else node

    listing_id = (
        listing.get("id")
        or safe_get(listing, "listing", "id")
        or safe_get(listing, "marketplace_listing", "id")
    )
    if not listing_id:
        return None

    title: str = (
        listing.get("marketplace_listing_title")
        or listing.get("title")
        or safe_get(listing, "name")
        or ""
    )

    # FIX C3: Facebook stores price as integer cents in amount_with_offset_in_currency
    price_obj = listing.get("listing_price") or {}
    amount: float | str = ""
    currency = "AUD"
    if isinstance(price_obj, dict):
        currency = price_obj.get("currency") or "AUD"
        amount_raw = (
            price_obj.get("amount_with_offset_in_currency")  # PRIMARY: integer cents
            or price_obj.get("amount")
            or price_obj.get("value")
            or safe_get(price_obj, "formatted_amount")
        )
        if amount_raw is not None and amount_raw != "":
            try:
                # amount_with_offset_in_currency is cents (e.g. 150000 = $1,500.00)
                raw_float = float(amount_raw)
                amount = raw_float / 100.0 if raw_float > 9999 else raw_float
            except (ValueError, TypeError):
                amount = str(amount_raw)

    location: str = (
        safe_get(listing, "location", "reverse_geocode", "city_page", "display_name")
        or safe_get(listing, "location_text", "text")
        or safe_get(listing, "location", "name")
        or ""
    )

    seller_name: str = (
        safe_get(listing, "marketplace_listing_seller", "name")
        or safe_get(listing, "seller", "name")
        or ""
    )

    description: str = (
        listing.get("redacted_description")
        or listing.get("description")
        or ""
    )

    lower_blob = " ".join([str(title), str(description)]).lower()

    # FIX C4: extract from GraphQL structured condition enum first, fall back to text scan
    condition_raw = (
        listing.get("condition")
        or safe_get(listing, "marketplace_listing_renderable_fields", "condition")
        or safe_get(listing, "listing_attributes", "condition")
        or ""
    )
    condition = CONDITION_MAP.get(str(condition_raw).lower().strip(), "")
    if not condition:
        # Text-scan fallback — check most-specific labels first
        for label, mapped in [
            ("like new", "like_new"),
            ("very good", "very_good"),
            ("refurbished", "refurbished"),
            ("new", "new"),
            ("good", "used_good"),
            ("fair", "fair"),
            ("used", "used"),
        ]:
            if label in lower_blob:
                condition = mapped
                break
        else:
            condition = "unknown"

    # FIX H4: extract listing creation timestamp if available
    creation_time = (
        listing.get("creation_time")
        or safe_get(listing, "marketplace_listing_date_time_info", "creation_time")
        or ""
    )
    listing_date = ""
    if creation_time:
        try:
            listing_date = dt.datetime.utcfromtimestamp(int(creation_time)).strftime("%Y-%m-%dT%H:%M:%SZ")
        except (ValueError, TypeError, OSError):
            listing_date = str(creation_time)

    # Battery
    battery = extract_battery_fields(lower_blob)

    risk_flags = ["PRIVATE_MARKETPLACE", "NO_WARRANTY", "NO_RETURNS"]
    if battery["battery_disclosure_level"] == "none":
        risk_flags.append("BATTERY_UNDISCLOSED")

    product_url = f"https://www.facebook.com/marketplace/item/{listing_id}/"

    return {
        "vendor_item_id": str(listing_id),
        "product_name": title,
        "product_url": product_url,
        "source_label": "facebook_har",
        "source_platform": "FB_MARKETPLACE",   # FIX H1
        "source_tier": 3,
        "seller_risk_score": 3,                # FIX H1
        "list_price_aud": amount,
        "currency": currency,
        "condition": condition,
        "seller_name": seller_name,
        "seller_class": "private",
        "seller_feedback_count": "",
        "seller_feedback_pct": "",
        "shipping_cost_aud": "",
        "listing_country": "AU",
        "listing_date": listing_date,          # FIX H4
        "listing_status": "active",            # FIX H4
        "returns_accepted": False,
        "warranty_months": 0,
        "battery_disclosure_level": battery["battery_disclosure_level"],
        "battery_health_pct": battery["battery_health_pct"],
        "battery_cycle_count": battery["battery_cycle_count"],
        "battery_replaced": battery["battery_replaced"],
        "risk_flags": ",".join(risk_flags),
        "price_collected_at": dt.datetime.now().isoformat(timespec="seconds"),
        "location_suburb": location,
        "description_snippet": str(description)[:200],
    }


def extract_marketplace_rows(har: Dict[str, Any]) -> List[Dict[str, Any]]:
    entries = safe_get(har, "log", "entries", default=[])
    rows: Dict[str, Dict[str, Any]] = {}
    entries_scanned = 0

    for entry in entries:
        url = safe_get(entry, "request", "url", default="") or ""
        if "graphql" not in url.lower() and "marketplace" not in url.lower():
            continue

        payload = extract_response_json(entry)
        if not payload:
            continue

        entries_scanned += 1
        for node in walk(payload):
            if isinstance(node, dict) and looks_like_listing(node):
                row = extract_listing_candidate(node)
                if row and row.get("vendor_item_id"):
                    rows[row["vendor_item_id"]] = row

    print(f"[info] GraphQL/marketplace entries scanned: {entries_scanned}")
    return list(rows.values())


def extract_marketplace_rows_from_json(json_data: list) -> list[dict]:
    rows: dict[str, dict] = {}
    entries_scanned = 0

    for entry in json_data:
        payload = entry.get("data")
        if not payload:
            continue

        entries_scanned += 1
        for node in walk(payload):
            if isinstance(node, dict) and looks_like_listing(node):
                row = extract_listing_candidate(node)
                if row and row.get("vendor_item_id"):
                    rows[row["vendor_item_id"]] = row

    print(f"[info] GraphQL/marketplace entries scanned from JSON dump: {entries_scanned}")
    return list(rows.values())


def extract_parsehub_rows(json_data: dict) -> list[dict]:
    """Extract rows from a ParseHub JSON output.
    Assumes the ParseHub template extracts a list of 'listings' with 'title', 'price', 'url', etc.
    """
    rows: dict[str, dict] = {}
    
    # Parsehub usually puts list data under the name you gave it in the template, e.g., 'listings' or 'results'
    # We'll look for a few common list keys, or just iterate if the root is a list.
    listings_raw = json_data.get("listings") or json_data.get("results") or json_data.get("items") or []
    if not listings_raw and isinstance(json_data, list):
        listings_raw = json_data
        
    for item in listings_raw:
        url = item.get("url") or item.get("product_url") or ""
        # Extract vendor_item_id from Facebook Marketplace URL
        # e.g., https://www.facebook.com/marketplace/item/123456789/
        match = re.search(r"item/(\d+)", url)
        vendor_item_id = match.group(1) if match else ""
        if not vendor_item_id:
            continue
            
        title = item.get("title") or item.get("name") or ""
        price_raw = item.get("price") or item.get("list_price_aud") or ""
        
        # Clean price (e.g. "A$1,500", "$1500")
        price_clean = re.sub(r"[^\d\.]", "", str(price_raw))
        amount = float(price_clean) if price_clean else ""
        
        condition_raw = item.get("condition") or "unknown"
        condition = CONDITION_MAP.get(str(condition_raw).lower().strip(), "unknown")
        
        location = item.get("location") or ""
        
        row = {
            "vendor_item_id": vendor_item_id,
            "product_name": title,
            "product_url": url,
            "source_label": "facebook_parsehub",
            "source_platform": "FB_MARKETPLACE",
            "source_tier": 3,
            "seller_risk_score": 3,
            "list_price_aud": amount,
            "currency": "AUD",
            "condition": condition,
            "seller_name": item.get("seller_name", ""),
            "seller_class": "private",
            "seller_feedback_count": "",
            "seller_feedback_pct": "",
            "shipping_cost_aud": "",
            "listing_country": "AU",
            "listing_date": "",
            "listing_status": "active",
            "returns_accepted": False,
            "warranty_months": 0,
            "battery_disclosure_level": "none",
            "battery_health_pct": "",
            "battery_cycle_count": "",
            "battery_replaced": False,
            "risk_flags": "PRIVATE_MARKETPLACE,NO_WARRANTY,NO_RETURNS",
            "price_collected_at": dt.datetime.now().isoformat(timespec="seconds"),
            "location_suburb": location,
            "description_snippet": str(item.get("description", ""))[:200],
        }
        rows[vendor_item_id] = row
        
    print(f"[info] ParseHub listings parsed: {len(rows)}")
    return list(rows.values())


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in FIELDS})


def main() -> None:
    args = parse_args()
    output_path = Path(args.output)

    if args.har:
        har_path = Path(args.har)
        print(f"[info] Loading HAR: {har_path}")
        har = load_har(har_path)
        rows = extract_marketplace_rows(har)
    elif args.json_dump:
        json_path = Path(args.json_dump)
        print(f"[info] Loading JSON Dump: {json_path}")
        try:
            with json_path.open("r", encoding="utf-8", errors="replace") as f:
                json_data = json.load(f)
            rows = extract_marketplace_rows_from_json(json_data)
        except Exception as exc:
            print(f"[error] Failed to load JSON dump: {exc}", file=sys.stderr)
            sys.exit(1)
    else:
        parsehub_path = Path(args.parsehub)
        print(f"[info] Loading ParseHub Output: {parsehub_path}")
        try:
            with parsehub_path.open("r", encoding="utf-8", errors="replace") as f:
                json_data = json.load(f)
            rows = extract_parsehub_rows(json_data)
        except Exception as exc:
            print(f"[error] Failed to load ParseHub JSON: {exc}", file=sys.stderr)
            sys.exit(1)

    write_csv(output_path, rows)

    print(f"[done] facebook_har rows written: {len(rows)}")
    print(f"[done] output: {output_path}")
    if len(rows) == 0:
        print(
            "[warn] Zero rows extracted. Ensure the HAR/JSON was captured while browsing "
            "Facebook Marketplace listings, not just the home page."
        )


if __name__ == "__main__":
    main()
