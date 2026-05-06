# Audit Checklist Prompt

**Role**: You are a Data Ingestion Coordinator.

Attached is my `audit_context.md` file containing my hardware shortlist CSV and all individual product cards.

**Your tasks:**

1. **Cross-reference** every row in the CSV against the product cards. Tell me if any CSV row is missing a product card, or if any product card is not in the CSV.
2. **Scan** all product cards for fields that are marked `UNKNOWN` or are clearly missing data.
3. **Generate** a 'Data-Ready Checklist' markdown table containing: `[Intake ID] | [Item Name] | [Missing Field]`. Do not attempt to guess the values, just output the exact checklist.
