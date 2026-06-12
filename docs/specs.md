# Spec: Open-World AI Hardware Procurement Agent

## Objective

**What we are building:** A conversational AI agent that discovers, researches, and scores AI-capable laptops available in the Australian market in real time, and returns a ranked recommendation with a clear BUY / WAIT / INVESTIGATE verdict.

**Why:** The existing pipeline (`build_shortlist.py`, `rubric_weighting_engine.py`, 25+ scripts) is a closed-world scorer — it can only rank products already stored as markdown cards in `cards/`. It cannot discover new products, verify live AU pricing, or respond to new model releases. This agent architecture replaces the entire pipeline.

**Who uses it:** A single developer asking natural language procurement questions during a one-time laptop purchase decision for CareerCopilot MVP development (Q3 2026).

**Context inherited from existing repo:**
- Policy rules: `AGENTS.md` — canonical decision authority, do not duplicate
- Budget: ≤ 5,000 AUD hard cap
- MCDA weights: Performance Headroom (25%), Price Value (20%), Future Proof (20%), Portability (20%), Track2 Avoidance (15%)
- Target hardware: Track 1B (Unified Memory ≥ 32GB, Apple Silicon or AMD Strix Halo) preferred over Track 1A (discrete VRAM ≥ 8GB)

---

## Assumptions

Before any agent implements this spec, verify:

1. Google Search grounding is available as a tool (AI Studio or ADK `google_search` tool)
2. No GCP billing, AlloyDB, or Vertex AI Search infrastructure is required for the prototype
3. Existing `cards/*.md` files are treated as **reference data only**, not as the live product catalog
4. This agent **replaces** — not wraps — the existing Python pipeline scripts
5. AU market primary sources: JB Hi-Fi, Scorptec, MSY, Amazon AU, eBay AU

> Correct any of these before proceeding to implementation.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Agent framework | Google ADK (`google-adk`) or AI Studio Build (prototype) |
| LLM | Gemini 2.0 Flash (research sweeps) / Gemini 2.5 Pro (MCDA scoring + verdict) |
| Search grounding | Google Search tool (AI Studio) / Tavily or Google Custom Search API (ADK) |
| Page Extraction | Jina Reader (`https://r.jina.ai/`) to convert HTML to Markdown |
| Policy source | `AGENTS.md` + `config/procurement_policy.json` |
| Output format | Structured JSON → Markdown card (optionally written to `cards/laptops/`) |
| Runtime | Python 3.11+, `uv` for dependency management |

---

## Architecture: 3-Tool Open-World Agent

The agent uses exactly **three tools**. No more.

```
User Spec (natural language)
        |
[TOOL 1] search_web(query)
  Input:  "RTX 5070 laptop AU 2026 buy"
  Output: list of retailer URLs + headline specs + prices
  Source: Google Search grounding (AI Studio) / Tavily or Custom Search API (ADK)
        |
[TOOL 2] extract_product(url)
  Input:  retailer product page URL
  Output: structured dict:
    item_name, price_aud, in_stock,
    vram_gb OR unified_memory_gb,
    screen_size_in, touchscreen,
    cpu_model, ram_gb, warranty_months,
    retailer, url, date_checked
  Source: Jina Reader API (https://r.jina.ai/{url}) fallback to search snippet if blocked
        |
[TOOL 3] score_candidate(spec_dict)
  Input:  structured product dict
  Output: MCDA score breakdown + BUY/WAIT/INVESTIGATE
  Source: AGENTS.md policy applied inline
        |
Ranked output + verdict
Optional: write card to cards/laptops/
```

### Interaction Flow (from ADK personalized-shopping pattern)

```
Step 1: RECEIVE spec
        → if underspecified, ask ONE clarifying question, then proceed
Step 2: SEARCH
        → call search_web() with 2-3 targeted AU market queries
Step 3: EXTRACT
        → call extract_product() on top 3-5 results
Step 4: SCORE
        → apply policy gates from AGENTS.md (hard rejects first)
        → apply MCDA weights from procurement_policy.json
Step 5: RESPOND
        → ranked table + top recommendation + verdict
Step 6: OPTIONAL
        → write passing candidates as new cards to cards/laptops/
```

---

## Policy Gates (inherited from AGENTS.md — do not redefine here)

Apply in order. Hard rejects do not proceed to MCDA scoring:

| Gate | Type | Rule |
|---|---|---|
| Price | HARD REJECT | price_aud > 5000 |
| Stock | HARD REJECT | in_stock = False |
| VRAM floor | HARD REJECT | unified_memory_gb < 16 AND vram_gb < 8 |
| Thermal | SOFT PENALTY | Confirmed sustained throttling → -1 to -2 on Performance_Headroom |
| Toolchain | SOFT PENALTY | ROCm/AMD setup complexity → -1 on Track2_Avoidance |
| UNKNOWN track | FLAG | Neither unified_memory_gb nor vram_gb populated → flag, do not silently drop |

**Track classification:**
- **Track 1B**: `unified_memory_gb >= 16` (Apple Silicon M-series, AMD Strix Halo / Ryzen AI Max)
- **Track 1A**: `vram_gb >= 8` (discrete GPU laptops, NVIDIA RTX or AMD RDNA)
- **UNKNOWN**: Must be explicitly flagged in output

---

## Project Structure

```
/
├── AGENTS.md                       ← Policy authority (read-only)
├── CLAUDE.md                       ← CLI execution bounds (read-only)
├── config/
│   ├── procurement_policy.json     ← MCDA weights + budget caps (source of truth)
│   └── shortlist_schema.json       ← Column schema reference
├── agent/                          [NEW]
│   ├── agent.py                    ← ADK agent definition
│   ├── tools.py                    ← search_web, extract_product, score_candidate
│   ├── prompt.py                   ← System prompt derived from AGENTS.md
│   └── eval/
│       └── test_eval.py            ← tool_trajectory + response_match scoring
├── cards/
│   └── laptops/                    ← Agent writes new discovered cards here
├── docs/
│   ├── specs.md                    ← This file
│   └── ai_studio_vibe_code.md      ← AI Studio prototype prompting strategy
└── scratch/
    └── procurement_context_pack.xml ← Existing context pack (Perplexity / Claude)
```

---

## Code Style

All tool inputs and outputs use typed dicts. Agents and LLMs implementing this spec must match these schemas exactly:

```python
# Product dict — matches config/shortlist_schema.json
product = {
    "item_name": str,
    "price_aud": float | None,         # None = UNKNOWN → soft penalty
    "in_stock": bool,                   # False = hard reject
    "vram_gb": float | None,            # Discrete GPU VRAM
    "unified_memory_gb": float | None,  # Apple Silicon / Strix Halo
    "screen_size_in": float | None,
    "touchscreen": bool,
    "cpu_model": str,
    "retailer": str,                    # e.g. "JB_HI_FI", "SCORPTEC", "AMAZON_AU"
    "url": str,
    "date_checked": str,                # ISO 8601 e.g. "2026-06-12"
    "track": str,                       # "1A" | "1B" | "1.5" | "UNKNOWN"
}

# MCDA score output
score = {
    "candidate_id": str,
    "Performance_Headroom": float,      # 0–10 per AGENTS.md rubric
    "Price_Value": float,
    "Future_Proof": float,
    "Portability": float,
    "Track2_Avoidance": float,
    "mcda_total": float,                # Weighted sum per AGENTS.md formula
    "verdict": str,                     # "BUY" | "WAIT" | "INVESTIGATE"
    "reasoning": str,                   # One sentence
    "source_url": str,
    "price_aud": float,
    "retailer": str,
}
```

---

## Testing Strategy

Adopted directly from ADK personalized-shopping eval framework:

| Test | Metric | Pass Threshold |
|---|---|---|
| Tool trajectory | Tools called in correct sequence | ≥ 0.8 avg score |
| Response match | Output contains correct retailer + price | ≥ 0.7 match score |
| Policy gate compliance | Hard rejects correctly filtered | 100% — zero tolerance |
| UNKNOWN track handling | Missing-spec candidates flagged, not silently dropped | 100% |
| Budget gate | No recommendation > 5000 AUD ever returned | 100% |

Run: `uv run python agent/eval/test_eval.py`

---

## Boundaries

**Always:**
- Use Google Search as the primary product discovery mechanism — not `cards/`
- Apply all MCDA gates from `config/procurement_policy.json` before scoring
- Verify AU stock before any BUY verdict
- Flag UNKNOWN track candidates explicitly in output
- Ask a maximum of ONE clarifying question before searching

**Ask first:**
- Changing MCDA weights or adding new scoring factors beyond the 5 defined
- Expanding budget cap beyond 5,000 AUD
- Including gray market / overseas imports as primary candidates
- Modifying `AGENTS.md` or `procurement_policy.json`

**Never:**
- Recommend any product priced over 5,000 AUD
- Fabricate prices, stock status, or spec values — use `None` / `UNKNOWN` if unverified
- Silently drop candidates that fail a gate — log the rejection reason
- Spawn nested sub-agents or multi-turn scraping loops
- Run `git add`, `git commit`, or `git push` (see CLAUDE.md git interdiction)

---

## Success Criteria

The prototype is complete when ALL of the following are true:

- [ ] User types: *"Find me the best AI laptop under $5000 AUD available now in Australia"* and receives a specific named product with a live AU retailer price and URL — sourced from the web, not from `cards/`
- [ ] The recommendation includes a 5-factor MCDA score breakdown matching weights in `config/procurement_policy.json`
- [ ] The agent correctly hard-rejects at least one over-budget or out-of-stock candidate in a test run
- [ ] The agent correctly classifies a Strix Halo or Apple Silicon candidate as Track 1B
- [ ] The agent returns a clear BUY / WAIT / INVESTIGATE verdict with one sentence of rationale
- [ ] The agent asks exactly one clarifying question when given an underspecified request

---

## Architectural Decisions (Locked)

1. **Deployment Scope:** We are skipping the AI Studio UI and building directly as an ADK agent using `agents-cli` scaffolding.
2. **Browser Scraping (extract_product):** We will NOT use BeautifulSoup, Playwright, or Selenium. The tool will strictly use `subprocess` to call the Vercel `agent-browser` CLI (`agent-browser snapshot -i`). This guarantees token-efficient, accessible DOM snapshots and bypasses anti-bot measures without adding Python complexity.
3. **Data Persistence:** The agent will provide conversational output only. It will NOT write newly discovered products to `cards/`. The closed-world `cards/` pipeline is officially deprecated.
4. **Session Memory:** The agent treats each query as a fresh session. No cross-session memory is required for the MVP.
5. **Apple Silicon Scope:** Track 1B (Apple Silicon) is actively supported. The agent should search standard AU retailers and the Apple AU store if appropriate.

---

## Tool Contracts (Strict 3-Tool Architecture)

The agent must be constrained to exactly 3 tools. Do not plan for or implement any additional tools.

### 1. `search_web(query: str) -> str`
- **Purpose:** Finds live listings and prices across AU retailers.
- **Implementation:** Wrapper around a standard search API (e.g., Google Custom Search or Serper). Must include "site:.com.au" or "Australia" implicitly if the user forgets.

### 2. `extract_product(url: str) -> str`
- **Purpose:** Extracts hardware specs and live price from a specific retailer URL.
- **Implementation:** Must strictly use the `subprocess` module to call `@vercel/agent-browser` (via `npx -y github:vercel-labs/agent-browser`). 
- **Required Logic Flow:**
  1. `agent-browser open [url]`
  2. `agent-browser wait --load networkidle` (to ensure React/prices load)
  3. `agent-browser snapshot -i` (capture the token-efficient accessibility tree)
  4. `agent-browser close`
  5. Return the snapshot text.

### 3. `score_candidate(candidate_data: dict) -> dict`
- **Purpose:** Applies the 5-factor MCDA policy from `AGENTS.md`.
- **Implementation:** A pure Python function. Takes a dictionary of extracted specs, applies the weighting matrix (Performance, Price, Future Proof, Portability, Track2 Avoidance), and returns a structured breakdown (Score out of 10 for each, and a final BUY/WAIT/INVESTIGATE verdict).
- **Hard Constraints:** Must throw an immediate `Reject` exception or zero-score if the price > 5000 AUD or memory < 32GB (for Track 1B).
