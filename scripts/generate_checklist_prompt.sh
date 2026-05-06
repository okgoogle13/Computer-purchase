#!/bin/bash
# scripts/generate_checklist_prompt.sh
# Packs the CSV and product cards into a context file for ChatGPT/Gemini and checks for schema drift

cd "$(dirname "$0")/.." || exit 1

OUTPUT_FILE="NotebookLM_Workspaces/audit_context.md"

echo "Running Repomix to pack shortlist and product cards..."
npx --yes repomix --style markdown --output "$OUTPUT_FILE" \
    --include "NotebookLM_Workspaces/intake/shortlist/*.csv,NotebookLM_Workspaces/**/*.md" \
    --ignore "**/raw/**,NotebookLM_Workspaces/MegaBundle_*.md,NotebookLM_Workspaces/*_context.md"

echo "Appending Schema Drift Report to $OUTPUT_FILE..."
echo "" >> "$OUTPUT_FILE"
echo "## Schema Drift Report" >> "$OUTPUT_FILE"
echo "Run: grep -rh '^## ' NotebookLM_Workspaces/**/*.md | sort | uniq -c | sort -rn" >> "$OUTPUT_FILE"

# Find all lines starting with '| **' in product cards to detect schema variants in markdown tables
grep -rh "^| \*\*" NotebookLM_Workspaces/ 2>/dev/null | \
  sed 's/ \*\*//g' | sort | uniq -c | sort -rn >> "$OUTPUT_FILE"

echo "✅ Audit Context generated: $OUTPUT_FILE"
