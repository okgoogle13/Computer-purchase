#!/usr/bin/env python3
"""
map_facebook_to_intake.py

Converts raw Facebook Marketplace parsed CSV data into the canonical intake schema.
Uses regex heuristics to extract specs (GPU, VRAM, RAM, CPU) from listing titles and descriptions.
Calculates Category, Track, and Pathway settings based on the extracted specs.

Usage:
    python scripts/data_collection/map_facebook_to_intake.py
"""

import csv
import re
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

def extract_specs(title: str, desc: str) -> dict:
    """Extract GPU, VRAM, RAM, CPU, and Screen Size from title and description using heuristics."""
    text = f"{title} | {desc}".lower()
    
    # 1. GPU Extraction
    gpu_model = "UNKNOWN"
    vram_gb = "UNKNOWN"
    
    # Check for Workstation GPUs
    workstation_match = re.search(r'\b(rtx\s*[a\d]{4,5}\b|a5000|a4000|a2000|quadro\s*[\w\d]+|radeon\s*pro\s*w\d+)', text)
    if workstation_match:
        gpu_model = workstation_match.group(1).upper()
        if "A5000" in gpu_model:
            vram_gb = "16"
        elif "A4000" in gpu_model:
            vram_gb = "16"
        elif "A2000" in gpu_model:
            vram_gb = "6" if "12gb" not in text else "12"
            
    # Check for Consumer GPUs
    else:
        consumer_match = re.search(r'\b(rtx\s*[345]0\d{2}\s*t?i?|geforce\s*rtx\s*[345]0\d{2}\s*t?i?|gtx\s*\d{3,4}\s*t?i?|rx\s*\d{4}\s*x?t?|radeon\s*rx\s*\d{4}\s*x?t?)\b', text)
        if consumer_match:
            gpu_model = consumer_match.group(1).upper().replace("GEFORCE ", "")
            # Deduce VRAM defaults for laptop/desktop consumer cards if not explicitly in text
            if "5080" in gpu_model:
                vram_gb = "16"
            elif "5070" in gpu_model:
                vram_gb = "12"
            elif "4090" in gpu_model:
                vram_gb = "16"
            elif "4080" in gpu_model:
                vram_gb = "12"
            elif "4070" in gpu_model:
                vram_gb = "8"
            elif "4060" in gpu_model:
                vram_gb = "8"
            elif "3080" in gpu_model:
                vram_gb = "16" if "16gb" in text or "16g" in text else "8"
            elif "3070" in gpu_model:
                vram_gb = "8"
            elif "3060" in gpu_model:
                vram_gb = "6"
            elif "6850" in gpu_model:
                vram_gb = "12"
            elif "6800" in gpu_model:
                vram_gb = "16" if "16gb" in text or "16g" in text else "8"
    
    # Override VRAM if explicitly mentioned (e.g. "12gb vram", "16gb graphics")
    vram_explicit = re.search(r'(\d+)\s*(?:gb|g)\s*(?:vram|graphics|dedicated|gpu\s*ram)', text)
    if vram_explicit:
        vram_gb = vram_explicit.group(1)

    # 2. RAM Extraction
    ram_gb = "UNKNOWN"
    ram_match = re.search(r'\b(\d+)\s*(?:gb|g)\s*(?:ram|system\s*memory|ddr[45])\b', text)
    if ram_match:
        ram_gb = ram_match.group(1)
    else:
        # Fallback: look for generic "32gb" or "64gb" or "16gb" in title
        title_ram = re.search(r'\b(16|32|64)\s*(?:gb|g)\b', title.lower())
        if title_ram:
            ram_gb = title_ram.group(1)
            
    # 3. CPU Extraction
    cpu_model = "UNKNOWN"
    cpu_match = re.search(r'\b(i[579]-\d{4,5}\w*|ryzen\s*[579]\s*\d{4}\w*|ryzen\s*ai\s*\d+\s*\w*|hx\s*\d{3})\b', text)
    if cpu_match:
        cpu_model = cpu_match.group(1).upper()
        
    # 4. Screen Size Extraction
    screen_size = "UNKNOWN"
    screen_match = re.search(r'\b(13|14|15|16|17|18)(?:\.(\d))?\s*(?:inch|in|\"|\-inch)\b', text)
    if screen_match:
        val = screen_match.group(1)
        dec = screen_match.group(2)
        screen_size = f"{val}.{dec}" if dec else val

    return {
        "gpu_model": gpu_model,
        "vram_gb": vram_gb,
        "ram_gb": ram_gb,
        "cpu_model": cpu_model,
        "screen_size_in": screen_size
    }

def classify_hardware(title: str, gpu_model: str) -> tuple[str, str, str]:
    """Returns (category, track, pathway) based on mapped fields."""
    title_lower = title.lower()
    gpu_lower = gpu_model.lower()
    
    # 1. Category
    if any(x in title_lower or x in gpu_lower for x in ["desktop", "tower", "pc", "aurora", "gaming pc", "custom build"]):
        category = "Desktop"
    elif any(x in title_lower for x in ["gpu", "graphics card", "rtx", "rx"]) and not any(x in title_lower for x in ["laptop", "notebook"]):
        # Might be a component if title is just the card
        if any(x in title_lower for x in ["laptop", "notebook", "book", "zephyrus", "legion", "strix", "omen", "katana"]):
            category = "Laptop"
        else:
            category = "Component"
    else:
        category = "Laptop"
        
    # 2. Track & Pathway
    track = "1"
    pathway = "1A"
    
    if category == "Desktop":
        track = "1.5"
        pathway = "UNKNOWN"
    elif category == "Component":
        track = "2"
        pathway = "A"
    else:
        # Laptops
        if "strix halo" in title_lower or "ryzen ai max" in title_lower or "ryzen ai max+" in title_lower:
            track = "1"
            pathway = "1B"
        else:
            track = "1"
            pathway = "1A"
            
    return category, track, pathway

def main():
    today = datetime.today().strftime("%Y-%m-%d")
    input_path = REPO_ROOT / "data" / "processed" / f"facebook_marketplace_{today}.csv"
    output_path = REPO_ROOT / "data" / "processed" / f"facebook_marketplace_{today}_processed.csv"
    
    if not input_path.exists():
        print(f"Error: Input file {input_path} does not exist.")
        return
        
    print(f"Reading raw Facebook listings from: {input_path}")
    listings = []
    with input_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            listings.append(row)
            
    print(f"Loaded {len(listings)} raw listings.")
    
    mapped_rows = []
    for row in listings:
        title = row["product_name"]
        desc = row["description_snippet"]
        
        # Skip items with no title or price
        if not title or not row["list_price_aud"]:
            continue
            
        specs = extract_specs(title, desc)
        category, track, pathway = classify_hardware(title, specs["gpu_model"])
        
        # Build canonical dict
        canon = {
            "date_found": today,
            "source_batch": f"facebook_marketplace_{today}",
            "track": track,
            "pathway": pathway,
            "category": category,
            "item_name": title,
            "price_aud": row["list_price_aud"],
            "gpu_model": specs["gpu_model"],
            "vram_gb": specs["vram_gb"],
            "unified_memory_gb": "UNKNOWN" if track != "1" or pathway != "1B" else specs["ram_gb"],
            "ram_gb": specs["ram_gb"],
            "cpu_model": specs["cpu_model"],
            "condition": row["condition"].title() if row["condition"] != "unknown" else "Used",
            "retailer": row["seller_name"] if row["seller_name"] else "Facebook Private Seller",
            "url": row["product_url"],
            "au_stock_confirmed": "Yes", # Local pickup in Melb
            "verification_status": "Unverified", # Private market requires manual checks
            "status": "Active",
            "notes": f"Scraped from Facebook Marketplace Melb. Suburb: {row['location_suburb']}. Description: {desc}",
            "seller_class": "private",
            "source_platform": "FB_MARKETPLACE",
            "screen_size_in": specs["screen_size_in"],
            "vendor_item_id": row["vendor_item_id"],
            "seller_risk_score": "3",
            "battery_disclosure_level": row["battery_disclosure_level"],
            "battery_health_pct": row["battery_health_pct"],
            "battery_cycle_count": row["battery_cycle_count"],
            "battery_replaced": row["battery_replaced"],
            "risk_flags": row["risk_flags"]
        }
        mapped_rows.append(canon)
        
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CANONICAL_HEADER)
        writer.writeheader()
        writer.writerows(mapped_rows)
        
    print(f"Successfully wrote {len(mapped_rows)} mapped rows to: {output_path}")

if __name__ == "__main__":
    main()
