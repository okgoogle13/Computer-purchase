#!/usr/bin/env python3
import csv
from pathlib import Path

old_live_path = Path("shortlists/2026-06-07_shortlist_pricing_enriched_live.csv")
new_scaffold_path = Path("shortlists/2026-06-07_shortlist_pricing_enriched.csv")
output_path = Path("shortlists/2026-06-07_shortlist_pricing_enriched.csv")

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

ID_MAP = {
    "hp-zbook-ultra-14-g1a-mobile-workstation-ryzen-ai-max-385-32gb-unified": "hp-zbook-ultra-14-g1a-32gb-triforce",
    "asus-proart-gopro-edition-px13-hn7306eac-lx044w-strix-halo": "HN6306_proart_px13",
    "msi-raider-18hx-ai-a2xwig-refurbished": "rfb-msi-raider-18hx-ai-a2xwig",
    "msi-titan-18-hx-a14vig-refurbished": "rfb-msi-titan-18hx-a14vig",
    "msi-vector-a18-hx-a9wig-refurbished": "rfb-msi-vector-a18hx-a9wig",
    "msi-vector-gp78-hx-14v": "49_msi-vector-gp78-hx-14v",
    "lenovo-legion-9i-gen-10-18-rtx-5080-ebay": "36_lenovo-legion-9i-18-rtx-5080-ebay",
    "lenovo-legion-pro-7i-demo": "demo-lenovo-legion-pro-7i-rtx5090",
}

# 1. Read old pricing data
old_data = {}
if old_live_path.exists():
    with open(old_live_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            r_id = row.get("intake_id") or row.get("id") or ""
            if r_id:
                old_data[r_id] = {col: row.get(col, "") for col in PRICING_COLUMNS}
    print(f"Loaded old pricing for {len(old_data)} candidates.")
else:
    print("Old pricing file not found.")

# 2. Read new scaffold and merge
merged_rows = []
with open(new_scaffold_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    
    # Ensure all pricing columns are in fieldnames
    for col in PRICING_COLUMNS:
        if col not in fieldnames:
            fieldnames.append(col)
            
    for row in reader:
        # Initialize fields to empty if not there
        for col in PRICING_COLUMNS:
            if col not in row:
                row[col] = ""
                
        r_id = row.get("intake_id") or row.get("id") or ""
        old_id = ID_MAP.get(r_id, r_id)
        if old_id in old_data:
            # Copy all pricing columns
            for col in PRICING_COLUMNS:
                # Only overwrite if old data actually has a value
                val = old_data[old_id].get(col, "").strip()
                if val and val.upper() != "UNKNOWN":
                    row[col] = val
        merged_rows.append(row)

# 3. Write output
with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(merged_rows)

print(f"Successfully merged old pricing into new scaffold at {output_path}!")
print(f"Total rows: {len(merged_rows)}")
