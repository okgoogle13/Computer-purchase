import csv
from collections import defaultdict
import re

csv_path = "NotebookLM_Workspaces/intake/shortlist/2026-05-06_shortlist.csv"

# Load CSV to get VRAM, GPU, and status
rows = {}
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row.get('status', '').upper() == 'ACTIVE':
            # Parse VRAM to float for sorting
            vram_raw = row.get('vram_gb', '0')
            try: vram_val = float(vram_raw) if vram_raw != 'UNKNOWN' else 0.0
            except: vram_val = 0.0
            row['_vram_val'] = vram_val
            rows[row['intake_id']] = row

pricing_fields = {'price_aud', 'effective_best_price_aud', 'retailer', 'au_stock'}
spec_fields = {'vram_gb', 'unified_memory_gb', 'gpu_model', 'cpu_model', 'condition'}

pricing_todos = defaultdict(set)
spec_todos = defaultdict(set)

# Parse output.md
with open("output.md", 'r', encoding='utf-8') as f:
    for line in f:
        m = re.search(r'\|\s*(intake-\d+)\s*\|\s*([^\|]+?)\s*\|\s*([^\|]+?)\s*\|', line)
        if m:
            i_id = m.group(1).strip()
            field = m.group(3).strip()
            if i_id in rows:
                if field in pricing_fields:
                    pricing_todos[i_id].add(field)
                elif field in spec_fields:
                    spec_todos[i_id].add(field)

# Sort based on VRAM descending
sorted_ids = sorted(rows.keys(), key=lambda k: rows[k]['_vram_val'], reverse=True)

# Generate pricing to-do
print("### Pricing To-Do")
count = 0
for i_id in sorted_ids:
    if i_id in pricing_todos:
        row = rows[i_id]
        fields_str = ", ".join(sorted(pricing_todos[i_id]))
        print(f"| {i_id} | {row['item_name']} | {fields_str} | Scorptec, Mwave, Umart, Dell/HP Refurb |")
        count += 1
        if count >= 20: break

# Generate spec to-do
print("\n### Spec To-Do")
count = 0
for i_id in sorted_ids:
    if i_id in spec_todos:
        row = rows[i_id]
        fields_str = ", ".join(sorted(spec_todos[i_id]))
        print(f"| {i_id} | {row['item_name']} | {fields_str} | Vendor spec sheet, PSREF, or manual |")
        count += 1
        if count >= 20: break

