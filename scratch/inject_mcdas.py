import csv

input_path = "shortlists/2026-06-07_shortlist_pricing_enriched_live.csv"
output_path = "shortlists/2026-06-07_shortlist_pricing_enriched_live.csv"

rows = []
with open(input_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    if "Upgrade_Ceiling" not in fieldnames:
        fieldnames.append("Upgrade_Ceiling")
    
    for row in reader:
        item_id = row.get("intake_id", "") or row.get("id", "")
        # Add a dummy Upgrade_Ceiling if missing
        if not row.get("Upgrade_Ceiling"):
            row["Upgrade_Ceiling"] = "7"
        rows.append(row)

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Upgrade_Ceiling injected successfully.")
