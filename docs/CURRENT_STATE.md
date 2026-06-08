# Current State

**Last Updated:** 2026-06-08

## Agent Tooling (New)

- **`scripts/agents/spec_clarifier/`** — Phase 0 conversational intake agent (ADK pattern, `gemini-2.5-flash`). Run before `build_shortlist.py` to interactively clarify track, VRAM floor, budget, and portability requirements. Outputs structured JSON; pass to shortlist via `--spec-json`. No external services required.

## Decision Frame

The repository now uses the simplified CareerCopilot hardware policy in `AGENTS.md`.

Primary objective:

- Buy one Track 1 laptop that helps ship CareerCopilot MVP in Q3 2026.
- Prefer enough headroom for Q4 2026 advanced features.
- Defer Track 2 unless no viable Track 1 candidate exists or a verified Track 2 unicorn is immediately available.

## Active Policy

- Track 1 budget cap: 5,000 AUD.
- Track 1A discrete laptop floor: 12 GB VRAM (Discovery) / 16 GB VRAM (Preferred).
- Track 1B Strix Halo floor: 16 GB unified memory.
- Track 1.5 desktop alternative floor: 16 GB VRAM.
- Track 2 is trigger-based, not a default buying lane.

## Active Scoring

Final decisions use fixed-weight MCDA:

- Performance_Headroom: 25%
- Price_Value: 20%
- Future_Proof: 20%
- Portability: 20%
- Track2_Avoidance: 15%

Strix Halo calibration now applies:

- Unified memory is a capacity advantage, not automatic parity with high-VRAM discrete GPU throughput.
- Default Strix Halo caps: `Performance_Headroom <= 7`; `Track2_Avoidance` capped by memory tier unless benchmark evidence supports higher.

## Current Leaderboard (Track 1 - Laptops)

All listed candidates are confirmed **GOOD_ENOUGH** (AU stock verified, price within cap, acceptable warranty and thermals):

1. **ASUS ROG Flow Z13 (2025) (Strix Halo)**
   - Score: **7.00**
   - Key Spec: **32GB Unified Memory**
   - Price: **$4,499.00** (ASUS Store AU verified)
   - Form Factor: 13.4" Detachable Tablet (Track 1B)

2. **ASUS ProArt GoPro Edition PX13 HN7306EAC-LX044W (Strix Halo)**
   - Score: **6.86** (Adjusted from 7.00)
   - Key Spec: **128GB Unified Memory**
   - Price: **$4,799.00** (PLE Computers verified)
   - Form Factor: 13.3" 2-in-1 Flip Laptop (Track 1B)

3. **Lenovo Legion Pro 7i Gen 10 16 (83F5XA01AU)**
   - Score: **6.80**
   - Key Spec: **16GB VRAM (RTX 5080)**
   - Price: **$3,827.45** (Lenovo Outlet AU Certified Refurbished)
   - Form Factor: 16" Performance Laptop (Track 1A)

4. **HP OMEN MAX 16-ah0013TX**
   - Score: **6.80**
   - Key Spec: **16GB VRAM (RTX 5080)**
   - Price: **$3,799.00** (HP Australia + student discount verified)
   - Form Factor: 16" Traditional Laptop (Track 1A)

5. **MSI VECTOR GP78 HX 14V**
   - Score: **6.46** (Adjusted from 6.80 due to seller risk)
   - Key Spec: **16GB VRAM (RTX 4090)**
   - Price: **$2,499.00** (MikePC AU Refurbished / Ex-demo)
   - Form Factor: 17.3" Gaming Laptop (Track 1A)

6. **Lenovo Legion Pro 7i Gen 10 16 (83F5X003R1)**
   - Score: **5.65**
   - Key Spec: **12GB VRAM (RTX 5070 Ti)**
   - Price: **$3,288.45** (Lenovo Outlet AU Certified Refurbished)
   - Form Factor: 16" Performance Laptop (Track 1A)

7. **MSI Raider 18HX AI A2XWIG (Refurbished)**
   - Score: **5.51** (Adjusted from 5.80)
   - Key Spec: **16GB VRAM (RTX 5080)**
   - Price: **$4,699.00** (JW Computers Refurbished)
   - Form Factor: 18" Desktop Replacement (Track 1A)

## Top Track 1.5 Option (Desktop Alternative)

- **Alienware Aurora R12 (Refurbished)**
  - Score: **6.80**
  - Key Spec: **24GB VRAM (RTX 3090)**
  - Price: **$3,884.00** (Refurbished AU stock verified)
  - Form Factor: Refurbished Prebuilt Desktop (Track 1.5)

## Top Track 2 Workstations (MCDA Scored)

These options represent maximum non-portable VRAM capability under the workstation research lane:

1. **Dell Precision T7910 (Refurbished Base)**
   - Score: **7.80**
   - Key Spec: **24GB VRAM (RTX 3090)**
   - Price: **$1,875.00** (Refurbished)
   - Form Factor: Enterprise Desktop Workstation (Pathway B)

2. **Dell Precision 5820 Tower Workstation (32GB RAM)**
   - Score: **7.60**
   - Key Spec: **24GB VRAM (RTX 3090)**
   - Price: **$2,399.00** (Refurbished)
   - Form Factor: Enterprise Desktop Workstation (Pathway B)

3. **Dell Precision 5820 Tower Bundle / Recompute Tower + ACT ThinkPad**
   - Score: **7.00**
   - Key Spec: **24GB VRAM (RTX 3090)**
   - Price: **$3,558.00** (Refurbished)
   - Form Factor: Enterprise Desktop Workstation Bundle (Pathway B)

## Immediate Work

1. Complete purchase transaction of the selected Track 1 leader (ASUS ROG Flow Z13 or Lenovo Legion Pro 7i RTX 5080) depending on portability preference.
2. Regenerate the shortlist once new batches are received.
3. Keep all VRAM and price checking evidence synced under `/cards/` directory.

## Deferred

- Pathway A custom workstation integration remains deferred until MVP revenue fires.
- Apple Silicon remains out of scope.
- Archive and historical research files should not be treated as active policy.

