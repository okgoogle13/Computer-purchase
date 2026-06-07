#!/usr/bin/env python3
import csv
from pathlib import Path

# Paths
live_csv_path = Path("shortlists/2026-06-07_shortlist_pricing_enriched_live.csv")
mcda_csv_path = Path("shortlists/2026-06-07_shortlist_mcda_filled.csv")

# Load MCDA scores mapping (intake_id -> scores)
mcda_scores = {}
with open(mcda_csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        r_id = row.get("intake_id") or row.get("id") or ""
        if r_id:
            mcda_scores[r_id] = {
                "Performance_Headroom": row.get("Performance_Headroom"),
                "Price_Value": row.get("Price_Value"),
                "Future_Proof": row.get("Future_Proof"),
                "Portability": row.get("Portability"),
                "Track2_Avoidance": row.get("Track2_Avoidance"),
                "Upgrade_Ceiling": row.get("Upgrade_Ceiling") or "0",  # default to 0 if empty
            }

# Verified active laptop candidates data
verified_deals = {
    "hp-zbook-ultra-14-g1a-32gb-triforce": {
        "current_best_price_aud": "2999.00",
        "effective_best_price_aud": "2999.00",
        "current_best_retailer": "hub by Triforce",
        "current_best_url": "https://hub.triforce.com.au/product/hp-zbook-ultra-g1a-mobile-workstation/",
        "in_stock_now": "yes",
        "au_stock": "Yes",
        "seller_class": "MAJOR_RETAILER_AU",
        "source_platform": "MAJOR_RETAILER_AU",
        "warranty_months_confirmed": "12",
        "acl_covered": "yes",
        "pricing_checked_at": "2026-06-07"
    },
    "HN6306_proart_px13": {
        "current_best_price_aud": "4799.00",
        "effective_best_price_aud": "4799.00",
        "current_best_retailer": "PLE Computers",
        "current_best_url": "https://www.ple.com.au/Products/662057/ASUS-ProArt-PX13-133-Touchscreen-Creator-Laptop",
        "in_stock_now": "yes",
        "au_stock": "Yes",
        "seller_class": "MAJOR_RETAILER_AU",
        "source_platform": "MAJOR_RETAILER_AU",
        "warranty_months_confirmed": "12",
        "acl_covered": "yes",
        "pricing_checked_at": "2026-06-07"
    },
    "intake-080": {
        "current_best_price_aud": "3999.00",
        "effective_best_price_aud": "3999.00",
        "current_best_retailer": "HP Australia",
        "current_best_url": "https://www.hp.com/au-en/shop/omen-max-laptop-16-ah0013tx.html",
        "in_stock_now": "yes",
        "au_stock": "Yes",
        "seller_class": "MANUFACTURER_AU",
        "source_platform": "MANUFACTURER_AU",
        "warranty_months_confirmed": "24",
        "acl_covered": "yes",
        "pricing_checked_at": "2026-06-07"
    }
}

# Known expired deals
expired_deals = {
    "rfb-msi-vector-a18hx-a9wig",
    "49_msi-vector-gp78-hx-14v",
    "052_alienware-m18-r2-rtx-4080-ebay-mkt-011",
    "053_alienware-m18-r2-rtx-4080-ebay-mkt-012",
    "054_alienware-m18-r2-rtx-4090-ebay-mkt-013",
    "055_alienware-m18-r2-rtx-4090-ebay-mkt-014",
    "056_alienware-area-51-18-rtx-5070-ti-ebay-mkt-015",
    "057_alienware-area-51-18-rtx-5070-ti-ebay-mkt-016",
    "36_lenovo-legion-9i-18-rtx-5080-ebay",
    "intake-075",
    "intake-079",
    "rfb-msi-titan-18hx-a14vig",
}

# Read live CSV rows and update
updated_rows = []
with open(live_csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    
    # Ensure Upgrade_Ceiling is in fieldnames
    if "Upgrade_Ceiling" not in fieldnames:
        fieldnames.append("Upgrade_Ceiling")
        
    for row in reader:
        r_id = row.get("intake_id") or row.get("id") or ""
        
        # 1. Merge manual MCDA scores if available
        if r_id in mcda_scores:
            for k, v in mcda_scores[r_id].items():
                row[k] = v
        
        # 2. Populate verified deals
        if r_id in verified_deals:
            for k, v in verified_deals[r_id].items():
                row[k] = v
            row["status"] = "GOOD_ENOUGH"
            row["au_stock"] = "Yes"
            row["in_stock_now"] = "yes"
            
        # 3. Mark expired deals as out of stock
        elif r_id in expired_deals or (row.get("category") == "laptop" and r_id not in verified_deals):
            row["in_stock_now"] = "no"
            row["au_stock"] = "No"
            row["status"] = "NEEDS_REVIEW"
            
        updated_rows.append(row)

# Write back to live CSV
with open(live_csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)

print(f"Successfully merged MCDA scores and updated verified/expired deals in {live_csv_path}!")
