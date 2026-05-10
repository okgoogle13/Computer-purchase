# Current State

**Last Updated:** 2026-05-11

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

## Current Leaderboard (Track 1)

1.  **MSI Raider GE68 HX 13V (RTX 4090)**
    - Score: **7.85**
    - Key Spec: **16GB VRAM (RTX 4090)**
    - Price: **$2,899.00**
    - Form Factor: 16" Performance Laptop

2.  **ASUS ProArt GoPro Edition PX13 HN7306EAC-LX044W (Strix Halo)**
    - Score: **7.6**
    - Key Spec: **128GB Unified Memory**
    - Effective Price: **$4,497.00** (Officeworks live listing checked 2026-05-11)
    - Form Factor: 13.3" 2-in-1 Flip Laptop

3.  **HP ZBook Ultra 14 G1a (Strix Halo)**
    - Score: **7.0**
    - Key Spec: **32GB Unified Memory**
    - Price: **$3,699.00**
    - Form Factor: 14" Traditional Laptop

4.  **ASUS ROG Flow Z13 (2026) GZ302EA**
    - Score: **6.8**
    - Key Spec: **32GB Unified Memory**
    - Price: **$4,499.00**
    - Form Factor: 13.4" Detachable Tablet

5.  **Lenovo Legion 9i Gen 10 (Lenovo Direct)**
    - Score: **6.5** (Adjusted with ~$4,300 effective price)
    - Key Spec: **16GB VRAM (RTX 5080) / 64GB RAM**
    - Price: **$4,300.00** (Effective via EDU + TopCashback)
    - Form Factor: 18" Desktop Replacement

## Top Track 2 Unicorn

- **HP Z2 Mini G1a AI (Strix Halo)**
  - Price: **$3,395.00**
  - Key Spec: **32GB Unified (Expandable to 128GB)**
  - Use Case: Maximum non-portable value.

## Immediate Work

1. Execute Secondary-Market Laptop Discovery Pass (Alienware, 12GB+ floor, $5k cap).
2. Regenerate the shortlist using the updated policy config.
3. Enrich live pricing for viable Track 1 candidates first.
4. Fill MCDA factor scores only after price, AU stock, warranty, and thermal evidence are checked.
5. Run the MCDA ranking engine and recommend the highest-ranked GOOD_ENOUGH candidate.
6. Apply Track Escalation Rule only if no Track 1 candidate clears gates or a verified Track 2 unicorn appears.

## Deferred

- Track 2 Pathway A/B/C build-out is deferred until a trigger fires.
- Apple Silicon remains out of scope unless the user explicitly reopens it.
- Archive and historical research files should not be treated as active policy.
