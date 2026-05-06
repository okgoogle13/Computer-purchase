import csv
import glob
import os
import re

CRITICAL_FIELDS = {
    'vram_gb',
    'unified_memory_gb',
    'price_aud',
    'effective_best_price_aud',
    'condition',
    'retailer',
    'au_stock',
    'gpu_model',
    'cpu_model'
}

csv_path = "NotebookLM_Workspaces/intake/shortlist/2026-05-06_shortlist.csv"
md_paths = glob.glob("NotebookLM_Workspaces/**/*.md", recursive=True)

ignore_dirs = ['raw', '01_Research_Methods_and_Decision_System']
md_paths = [p for p in md_paths if not any(ign in p for ign in ignore_dirs) and not os.path.basename(p).startswith('MegaBundle_') and not p.endswith('_context.md')]
# Include only the main card folders
card_folders = ['02_Refurbished_Desktop_Towers', '04_Laptops_Mainline', '05_Apple_Silicon_Laptops', '06_Mini_PCs_and_eGPU']
md_paths = [p for p in md_paths if any(cf in p for cf in card_folders)]

shortlist = []
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row.get('status', '').upper() == 'ACTIVE':
            shortlist.append(row)

cards = {}
for p in md_paths:
    if "template" in os.path.basename(p).lower(): continue
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
        intake_id = ""
        base = os.path.basename(p)
        if base.startswith("intake-"):
            intake_id = base.split("_")[0]
        else:
            m = re.search(r'intake_id\s*[:|]\s*([a-zA-Z0-9-]+)', content)
            if m: intake_id = m.group(1).strip()
        
        # Detect library-style cards (e.g. "23_model-name.md") with no intake_id
        if re.match(r'^\d+_', base):
            if 'intake_id' not in content:
                # Treat as library/future card, skip for this QA run
                continue
        
        cards[p] = {
            'content': content,
            'filename': base,
            'intake_id': intake_id
        }

# 1. Cross-link
shortlist_ids = {row.get('intake_id', ''): row for row in shortlist if row.get('intake_id')}
card_ids = {data['intake_id']: p for p, data in cards.items() if data['intake_id']}

orphaned_rows = []
for row in shortlist:
    i_id = row.get('intake_id', '')
    if not i_id or i_id not in card_ids:
        # Check by item_name approximation
        matched = False
        target = re.sub(r'[^a-z0-9]', '', row.get('item_name', '').lower())
        for p, data in cards.items():
            c_name = re.sub(r'[^a-z0-9]', '', data['filename'].lower())
            if target in c_name or c_name in target:
                matched = True
                break
        if not matched:
            orphaned_rows.append(row)

orphaned_cards = []
for p, data in cards.items():
    i_id = data['intake_id']
    if not i_id:
        continue  # no intake_id -> ignore for orphaned list
    if i_id not in shortlist_ids:
        orphaned_cards.append(data)

print("### 1. Cross-link shortlist rows and product cards\n")
print("#### Orphaned Shortlist Rows")
print("| intake_id | item_name | reason |")
print("|---|---|---|")
if not orphaned_rows:
    print("| None | None | All rows have matching cards |")
for row in orphaned_rows:
    print(f"| {row.get('intake_id','N/A')} | {row.get('item_name','N/A')} | No matching product card found |")

print("\n#### Orphaned Product Cards")
print("| intake_id | card_filename | reason |")
print("|---|---|---|")
if not orphaned_cards:
    print("| None | None | All cards are in shortlist CSV |")
for card in orphaned_cards:
    print(f"| {card.get('intake_id','N/A')} | {card['filename']} | Not found in shortlist CSV |")

# 2. UNKNOWN fields checklist
print("\n### 2. UNKNOWN fields checklist\n")
print("| intake_id | item_name | field_name | location | brief note |")
print("|---|---|---|---|---|")
for row in shortlist:
    for k, v in row.items():
        if v.strip() == "UNKNOWN" and k in CRITICAL_FIELDS:
            print(f"| {row.get('intake_id','N/A')} | {row.get('item_name','N/A')} | {k} | CSV | Needs human research |")

for p, data in cards.items():
    i_id = data['intake_id'] or 'N/A'
    item_name = shortlist_ids.get(i_id, {}).get('item_name', 'N/A')
    
    for line in data['content'].split('\n'):
        if "UNKNOWN" in line:
            field_name = None
            m = re.search(r'\|\s*\*\*([^\*]+)\*\*\s*\|\s*UNKNOWN', line)
            if m:
                field_name = m.group(1).strip()
            else:
                m = re.search(r'[-*]\s*\*\*([^\*]+)\*\*:\s*UNKNOWN', line)
                if m:
                    field_name = m.group(1).strip()
            
            if field_name:
                field_key = field_name.strip().lower().replace(' ', '_')
                if field_key in CRITICAL_FIELDS:
                    print(f"| {i_id} | {item_name} | {field_name} | Card | Needs human research |")

# 3. Schema drift sanity
csv_fields = set(shortlist[0].keys()) if shortlist else set()
card_fields = set()
for p, data in cards.items():
    for line in data['content'].split('\n'):
        m = re.search(r'\|\s*\*\*([^\*]+)\*\*\s*\|', line)
        if m: card_fields.add(m.group(1).strip())
        m = re.search(r'[-*]\s*\*\*([^\*]+)\*\*:', line)
        if m: card_fields.add(m.group(1).strip())

print("\n### 3. Schema drift sanity\n")
print("CSV Fields:", sorted(list(csv_fields)))
print("Card Fields:", sorted(list(card_fields)))

