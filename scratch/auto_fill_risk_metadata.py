import re
from pathlib import Path

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

def update_frontmatter_fields(md_text: str, updates: dict) -> str:
    match = re.search(r"^---\s*\n(.*?)\n---", md_text, re.DOTALL | re.MULTILINE)
    if not match:
        return md_text
    
    fm_content = match.group(1)
    
    for key, val in updates.items():
        # Replace or add key
        if re.search(rf"^{key}:", fm_content, re.MULTILINE):
            fm_content = re.sub(rf"^{key}:.*$", f"{key}: {val}", fm_content, flags=re.MULTILINE)
        else:
            fm_content = fm_content.rstrip() + f"\n{key}: {val}"
            
    return md_text[:match.start(1)] + fm_content + md_text[match.end(1):]

def is_unknown(val: str) -> bool:
    v = str(val or "").strip().upper()
    return v in ("", "UNKNOWN", "N/A", "NONE", "-")

def infer_risk_metadata(row: dict) -> tuple[str, str]:
    retailer = str(row.get("retailer") or row.get("seller_name") or "").strip().lower()
    platform = str(row.get("source_platform") or "").strip().upper()
    seller = str(row.get("seller_class") or "").strip().upper()
    
    # 1. Retailer mapping
    retailer_map = {
        "hub by triforce": ("MAJOR_RETAILER_AU", "MAJOR_RETAILER_AU"),
        "triforce": ("MAJOR_RETAILER_AU", "MAJOR_RETAILER_AU"),
        "ple computers": ("MAJOR_RETAILER_AU", "MAJOR_RETAILER_AU"),
        "ple": ("MAJOR_RETAILER_AU", "MAJOR_RETAILER_AU"),
        "jw computers": ("MAJOR_RETAILER_AU", "MAJOR_RETAILER_AU"),
        "jw": ("MAJOR_RETAILER_AU", "MAJOR_RETAILER_AU"),
        "centre com": ("MAJOR_RETAILER_AU", "MAJOR_RETAILER_AU"),
        "scorptec": ("MAJOR_RETAILER_AU", "MAJOR_RETAILER_AU"),
        "harvey norman": ("MAJOR_RETAILER_AU", "MAJOR_RETAILER_AU"),
        "officeworks": ("MAJOR_RETAILER_AU", "MAJOR_RETAILER_AU"),
        "dell outlet": ("MAJOR_RETAILER_AU", "REFURB_SELLER"),
        "dell outlet australia": ("MAJOR_RETAILER_AU", "REFURB_SELLER"),
        "dell australia": ("MANUFACTURER_AU", "MANUFACTURER_AU"),
        "dell": ("MANUFACTURER_AU", "MANUFACTURER_AU"),
        "hp australia": ("MANUFACTURER_AU", "MANUFACTURER_AU"),
        "hp": ("MANUFACTURER_AU", "MANUFACTURER_AU"),
        "lenovo outlet au": ("MANUFACTURER_AU", "MANUFACTURER_AU"),
        "lenovo outlet": ("MANUFACTURER_AU", "MANUFACTURER_AU"),
        "lenovo australia": ("MANUFACTURER_AU", "MANUFACTURER_AU"),
        "lenovo": ("MANUFACTURER_AU", "MANUFACTURER_AU"),
        "asus store au": ("MANUFACTURER_AU", "MANUFACTURER_AU"),
        "asus store": ("MANUFACTURER_AU", "MANUFACTURER_AU"),
        "asus": ("MANUFACTURER_AU", "MANUFACTURER_AU"),
        "recompute": ("MAJOR_RETAILER_AU", "REFURB_SELLER"),
        "ebay": ("EBAY_AU", "EBAY_AU"),
        "amazon": ("AMAZON_AU", "AMAZON_AU"),
        "green beast gaming": ("MAJOR_RETAILER_AU", "MAJOR_RETAILER_AU"),
    }
    
    for r_key, (plat, sel) in retailer_map.items():
        if r_key in retailer:
            return plat, sel
            
    # 2. Platform/seller translations
    if "fb_marketplace" in platform.lower() or "facebook" in platform.lower() or "marketplace" in platform.lower():
        return "FB_MARKETPLACE", "PRIVATE_SELLER"
    if "ebay" in platform.lower() or "ebay" in seller.lower():
        return "EBAY_AU", "EBAY_AU"
    if "amazon" in platform.lower():
        return "AMAZON_AU", "AMAZON_AU"
    if "private" in seller.lower():
        return "FB_MARKETPLACE", "PRIVATE_SELLER"
        
    return platform, seller

cards_dir = Path("cards")
all_cards = list(cards_dir.rglob("*.md"))

updated_count = 0
for path in all_cards:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)
    if not fm:
        continue
        
    status = fm.get("status", "").strip().upper()
    if status in ("ARCHIVED", "REJECTED", "SOLD"):
        continue
        
    current_plat = fm.get("source_platform", "")
    current_seller = fm.get("seller_class", "")
    
    if is_unknown(current_plat) or is_unknown(current_seller):
        inferred_plat, inferred_seller = infer_risk_metadata(fm)
        
        updates = {}
        if is_unknown(current_plat) and not is_unknown(inferred_plat):
            updates["source_platform"] = inferred_plat
        if is_unknown(current_seller) and not is_unknown(inferred_seller):
            updates["seller_class"] = inferred_seller
            
        if updates:
            new_text = update_frontmatter_fields(text, updates)
            path.write_text(new_text, encoding="utf-8")
            print(f"Updated {path.name}: {updates}")
            updated_count += 1

print(f"\nSuccessfully backfilled risk metadata for {updated_count} cards.")
