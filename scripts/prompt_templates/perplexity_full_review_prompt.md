# Perplexity Sonar Deep Research — Full End-to-End Review Prompt
**Version:** 2026-06-12
**Scope:** Combined codebase integrity review + AU market opportunity discovery
**Platform note:** Perplexity has no file system access. All repository context is pasted inline below.

---

## HOW TO USE THIS PROMPT

1. Open `scratch/procurement_context_pack.xml` and copy the entire file.
2. Replace the `<<< PASTE XML HERE >>>` block in Section 1 below with that content.
3. Optionally paste the top 10 rows of `shortlists/shortlist_ranked.csv` into the placeholder in Section 2.
4. Submit the full assembled prompt to Perplexity Sonar — Deep Research mode.
5. Save the response to `scratch/perplexity_review_YYYY-MM-DD.md`.
6. Bring the output back to Claude (Opus) for the MCDA decision step.

---

## SECTION 1 — CODEBASE CONTEXT (repomix pack)

The repository pack below was generated with:
```
repomix --style xml --output scratch/procurement_context_pack.xml \
  --include "AGENTS.md,CLAUDE.md,README.md,TASKS.md,config/*.json,\
scripts/build_shortlist.py,scripts/build_shortlist_laptops.py,\
scripts/build_shortlist_desktops.py,scripts/build_shortlist_mini_pcs.py,\
scripts/build_shortlist_components.py,scripts/build_shortlist_apple_silicon.py,\
scripts/scoring/rubric_weighting_engine.py,scripts/scoring/auto_score_cards.py,\
scripts/scoring/ranking_feedback_loop.py,\
scripts/policy_drift_check.py,scripts/pipeline_integrity_check.py,\
scripts/run_automated_pipeline.py,\
scripts/enrich_shortlist_pricing.py,scripts/fill_shortlist_live_pricing.py,\
scripts/fill_mcda_gaps.py,scripts/normalize_intake.py,scripts/intake_to_cards.py"
```

Pack contents: 24 files, ~54k tokens. Treat as read-only ground truth.

```
<<< PASTE ENTIRE CONTENTS OF scratch/procurement_context_pack.xml HERE >>>
```

---

## SECTION 2 — ACTIVE SHORTLIST CONTEXT

Current ranked shortlist (top rows from `shortlists/shortlist_ranked.csv`).
Paste the header row + top 10 data rows here:

```
<<< PASTE HEAD OF shortlists/shortlist_ranked.csv HERE >>>
```

Key facts from the current shortlist (as of 2026-06-12):
- **Top-ranked active candidate:** Lenovo Legion Pro 7i Gen 10 (intake-077), RTX 5090 24GB, $5,020.95 AUD — Certified Refurbished via Lenovo Outlet AU. Status: NEEDS_REVIEW (price > $5k cap, allowed via ≥24GB VRAM override). MCDA: 7.40.
- **BUY_CANDIDATE #1:** ASUS ROG Flow Z13 2025 (Strix Halo), 32GB unified, $4,499 AUD — MANUFACTURER_AU verified. MCDA: 7.00.
- **BUY_CANDIDATE #2:** ASUS ProArt PX13 HN7306EAC (Strix Halo), 128GB unified, $4,799 AUD. MCDA: 6.86 (adjusted).
- **Policy cap:** $5,000 AUD Track 1. Exception A: up to $6,000 AUD for ≥24GB VRAM.
- **Source priority:** MANUFACTURER_AU > MAJOR_RETAILER_AU > AMAZON_AU > EBAY_AU > GUMTREE_AU/FB_MARKETPLACE > GRAY_IMPORT.

---

## SECTION 3 — POLICY REFERENCE (inline, no file access needed)

### Budget & Track Gates
| Track | Pathway | Budget Cap AUD | VRAM Minimum |
|-------|---------|----------------|--------------|
| 1A | Discrete GPU Laptop | $5,000 (≤$6,000 if ≥24GB VRAM) | 8 GB discrete |
| 1B | Unified Memory Laptop | $5,000 | 16 GB unified (32 GB+ preferred) |
| 1.5 | Desktop (Exception A only) | $5,000 | 16 GB |

### MCDA Formula
```
MCDA = (Performance_Headroom × 0.25)
     + (Price_Value × 0.20)
     + (Future_Proof × 0.20)
     + (Portability × 0.20)
     + (Track2_Avoidance × 0.15)
```

### MCDA Factor Rubrics (from `AGENTS.md`)
- **Performance_Headroom:** 2–3 = 8GB; 4–5 = 12GB; 6–7 = 16GB or Strix Halo/M-series Pro; 8–10 = 24GB+ discrete or 64–128GB+ unified.
- **Price_Value:** 10 = exceptional value/discounts; 5 = fair market; 0 = at cap with no differentiation.
- **Future_Proof:** Mirrors Performance_Headroom tiers.
- **Portability:** 10 = ultraportable; 7–8 = 14–16" creator; 4–6 = heavy DTR; 0–3 = desktop.
- **Track2_Avoidance:** 32GB unified = 5–6; 64GB = 7; 128GB = 8.

### GPU Sweep Tiers (from `config/search_archetypes.json`)
RTX 5090 Laptop 24GB · RTX 5080 Laptop 16GB · RTX 5070 Ti Laptop 12GB · RTX 5070 Laptop 12GB · RTX 4090 Laptop 16GB · RTX 4080 Laptop 12GB · RTX 3080 Ti Laptop 16GB · RTX 3080 Laptop 16GB · RTX 4070 Ti Laptop 12GB · RTX 5000 Ada Laptop 16GB · RTX A5500 Laptop 16GB · RTX 4000 Ada Laptop 12GB · RTX 3500 Ada Laptop 12GB · Radeon RX 7900M 16GB · Ryzen AI Max Strix Halo 32GB+ · RTX Spark Laptop 32GB+ · RTX 3090 24GB Desktop Refurb · Minisforum AI X1 Pro Ryzen AI Max 64GB · Minisforum DEG2 RTX 5070 Ti · HP Z2 Mini G1a Ryzen AI Max 64GB

---

## SECTION 4 — REVIEW TASK A: CODEBASE INTEGRITY

Using the codebase pack in Section 1, perform a rigorous engineering review. For every finding: state `Severity (Critical/High/Medium/Low)` · `file:function-or-region` · `problem` · `concrete fix`. Confidence-tag each claim `[High]`, `[Medium]`, or `[Low]`.

### A1. Policy & Config Consistency
- Do `config/procurement_policy.json`, `config/search_archetypes.json`, and `config/shortlist_schema.json` agree with each other and with `AGENTS.md`/`CLAUDE.md`?
- Are any budget caps, VRAM floors, track gates, or source-priority constants **hardcoded in Python** rather than read from config? (drift risk — name each one)
- Does `scripts/policy_drift_check.py` actually detect the drift patterns you identify? Name any gaps.

### A2. Scoring Engine Correctness
- Audit `scripts/scoring/rubric_weighting_engine.py`: weight normalisation, null/NaN handling, tie-breaking, final MCDA formula. Do weights sum to 1.0?
- Cross-check `scripts/scoring/auto_score_cards.py` and `scripts/scoring/ranking_feedback_loop.py` for any scoring logic that contradicts the rubric engine.
- Does the `Seller_Risk_Multiplier` / `Source_Platform_Penalty` / `Risk_Adjustment` chain in the pipeline match the penalty rules in `AGENTS.md`?

### A3. Pipeline Data Flow
- Trace a candidate row through the full chain:
  `normalize_intake.py` → `intake_to_cards.py` → `build_shortlist*.py` → `enrich_shortlist_pricing.py` → `fill_shortlist_live_pricing.py` → `fill_mcda_gaps.py` → scoring
- Where can a column be silently dropped, renamed without a schema guard, or type-coerced incorrectly?
- Does `scripts/pipeline_integrity_check.py` cover the failure modes you find? List gaps.

### A4. Robustness & Error Handling
- Unhandled exceptions, bare `except:`, silent write failures, missing-file / empty-CSV paths.
- `run_automated_pipeline.py`: does a mid-pipeline failure leave a coherent state, or a corrupted half-written shortlist?
- Live-pricing steps (`fill_shortlist_live_pricing.py`): what happens on network timeout, CAPTCHA block, or partial write?

### A5. Duplication Across Build-Shortlist Modules
- The six `build_shortlist*.py` files — quantify shared logic that should be factored into a common helper.
- Identify divergence between them that looks accidental rather than intentional.

### A6. Security & Data Hygiene
- Secrets, tokens, cookies, or PII in any config or code file.
- Unsafe subprocess/shell invocations, unvalidated file paths, injection surfaces in scraping or pricing steps.

**Output contract for Section 4:** Return subsections A1–A6. Each finding: `Severity · file:region · problem · fix`. Close with a **Priority Action List (top 5)** ordered by risk. If a subsection has zero findings, state that explicitly.

---

## SECTION 5 — REVIEW TASK B: AU MARKET OPPORTUNITY DISCOVERY

Follow the two-phase workflow from `scripts/prompt_templates/cross_platform_research_core.md` exactly. The canonical logic is reproduced below.

### Phase 1: Prior-Conversation Coverage Audit
Review the shortlist context in Section 2. Identify:
- Recommendations made in prior context that are missing from the active shortlist/intake rows.
- Shortlist rows that have no corresponding product card in `cards/` (see definitions below).
- Product cards referenced in the shortlist that appear orphaned or have critical UNKNOWN fields.

Produce an explicit **"missed or untracked recommendation set"** before any new market discovery.

### Phase 2: Net-New AU Market Discovery
Only after Phase 1, search the live AU web for candidates not already covered by the shortlist or existing cards. Prioritise:
1. RTX 4090 16GB laptop — AU clearance or refurb under $5,000 AUD
2. RTX 4080 12GB laptop — AU stock under $4,500 AUD
3. RTX 3080 Ti 16GB laptop — AU new/refurb under $4,000 AUD
4. RX 7900M 16GB laptop — AU stock
5. RTX 5000 Ada 16GB laptop / RTX A5500 laptop — AU availability

Distinguish Phase 1 recovery items from Phase 2 genuinely new options in your output.

### Definitions
- **Missing:** No product card exists in `cards/laptops/`, `cards/desktops/`, `cards/mini_pcs/`, `cards/components/`, or `cards/apple_silicon/`.
- **Underutilized:** Card exists but item is absent from active shortlist rows, or present but mapped to the wrong track/pathway.

### Non-Negotiables
- No silent drops. Keep unresolved facts as `UNKNOWN`.
- Distinguish observed facts from inference.
- Do not propose editing repository files.
- Do not compute or assign new MCDA scores.
- Tag each claim with confidence: `[High]`, `[Medium]`, `[Low]`.
- For pricing: distinguish **ask price** vs **sold price** vs **verified clearance**.

**Output contract for Section 5:** Return sections A–G as defined in `cross_platform_research_core.md`:

- **A. Current Blind Spots** — table: `Candidate | Track/Pathway | Why High-Upside | Budget Posture | Evidence Strength | Notes`. Prefix each row `Phase1-Missed` or `Phase2-New`.
- **B. Priority Opportunity Queue** — ranked P1/P2/P3.
- **C. Verification Tasks** — exact fields to verify per P1/P2 opportunity.
- **D. Conflicts and Unknowns** — source disagreements; provisional preferred value with reason.
- **E. Suggested Track/Pathway Rechecks** — one-line per opportunity.
- **F. Dedup Log** — use labels: `Merged opportunity` / `Kept separate with reason` / `Discarded as non-material duplicate`.
- **G. Central IDE Handoff** — compact JSON/JSONL, one object per opportunity, stable keys: `candidate`, `track_pathway`, `priority`, `why_high_upside`, `budget_posture`, `evidence_strength`, `verification_tasks`, `conflicts`, `recommended_action`.

---

## SECTION 6 — FINAL SELF-CHECK (before submitting your response)

Verify your output satisfies all of:
- [ ] Section 4 (A1–A6) complete — zero silent omissions; explicit "no findings" where clean.
- [ ] Section 5 (A–G) complete and ordered.
- [ ] Every finding cites a specific `file:region`.
- [ ] No MCDA scoring, card-creation, or file-edit instructions in Section 5.
- [ ] All pricing claims distinguish ask vs sold vs verified clearance.
- [ ] All claims confidence-tagged `[High]` / `[Medium]` / `[Low]`.
- [ ] Section 5-G handoff is valid JSON/JSONL with stable keys only.

---

## REFERENCE FILE PATHS (for your record — not pasted inline)

| Purpose | File path |
|---------|-----------|
| Repomix context pack (paste into Section 1) | `scratch/procurement_context_pack.xml` |
| Active ranked shortlist (paste top rows into Section 2) | `shortlists/shortlist_ranked.csv` |
| Canonical research core logic | `scripts/prompt_templates/cross_platform_research_core.md` |
| Perplexity market-discovery wrapper | `scripts/prompt_templates/cross_platform_prompt_perplexity.md` |
| Codebase review prompt (this file) | `scripts/prompt_templates/perplexity_full_review_prompt.md` |
| Policy config | `config/procurement_policy.json` |
| Search archetypes / GPU tiers | `config/search_archetypes.json` |
| Shortlist schema | `config/shortlist_schema.json` |
| Procurement decision rules | `AGENTS.md` |
| Model routing & pipeline commands | `CLAUDE.md` |
