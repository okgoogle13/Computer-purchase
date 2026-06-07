import re
from pathlib import Path

# Procurement limits from config
BUDGET_LAPTOP = 5000.0
BUDGET_TRACK2_A = 5000.0
BUDGET_TRACK2_B = 4000.0
BUDGET_TRACK2_C = 3500.0

LAPTOP_DISCRETE_VRAM_FLOOR = 8.0
LAPTOP_UNIFIED_MEM_FLOOR = 16.0

def parse_float(val) -> float | None:
    if not val:
        return None
    text = str(val).strip().replace("$", "").replace(",", "").upper()
    if text in ("UNKNOWN", "N/A", "NONE", "-"):
        return None
    try:
        # extract numeric parts
        m = re.search(r"[-+]?\d*\.\d+|\d+", text)
        return float(m.group(0)) if m else None
    except Exception:
        return None

def parse_frontmatter(md_text: str) -> dict:
    match = re.search(r"^---\s*\n(.*?)\n---", md_text, re.DOTALL | re.MULTILINE)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        fm[key.strip()] = val.strip()
    return fm

def update_frontmatter_status(md_text: str, new_status: str) -> str:
    # Match the frontmatter block
    match = re.search(r"^---\s*\n(.*?)\n---", md_text, re.DOTALL | re.MULTILINE)
    if not match:
        return md_text
    
    fm_content = match.group(1)
    # Check if status is already in frontmatter
    if re.search(r"^status:", fm_content, re.MULTILINE):
        # replace existing status
        new_fm_content = re.sub(r"^status:.*$", f"status: {new_status}", fm_content, flags=re.MULTILINE)
    else:
        # append status to frontmatter
        new_fm_content = fm_content.rstrip() + f"\nstatus: {new_status}"
        
    return md_text[:match.start(1)] + new_fm_content + md_text[match.end(1):]

def track_1b_soc_confirmed(row: dict) -> bool:
    candidates = [
        row.get("gpu"),
        row.get("gpu_model"),
        row.get("name"),
    ]
    raw = " ".join(str(v or "").strip() for v in candidates).strip()
    if not raw:
        return False
    normalized = raw.lower()
    indicators = ("strix halo", "ryzen ai max", "ryzen ai max+")
    return any(indicator in normalized for indicator in indicators)

cards_dir = Path("cards")
all_cards = list(cards_dir.rglob("*.md"))

retired_count = 0
for path in all_cards:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)
    if not fm:
        continue
        
    status = fm.get("status", "").strip().upper()
    if status in ("ARCHIVED", "REJECTED", "SOLD"):
        continue
        
    category = fm.get("category", "").strip().lower()
    track = fm.get("track", "").strip()
    pathway = fm.get("pathway", "").strip().upper()
    
    price = parse_float(fm.get("price_aud") or fm.get("list_price_aud"))
    vram = parse_float(fm.get("vram"))
    unified = parse_float(fm.get("unified_memory"))
    screen = parse_float(fm.get("screen_size_in"))
    
    reasons = []
    
    # 1. Laptop (Track 1) Caps and Floors
    if "laptop" in category or track == "1":
        # Price Check
        if price is not None and price > BUDGET_LAPTOP:
            reasons.append(f"Price {price} > laptop budget {BUDGET_LAPTOP}")
            
        # Screen Check (Track 1A discrete)
        if pathway == "1A":
            if screen is not None and screen < 16.0:
                reasons.append(f"Screen size {screen} < 16 inches floor")
            if vram is not None and vram < LAPTOP_DISCRETE_VRAM_FLOOR:
                reasons.append(f"VRAM {vram} < discrete floor {LAPTOP_DISCRETE_VRAM_FLOOR} GB")
                
        # Unified Memory & SoC Check (Track 1B Strix Halo)
        if pathway == "1B":
            if unified is not None and unified < LAPTOP_UNIFIED_MEM_FLOOR:
                reasons.append(f"Unified memory {unified} < floor {LAPTOP_UNIFIED_MEM_FLOOR} GB")
            if not track_1b_soc_confirmed(fm):
                reasons.append("SoC not confirmed as Strix Halo / Ryzen AI Max")

    # 2. Track 2 Workstation Caps
    elif track == "2":
        if pathway == "A" and price is not None and price > BUDGET_TRACK2_A:
            reasons.append(f"Price {price} > Track 2A budget {BUDGET_TRACK2_A}")
        elif pathway == "B" and price is not None and price > BUDGET_TRACK2_B:
            reasons.append(f"Price {price} > Track 2B budget {BUDGET_TRACK2_B}")
        elif pathway == "C" and price is not None and price > BUDGET_TRACK2_C:
            reasons.append(f"Price {price} > Track 2C budget {BUDGET_TRACK2_C}")
            
    if reasons:
        new_text = update_frontmatter_status(text, "ARCHIVED")
        path.write_text(new_text, encoding="utf-8")
        print(f"Retired card {path.name}: {'; '.join(reasons)}")
        retired_count += 1

print(f"\nRetired {retired_count} policy-violating cards.")
