#!/usr/bin/env python3
import csv
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def main():
    today = "2026-06-07"
    
    # 1. Define candidates data from the user request
    candidates = [
        {
            "listing_id": "137317465327",
            "title": "GIGABYTE AORUS 17.4\" YE5- 17.3\" RTX 3080ti 300Hz, Intel i7 12th gen 14c 20t 32gb",
            "url": "https://www.ebay.com.au/itm/137317465327",
            "price_raw": "1450.00",
            "price_aud": "1481.57", # price + shipping
            "retailer": "eBay AU",
            "condition": "Used",
            "cpu_model": "i7 12th gen",
            "gpu_model": "RTX 3080 Ti Laptop GPU",
            "ram_gb": "32",
            "vram_gb": "16",
            "screen_size_in": "17.3",
            "storage": "UNKNOWN"
        },
        {
            "listing_id": "366238793776",
            "title": "Razer Blade 18\" QHD+ 240Hz i9-13950HX RTX4090 2TB 32GB W11H Gaming Laptop",
            "url": "https://www.ebay.com.au/itm/366238793776",
            "price_raw": "4739.00",
            "price_aud": "4139.00", # effective price after discounts
            "retailer": "Razer AU",
            "condition": "New",
            "cpu_model": "i9-13950HX",
            "gpu_model": "RTX 4090 Laptop GPU",
            "ram_gb": "32",
            "vram_gb": "16",
            "screen_size_in": "18.0",
            "storage": "2TB"
        },
        {
            "listing_id": "157942587348",
            "title": "(A+)Asus ROG Strix SCAR 17 SE 17.3\" i7-12950HX 32G 2TB SSD RTX3080Ti FHD 360Hz",
            "url": "https://www.ebay.com.au/itm/157942587348",
            "price_raw": "2499.00",
            "price_aud": "2517.00", # price + shipping
            "retailer": "eBay AU",
            "condition": "Used",
            "cpu_model": "i7-12950HX",
            "gpu_model": "RTX 3080 Ti Laptop GPU",
            "ram_gb": "32",
            "vram_gb": "16",
            "screen_size_in": "17.3",
            "storage": "2TB SSD"
        },
        {
            "listing_id": "168263146829",
            "title": "Lenovo Legion 9i 18\" WQUXGA Intel Ultra 9 240Hz 2TB 64GB RTX5080 Gaming Laptop",
            "url": "https://www.ebay.com.au/itm/168263146829",
            "price_raw": "4755.75",
            "price_aud": "4755.75",
            "retailer": "eBay AU",
            "condition": "Open Box",
            "cpu_model": "Intel Ultra 9",
            "gpu_model": "RTX 5080 Laptop GPU",
            "ram_gb": "64",
            "vram_gb": "16",
            "screen_size_in": "18.0",
            "storage": "2TB"
        },
        {
            "listing_id": "116762331758",
            "title": "Razer Blade Pro 17 17.3\" Intel Core i7-10875H Gaming Laptop",
            "url": "https://www.ebay.com.au/itm/116762331758",
            "price_raw": "2299.00",
            "price_aud": "2334.00", # price + shipping
            "retailer": "eBay AU",
            "condition": "Open Box",
            "cpu_model": "i7-10875H",
            "gpu_model": "UNKNOWN",
            "ram_gb": "UNKNOWN",
            "vram_gb": "UNKNOWN",
            "screen_size_in": "17.3",
            "storage": "UNKNOWN"
        },
        {
            "listing_id": "358603401448",
            "title": "Asus Rog Strix 17 RTX 4090 laptop QHD 240Hz display 64Gb ram DDR5",
            "url": "https://www.ebay.com.au/itm/358603401448",
            "price_raw": "3600.00",
            "price_aud": "3626.80", # price + shipping
            "retailer": "eBay AU",
            "condition": "Used",
            "cpu_model": "UNKNOWN",
            "gpu_model": "RTX 4090 Laptop GPU",
            "ram_gb": "64",
            "vram_gb": "16",
            "screen_size_in": "17.0",
            "storage": "UNKNOWN"
        }
    ]
    
    # 2. Write to enriched_watchlist_2026-06-07.csv
    enriched_csv = REPO_ROOT / "data" / "processed" / f"enriched_watchlist_{today}.csv"
    enriched_csv.parent.mkdir(parents=True, exist_ok=True)
    
    fieldnames = ["listing_id", "title", "url", "price_raw", "price_aud", "retailer", "condition", 
                  "cpu_model", "gpu_model", "ram_gb", "vram_gb", "screen_size_in", "storage"]
                  
    with open(enriched_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(candidates)
        
    print(f"Wrote enriched candidates to: {enriched_csv}")

    # 3. Run map_ebay_to_intake.py
    print("Running map_ebay_to_intake.py...")
    subprocess.run(["python", "scripts/data_collection/map_ebay_to_intake.py"], cwd=REPO_ROOT, check=True)
    
    # 4. Run intake_to_cards.py
    processed_csv = REPO_ROOT / "data" / "processed" / f"ebay_watchlist_{today}_processed.csv"
    print(f"Running intake_to_cards.py on {processed_csv}...")
    subprocess.run([
        "python", "scripts/intake_to_cards.py", str(processed_csv), "--overwrite", "--prefix", "intake"
    ], cwd=REPO_ROOT, check=True)
    
    print("Ingestion and initial card generation completed successfully!")

if __name__ == "__main__":
    main()
