#!/usr/bin/env python3
import csv
from pathlib import Path

csv_path = Path("shortlists/2026-06-07_shortlist_pricing_enriched_live.csv")
if not csv_path.exists():
    print("CSV file not found!")
    exit(1)

with open(csv_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

mappings = {
    "RTX 5070": 12.0,
    "RTX 4080": 12.0,
    "RTX 3070": 8.0,
    "RTX 3050": 4.0,
    "RTX 3060": 6.0,
    "RTX 4070": 8.0,
    "RTX 4060": 8.0,
    "RTX 5060": 8.0,
}

updated_count = 0
for row in rows:
    if row.get("vram_gb") == "UNKNOWN" or not row.get("vram_gb"):
        gpu = row.get("gpu_model", "").upper()
        item_name = row.get("item_name", "").upper()
        
        # Special case: intake-106 name mentions RTX3080 16GB
        if "RTX3080" in gpu or "RTX 3080" in gpu:
            if "16GB" in item_name:
                row["vram_gb"] = "16.0"
            else:
                row["vram_gb"] = "8.0"
            updated_count += 1
            print(f"Updated {row['intake_id']} ({gpu}) -> VRAM: {row['vram_gb']}")
            continue
            
        found = False
        gpu_clean = gpu.replace(" ", "")
        for key, val in mappings.items():
            key_clean = key.replace(" ", "")
            if key_clean in gpu_clean:
                row["vram_gb"] = str(val)
                updated_count += 1
                found = True
                print(f"Updated {row['intake_id']} ({gpu}) -> VRAM: {val}")
                break
        if not found:
            print(f"Could not infer VRAM for {row['intake_id']} ({gpu})")

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Completed: updated {updated_count} rows.")
