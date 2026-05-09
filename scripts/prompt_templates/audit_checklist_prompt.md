# Audit Checklist Prompt

**Role**: You are a Data Ingestion Coordinator.

Attached is my `audit_context.md` file containing the active hardware shortlist CSVs, product cards, `AGENTS.md`, and procurement policy config.

**Your tasks:**

1. **Cross-reference** every shortlist row against product cards. Report rows with no card and cards with no row.
2. **Scan** all product cards for `UNKNOWN`, stale, contradictory, or missing decision fields.
3. **Focus on MCDA-critical fields:** price, effective price, AU stock, VRAM/unified memory, screen size, thermal risk, warranty/ACL, pathway, and Track 2 trigger status.
4. **Generate** a data-ready checklist table:
   `[Intake ID] | [Item Name] | [Pathway] | [Missing Field] | [Why It Matters]`.

Do not guess values. Output only the exact checklist and any card/CSV mapping mismatches.
