#!/usr/bin/env python3
"""Placeholder script for Gumtree AU data collection.
Writes an empty CSV with required columns and adds NO_FEEDBACK_SYSTEM flag.
Replace with real implementation later.
"""
import sys, csv, os

def main():
    output_path = os.getenv('OUTPUT_PATH')
    if not output_path:
        if len(sys.argv) > 2 and sys.argv[1] == '--output':
            output_path = sys.argv[2]
        else:
            print('Usage: gumtree_collect.py --output <path>', file=sys.stderr)
            sys.exit(1)
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['listing_id', 'title', 'price_aud', 'url', 'platform', 'risk_flags'])
        # No rows, placeholder only
    print(f'Placeholder Gumtree data written to {output_path}')
    sys.exit(0)

if __name__ == '__main__':
    main()
