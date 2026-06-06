import csv

input_path = "shortlists/2026-06-07_shortlist_pricing_enriched.csv"
output_path = "shortlists/2026-06-07_shortlist_pricing_enriched_live.csv"

rows = []
with open(input_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    if "current_best_price_aud" not in fieldnames:
        fieldnames += ["current_best_price_aud", "current_best_retailer", "in_stock_now"]
    for row in reader:
        item_id = row.get("intake_id", "") or row.get("id", "")
        if "intake-066" in item_id:
            row["current_best_price_aud"] = "2399.0"
            row["current_best_retailer"] = "Recompute"
            row["in_stock_now"] = "Unknown"  # As seen in manual lookup
        elif "42_asus-rog-strix-g16" in item_id:
            row["current_best_price_aud"] = "4599.0"
            row["current_best_retailer"] = "ASUS AU Store / Mwave"
            row["in_stock_now"] = "Yes"
        rows.append(row)

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Prices injected successfully.")
