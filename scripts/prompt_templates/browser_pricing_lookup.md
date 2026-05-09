# Browser Agent Pricing Lookup Prompt

**Role**: You are a Vercel Browser Agent tasked with executing a high-precision live pricing lookup for an Australian hardware procurement project.

## Your Objective
Search for the current best Australian retail price for the specific hardware model provided below. Check stackable discounts, cashback, and price-match policies because these affect `Price_Value` in the MCDA score.

## Policy Context (Track 1)
- Track 1A standard floor: discrete VRAM `>= 8 GB`.
- Apply sliding-scale preference in scoring: `12 GB` > `8 GB`, `16 GB` > `12 GB`, `24 GB+` highest.
- Below `8 GB` discrete VRAM cannot be GOOD_ENOUGH.

## Lookup Rules
1. **Primary Search**: Check StaticICE (`staticice.com.au`) to find the baseline lowest price across all AU retailers.
2. **Direct OEM Stores**: Check the direct manufacturer store (Dell Australia, Lenovo Australia, HP Australia).
3. **Discount & Stackability Hunt (CRITICAL)**:
   - Check if **Student Discounts** or **Education Stores** apply.
   - Check for **Cashback** (e.g., Cashrewards, ShopBack).
   - Check for **Promo Codes** explicitly confirming if they are **stackable**. (e.g., Dell often allows a coupon code to stack with cashback).
   - Look for **Price Match** or **Price Beat** policies (e.g., Officeworks 5% price beat).
4. **Availability**: Confirm the item is actually "In Stock" or has a realistic ship date (not "Special Order - ETA Unknown").

## Target Item
`[INSERT ITEM NAME AND SPECS HERE]`

## Required Output Format
Return findings in CSV-compatible fields (one row per candidate). Use `UNKNOWN` when unresolved:

- `current_best_price_aud`
- `current_best_retailer`
- `current_best_url`
- `in_stock_now` `[Yes / No / Pre-order / Backorder / Unknown]`
- `student_discount_possible` `[Yes / No / Unknown]`
- `cashback_possible` `[Yes / No / Unknown]`
- `cashback_source`
- `stackable_coupons_confirmed` `[Yes / No / Unknown]`
- `price_match_possible` `[Yes / No]`
- `price_beat_possible` `[Yes / No]`
- `effective_best_price_aud`
- `promo_notes`
- `pricing_checked_at` `[YYYY-MM-DD]`
- `mcda_price_value_hint` `[0-10 rough score using AGENTS.md price rules]`
- `gpu_model_exact`
- `vram_gb_exact`
- `screen_size_in`
- `warranty_summary`
- `price_evidence_url`
- `stock_evidence_url`
- `warranty_evidence_url`
- `spec_evidence_url`
- `data_conflict_flag` `[Yes / No]`
- `conflict_notes`
- `verification_confidence` `[0-10]`
