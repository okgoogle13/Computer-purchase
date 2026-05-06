import csv

csv_path = "NotebookLM_Workspaces/intake/shortlist/2026-05-06_shortlist.csv"

# First, read all rows
rows = []
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)

# The list of orphans from our previous run
orphaned_ids = {
    'intake-048', 'intake-049', 'intake-018', 'intake-007', 'intake-008',
    'intake-016', 'intake-032', 'intake-033', 'intake-037', 'intake-043',
    'intake-044', 'intake-054', 'intake-055', 'intake-017', 'intake-002',
    'intake-022', 'intake-019', 'intake-024', 'intake-025', 'intake-026',
    'intake-062', 'intake-063', 'intake-064', 'intake-001', 'intake-028',
    'intake-056', 'intake-029', 'intake-027', 'intake-020', 'intake-021',
    'intake-057', 'intake-067', 'intake-030', 'intake-031', 'intake-070',
    'intake-068', 'intake-069', 'intake-061'
}

parked_log = []

for row in rows:
    item_name = row.get('item_name', '').lower()
    i_id = row.get('intake_id', '')
    
    # Identify if it's generic, synthetic, or an orphan
    is_generic = 'build' in item_name or 'concept' in item_name
    is_orphan = i_id in orphaned_ids
    
    if is_generic or is_orphan:
        row['status'] = 'PARKED'
        reason = []
        if is_generic: reason.append("Generic/synthetic name")
        if is_orphan: reason.append("No matching product card")
        parked_log.append((i_id, row.get('item_name'), " & ".join(reason)))

# Write back
with open(csv_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("### PARKED rows")
for p in parked_log:
    print(f"| {p[0]} | {p[1]} | {p[2]} |")
    
