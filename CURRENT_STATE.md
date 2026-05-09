# Current State

**Last Updated:** 2026-05-09

## Decision Frame

The repository now uses the simplified CareerCopilot hardware policy in `AGENTS.md`.

Primary objective:

- Buy one Track 1 laptop that helps ship CareerCopilot MVP in Q3 2026.
- Prefer enough headroom for Q4 2026 advanced features.
- Defer Track 2 unless no viable Track 1 candidate exists or a verified Track 2 unicorn is immediately available.

## Active Policy

- Track 1 budget cap: 5,000 AUD.
- Track 1A discrete laptop floor: 16 GB VRAM.
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

## Current Leaderboard (Track 1)

1.  **ASUS ProArt PX13 HN6306 (Strix Halo)**
    - Score: **10.0**
    - Key Spec: **128GB Unified Memory**
    - Effective Price: **$4,319.10** (JB Hi-Fi + 10% Student Discount)
    - Form Factor: 13.3" 2-in-1 Flip Laptop

2.  **ASUS ROG Flow Z13 (2026) GZ302EA**
    - Score: **9.2**
    - Key Spec: **32GB Unified Memory**
    - Price: **$3,824.00**
    - Form Factor: 13.4" Detachable Tablet

3.  **HP ZBook Ultra 14 G1a (Strix Halo)**
    - Score: **8.9**
    - Key Spec: **32GB Unified Memory**
    - Price: **$4,200.00**
    - Form Factor: 14" Traditional Laptop

4.  **Lenovo Legion 9i Gen 10 (Lenovo Direct)**
    - Score: **6.5** (Adjusted with ~$4,300 effective price)
    - Key Spec: **16GB VRAM (RTX 5080) / 64GB RAM**
    - Price: **$4,300.00** (Effective via EDU + TopCashback)
    - Form Factor: 18" Desktop Replacement

5.  **MSI Raider GE68 HX 13V (RTX 4090)**
    - Score: **7.85**
    - Key Spec: **16GB VRAM (RTX 4090)**
    - Price: **$2,899.00**
    - Form Factor: 16" Performance Laptop

## Top Track 2 Unicorn

- **HP Z2 Mini G1a AI (Strix Halo)**
  - Price: **$3,395.00**
  - Key Spec: **32GB Unified (Expandable to 128GB)**
  - Use Case: Maximum non-portable value.

## Immediate Work

1. Regenerate the shortlist using the updated policy config.
2. Enrich live pricing for viable Track 1 candidates first.
3. Fill MCDA factor scores only after price, AU stock, warranty, and thermal evidence are checked.
4. Run the MCDA ranking engine and recommend the highest-ranked GOOD_ENOUGH candidate.
5. Apply Track Escalation Rule only if no Track 1 candidate clears gates or a verified Track 2 unicorn appears.

## Deferred

- Track 2 Pathway A/B/C build-out is deferred until a trigger fires.
- Apple Silicon remains out of scope unless the user explicitly reopens it.
- Archive and historical research files should not be treated as active policy.
