#!/usr/bin/env python3
import os
import re
from pathlib import Path

def extract_vram(text):
    match = re.search(r"vram:\s*([0-9.]+)", text, re.IGNORECASE)
    if match: return float(match.group(1))
    match = re.search(r"unified_memory:\s*([0-9.]+)", text, re.IGNORECASE)
    if match: return float(match.group(1))
    return 8.0

def extract_price(text):
    match = re.search(r"price_aud:\s*[\$]?([0-9,.]+)", text, re.IGNORECASE)
    if match: 
        val = match.group(1).replace(",", "")
        try: return float(val)
        except: return 5000.0
    return 5000.0

def score_card(filepath):
    path = Path(filepath)
    content = path.read_text(encoding='utf-8')

    # Find frontmatter between --- and ---
    match = re.search(r"---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False
    
    frontmatter = match.group(1)
    
    vram = extract_vram(frontmatter)
    price = extract_price(frontmatter)
    is_laptop = "laptop" in str(path).lower()
    is_mini = "mini" in str(path).lower()
    
    perf = 3
    if vram >= 24: perf = 9
    elif vram >= 16: perf = 7
    elif vram >= 12: perf = 5
    
    future = 3
    if vram >= 24: future = 9
    elif vram >= 16: future = 7
    elif vram >= 12: future = 5
    
    port = 2
    if is_laptop:
        port = 8
        if "18" in content or "17.3" in content:
            port = 5
    elif is_mini:
        port = 7
    
    t2 = 0
    if vram >= 24: t2 = 9
    elif vram >= 16: t2 = 7
    elif vram >= 12: t2 = 4
    
    price_val = max(0, min(10, int(10 - (price - 2000) / 400)))
    
    fm_lines = frontmatter.strip().splitlines()
    fm_dict = {}
    for line in fm_lines:
        if ":" in line:
            k, v = line.split(":", 1)
            fm_dict[k.strip()] = v.strip()
    
    fm_dict["Performance_Headroom"] = str(perf)
    fm_dict["Price_Value"] = str(price_val)
    fm_dict["Future_Proof"] = str(future)
    fm_dict["Portability"] = str(port)
    fm_dict["Track2_Avoidance"] = str(t2)
    
    new_fm = "\n".join([f"{k}: {v}" for k, v in fm_dict.items()])
    new_content = content.replace(frontmatter, new_fm)
    
    if new_content != content:
        path.write_text(new_content, encoding='utf-8')
        return True
    return False

root = Path("cards")
count = 0
for md_file in root.rglob("*.md"):
    if score_card(md_file):
        count += 1

print(f"Updated {count} cards with new scoring fields.")
