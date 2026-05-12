import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.harvest_llm_recommendations import (
    _match_shortlist_row,
    dedupe_candidates,
    decide_action,
    extract_candidates_from_log,
    normalize_item_name,
)


def test_normalize_item_name_strips_parenthetical_noise_and_punctuation():
    assert (
        normalize_item_name('Lenovo Legion 9i Gen 10 18" RTX 5080 (eBay)')
        == "lenovo legion 9i gen 10 18 rtx 5080"
    )


def test_extract_candidates_from_log_parses_heading_vram_and_price():
    log_text = """
## Lenovo Legion 9i Gen 10 18\" RTX 5080 (eBay)
- GPU: 12GB
- Price: AUD $3000
""".strip()

    rows = extract_candidates_from_log(log_text)

    assert len(rows) == 1
    assert rows[0]["item_name"] == "lenovo legion 9i gen 10 18 rtx 5080"
    assert rows[0]["vram_gb"] == 12
    assert rows[0]["price_aud"] == 3000.0


def test_extract_candidates_ignores_non_product_heading():
    log_text = """
## Market Summary
- Price: AUD $3000
## Lenovo Legion 9i Gen 10 18\" RTX 5080
- GPU: 12GB
""".strip()

    rows = extract_candidates_from_log(log_text)
    assert len(rows) == 1
    assert rows[0]["item_name"] == "lenovo legion 9i gen 10 18 rtx 5080"


def test_extract_candidates_does_not_set_price_for_non_aud_line():
    log_text = """
## Lenovo Legion 9i Gen 10 18\" RTX 5080
- GPU: 12GB
- Price: $3000
""".strip()

    rows = extract_candidates_from_log(log_text)
    assert len(rows) == 1
    assert "price_aud" not in rows[0]


def test_extract_candidates_accepts_aud_price_without_dollar_symbol():
    log_text = """
## Lenovo Legion 9i Gen 10 18\" RTX 5080
- GPU: 12GB
- Price: AUD 3000
""".strip()

    rows = extract_candidates_from_log(log_text)
    assert len(rows) == 1
    assert rows[0]["price_aud"] == 3000.0


def test_extract_candidates_ignores_implausible_vram_value():
    log_text = """
## ASUS TUF Gaming A16 — AMD Strix Halo
- GPU: 6496128GB
""".strip()

    rows = extract_candidates_from_log(log_text)
    assert len(rows) == 1
    assert "vram_gb" not in rows[0]


def test_decide_action_returns_skip_existing_when_key_fields_populated():
    shortlist_row = {
        "MCDA_Total": "8.2",
        "effective_best_price_aud": "2999",
        "current_best_url": "https://example.com/item",
        "in_stock_now": "YES",
        "seller_class": "MAJOR_RETAILER_AU",
        "source_platform": "MAJOR_RETAILER_AU",
    }

    assert decide_action(shortlist_row=shortlist_row) == "skip_existing"


def test_decide_action_returns_append_new_when_no_shortlist_row():
    assert decide_action(shortlist_row=None) == "append_new"


def test_decide_action_returns_update_partial_when_fields_missing():
    shortlist_row = {
        "MCDA_Total": "8.2",
        "effective_best_price_aud": "UNKNOWN",
        "current_best_url": "",
    }

    assert decide_action(shortlist_row=shortlist_row) == "update_partial"


def test_decide_action_requires_risk_fields_for_skip_existing():
    shortlist_row = {
        "MCDA_Total": "8.2",
        "effective_best_price_aud": "2999",
        "current_best_url": "https://example.com/item",
        "in_stock_now": "YES",
        "seller_class": "",
        "source_platform": "MAJOR_RETAILER_AU",
    }

    assert decide_action(shortlist_row=shortlist_row) == "update_partial"


def test_cli_smoke_runs_with_required_args(tmp_path):
    log_path = tmp_path / "sample_log.md"
    shortlist_path = tmp_path / "shortlist.csv"
    out_path = tmp_path / "report.json"

    log_path.write_text(
        '## Lenovo Legion 9i Gen 10 18" RTX 5080 (eBay)\n- GPU: 12GB\n- Price: AUD $3000\n',
        encoding="utf-8",
    )
    shortlist_path.write_text(
        "item_name,MCDA_Total,effective_best_price_aud,current_best_url\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "scripts.harvest_llm_recommendations",
            "--log",
            str(log_path),
            "--shortlist",
            str(shortlist_path),
            "--out",
            str(out_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert out_path.exists()


def test_cli_output_json_has_counts_and_actions_structure(tmp_path):
    log_path = tmp_path / "sample_log.md"
    shortlist_path = tmp_path / "shortlist.csv"
    out_path = tmp_path / "report.json"

    log_path.write_text(
        '## Lenovo Legion 9i Gen 10 18" RTX 5080 (eBay)\n- GPU: 12GB\n- Price: AUD $3000\n',
        encoding="utf-8",
    )
    shortlist_path.write_text(
        "item_name,MCDA_Total,effective_best_price_aud,current_best_url\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "scripts.harvest_llm_recommendations",
            "--log",
            str(log_path),
            "--shortlist",
            str(shortlist_path),
            "--out",
            str(out_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    payload = json.loads(out_path.read_text(encoding="utf-8"))

    assert "counts" in payload
    assert "actions" in payload
    assert isinstance(payload["counts"], dict)
    assert isinstance(payload["actions"], list)

    assert payload["counts"]["total_candidates"] == 1
    assert payload["counts"]["append_new"] == 1
    assert payload["counts"]["skip_existing"] == 0
    assert payload["counts"]["update_partial"] == 0

    assert len(payload["actions"]) == 1
    assert payload["actions"][0]["item_name"] == "lenovo legion 9i gen 10 18 rtx 5080"
    assert payload["actions"][0]["action"] == "append_new"


def test_cli_dedupes_duplicate_normalized_item_names(tmp_path):
    log_path = tmp_path / "sample_log.md"
    shortlist_path = tmp_path / "shortlist.csv"
    out_path = tmp_path / "report.json"

    log_path.write_text(
        (
            '## Lenovo Legion 9i Gen 10 18" RTX 5080 (eBay)\n'
            "- GPU: 12GB\n"
            "- Price: AUD $3000\n"
            '## Lenovo Legion 9i Gen 10 18" RTX 5080 (refurb)\n'
            "- GPU: 12GB\n"
            "- Price: AUD $3100\n"
        ),
        encoding="utf-8",
    )
    shortlist_path.write_text(
        "item_name,MCDA_Total,effective_best_price_aud,current_best_url\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "scripts.harvest_llm_recommendations",
            "--log",
            str(log_path),
            "--shortlist",
            str(shortlist_path),
            "--out",
            str(out_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    payload = json.loads(out_path.read_text(encoding="utf-8"))
    assert payload["counts"]["total_candidates"] == 1
    assert len(payload["actions"]) == 1
    assert payload["actions"][0]["item_name"] == "lenovo legion 9i gen 10 18 rtx 5080"


def test_duplicate_entries_merge_to_richer_evidence():
    candidates = [
        {"item_name": "asus rog strix g16 rtx 4070", "vram_gb": 8},
        {"item_name": "asus rog strix g16 rtx 4070", "price_aud": 2899.0},
    ]
    merged = dedupe_candidates(candidates)
    assert len(merged) == 1
    assert merged[0]["item_name"] == "asus rog strix g16 rtx 4070"
    assert merged[0]["vram_gb"] == 8
    assert merged[0]["price_aud"] == 2899.0


def test_cli_missing_required_args_returns_non_zero():
    result = subprocess.run(
        [sys.executable, "-m", "scripts.harvest_llm_recommendations"],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0


def test_match_shortlist_row_uses_canonical_key_fallback():
    shortlist_rows = [
        {
            "item_name": "Lenovo Legion 9i Gen 10 18 RTX 5080",
            "Machine": "",
            "MCDA_Total": "7.0",
        }
    ]

    matched = _match_shortlist_row(
        shortlist_rows, "lenovo legion 9i gen 10 18 rtx 5080 ebay listing"
    )
    assert matched is not None
    assert matched["item_name"] == "Lenovo Legion 9i Gen 10 18 RTX 5080"
