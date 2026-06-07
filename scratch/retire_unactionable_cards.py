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

def update_frontmatter_status(md_text: str, new_status: str) -> str:
    match = re.search(r"^---\s*\n(.*?)\n---", md_text, re.DOTALL | re.MULTILINE)
    if not match:
        return md_text
    
    fm_content = match.group(1)
    if re.search(r"^status:", fm_content, re.MULTILINE):
        new_fm_content = re.sub(r"^status:.*$", f"status: {new_status}", fm_content, flags=re.MULTILINE)
    else:
        new_fm_content = fm_content.rstrip() + f"\nstatus: {new_status}"
        
    return md_text[:match.start(1)] + new_fm_content + md_text[match.end(1):]

def is_unknown(val: str) -> bool:
    v = str(val or "").strip().upper()
    return v in ("", "UNKNOWN", "N/A", "NONE", "-")

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
        
    price = fm.get("price_aud", "") or fm.get("list_price_aud", "")
    retailer = fm.get("retailer", "") or fm.get("seller_name", "")
    url = fm.get("url", "") or fm.get("product_url", "")
    
    # Check if price, retailer, and URL are all unknown/empty
    if is_unknown(price) and is_unknown(retailer) and is_unknown(url):
        new_text = update_frontmatter_status(text, "ARCHIVED")
        path.write_text(new_text, encoding="utf-8")
        print(f"Retired unactionable card: {path.name} (no price, retailer, or url)")
        retired_count += 1

print(f"\nRetired {retired_count} unactionable cards.")
