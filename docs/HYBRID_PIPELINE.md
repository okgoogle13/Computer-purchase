# CareerCopilot Hardware Decision Engine: Hybrid Pipeline & MCDA Scoring

The CareerCopilot hardware decision engine is designed to ensure the MVP is shipped in Q3 2026, while preserving headroom for Q4 2026 advanced features, and minimizing overall acquisition risk.

---

## 7-Factor MCDA Model

To accurately reflect real-world hardware value and prevent risky purchasing decisions (e.g. untested secondary-market laptop listings with undisclosed battery health or import risk), the MCDA ranking engine uses a 7-factor model:

$$SCORE = \sum (Factor \times Weight)$$

### MCDA Weights

The weights are balanced to prioritize performance headroom while keeping risk and pricing in check:

| Factor | Weight | Description |
| :--- | :--- | :--- |
| **Performance_Headroom** | `0.20` | Local AI capacity/headroom for MVP and Q4. |
| **Price_Value** | `0.16` | Value based on risk-adjusted price vs budget. |
| **Future_Proof** | `0.16` | Runway/resale value, adjusted for age and platform risk. |
| **Portability** | `0.16` | Portability fit (laptops/field-work practicality). |
| **Track2_Avoidance** | `0.12` | Likelihood this purchase defers/avoids a Track 2 workstation. |
| **Upgrade_Ceiling** | `0.10` | Maximum potential ram/storage upgrade capacity. |
| **Acquisition_Risk** | `0.10` | Safety of the listing and transaction (higher = safer). |
| **Total** | `1.00` | Weights sum exactly to 1.0. |

---

## Acquisition Risk and Battery Health Scoring

Acquisition Risk evaluates the transaction's safety, warranty terms, and battery health. 

### 1. Battery Disclosure Level Scoring Table

Scores the transparency of battery health transparency in a listing (0.0 to 10.0 scale):

| Level | Score | Description |
| :--- | :--- | :--- |
| `tested_pct_cycles` | **10.0** | Capacity percentage AND cycle count both provided. |
| `replaced` | **9.0** | Seller explicitly states battery is new or recently replaced. |
| `tested_pct` | **8.0** | Capacity percentage provided but cycle count is missing. |
| `health_range_claim` | **6.0** | Estimated range given (e.g., "80-89% health"). |
| `vague_claim` | **3.0** | Non-specific claim (e.g., "holds charge well", "good battery"). |
| `none` | **1.0** | No battery information provided in the listing. |
| `sold_as_is` | **0.0** | Explicitly stated as untested, not guaranteed, or sold as-is. |

### 2. Battery Health Value Scoring Table

Scores actual battery health when quantified values exist:

- **Battery Replaced:** Returns **10.0** immediately.
- **Battery Health %:**
  - $\ge 95\%$ : **10.0**
  - $\ge 85\%$ : **8.0**
  - $\ge 75\%$ : **6.0**
  - $\ge 65\%$ : **4.0**
  - $\ge 55\%$ : **2.0**
  - $< 55\%$ : **0.0**
  - *Undisclosed/Missing*: Defaults to **3.0** (penalized, not zeroed).
- **Cycle Count Adjustments:**
  - $> 800$ cycles: Deduct **2.0** from health score (capped at minimum 0.0).
  - $> 500$ cycles: Deduct **1.0** from health score (capped at minimum 0.0).

Combined Battery Score Formula:
$$battery\_score = (battery\_disclosure\_score \times 0.5) + (battery\_health\_value\_score \times 0.5)$$

### 3. Seller Class Scores Table

Modifiers applied to the baseline Acquisition Risk score based on the source's professional tier:

| Seller Class | Modifier | Description |
| :--- | :--- | :--- |
| `commercial_oem` | **+3.0** | Official manufacturer AU stores or direct outlets. |
| `commercial_refurb` | **+2.0** | Professional refurbishing businesses. |
| `commercial_seller` | **+1.0** | Regular commercial store or business sellers. |
| `private` | **-1.5** | Individual private sellers (no commercial recourse). |
| `unknown` | **-1.0** | Unclassified seller tier. |

### 4. Age Penalty Table

Applied to the baseline Future_Proof score to penalize legacy generations:

- **Age $\le 1$ year** (2025–2026): **0.0** (No penalty)
- **Age $\le 3$ years** (2023–2024): **-0.5**
- **Age $\le 5$ years** (2021–2022): **-1.5**
- **Age $\le 7$ years** (2019–2020): **-2.5**
- **Age $> 7$ years** (Pre-2019): **-3.5**

### 5. Risk-Adjusted Price Formula

To represent the "true cost" of a listing (incorporating warranty, battery replacement, and transaction risk), the baseline `Price_Value` factor is calculated using a **risk-adjusted price**:

$$risk\_adjusted\_price = list\_price\_aud + shipping\_cost\_aud + \sum Premium\_Adjustments$$

Premium adjustments are added for the following risks:
- **Missing Battery Disclosure:** Add **$120 AUD** if disclosure level is `none` or `sold_as_is`.
- **No Warranty:** Add **$150 AUD** if `warranty_months == 0`.
- **Import Risk:** Add **$80 AUD** if `listing_country` is not `"AU"`.
- **No Recourse:** Add **$100 AUD** if `seller_class == "private"` and `returns_accepted` is False.

---

## Risk Flags and Triggers

During pipeline live verification, the following flags are appended to `risk_flags` automatically to alert decision-makers:

- `AGE_RISK_4YR+`: Triggered if manufacture year is older than 4 years (Age > 4).
- `PRIVATE_SELLER`: Triggered if seller class is `private`.
- `NO_WARRANTY`: Triggered if warranty duration is 0 months.
- `NO_RETURNS`: Triggered if returns are not accepted.
- `BATTERY_UNDISCLOSED`: Triggered if battery disclosure level is `none` or `sold_as_is`.
- `BATTERY_DEGRADED`: Triggered if battery health capacity is reported below 70%.
- `NON_AU_SELLER`: Triggered if listing country is not `"AU"`.
- `NEW_SELLER`: Triggered if seller feedback count is less than 10.
