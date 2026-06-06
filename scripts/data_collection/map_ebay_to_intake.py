#!/usr/bin/env python3
"""
map_ebay_to_intake.py

Converts enriched eBay watchlist CSV data into the canonical intake schema.
Calculates Category, Track, and Pathway settings based on the specs.

Usage:
    python scripts/data_collection/map_ebay_to_intake.py
"""

import csv
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parents[2]

CANONICAL_HEADER = [
    "date_found", "source_batch", "track", "pathway", "category",
    "item_name", "price_aud", "gpu_model", "vram_gb", "unified_memory_gb",
    "ram_gb", "cpu_model", "condition", "retailer", "url",
    "au_stock_confirmed", "verification_status", "status", "notes",
    "seller_class", "source_platform", "screen_size_in",
    "vendor_item_id", "seller_risk_score", "battery_disclosure_level",
    "battery_health_pct", "battery_cycle_count", "battery_replaced",
    "risk_flags"
]

def classify_hardware(row: dict) -> tuple[str, str, str]:
    """Returns (category, track, pathway)."""
    title = row["title"].lower()
    gpu = row["gpu_model"].lower()
    cpu = row["cpu_model"].lower()
    
    # 1. Category Classification
    if any(x in title or x in gpu for x in ["desktop", "tower", "pc", "aurora", "thinkstation", "7920", "gaming pc"]):
        category = "Desktop"
    else:
        category = "Laptop"
        
    # 2. Track & Pathway Classification
    track = "1"
    pathway = "1A" # Default to laptop path 1A
    
    if category == "Desktop":
        if "7920" in title or "p620" in title or "threadripper" in title:
            # High-end workstations
            track = "2"
            pathway = "B"
        else:
            # Single GPU refurbished gaming PC
            track = "1.5"
            pathway = "UNKNOWN"
    else:
        # Laptops
        if "strix halo" in title or "ryzen ai max" in title or "ryzen ai max+" in title:
            track = "1"
            pathway = "1B"
        else:
            track = "1"
            pathway = "1A"
            
    return category, track, pathway

def main():
    today = datetime.today().strftime("%Y-%m-%d")
    input_path = REPO_ROOT / "data" / "processed" / f"enriched_watchlist_{today}.csv"
    output_path = REPO_ROOT / "data" / "processed" / f"ebay_watchlist_{today}_processed.csv"
    
    if not input_path.exists():
        print(f"Error: Input file {input_path} does not exist.")
        return
        
    print(f"Reading enriched candidates from: {input_path}")
    candidates = []
    with input_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip invalid rows or rows with empty details
            if not row["title"] or row["price_aud"] == "UNKNOWN":
                continue
            candidates.append(row)
            
    print(f"Loaded {len(candidates)} valid enriched candidates.")
    
    mapped_rows = []
    for row in candidates:
        category, track, pathway = classify_hardware(row)
        
        # Build canonical dict
        canon = {
            "date_found": today,
            "source_batch": f"ebay_watchlist_{today}",
            "track": track,
            "pathway": pathway,
            "category": category,
            "item_name": row["title"],
            "price_aud": row["price_aud"],
            "gpu_model": row["gpu_model"],
            "vram_gb": row["vram_gb"],
            "unified_memory_gb": "UNKNOWN",
            "ram_gb": row["ram_gb"],
            "cpu_model": row["cpu_model"],
            "condition": "Used" if "used" in row["condition"].lower() else "Refurbished",
            "retailer": "eBay AU",
            "url": row["url"],
            "au_stock_confirmed": "Yes",
            "verification_status": "Verified",
            "status": "Active",
            "notes": f"Scraped from eBay Watchlist. Listing ID: {row['listing_id']}. Storage: {row.get('storage', 'UNKNOWN')}",
            "seller_class": "EBAY_AU",
            "source_platform": "EBAY_AU",
            "screen_size_in": row.get("screen_size_in", "UNKNOWN"),
            "vendor_item_id": row["listing_id"],
            "seller_risk_score": "UNKNOWN",
            "battery_disclosure_level": "UNKNOWN",
            "battery_health_pct": "UNKNOWN",
            "battery_cycle_count": "UNKNOWN",
            "battery_replaced": "UNKNOWN",
            "risk_flags": "UNKNOWN"
        }
        mapped_rows.append(canon)
        
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CANONICAL_HEADER)
        writer.writeheader()
        writer.writerows(mapped_rows)
        
    print(f"Successfully wrote {len(mapped_rows)} mapped rows to: {output_path}")

if __name__ == "__main__":
    main()
