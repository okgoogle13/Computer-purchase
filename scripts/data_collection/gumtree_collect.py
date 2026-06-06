#!/usr/bin/env python3
"""
Collect Gumtree laptop listings into canonical CSV format.

This implementation uses HTTP requests + BeautifulSoup for search results pages.
It is intended as a practical first-pass collector for public Gumtree pages.

Requirements:
  pip install requests beautifulsoup4

Usage:
  python scripts/data_collection/gumtree_collect.py \
    --query "gaming laptop RTX" \
    --output data/processed/gumtree_2026-06-06.csv \
    --max-pages 3

  # Debug selectors / verify DOM against current Gumtree markup:
  python scripts/data_collection/gumtree_collect.py \
    --query "gaming laptop RTX" \
    --output data/processed/gumtree_debug.csv \
    --max-pages 1 --debug

How to capture a HAR file for Facebook Marketplace:
  This script is for Gumtree only. For Facebook Marketplace, use facebook_collect.py
  with a HAR export from your browser dev tools (Network tab → Export HAR).
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import time
from pathlib import Path
from urllib.parse import quote_plus

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-AU,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

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

LAPTOP_INCLUDE = [
    "laptop", "notebook", "macbook", "thinkpad", "xps",
    "razer", "zephyrus", "proart", "elitebook", "precision",
    "blade", "rog", "legion",
]

LAPTOP_EXCLUDE = [
    "charger", "bag", "sleeve", "dock", "parts", "broken",
    "faulty", "for parts", "screen", "keyboard", "battery only",
]

# FIX M1: retry config
MAX_RETRIES = 3
RETRY_BACKOFF_S = 2.0


def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Collect Gumtree AU laptop listings into canonical CSV."
    )
    parser.add_argument("--query", required=True, help="Search query string")
    parser.add_argument("--output", required=True, help="Output CSV path")
    parser.add_argument("--max-pages", type=int, default=3, help="Max pages to fetch (default: 3)")
    parser.add_argument("--base-url", default="https://www.gumtree.com.au", help="Base Gumtree URL")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Write raw HTML of page 1 to gumtree_debug_page1.html for selector verification",
    )
    return parser.parse_args()


def parse_price(text: str) -> float | str:
    if not text:
        return ""
    cleaned = text.replace("$", "").replace("AUD", "").replace(",", "")
    m = re.search(r"(\d[\d.]*)", cleaned)
    return float(m.group(1)) if m else ""


# FIX C6: most-specific strings checked BEFORE their substrings ("like new" before "new")
def infer_condition(text: str) -> str:
    s = (text or "").lower()
    if "like new" in s:
        return "like_new"
    if "very good" in s or "excellent" in s:
        return "very_good"
    if "new" in s:
        return "new"
    if "good" in s or "used" in s:
        return "used"
    if "fair" in s:
        return "fair"
    return "unknown"


def extract_listing_date(text: str) -> str:
    """FIX H4: extract relative timestamp from listing text if present."""
    s = (text or "").lower()
    # Gumtree shows e.g. "3 days ago", "2 hours ago", "just now"
    m = re.search(r"(\d+\s+(?:minute|hour|day|week|month)s?\s+ago|just\s+now)", s)
    return m.group(0).strip() if m else ""


# FIX M4: battery logic extracted into standalone function (mirrors battery_utils.py pattern)
def extract_battery_fields(text: str) -> dict:
    s = (text or "").lower()
    result = {
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


def valid_laptop(title: str) -> bool:
    s = (title or "").lower()
    if not any(k in s for k in LAPTOP_INCLUDE):
        return False
    if any(k in s for k in LAPTOP_EXCLUDE):
        return False
    return True


def listing_id_from_url(url: str) -> str:
    m = re.search(r"/v-[^/]+/(\d+)", url)
    return m.group(1) if m else re.sub(r"[^a-zA-Z0-9]+", "-", url).strip("-")[-64:]


def parse_cards(html: str, base_url: str, debug: bool = False) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")

    # FIX C2: expanded, resilient selector set covering old and new Gumtree DOM patterns
    selectors = "a[href*='/s-ad/'], a[href*='/v-'], article a[href], .listing-link"
    candidates = soup.select(selectors)

    if debug:
        print(f"[debug] Total <a> candidates matched by selectors: {len(candidates)}")

    cards = []
    for a in candidates:
        title = a.get_text(" ", strip=True)
        href = a.get("href", "").strip()
        if not href or not title or not valid_laptop(title):
            continue

        url = href if href.startswith("http") else f"{base_url}{href}"
        container = a.find_parent(["article", "li", "div"]) or a
        text_blob = container.get_text(" ", strip=True)

        price = parse_price(text_blob)
        condition = infer_condition(text_blob)
        battery = extract_battery_fields(text_blob)
        listing_date = extract_listing_date(text_blob)

        # FIX H1: seller_risk_score populated (3 = private/no-feedback-system tier)
        seller_class = "private"
        if "dealer" in text_blob.lower() or "store" in text_blob.lower():
            seller_class = "commercial_seller"

        risk_flags = ["NO_FEEDBACK_SYSTEM"]
        if seller_class == "private":
            risk_flags.append("PRIVATE_SELLER")
        risk_flags.append("NO_RETURNS")
        risk_flags.append("NO_WARRANTY")
        if battery["battery_disclosure_level"] == "none":
            risk_flags.append("BATTERY_UNDISCLOSED")

        cards.append({
            "vendor_item_id": listing_id_from_url(url),
            "product_name": title,
            "product_url": url,
            "source_label": "gumtree_http",
            "source_platform": "GUMTREE_AU",       # FIX H1
            "source_tier": 3,
            "seller_risk_score": 3,                 # FIX H1
            "list_price_aud": price,
            "currency": "AUD",
            "condition": condition,
            "seller_name": "",
            "seller_class": seller_class,
            "seller_feedback_count": "",
            "seller_feedback_pct": "",
            "shipping_cost_aud": "",
            "listing_country": "AU",
            "listing_date": listing_date,           # FIX H4
            "listing_status": "active",             # FIX H4 — live page = active
            "returns_accepted": False,
            "warranty_months": 0,
            "battery_disclosure_level": battery["battery_disclosure_level"],
            "battery_health_pct": battery["battery_health_pct"],
            "battery_cycle_count": battery["battery_cycle_count"],
            "battery_replaced": battery["battery_replaced"],
            "risk_flags": ",".join(risk_flags),
            "price_collected_at": dt.datetime.now().isoformat(timespec="seconds"),
            "location_suburb": "",
            "description_snippet": text_blob[:200],
        })

    deduped = {}
    for row in cards:
        deduped[row["vendor_item_id"]] = row
    return list(deduped.values())


# FIX M1: retry wrapper with exponential backoff
def get_with_retry(session: requests.Session, url: str, timeout: int = 30) -> requests.Response:
    last_exc: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = session.get(url, timeout=timeout)
            r.raise_for_status()
            return r
        except requests.RequestException as exc:
            last_exc = exc
            if attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF_S * attempt
                print(f"[warn] Attempt {attempt}/{MAX_RETRIES} failed ({exc}). Retrying in {wait:.0f}s…")
                time.sleep(wait)
            else:
                print(f"[error] All {MAX_RETRIES} attempts failed for {url}: {exc}")
    raise last_exc  # type: ignore[misc]


def main() -> None:
    args = parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update(HEADERS)

    all_rows: dict[str, dict] = {}
    q = quote_plus(args.query)

    for page in range(1, args.max_pages + 1):
        # FIX C1: correct Gumtree AU search param is `q=`, not `searchfield=`
        url = f"{args.base_url}/s-laptops/c18320?sort=rank&q={q}&pageNum={page}"
        print(f"[info] Fetching page {page}: {url}")

        r = get_with_retry(session, url)

        # FIX C2: debug dump for DOM/selector verification
        if args.debug and page == 1:
            debug_path = Path("gumtree_debug_page1.html")
            debug_path.write_text(r.text, encoding="utf-8")
            print(f"[debug] Raw HTML written to {debug_path} — inspect to verify selectors")

        page_rows = parse_cards(r.text, args.base_url, debug=args.debug)
        print(f"[info] Page {page}: {len(page_rows)} valid laptop listings parsed")

        if not page_rows:
            print(f"[info] No listings on page {page}, stopping early.")
            break

        for row in page_rows:
            all_rows[row["vendor_item_id"]] = row

        # Polite crawl delay
        if page < args.max_pages:
            time.sleep(1.5)

    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for row in all_rows.values():
            writer.writerow(row)

    print(f"[done] gumtree rows written: {len(all_rows)}")
    print(f"[done] output: {output}")


if __name__ == "__main__":
    main()
