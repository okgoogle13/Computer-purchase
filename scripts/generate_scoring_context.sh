#!/bin/bash
# scripts/generate_scoring_context.sh
# Generates a scoring context bundle explicitly including the policy and rubric documents

cd "$(dirname "$0")/.." || exit 1

OUTPUT_FILE="NotebookLM_Workspaces/scoring_context.md"

echo "Running Repomix to pack shortlist, product cards, and scoring policies..."
npx --yes repomix --style markdown --output "$OUTPUT_FILE" \
    --include "NotebookLM_Workspaces/intake/shortlist/*.csv,NotebookLM_Workspaces/**/*.md,AGENTS.md,config/*.json,scripts/*.py" \
    --ignore "**/raw/**,NotebookLM_Workspaces/MegaBundle_*.md,NotebookLM_Workspaces/*_context.md"

echo "✅ Scoring Context generated: $OUTPUT_FILE"
