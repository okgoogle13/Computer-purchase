# CLAUDE.md
This file provides strict execution boundaries and guidance to Claude Code (`claude.ai/code`) when working with code in this repository.
## Project PurposeAI-assisted hardware procurement decision system for selecting hardware to ship CareerCopilot MVP (Q3 2026). The system uses a 5-phase pipeline: intake → shortlist → live pricing → manual MCDA scoring → ranked recommendation.

**Default goal:** Buy one Track 1 laptop that is outcome-enabled, AU-available, ≤5,000 AUD, and free of disqualifying thermal risk. Do not wait for Track 2.
## Token Efficiency & Session Optimization*CRITICAL: Local usage audits reveal a major token bleed ($13.11/session) driven by nested subagent loops (98%) and heavy background planning plugins (11%). You must adhere to these strict execution rules:*
### Anti-patterns (Avoid Costly Loops)- **NO Subagent Spawning**: You are forbidden from spawning background/nested subagents for file exploration, data cleanup, or configuration syncs. Defer these to `Antigravity CLI` via the routing matrix.
- **NO Automatic Plan Execution**: Do not invoke `/superpowers:executing-plans` or heavy chain skills. Break work into single-step bash strings.
- **NO Full-File Reading**: Never re-read full CSV files to inspect layout or look up single records. Use `head -n 5`, `grep`, or targeted tools.
- **Context Boundary Threshold**: When session length reaches or exceeds 100k tokens, you MUST halt and explicitly instruct the user: *"Context size is high. Please run `/compact` or `/clear` to reset our token window before we proceed."*
### Model Routing and Skill InvocationTo conserve Anthropic tokens, tasks are strictly categorized. If you hit a token ceiling or API rate limit, drop down to the fallback models immediately.


| Task Type | Primary Model / Command | Fallback Path (Token Wall) | Skill / Tool Execution |
| :--- | :--- | :--- | :--- |
| Grep, structural layout, CSV row check | `[HAIKU]` — `/model haiku` | `gemini-3.5-flash` | Direct bash tools only — no skills |
| Shortlist filtering & policy gate sweeps | `[HAIKU]` — `/model haiku` | `gemini-3.5-flash` | Direct bash tools only — no skills |
| Phase 1 product card coverage audit | `[GEMINI-FLASH-LOW]` | `gemini-3.1-flash-lite` | `Skill("gemini-card-audit")` |
| Opportunity gap / lost-opportunity audit | `[GEMINI-FLASH-MEDIUM]` | `gemini-3.1-pro` | `Skill("opportunity-audit")` |
| Secondary-market / private-sale search | `[GEMINI-FLASH-MEDIUM]` | `gemini-3.1-pro` | `Skill("gaming-laptop-private-sale")` |
| Refurb workstation AU web search | `[GEMINI-FLASH-MEDIUM]` | `gemini-3.1-pro` | `Skill("refurb-workstation-au")` |
| Live AU price / stock data parsing | `[SONNET]` — `/model sonnet` | `gemini-3.1-pro` | `Skill("price-verify")` |
| Live web browser scraping loop | `[SONNET]` — `/model sonnet` | Vercel CLI (Manual) | `Skill("agent-browser")` (Max 3 turns) |
| Git operations / Version control | **FORBIDDEN** | GitHub Copilot CLI | Instruct user to handle via `@copilot` |
| Final recommendation / MCDA check | `[SONNET]` — `/model sonnet` | `gemini-3.1-pro` | Direct execution — Pre-Decision Checklist |
### Routing Constraints- **Git Interdiction**: You are banned from executing `git add`, `git commit`, `git push`, or `git diff`.- **Vercel Browser Agent Rules**: Limit automated navigation to a maximum of 3 browser action turns per interaction block to avoid high-context runaway costs.
## Pipeline Commands```bash
# Full Orchestrated Pipeline Run
python3 scripts/run_automated_pipeline.py --batch YYYY-MM-DD

# Phase 0 — Spec Clarification (Interactive)
python scripts/agents/spec_clarifier/agent.py

# Phase 1 — Intake normalization & card creation
python3 scripts/run_gemini_card_audit.py

# Phase 2 — Shortlist Building
python scripts/build_shortlist.py
python scripts/build_shortlist.py --spec-json '{"track_preference":"1A","budget_cap_aud":4500}'
python scripts/build_shortlist.py --archetype gaming_laptop_private_sale
python scripts/build_shortlist.py --watchlist

# Phase 3a — Pricing schema scaffold only (No web calls)
python scripts/enrich_shortlist_pricing.py shortlists/shortlist_profile-laptop.csv

# Phase 3b — Live pricing fill (Cookie-wrapped browser search)
python scripts/fill_shortlist_live_pricing.py shortlists/shortlist_profile-laptop_pricing_enriched.csv

# Phase 4 — Fill missing MCDA score data
python scripts/fill_mcda_gaps.py shortlists/shortlist_profile-laptop_pricing_enriched_live.csv

# Phase 5 — MCDA ranking execution
python scripts/scoring/rubric_weighting_engine.py --csv shortlists/shortlist_profile-laptop_pricing_enriched_live.csv --output-csv shortlists/shortlist_profile-laptop_ranked.csv
```
## Architecture**Policy authority:** `AGENTS.md` > `config/procurement_policy.json` > CSV ledger > cards > live sources.

**Key files:**
- `AGENTS.md` — Canonical decision rules, weights, scoring formulas, and model matrices.
- `config/procurement_policy.json` — Budget caps, VRAM floor configs.
- `config/search_archetypes.json` — GPU search criteria, source query rules.
- `shortlists/` — CSV working files across pipeline stages.
- `cards/` — Markdown product data organized by category (`cards/laptops/`, etc., and watchlist `cards/watchlist/` for unreleased models).
