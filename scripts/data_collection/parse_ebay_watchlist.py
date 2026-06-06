#!/usr/bin/env python3
"""
parse_ebay_watchlist.py

Parses the raw eBay watchlist HTML collected by scrape_ebay_watchlist.py
and extracts candidate records (URL, title, listing ID, price, seller).

Usage:
    python scripts/data_collection/parse_ebay_watchlist.py [--html path/to/watchlist.html]
"""

import re
import sys
import json
import csv
from pathlib import Path
from html.parser import HTMLParser
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parents[2]

class EbayHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_anchor = False
        self.current_href = None
        self.current_text = []
        self.links = [] # List of dict: {href, text}
        self.all_text_tokens = [] # Flat list of all text tokens for price heuristics
        
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            attrs_dict = dict(attrs)
            href = attrs_dict.get("href", "")
            # Look for eBay item link pattern
            if "/itm/" in href or "ebay.com.au/itm/" in href:
                self.in_anchor = True
                self.current_href = href
                self.current_text = []

    def handle_data(self, data):
        clean_data = data.strip()
        if clean_data:
            self.all_text_tokens.append(clean_data)
        if self.in_anchor:
            self.current_text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.in_anchor:
            self.in_anchor = False
            title = " ".join(self.current_text).strip()
            # Clean up title whitespace
            title = re.sub(r'\s+', ' ', title)
            if title and self.current_href:
                self.links.append({
                    "url": self.current_href,
                    "title": title
                })

def extract_listing_id(url: str) -> str:
    # Match 12-digit listing ID in eBay URL
    match = re.search(r'/itm/(?:[^/]+/)?(\d{12})', url)
    if match:
        return match.group(1)
    return "UNKNOWN"

def clean_url(url: str) -> str:
    # Strip tracking parameters from eBay URL
    match = re.search(r'(https://www\.ebay\.com\.au/itm/\d{12})', url)
    if match:
        return match.group(1)
    return url

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Parse eBay watchlist HTML.")
    parser.add_argument("--html", type=str, default=None, help="Path to raw HTML file")
    args = parser.parse_args()

    # Find the latest HTML file if not specified
    html_path = None
    if args.html:
        html_path = Path(args.html)
    else:
        watchlist_dir = REPO_ROOT / "data" / "raw" / "ebay_watchlist"
        if watchlist_dir.exists():
            html_files = sorted(watchlist_dir.glob("watchlist_*.html"))
            if html_files:
                html_path = html_files[-1]
                
    if not html_path or not html_path.exists():
        print("Error: No watchlist HTML file found. Run scrape_ebay_watchlist.py first.", file=sys.stderr)
        sys.exit(1)

    print(f"Parsing eBay watchlist HTML: {html_path}")
    html_content = html_path.read_text(encoding="utf-8", errors="replace")
    
    parser = EbayHTMLParser()
    parser.feed(html_content)
    
    # Pre-parse listing prices from HTML using regex
    parsed_prices = {}
    for match in re.finditer(r'\"listingId\":\"(\d+)\".*?\"displayPrice\":.*?\"value\":([0-9.]+)', html_content):
        list_id, price_val = match.groups()
        val_float = float(price_val)
        if list_id in parsed_prices:
            parsed_prices[list_id] = min(parsed_prices[list_id], val_float)
        else:
            parsed_prices[list_id] = val_float

    # Process extracted links to deduplicate by listing ID
    candidates = {}
    for link in parser.links:
        url = link["url"]
        title = link["title"]
        
        # Skip generic links that happen to contain /itm/ but aren't items
        if len(title) < 10 or "feedback" in title.lower() or "shipping" in title.lower():
            continue
            
        listing_id = extract_listing_id(url)
        if listing_id != "UNKNOWN" and listing_id not in candidates:
            cleaned_url = clean_url(url)
            
            # Use pre-parsed price if available
            price = "UNKNOWN"
            if listing_id in parsed_prices:
                price = f"{parsed_prices[listing_id]:.2f}"
            
            candidates[listing_id] = {
                "listing_id": listing_id,
                "title": title,
                "url": cleaned_url,
                "price_raw": price,
                "retailer": "eBay AU",
                "condition": "Used/Refurbished"
            }

    print(f"Extracted {len(candidates)} unique candidates from watchlist.")
    
    # Output parsed results to JSON and CSV
    today = datetime.today().strftime("%Y-%m-%d")
    out_dir = REPO_ROOT / "data" / "processed"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    json_out = out_dir / f"parsed_watchlist_{today}.json"
    json_out.write_text(json.dumps(list(candidates.values()), indent=2), encoding="utf-8")
    print(f"Saved parsed watchlist JSON to {json_out}")
    
    csv_out = out_dir / f"parsed_watchlist_{today}.csv"
    with csv_out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["listing_id", "title", "url", "price_raw", "retailer", "condition"])
        writer.writeheader()
        writer.writerows(candidates.values())
    print(f"Saved parsed watchlist CSV to {csv_out}")

if __name__ == "__main__":
    main()
