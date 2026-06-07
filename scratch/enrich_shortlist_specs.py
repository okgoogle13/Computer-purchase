#!/usr/bin/env python3
import csv
import re
from pathlib import Path

input_path = Path("shortlists/2026-06-07_shortlist_profile-laptop_pricing_enriched.csv")
output_path = Path("shortlists/2026-06-07_shortlist_pricing_enriched_live.csv")

if not input_path.exists():
    print(f"Error: Input file {input_path} does not exist.")
    exit(1)

with input_path.open("r", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames or [])
    rows = list(reader)

# GPU VRAM mappings (Laptop/Mobile GPUs)
gpu_vram_map = {
    "RTX 5090": 24.0,
    "RTX 5080": 16.0,
    "RTX 5070 TI": 12.0,
    "RTX 5070": 12.0,
    "RTX 5060": 8.0,
    "RTX 4090": 16.0,
    "RTX 4080": 12.0,
    "RTX 4070": 8.0,
    "RTX 4060": 8.0,
    "RTX 3080 TI": 16.0,
    "RTX 3080": 16.0,
    "RTX 3070 TI": 8.0,
    "RTX 3070": 8.0,
    "RTX 3060": 6.0,
    "RTX 3050 TI": 4.0,
    "RTX 3050": 4.0,
    "A5000": 16.0,
    "A4000": 16.0,
    "A2000": 6.0,
    "RX 6850M": 12.0,
    "RX 6800M": 12.0,
}

filtered_rows = []
for row in rows:
    # Get values
    item_name = str(row.get("item_name") or "").upper()
    gpu = str(row.get("gpu_model") or "").upper()
    vram_str = str(row.get("vram_gb") or "").upper()
    screen_str = str(row.get("screen_size_in") or "").upper()
    price_str = str(row.get("price_aud") or "").replace("$", "").replace(",", "").strip()

    # 1. Infer VRAM
    vram = None
    if vram_str not in ("UNKNOWN", "N/A", "NONE", "-") and vram_str != "":
        try:
            vram = float(vram_str)
        except ValueError:
            pass
            
    if vram is None:
        # Check title/desc for VRAM indicators first (e.g. "16GB GPU" or "12GB VRAM")
        vram_match = re.search(r'(\d+)\s*(GB|G)\s*(VRAM|GPU|GRAPHICS)', item_name)
        if vram_match:
            vram = float(vram_match.group(1))
        else:
            gpu_clean = gpu.replace(" ", "").replace("GEFORCE", "").strip()
            for key, val in gpu_vram_map.items():
                key_clean = key.replace(" ", "")
                if key_clean in gpu_clean or key_clean in item_name.replace(" ", ""):
                    vram = val
                    break
    if vram is not None:
        row["vram_gb"] = str(vram)
    else:
        row["vram_gb"] = "UNKNOWN"

    # 2. Infer Screen Size
    screen = None
    if screen_str not in ("UNKNOWN", "N/A", "NONE", "-") and screen_str != "":
        try:
            screen = float(screen_str)
        except ValueError:
            pass
            
    if screen is None:
        # Heuristics based on title
        if "G14" in item_name or "14-INCH" in item_name or " 14\"" in item_name or "14.0" in item_name or "PX13" in item_name or "A14" in item_name:
            screen = 14.0
        elif "15.6" in item_name or "15-INCH" in item_name or " 15\"" in item_name or "15.0" in item_name or "XPS 15" in item_name or "VAPOR 15" in item_name or "P15" in item_name:
            screen = 15.6
        elif "16-INCH" in item_name or " 16\"" in item_name or "16.0" in item_name or "G16" in item_name or "SLIM 5" in item_name or "LEGION PRO 7" in item_name or "LEGION PRO 5" in item_name or "X16" in item_name or "SLIM 7" in item_name or "OMEN MAX" in item_name or "A16" in item_name or "TUF F16" in item_name or "LEGION 7" in item_name or "LEGION 5 PRO" in item_name or "LEGION 9I" in item_name:
            screen = 16.0
        elif "17.3" in item_name or "17-INCH" in item_name or " 17\"" in item_name or "VECTOR GP78" in item_name or "RAIDER GE78" in item_name:
            screen = 17.3
        elif "18-INCH" in item_name or " 18\"" in item_name or "18.0" in item_name or "M18" in item_name or "AREA-51" in item_name or "TITAN 18" in item_name or "RAIDER 18" in item_name or "HELIOS 18" in item_name:
            screen = 18.0
            
    if screen is not None:
        row["screen_size_in"] = str(screen)
    else:
        # Check if it contains 16 or 15 in item name
        if "16" in item_name or "16S" in item_name:
            row["screen_size_in"] = "16.0"
        elif "15" in item_name:
            row["screen_size_in"] = "15.6"
        else:
            row["screen_size_in"] = "UNKNOWN"

    # 3. Basic validity filters
    # Skip standalone graphics cards or components misclassified as laptops
    if any(kw in item_name for kw in ["GRAPHICS CARD", "GRAPHIC CARD", "VIDEO CARD", "PCIE", "WATERBLOCK"]):
        continue
    if row.get("profile") == "Component" or row.get("category") == "Component" or row.get("Category_Group") == "Standalone_GPU":
        continue
    # Skip if item is obviously a component based on name
    if "GTX 1080" in item_name and "LAPTOP" not in item_name and "WORKSTATION" not in item_name:
        if "GRAPHICS" in item_name or "CARD" in item_name:
            continue
    if "RX-570" in item_name or "RX 570" in item_name:
        continue
    if "GIGABYTE 1080" in item_name:
        continue
    # Skip unknown price or price over budget
    if row.get("Price_Unknown") == "Yes" or not price_str or price_str.upper() == "UNKNOWN":
        continue
    try:
        price = float(price_str)
        if price > 5000.0:
            continue
    except ValueError:
        continue

    # Filter by capability floor (discrete VRAM >= 8GB or unified memory >= 16GB)
    unified_str = str(row.get("unified_memory_gb") or "").upper()
    unified = None
    if unified_str not in ("UNKNOWN", "N/A", "NONE", "-") and unified_str != "":
        try:
            unified = float(unified_str)
        except ValueError:
            pass
            
    # Strix Halo check for unified
    if "STRIX HALO" in item_name or "RYZEN AI MAX" in item_name or "HN6306" in item_name or "PROART PX13" in item_name:
        row["track"] = "1"
        row["pathway"] = "1B"
        if not unified:
            unified = 32.0 # fallback default for PX13/Strix Halo if unknown
            row["unified_memory_gb"] = "32.0"
            
    is_discrete_viable = (vram is not None and vram >= 8.0)
    is_unified_viable = (unified is not None and unified >= 16.0)
    
    if is_discrete_viable or is_unified_viable:
        # Add to shortlist
        filtered_rows.append(row)

with output_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_rows)

print(f"Viable candidates filtered and written: {len(filtered_rows)} rows written to {output_path}")
