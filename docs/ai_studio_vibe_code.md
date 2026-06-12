# AI Studio Vibe Code: Prototype Prompting Strategy

## Purpose

This document is a step-by-step prompting guide to build a working prototype of the open-world hardware procurement agent using **Google AI Studio Build**, with zero infrastructure setup. Each prompt is a complete message — paste it verbatim into AI Studio.

The goal is a working conversational agent in under 30 minutes.

---

## Pre-Flight Setup (2 minutes)

1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click **Build** → **New App**
3. Model: `Gemini 2.0 Flash` (fast, cheap, good at search)
4. In the right panel, enable **Google Search** as a tool ← critical step
5. You are now ready.

---

## PROMPT 1 — Establish Persona & Policy

Paste this as the **System Prompt** (not a chat message):

```
You are an AI hardware procurement assistant for the Australian market.

Your job is to help me find and buy the best AI-capable laptop available now in Australia, under a strict 5,000 AUD budget.

## Decision Authority
Follow these rules in this exact priority order:
1. Budget cap: NEVER recommend anything over 5,000 AUD (hard reject)
2. AU stock: Only recommend products currently in stock at an Australian retailer (hard reject)
3. Memory floor: Must have at least 32GB unified memory OR 8GB discrete VRAM (hard reject)
4. Preferred track: Track 1B (unified memory ≥ 32GB — Apple Silicon M-series or AMD Strix Halo / Ryzen AI Max) is preferred over Track 1A (discrete GPU)

## Approved AU Retailers (search these in priority order)
1. JB Hi-Fi (jbhifi.com.au)
2. Scorptec (scorptec.com.au)
3. MSY Technology (msy.com.au)
4. Amazon Australia (amazon.com.au)
5. eBay Australia (ebay.com.au)

## Interaction Rules
- If my request is underspecified, ask exactly ONE clarifying question, then search
- Always search the web before answering — do not guess prices or stock
- Never fabricate specs, prices, or availability — say UNKNOWN if you cannot verify

## Output Format
When presenting a recommendation, always include:
- Product name + retailer + live price in AUD + URL
- Track classification (1A or 1B)
- One sentence verdict: BUY / WAIT / INVESTIGATE and why
```

**Verification:** The system prompt is set. Move to Prompt 2.

---

## PROMPT 2 — First Live Search Test

Type this as your first chat message:

```
Find me the best AI development laptop available right now in Australia under $5000 AUD. I run Python, local LLMs, and I'm already on macOS.
```

**What to look for in the response:**
- ✅ Agent calls Google Search (you will see search queries appear)
- ✅ Returns a specific named product with a price ending in AUD
- ✅ Includes a retailer name and a URL
- ✅ Does NOT hallucinate a price — it should come from a live search result
- ❌ If it returns a generic answer without searching, check that Google Search tool is enabled

---

## PROMPT 3 — Add MCDA Scoring Structure

Once Prompt 2 works, update the **System Prompt** by adding this section at the bottom:

```
## Scoring (MCDA)
When comparing candidates, score each factor 0–10 and calculate a weighted total:

| Factor               | Weight |
|----------------------|--------|
| Performance Headroom | 25%    |
| Price vs Value       | 20%    |
| Future Proof         | 20%    |
| Portability          | 20%    |
| Track 2 Avoidance    | 15%    |

TOTAL = (PH × 0.25) + (PV × 0.20) + (FP × 0.20) + (Port × 0.20) + (T2A × 0.15)

Scoring rubric:
- Performance Headroom: 6–7 for 16GB unified / 16GB VRAM, 8–10 for 32GB+ unified or 24GB+ VRAM
- Future Proof: 6–7 for 16GB, 8–10 for 32GB+ unified or 24GB+ VRAM
- Portability: 10 for thin-and-light, 7–8 for standard 14–16", 4–6 for heavy desktop replacements
- Track 2 Avoidance: 7 for 64GB unified, 5–6 for 32–48GB, 8 for 128GB unified
- Price vs Value: 10 for excellent deal vs alternatives, 5 for fair market rate, 0 for at budget cap with weak specs

Always show the full score table when making a recommendation.
```

Then re-run:
```
Find me the top 2 AI laptops under $5000 AUD available now in Australia, with full MCDA scores for each.
```

**What to look for:**
- ✅ A table with 5 factor scores and a weighted total for each candidate
- ✅ A BUY / WAIT / INVESTIGATE verdict with reasoning
- ✅ Track classification for each (1A or 1B)

---

## PROMPT 4 — Stress Test: Policy Gates

Test that the agent correctly applies hard rejects:

```
What about the ASUS ROG Zephyrus G16 with RTX 4060? Is it a good option?
```

**What to look for:**
- ✅ Agent searches for current AU price
- ✅ If price > $5000, agent should say "hard reject — over budget"
- ✅ If VRAM is 8GB, agent should classify as Track 1A (not preferred)
- ✅ Agent should NOT recommend it as BUY if it fails a gate
- ❌ If agent says "great option!" without checking price — the policy gates are not working

Then test an out-of-stock rejection:
```
Check if the ASUS ProArt Studiobook 16 with HX 370 is available in Australia right now.
```

---

## PROMPT 5 — Test Open-World Discovery

This is the core test — asking about a product NOT in the existing cards/:

```
Are there any new Strix Halo laptops with 64GB or 128GB unified memory available in Australia? What are the prices?
```

**What to look for:**
- ✅ Agent searches for this specific product category
- ✅ Returns models and prices it found via search, not from memory
- ✅ If it finds one in AU stock, classifies it Track 1B with high Track2_Avoidance score
- ✅ If none available, says "none confirmed in AU stock" — does not hallucinate availability
- ❌ If it answers from training data without searching — the Google Search tool is not working

---

## PROMPT 6 — Final Recommendation Request

Once all previous prompts work, ask for the final recommendation:

```
Based on everything you've found today, give me your top recommendation. Format it as:

**RECOMMENDED: [Product Name]**
- Retailer: [name + URL]
- Price: [AUD]
- Track: [1A or 1B]
- MCDA Score: [total]/10
  - Performance Headroom: [X]/10
  - Price vs Value: [X]/10
  - Future Proof: [X]/10
  - Portability: [X]/10
  - Track 2 Avoidance: [X]/10
- Verdict: [BUY / WAIT / INVESTIGATE]
- Reasoning: [one sentence]
- Checked: [today's date]
```

**Success:** If this returns a complete, structured output with real prices and URLs from AU retailers — the prototype works. The architecture is validated.

---

## Iteration Notes

### If the agent hallucinates prices
Add to system prompt: *"You MUST search the web before stating any price. If you cannot verify a price via search, say 'price unverified — check retailer directly'."*

### If the agent searches but gets irrelevant results
Refine the search instruction: *"When searching for AU prices, always include the terms 'Australia', 'AUD', and the current year in your search queries."*

### If the agent recommends over-budget products
Add to system prompt immediately after the budget rule: *"This is a HARD LIMIT. If a search result shows any price over 5000 AUD, do not include it in your recommendation. No exceptions."*

### If scores feel arbitrary
Add example calibration to the system prompt: *"Example: MacBook Pro M4 Max 48GB = Performance_Headroom 8, Future_Proof 8. Use this as your calibration anchor."*

---

## Graduating to ADK

Once the AI Studio prototype is validated, the agent structure maps directly to:

```python
# agent/agent.py
from google.adk.agents import Agent
from agent.tools import search_web, extract_product, score_candidate
from agent.prompt import SYSTEM_PROMPT

procurement_agent = Agent(
    name="procurement_agent",
    model="gemini-2.0-flash",
    instruction=SYSTEM_PROMPT,
    tools=[search_web, extract_product, score_candidate],
)
```

Each AI Studio system prompt section becomes a section in `agent/prompt.py`.
Each "what to look for" block becomes a test case in `agent/eval/test_eval.py`.

---

## Reference

- Full build spec: [specs.md](./specs.md)
- Policy authority: [AGENTS.md](../AGENTS.md)
- MCDA weights source: [config/procurement_policy.json](../config/procurement_policy.json)
- ADK pattern reference: [google/adk-samples personalized-shopping](https://github.com/google/adk-samples/tree/main/python/agents/personalized-shopping)
