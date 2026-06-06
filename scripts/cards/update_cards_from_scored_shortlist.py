#!/usr/bin/env python3
"""Placeholder for updating laptop cards from scored shortlist.
It reads the scored CSV, and for each row creates/updates a markdown file
under `cards/laptops/` with front‑matter only (YAML). Existing body sections
are preserved – this stub only writes the file if it does not exist; if it
exists it merges front‑matter keys without touching the body.
"""
import csv, os, sys, yaml, pathlib

def load_csv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))

def ensure_card(card_path, front_matter):
    if not os.path.exists(card_path):
        # create new file with front‑matter and stub sections
        with open(card_path, 'w') as f:
            f.write('---\n')
            yaml.dump(front_matter, f)
            f.write('---\n\n')
            f.write('## Battery Health\n\n')
            f.write('## Acquisition Risk\n\n')
            f.write('## Evidence\n\n')
            f.write('## Notes\n')
        return
    # merge front‑matter (preserve body)
    with open(card_path, 'r') as f:
        content = f.read()
    if content.startswith('---'):
        parts = content.split('---', 2)
        existing = yaml.safe_load(parts[1]) or {}
        existing.update(front_matter)
        new_front = yaml.dump(existing)
        new_content = f'---\n{new_front}---{parts[2]}'
        with open(card_path, 'w') as f:
            f.write(new_content)

def main():
    if len(sys.argv) != 3 or sys.argv[1] != '--input':
        print('Usage: update_cards_from_scored_shortlist.py --input <scored_csv>', file=sys.stderr)
        sys.exit(1)
    csv_path = sys.argv[2]
    rows = load_csv(csv_path)
    cards_dir = os.path.join('cards', 'laptops')
    os.makedirs(cards_dir, exist_ok=True)
    for row in rows:
        if row.get('Policy_Status') != 'PASS':
            continue
        card_name = f"{row['item_name'].replace(' ', '_')}.md"
        card_path = os.path.join(cards_dir, card_name)
        front = {
            'item_name': row['item_name'],
            'risk_adjusted_price': row.get('risk_adjusted_price'),
            'risk_flags': row.get('risk_flags'),
            'score': row.get('score'),
            'performance_headroom': row.get('performance_headroom'),
            'price_value': row.get('price_value'),
            'future_proof': row.get('future_proof'),
            'portability': row.get('portability'),
            'track2_avoidance': row.get('track2_avoidance'),
        }
        ensure_card(card_path, front)
    print('Card update placeholder completed.')

if __name__ == '__main__':
    main()
