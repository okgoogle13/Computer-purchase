#!/usr/bin/env python3
"""Placeholder script for Facebook Marketplace data collection.
This stub uses Browserless API to perform a simple search and writes an empty CSV.
Replace with real implementation as needed.
"""
import sys, csv, os

def main():
    output_path = os.getenv('OUTPUT_PATH')
    if not output_path:
        if len(sys.argv) > 2 and sys.argv[1] == '--output':
            output_path = sys.argv[2]
        else:
            print('Usage: facebook_collect.py --output <path>', file=sys.stderr)
            sys.exit(1)
    # Write header only CSV
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['listing_id', 'title', 'price_aud', 'url', 'platform'])
    print(f'Placeholder Facebook data written to {output_path}')
    sys.exit(0)

if __name__ == '__main__':
    main()
