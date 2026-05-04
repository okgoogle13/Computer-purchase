# ChatGPT Agent Mode — AU Laptop Research Prompt
# Purpose: Use browser control to collect AU retailer data for the 4 RTX 5090 laptop targets.
# Output will be pasted directly into the repo card shells and CSV by the local agent.
# Generated: 2026-05-03

---

## PROMPT (paste this into ChatGPT Agent Mode / Computer Use)

```
You are a hardware research agent with browser control.

Your job is to collect Australian retailer data for 4 specific laptop models and return it in a structured format I can paste directly into my repo files.

---

## TASK

Search Australian retailer websites for each of the 4 laptops below.
For each laptop, visit at least 2 AU retailer pages and collect the exact fields listed.

Do NOT guess or infer values. If a field is not listed on the retailer page, write UNKNOWN.

---

## LAPTOPS TO RESEARCH

1. ASUS ROG Strix Scar 18 (2025) with RTX 5090 Laptop GPU
2. Lenovo Legion 9i Gen 10 18" with RTX 5090 Laptop GPU
3. MSI Raider A18 HX with RTX 5090 Laptop GPU
4. MSI Titan (any 2025 18" variant) with RTX 5090 Laptop GPU
   - Note: confirm exact model name (e.g. Titan GT77 HX, Titan 18 HX, etc.)

---

## AU RETAILERS TO CHECK (in order of preference)

- JB Hi-Fi: https://www.jbhifi.com.au
- Centre Com: https://www.centrecom.com.au
- Scorptec: https://www.scorptec.com.au
- Affordable Laptops: https://www.affordablelaptops.com.au
- PLE Computers: https://www.ple.com.au
- ASUS AU store: https://rog.asus.com/au/laptops/
- Lenovo AU store: https://www.lenovo.com/au/en/laptops/legion-laptops/
- MSI AU store: https://au.msi.com/Laptops

---

## FIELDS TO COLLECT FOR EACH LAPTOP

For each laptop, collect ALL of the following. Write UNKNOWN if not found on the page.

1.  Retailer name
2.  Retailer URL (direct product page URL)
3.  In stock right now? (Yes / No / Check store)
4.  Price (AUD, inc. GST — exact listed price)
5.  Exact model name / SKU as shown on the retailer page
6.  GPU confirmed (e.g. "RTX 5090 Laptop GPU, 24 GB GDDR7")
7.  CPU model (e.g. "Intel Core i9-14900HX")
8.  RAM installed (e.g. "32 GB DDR5")
9.  RAM max supported (e.g. "64 GB")
10. Free RAM slots (count — how many slots are empty)
11. SSD installed (e.g. "2 TB NVMe")
12. Free M.2 slots (count — how many are empty)
13. Charger / PSU wattage (e.g. "330 W")
14. Weight (kg)
15. Warranty — term (e.g. "2 years")
16. Warranty — type (e.g. "carry-in", "onsite", "depot")
17. Panel type (e.g. "QHD IPS 240 Hz", "OLED", "MiniLED")
18. Sustained TGP in watts — check the product spec sheet or any linked review. If listed as a range (e.g. "150 W – 175 W"), capture both values.
19. Thermal flag — note any mention of "runs hot", "throttles", "excellent thermals", etc. from the retailer page or a pinned review link.

---

## OUTPUT FORMAT

Return a separate block for each laptop using exactly this format.
Use the field names exactly as shown — they map directly to my repo files.

---

### LAPTOP 1: ASUS ROG Strix Scar 18 (2025) RTX 5090
<!-- Maps to: NotebookLM_Workspaces/Laptops/30_asus-rog-strix-scar-18-rtx-5090-2025.md -->
<!-- CSV row: ASUS_ROG_Scar18_2025_RTX5090_24GB in laptop_candidates.csv -->

- Retailer name: 
- Retailer URL: 
- In stock: 
- Price (AUD): 
- Exact model name / SKU: 
- GPU confirmed: 
- CPU: 
- RAM installed: 
- RAM max supported: 
- Free RAM slots: 
- SSD installed: 
- Free M.2 slots: 
- Charger wattage: 
- Weight: 
- Warranty term: 
- Warranty type: 
- Panel type: 
- Sustained TGP: 
- Thermal flag: 

---

### LAPTOP 2: Lenovo Legion 9i Gen 10 18" RTX 5090
<!-- Maps to: NotebookLM_Workspaces/Laptops/31_lenovo-legion-9i-18-rtx-5090.md -->
<!-- CSV row: Lenovo_Legion_Pro9i_RTX5090_24GB in laptop_candidates.csv -->

- Retailer name: 
- Retailer URL: 
- In stock: 
- Price (AUD): 
- Exact model name / SKU: 
- GPU confirmed: 
- CPU: 
- RAM installed: 
- RAM max supported: 
- Free RAM slots: 
- SSD installed: 
- Free M.2 slots: 
- Charger wattage: 
- Weight: 
- Warranty term: 
- Warranty type: 
- Panel type: 
- Sustained TGP: 
- Thermal flag: 

---

### LAPTOP 3: MSI Raider A18 HX RTX 5090
<!-- Maps to: NotebookLM_Workspaces/Laptops/32_msi-raider-a18-hx-rtx-5090.md -->
<!-- CSV row: MSI_Raider_A18_HX_RTX5090_24GB in laptop_candidates.csv -->

- Retailer name: 
- Retailer URL: 
- In stock: 
- Price (AUD): 
- Exact model name / SKU: 
- GPU confirmed: 
- CPU: 
- RAM installed: 
- RAM max supported: 
- Free RAM slots: 
- SSD installed: 
- Free M.2 slots: 
- Charger wattage: 
- Weight: 
- Warranty term: 
- Warranty type: 
- Panel type: 
- Sustained TGP: 
- Thermal flag: 

---

### LAPTOP 4: MSI Titan (2025, 18") RTX 5090
<!-- Maps to: NotebookLM_Workspaces/Laptops/33_msi-titan-rtx-5090.md -->
<!-- CSV row: MSI_Titan_GT77_RTX5090_24GB in laptop_candidates.csv -->

- Retailer name: 
- Retailer URL: 
- In stock: 
- Price (AUD): 
- Exact model name / SKU:          ← IMPORTANT: confirm exact Titan variant name here
- GPU confirmed: 
- CPU: 
- RAM installed: 
- RAM max supported: 
- Free RAM slots: 
- SSD installed: 
- Free M.2 slots: 
- Charger wattage: 
- Weight: 
- Warranty term: 
- Warranty type: 
- Panel type: 
- Sustained TGP: 
- Thermal flag: 

---

## ADDITIONAL NOTES

- Budget cap for this purchase is AUD 4,000. Flag with "⚠️ OVER BUDGET" if price exceeds this.
- Preferred sweet spot is AUD 2,500–3,500. Flag with "✅ IN SWEET SPOT" if in this range.
- If any laptop is completely unavailable in AU (no stock, no listing), write: "NOT LISTED IN AU — checked [retailer names]"
- If you find multiple configurations for the same chassis (e.g. 32 GB vs 64 GB RAM), return BOTH rows using the same format, labelled as CONFIG A and CONFIG B.
- Do not return summaries or recommendations — raw field data only. The local scoring engine handles ranking.

---

## AFTER COLLECTING ALL DATA

At the end, add a one-line stock summary:

STOCK SUMMARY:
- ASUS Scar 18 5090: [In stock at X / Not listed / Price only]
- Legion 9i 18 5090: [In stock at X / Not listed / Price only]
- MSI Raider A18 HX 5090: [In stock at X / Not listed / Price only]
- MSI Titan 5090: [In stock at X / Not listed / Price only — confirm model name]
```
