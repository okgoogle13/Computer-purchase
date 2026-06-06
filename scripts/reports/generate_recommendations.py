#!/usr/bin/env python3
"""
Generate a human-readable recommendations report from a ranked shortlist CSV.

The report satisfies the AGENTS.md recommendation format requirements, including:
  - Per-candidate buy/wait/do-not-buy verdict
  - MCDA factor scores
  - Track / pathway / GOOD ENOUGH status
  - Retailer, price, stock, and date metadata
  - Risk heat map, battery transparency, platform comparison, policy failures

Usage:
  python scripts/reports/generate_recommendations.py \\
    --input shortlists/shortlist_2026-06-06_ranked.csv \\
    --output reports/recommendations_2026-06-06.md
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
from collections import Counter, defaultdict
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate AGENTS.md-compliant recommendations report from ranked shortlist CSV."
    )
    parser.add_argument("--input", required=True, help="Ranked shortlist CSV")
    parser.add_argument("--output", required=True, help="Output markdown report path")
    return parser.parse_args()


def to_float(v: object, default: float = 0.0) -> float:
    try:
        return float(v)  # type: ignore[arg-type]
    except Exception:
        return default


def read_rows(path: Path) -> list[dict]:
    try:
        with path.open(newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except Exception as exc:
        raise SystemExit(f"[error] Could not read CSV {path}: {exc}") from exc


def top_candidates(rows: list[dict], limit: int = 3) -> tuple[list[dict], list[dict]]:
    passed = [r for r in rows if str(r.get("Policy_Status", "")).upper() == "GOOD_ENOUGH"]
    passed.sort(key=lambda r: to_float(r.get("Adjusted_MCDA_Total")), reverse=True)
    return passed[:limit], passed


def platform_summary(rows: list[dict]) -> Counter:
    return Counter(r.get("source_platform", "UNKNOWN") for r in rows)


def risk_heat(rows: list[dict]) -> dict[str, list[str]]:
    flags: dict[str, list[str]] = defaultdict(list)
    for r in rows:
        key = r.get("item_name") or "unknown"
        for flag in str(r.get("risk_flags", "")).split(";"):
            flag = flag.strip()
            if flag:
                flags[key].append(flag)
    return flags


def battery_summary(rows: list[dict]) -> tuple[int, int]:
    disclosed = [r for r in rows if str(r.get("battery_disclosure_level", "none")) != "none"]
    return len(disclosed), len(rows)


def render_table(rows: list[dict]) -> str:
    headers = [
        "item_name", "source_platform", "Adjusted_MCDA_Total",
        "Performance_Headroom", "Price_Value", "Future_Proof",
        "Portability", "Track2_Avoidance",
        "score_acquisition_risk", "risk_adjusted_price", "Policy_Status",
    ]
    lines = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join(["---"] * len(headers)) + "|",
    ]
    for r in rows:
        lines.append("| " + " | ".join(str(r.get(h, "")) for h in headers) + " |")
    return "\n".join(lines)


# FIX H2: AGENTS.md-compliant verdict determination
def determine_verdict(r: dict) -> str:
    status = str(r.get("Policy_Status", "")).upper()
    if status != "GOOD_ENOUGH":
        return "DO-NOT-BUY"
    stock = str(r.get("in_stock_now", "") or r.get("au_stock", "")).lower()
    if stock in ("false", "no", "out_of_stock", "unavailable", ""):
        return "WAIT — stock unconfirmed"
    score = to_float(r.get("Adjusted_MCDA_Total"))
    return "BUY" if score >= 5.0 else "WAIT — score below threshold"


# FIX H2: MCDA factor score block per AGENTS.md recommendation format
def render_candidate_block(i: int, r: dict) -> str:
    verdict = determine_verdict(r)
    track = r.get("track") or "UNKNOWN"
    pathway = r.get("pathway") or "UNKNOWN"
    good_enough = r.get("Policy_Status") or "UNKNOWN"
    retailer = r.get("current_best_retailer") or r.get("retailer") or "UNKNOWN"
    url = r.get("current_best_url") or r.get("url") or ""
    price = r.get("effective_best_price_aud") or r.get("price_aud") or "UNKNOWN"
    stock = r.get("in_stock_now") or r.get("au_stock") or "UNKNOWN"
    checked_at = r.get("pricing_checked_at") or "UNKNOWN"

    lines = [
        f"### {i}. {r.get('item_name', 'Unknown')}",
        "",
        f"- **Track / Pathway:** Track {track} (Pathway {pathway})",
        f"- **GOOD ENOUGH:** {good_enough}",
        (
            f"- **MCDA Score:** {r.get('Adjusted_MCDA_Total', '')}  "
            f"(Perf: {r.get('Performance_Headroom', '')}, "
            f"Value: {r.get('Price_Value', '')}, "
            f"Future: {r.get('Future_Proof', '')}, "
            f"Port: {r.get('Portability', '')}, "
            f"T2-Avoid: {r.get('Track2_Avoidance', '')})"
        ),
        f"- **Price:** ${price} AUD · Retailer: {retailer}",
        f"- **Stock:** {stock} · Checked: {checked_at}",
        f"- **URL:** {url}",
        f"- **Acquisition Risk Score:** {r.get('score_acquisition_risk', '')}",
        f"- **Battery Disclosure:** {r.get('battery_disclosure_level', 'none')}",
        f"- **Risk Flags:** {r.get('risk_flags', 'none')}",
        "",
        f"> **Verdict: {verdict}**",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        print(f"[error] Input CSV {input_path} does not exist.")
        return

    rows = read_rows(input_path)
    top3, passed = top_candidates(rows, 3)
    platform_counts = platform_summary(rows)
    risks = risk_heat(rows)
    disclosed, total = battery_summary(rows)
    policy_fails = [r for r in rows if str(r.get("Policy_Status", "")).upper() == "NEEDS_REVIEW"]

    # FIX L1: report header now includes generation timestamp
    generated_at = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    md = [
        f"# Recommendations Report",
        f"**Generated:** {generated_at}  ",
        f"**Total candidates evaluated:** {len(rows)}  ",
        f"**PASS:** {len(passed)}  ",
        f"**NEEDS_REVIEW:** {len(policy_fails)}",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
    ]

    if top3:
        for i, r in enumerate(top3, 1):
            md.append(
                f"{i}. **{r.get('item_name', 'Unknown')}** — "
                f"score {r.get('Adjusted_MCDA_Total', '')}, "
                f"acquisition risk {r.get('score_acquisition_risk', '')}, "
                f"source {r.get('source_platform', '')}, "
                f"battery disclosure: {r.get('battery_disclosure_level', '') or 'none'}. "
                f"**Verdict: {determine_verdict(r)}**"
            )
    else:
        md.append("No GOOD_ENOUGH candidates were found in the ranked shortlist.")

    # FIX H2: per-candidate AGENTS.md-compliant blocks
    md.extend(["", "## Buy Recommendations", ""])
    if top3:
        for i, r in enumerate(top3, 1):
            md.append(render_candidate_block(i, r))
    else:
        md.append(
            "> No candidates passed all gates. "
            "Re-check stock, broaden sources, or relax one policy threshold tier and re-score."
        )

    md.extend([
        "",
        "## Ranked Table",
        "",
        render_table(passed if passed else rows[:10]),
        "",
        "## Risk Heat Map",
        "",
    ])

    if risks:
        for item, item_flags in risks.items():
            md.append(f"- **{item}**: {', '.join(item_flags)}")
    else:
        md.append("- No risk flags found.")

    md.extend([
        "",
        "## Battery Health Transparency",
        "",
        f"- Listings with battery disclosure: {disclosed}/{total}",
        f"- Listings without battery disclosure: {max(total - disclosed, 0)}/{total}",
        "",
        "## Platform Comparison",
        "",
    ])

    for source, count in sorted(platform_counts.items()):
        md.append(f"- **{source}**: {count} rows")

    md.extend(["", "## Policy Failures / Blockers", ""])
    if policy_fails:
        # Show top 20 policy failures to keep report readable
        for r in policy_fails[:20]:
            blockers = r.get("Policy_Blockers") or "unspecified"
            md.append(f"- **{r.get('item_name', 'Unknown')}** — blockers: {blockers}")
        if len(policy_fails) > 20:
            md.append(f"- ... and {len(policy_fails) - 20} more candidates needing review.")
    else:
        md.append("- No policy failures.")

    md.extend(["", "## Recommended Next Actions", ""])
    if top3:
        for r in top3:
            verdict = determine_verdict(r)
            md.append(
                f"- **{r.get('item_name', 'Unknown')}** ({verdict}): "
                f"verify seller terms, battery evidence, and OEM specs for GPU/TB support "
                f"before purchase. Confirm live AU stock at retailer URL above."
            )
    else:
        md.append(
            "- Broaden collection sources (Gumtree, Facebook HAR, eBay) or "
            "relax one policy threshold tier and re-score."
        )

    output_path.write_text("\n".join(md).strip() + "\n", encoding="utf-8")
    print(f"[done] report generated: {output_path}")


if __name__ == "__main__":
    main()
