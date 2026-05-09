#!/bin/bash
# scripts/generate_scoring_context.sh
# Generates a scoring context bundle for the active CareerCopilot MCDA workflow.

cd "$(dirname "$0")/.." || exit 1

OUTPUT_FILE="NotebookLM_Workspaces/scoring_context.md"

echo "Running Repomix to pack active shortlist, product cards, and MCDA policies..."
npx --yes repomix --style markdown --output "$OUTPUT_FILE" \
    --include "AGENTS.md,README.md,CURRENT_STATE.md,config/*.json,scripts/*.py,scripts/README_*.md,scripts/prompt_templates/*.md,NotebookLM_Workspaces/intake/shortlist/*.csv,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/*.md,NotebookLM_Workspaces/04_Laptops_Mainline/*.md,NotebookLM_Workspaces/06_Mini_PCs_and_eGPU/*.md,NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/track2_pathway_a_build_spec.md,NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/README.md,NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/HOW_TO_MAINTAIN_RUBRIC.md,NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/template_product_card_output.md" \
    --ignore "**/raw/**,**/__pycache__/**,NotebookLM_Workspaces/MegaBundle_*.md,NotebookLM_Workspaces/*_context.md"

echo "✅ Scoring Context generated: $OUTPUT_FILE"
