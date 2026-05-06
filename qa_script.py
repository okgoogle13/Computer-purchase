import csv
import glob
import os
import re
from collections import defaultdict

csv_path = "NotebookLM_Workspaces/intake/shortlist/2026-05-06_shortlist.csv"
md_paths = glob.glob("NotebookLM_Workspaces/**/*.md", recursive=True)

# Ignore non-product card markdowns
ignore_dirs = ['raw', '01_Research_Methods_and_Decision_System']
md_paths = [p for p in md_paths if not any(ign in p for ign in ignore_dirs) and not os.path.basename(p).startswith('MegaBundle_') and not p.endswith('_context.md')]
# Also exclude non-product cards (e.g., README.md, AGENTS.md, config files, scoring context)
md_paths = [p for p in md_paths if 'intake-' in os.path.basename(p) or '02_Refurbished_Desktop_Towers' in p or '04_Laptops_Mainline' in p or '05_Apple_Silicon_Laptops' in p or '06_Mini_PCs_and_eGPU' in p]

shortlist = []
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        shortlist.append(row)

cards = {}
for p in md_paths:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
        intake_id = ""
        # try to extract intake_id from filename
        base = os.path.basename(p)
        if base.startswith("intake-"):
            intake_id = base.split("_")[0]
        # try to find intake_id in content
        m = re.search(r'intake_id[\s|:]*([a-zA-Z0-9-]+)', content)
        if m:
            intake_id = m.group(1).strip()
        
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
        # Check if filename roughly matches item_name?
        matched = False
        for p, data in cards.items():
            if row.get('item_name', '').lower().replace(' ', '-') in data['filename'].lower():
                matched = True
                break
        if not matched:
            orphaned_rows.append(row)

orphaned_cards = []
for p, data in cards.items():
    i_id = data['intake_id']
    # skip templates
    if 'template' in data['filename'].lower(): continue
    if not i_id or i_id not in shortlist_ids:
        orphaned_cards.append(data)

print("### Orphaned Shortlist Rows")
print("| intake_id | item_name | reason |")
print("|---|---|---|")
for row in orphaned_rows:
    print(f"| {row.get('intake_id','N/A')} | {row.get('item_name','N/A')} | No matching product card found |")

print("\n### Orphaned Product Cards")
print("| intake_id | card_filename | reason |")
print("|---|---|---|")
for card in orphaned_cards:
    print(f"| {card.get('intake_id','N/A')} | {card['filename']} | Not found in shortlist CSV |")

# 2. UNKNOWN fields
print("\n### Data-Ready Checklist")
print("| intake_id | item_name | field_name | location | brief note |")
print("|---|---|---|---|---|")
for row in shortlist:
    for k, v in row.items():
        if v.strip() == "UNKNOWN":
            print(f"| {row.get('intake_id','N/A')} | {row.get('item_name','N/A')} | {k} | CSV | Needs human research |")

for p, data in cards.items():
    # Only if not orphaned and not template
    if 'template' in data['filename'].lower(): continue
    i_id = data['intake_id']
    if not i_id: i_id = 'N/A'
    lines = data['content'].split('\n')
    item_name = 'N/A'
    if i_id in shortlist_ids:
        item_name = shortlist_ids[i_id].get('item_name', 'N/A')
    
    for line in lines:
        if "UNKNOWN" in line:
            # try to parse field name (table format: | **Field** | UNKNOWN |)
            m = re.match(r'\|\s*\*\*([^\*]+)\*\*\s*\|\s*UNKNOWN\s*\|', line)
            if m:
                print(f"| {i_id} | {item_name} | {m.group(1).strip()} | Card | Needs human research |")
            else:
                # KV format: Field: UNKNOWN
                m = re.match(r'^([^:]+):\s*UNKNOWN', line)
                if m:
                    print(f"| {i_id} | {item_name} | {m.group(1).strip()} | Card | Needs human research |")

# 3. Schema drift
csv_fields = list(shortlist[0].keys()) if shortlist else []
card_fields = set()
for p, data in cards.items():
    if 'template' in data['filename'].lower(): continue
    lines = data['content'].split('\n')
    for line in lines:
        m = re.match(r'\|\s*\*\*([^\*]+)\*\*\s*\|', line)
        if m:
            card_fields.add(m.group(1).strip())

print("\n### Schema Drift Sanity")
print("CSV Fields:", sorted(csv_fields))
print("Card Fields:", sorted(list(card_fields)))

