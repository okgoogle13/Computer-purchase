#!/bin/bash
# scripts/generate_checklist_prompt.sh
# Packs active CSVs and product cards into a context file for data-readiness audits.

cd "$(dirname "$0")/.." || exit 1

OUTPUT_FILE="NotebookLM_Workspaces/audit_context.md"

echo "Running Repomix to pack active shortlist and product cards..."
npx --yes repomix --style markdown --output "$OUTPUT_FILE" \
    --include "AGENTS.md,config/*.json,NotebookLM_Workspaces/intake/shortlist/*.csv,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/*.md,NotebookLM_Workspaces/04_Laptops_Mainline/*.md,NotebookLM_Workspaces/06_Mini_PCs_and_eGPU/*.md,NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/track2_pathway_a_build_spec.md,NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/template_product_card_output.md" \
    --ignore "**/raw/**,**/__pycache__/**,NotebookLM_Workspaces/MegaBundle_*.md,NotebookLM_Workspaces/*_context.md"

echo "Appending Schema Drift Report to $OUTPUT_FILE..."
echo "" >> "$OUTPUT_FILE"
echo "## Schema Drift Report" >> "$OUTPUT_FILE"
echo "Run: grep -rh '^## ' NotebookLM_Workspaces/**/*.md | sort | uniq -c | sort -rn" >> "$OUTPUT_FILE"

# Find all lines starting with '| **' in product cards to detect schema variants in markdown tables
grep -rh "^| \*\*" NotebookLM_Workspaces/02_Refurbished_Desktop_Towers NotebookLM_Workspaces/04_Laptops_Mainline NotebookLM_Workspaces/06_Mini_PCs_and_eGPU 2>/dev/null | \
  sed 's/ \*\*//g' | sort | uniq -c | sort -rn >> "$OUTPUT_FILE"

echo "✅ Audit Context generated: $OUTPUT_FILE"
