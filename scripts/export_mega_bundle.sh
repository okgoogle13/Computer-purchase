#!/bin/bash
# scripts/export_mega_bundle.sh
# Generates the Mega-Bundle for NotebookLM with a freshness manifest

cd "$(dirname "$0")/.." || exit 1

OUTPUT_FILE="NotebookLM_Workspaces/MegaBundle_$(date +%Y-%m-%d).md"

echo "Generating Freshness Manifest..."
MANIFEST="# MegaBundle Manifest\n\nGenerated: $(date -u '+%Y-%m-%dT%H:%M:%SZ')\n\n"
MANIFEST+="## Included Sources\n"
MANIFEST+=$(find NotebookLM_Workspaces/intake -name "*.md" -o -name "*.csv" 2>/dev/null | xargs ls -lt --time-style=long-iso 2>/dev/null | awk '{print "- " $6 " " $7 " " $8}')

echo -e "$MANIFEST" > /tmp/manifest_header.md

echo "Running Repomix to pack the repository..."
npx --yes repomix --style markdown --output /tmp/repomix_temp_mega.md \
    --ignore "**/raw/**,**/__pycache__/**,**/.git/**,NotebookLM_Workspaces/MegaBundle_*.md,NotebookLM_Workspaces/*_context.md"

echo "Combining manifest and repomix output..."
cat /tmp/manifest_header.md /tmp/repomix_temp_mega.md > "$OUTPUT_FILE"
rm /tmp/manifest_header.md /tmp/repomix_temp_mega.md

echo "✅ Mega-Bundle generated: $OUTPUT_FILE"
