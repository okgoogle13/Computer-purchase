#!/usr/bin/env python3
"""Deterministic harvest of candidate recommendations from LLM logs and exports."""

from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


CANONICAL_INTAKE_HEADER = [
    "date_found",
    "source_batch",
    "track",
    "pathway",
    "category",
    "item_name",
    "price_aud",
    "gpu_model",
    "vram_gb",
    "unified_memory_gb",
    "ram_gb",
    "cpu_model",
    "condition",
    "retailer",
    "url",
    "au_stock_confirmed",
    "verification_status",
    "status",
    "notes",
]
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")
VRAM_RE = re.compile(r"(?i)\b(?:gpu|vram)\b[^\d]*(\d{1,3})\s*gb\b")
PRICE_RE = re.compile(
    r"(?i)(?:A\$|AU\$)\s*([0-9][0-9,]*(?:\.[0-9]{1,2})?)|AUD\s*\$?\s*([0-9][0-9,]*(?:\.[0-9]{1,2})?)"
)
PRODUCT_HEADING_RE = re.compile(
    r"(?i)\b("
    r"rtx|rx|radeon|geforce|legion|rog|alienware|thinkstation|zephyrus|"
    r"predator|titan|raider|omen|proart|strix|ryzen ai max|threadripper|quadro"
    r")\b"
)
AUD_CONTEXT_RE = re.compile(r"(?i)\bAUD\b|A\$\s*\d|AU\$\s*\d")
URL_RE = re.compile(r"https?://[^\s\])>\"']+")
GPU_MODEL_RE = re.compile(
    r"(?i)\b("
    r"(?:NVIDIA\s+|GeForce\s+)?RTX\s+(?:20|30|40|50)\d{2}(?:\s*Ti|\s*SUPER|\s*Ada)?|"
    r"RTX\s+[A-Z]?\d{4}\s*Ada|"
    r"Radeon\s+RX\s+\d{4}M?|"
    r"Radeon\s+Pro\s+W\d{4}|"
    r"Ryzen\s+AI\s+Max\+?\s*\d{3}|"
    r"Strix\s+Halo"
    r")\b"
)
HARDWARE_SIGNAL_RE = re.compile(
    r"(?i)\b("
    r"rtx|radeon|geforce|vram|gddr|ryzen ai max|strix halo|legion|rog|"
    r"alienware|zbook|raider|titan|predator|omen|proart|thinkstation|"
    r"workstation|laptop|desktop|ebay|gumtree|mike pc|scorptec|dick smith"
    r")\b"
)
PROMPT_OR_META_RE = re.compile(
    r"(?i)\b(copy-paste|universal deep research prompt|you are chatgpt|"
    r"mandatory workflow|output contract|required focus|search pattern hints|"
    r"implicit_link|user_query|deep research app)\b"
)
VRAM_CONTEXT_RE = re.compile(
    r"(?i)(?:\bVRAM\b|\bGDDR\d?X?\b|GPU[^.\n|;]{0,40}?(\d{1,3})\s*GB)"
)
EXPLICIT_VRAM_RE = re.compile(r"(?i)\b(\d{1,3})\s*GB\s*(?:VRAM|GDDR\d?X?)\b")
GPU_NEAR_VRAM_RE = re.compile(
    r"(?i)\b(?:RTX|Radeon|GeForce)[^.\n|;]{0,60}?\b(\d{1,3})\s*GB\s*(?:VRAM|GDDR\d?X?)?\b"
)
RAM_RE = re.compile(r"(?i)\b(\d{1,3})\s*GB\s*(?:RAM|LPDDR\dX?|DDR[45])\b")
UNIFIED_RE = re.compile(r"(?i)\b(\d{1,3})\s*GB\s*(?:unified|unified memory)\b")
RETAILER_RE = re.compile(
    r"(?i)\b(?:at|from|via)\s+([A-Z][A-Za-z0-9&' .-]{2,40})(?:[.;,\n]|$)"
)
ALLOWED_EXTRACT_ROLES = {"user", "assistant"}
EXCLUDED_CONTENT_TYPES = {
    "thoughts",
    "tool",
    "browser",
    "code",
    "execution_output",
}


def normalize_item_name(value: str) -> str:
    """Lowercase and remove parenthetical noise and punctuation."""
    no_paren = re.sub(r"\([^)]*\)", " ", value)
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", " ", no_paren).lower()
    return " ".join(cleaned.split())


def _parse_number(value: str) -> float:
    return float(value.replace(",", ""))


def _format_number(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    return str(value)


def extract_candidates_from_log(log_text: str) -> list[dict[str, Any]]:
    """Parse markdown headings and attach explicit price/VRAM evidence lines."""
    rows: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    for raw_line in log_text.splitlines():
        line = raw_line.strip()

        m_heading = HEADING_RE.match(raw_line)
        if m_heading:
            if current:
                rows.append(current)
            heading_text = m_heading.group(1)
            if not PRODUCT_HEADING_RE.search(heading_text):
                current = None
                continue
            current = {"item_name": normalize_item_name(heading_text)}
            continue

        if not current:
            continue

        m_vram = VRAM_RE.search(line)
        if m_vram:
            vram = int(m_vram.group(1))
            if 1 <= vram <= 96:
                current["vram_gb"] = vram

        m_price = PRICE_RE.search(line)
        if m_price and AUD_CONTEXT_RE.search(line):
            amount = m_price.group(1) or m_price.group(2)
            current["price_aud"] = _parse_number(amount)

    if current:
        rows.append(current)

    return rows


def _extract_text_parts(content: dict[str, Any]) -> str:
    content_type = str(content.get("content_type") or "").lower()
    if content_type in EXCLUDED_CONTENT_TYPES:
        return ""

    parts = content.get("parts") or []
    text_parts = [part for part in parts if isinstance(part, str)]
    return "\n".join(text_parts).strip()


def _timestamp_from_chatgpt(value: Any) -> str:
    if value in (None, ""):
        return "UNKNOWN"
    try:
        return datetime.fromtimestamp(float(value)).isoformat()
    except (TypeError, ValueError, OSError):
        return "UNKNOWN"


def get_active_conversation_messages(conversation: dict[str, Any]) -> list[dict[str, Any]]:
    """Return extractable messages on the active branch only."""
    mapping = conversation.get("mapping") or {}
    current_node = conversation.get("current_node")
    node_ids: list[str] = []
    seen: set[str] = set()

    while current_node and current_node in mapping and current_node not in seen:
        seen.add(current_node)
        node_ids.append(current_node)
        current_node = mapping[current_node].get("parent")

    messages: list[dict[str, Any]] = []
    for node_id in reversed(node_ids):
        node = mapping.get(node_id) or {}
        message = node.get("message")
        if not isinstance(message, dict):
            continue

        role = ((message.get("author") or {}).get("role") or "").lower()
        if role not in ALLOWED_EXTRACT_ROLES:
            continue

        text = _extract_text_parts(message.get("content") or {})
        if not text:
            continue

        messages.append(
            {
                "conversation_id": conversation.get("conversation_id")
                or conversation.get("id")
                or "UNKNOWN",
                "conversation_title": conversation.get("title") or "UNKNOWN",
                "message_id": message.get("id") or node_id,
                "role": role,
                "timestamp": _timestamp_from_chatgpt(message.get("create_time")),
                "text": text,
            }
        )

    return messages


def _redact_excerpt(text: str, max_len: int = 500) -> str:
    redacted = re.sub(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", "[REDACTED_EMAIL]", text)
    redacted = re.sub(r"\b(?:\+?61|0)4\d{2}[ -]?\d{3}[ -]?\d{3}\b", "[REDACTED_PHONE]", redacted)
    redacted = collapse_whitespace(redacted)
    return redacted[:max_len].rstrip()


def collapse_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _candidate_chunks(text: str) -> list[str]:
    chunks: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        if line.startswith("|") and line.endswith("|"):
            if HARDWARE_SIGNAL_RE.search(line) and not re.fullmatch(r"\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?", line):
                chunks.append(line)
            continue

        if HARDWARE_SIGNAL_RE.search(line):
            chunks.append(line)

    return chunks


def _normalize_gpu_model(value: str) -> str:
    value = collapse_whitespace(value)
    value = re.sub(r"(?i)^(NVIDIA|GeForce)\s+", "", value)
    value = re.sub(r"(?i)\brtx\b", "RTX", value)
    value = re.sub(r"(?i)\bradeon\b", "Radeon", value)
    value = re.sub(r"(?i)\brx\b", "RX", value)
    value = re.sub(r"(?i)\bti\b", "Ti", value)
    value = re.sub(r"(?i)\bsuper\b", "SUPER", value)
    value = re.sub(r"(?i)\bada\b", "Ada", value)
    return value


def _extract_gpu_model(chunk: str) -> str:
    match = GPU_MODEL_RE.search(chunk)
    return _normalize_gpu_model(match.group(1)) if match else "UNKNOWN"


def _extract_int(match: re.Match[str] | None) -> str:
    if not match:
        return "UNKNOWN"
    value = int(match.group(1))
    if value < 1 or value > 256:
        return "UNKNOWN"
    return str(value)


def _extract_vram_gb(chunk: str) -> str:
    explicit = EXPLICIT_VRAM_RE.search(chunk)
    if explicit:
        return _extract_int(explicit)

    near_gpu = GPU_NEAR_VRAM_RE.search(chunk)
    if near_gpu and VRAM_CONTEXT_RE.search(chunk):
        return _extract_int(near_gpu)

    return "UNKNOWN"


def _extract_ram_gb(chunk: str) -> str:
    return _extract_int(RAM_RE.search(chunk))


def _extract_unified_memory_gb(chunk: str) -> str:
    return _extract_int(UNIFIED_RE.search(chunk))


def _extract_price_aud(chunk: str) -> str:
    match = PRICE_RE.search(chunk)
    if not match or not AUD_CONTEXT_RE.search(chunk):
        return "UNKNOWN"
    amount = match.group(1) or match.group(2)
    return _format_number(_parse_number(amount))


def _extract_url(chunk: str) -> str:
    match = URL_RE.search(chunk)
    return match.group(0).rstrip(".,") if match else "UNKNOWN"


def _extract_retailer(chunk: str) -> str:
    match = RETAILER_RE.search(chunk)
    if not match:
        return "UNKNOWN"
    retailer = collapse_whitespace(match.group(1))
    retailer = re.sub(r"\s+https?$", "", retailer, flags=re.IGNORECASE)
    return retailer or "UNKNOWN"


def _extract_condition(chunk: str) -> str:
    lowered = chunk.lower()
    if "open box" in lowered or "open-box" in lowered or "demo" in lowered:
        return "Open Box"
    if "refurb" in lowered or "remanufactured" in lowered:
        return "Refurbished"
    if "used" in lowered or "pre-owned" in lowered:
        return "Used"
    if "new" in lowered:
        return "New"
    return "UNKNOWN"


def _extract_item_name(chunk: str, gpu_model: str) -> str:
    heading = HEADING_RE.match(chunk)
    if heading:
        return heading.group(1).strip(" -*")

    bold = re.search(r"\*\*([^*]{3,120})\*\*", chunk)
    if bold:
        return bold.group(1).strip(" -*")

    line = re.sub(r"^[-*]\s*", "", chunk).strip()
    if "|" in line:
        cells = [cell.strip("* `") for cell in line.split("|") if cell.strip()]
        cells = [cell for cell in cells if not re.fullmatch(r":?-{3,}:?", cell)]
        if cells:
            return cells[0]

    if gpu_model != "UNKNOWN":
        before_gpu = re.split(re.escape(gpu_model), line, maxsplit=1, flags=re.IGNORECASE)[0]
        before_gpu = re.split(r"\s[-:–—]\s", before_gpu)[0]
        candidate = before_gpu.strip(" -*,|")
        if 3 <= len(candidate) <= 120 and HARDWARE_SIGNAL_RE.search(candidate + " " + gpu_model):
            return candidate

    return "UNKNOWN"


def _infer_track_pathway_category(chunk: str, gpu_model: str) -> tuple[str, str, str]:
    text = f"{chunk} {gpu_model}".lower()
    if "strix halo" in text or "ryzen ai max" in text:
        return "1", "1B", "Laptop"
    if "laptop" in text or any(term in text for term in ("legion", "rog", "alienware", "zbook", "raider", "titan")):
        return "1", "1A", "Laptop"
    if "desktop" in text or "workstation" in text or " pc" in text:
        return "1.5", "UNKNOWN", "Desktop"
    return "UNKNOWN", "UNKNOWN", "UNKNOWN"


def _candidate_confidence(row: dict[str, str]) -> int:
    score = 0
    if row["item_name"] != "UNKNOWN":
        score += 1
    if row["gpu_model"] != "UNKNOWN" or row["unified_memory_gb"] != "UNKNOWN":
        score += 1
    if row["url"] != "UNKNOWN":
        score += 1
    if row["price_aud"] != "UNKNOWN":
        score += 1
    if row["retailer"] != "UNKNOWN" or row["condition"] != "UNKNOWN":
        score += 1
    return score


def _sanitize_field(value: str) -> str:
    return collapse_whitespace(str(value).replace("\r", " ").replace("\n", " "))


def _sanitize_row(row: dict[str, str]) -> dict[str, str]:
    return {field: _sanitize_field(value) for field, value in row.items()}


def _model_signature(row: dict[str, str]) -> str:
    parts = [
        row.get("item_name", "UNKNOWN"),
        row.get("gpu_model", "UNKNOWN"),
        row.get("vram_gb", "UNKNOWN"),
        row.get("unified_memory_gb", "UNKNOWN"),
        row.get("category", "UNKNOWN"),
    ]
    return normalize_item_name(" ".join(part for part in parts if part != "UNKNOWN")) or "UNKNOWN"


def _listing_signature(row: dict[str, str]) -> str:
    parts = [
        _model_signature(row),
        row.get("url", "UNKNOWN"),
        row.get("retailer", "UNKNOWN"),
        row.get("condition", "UNKNOWN"),
        row.get("price_aud", "UNKNOWN"),
    ]
    return normalize_item_name(" ".join(part for part in parts if part != "UNKNOWN")) or _model_signature(row)


def _extract_candidate_from_chunk(
    chunk: str, message: dict[str, str], source_file: str
) -> tuple[dict[str, str], dict[str, Any]] | None:
    if PROMPT_OR_META_RE.search(chunk):
        return None

    gpu_model = _extract_gpu_model(chunk)
    vram_gb = _extract_vram_gb(chunk)
    unified_memory_gb = _extract_unified_memory_gb(chunk)
    ram_gb = _extract_ram_gb(chunk)
    item_name = _extract_item_name(chunk, gpu_model)
    price_aud = _extract_price_aud(chunk)
    url = _extract_url(chunk)
    retailer = _extract_retailer(chunk)
    condition = _extract_condition(chunk)
    track, pathway, category = _infer_track_pathway_category(chunk, gpu_model)

    row = {
        "date_found": message["timestamp"].split("T", 1)[0]
        if message["timestamp"] != "UNKNOWN"
        else "UNKNOWN",
        "source_batch": "ChatGPT-Export",
        "track": track,
        "pathway": pathway,
        "category": category,
        "item_name": item_name,
        "price_aud": price_aud,
        "gpu_model": gpu_model,
        "vram_gb": vram_gb,
        "unified_memory_gb": unified_memory_gb,
        "ram_gb": ram_gb,
        "cpu_model": "UNKNOWN",
        "condition": condition,
        "retailer": retailer,
        "url": url,
        "au_stock_confirmed": "UNKNOWN",
        "verification_status": "Needs Verification",
        "status": "Watchlist",
        "notes": (
            f"ChatGPT export provenance: {message['conversation_title']} "
            f"({message['conversation_id']}); message {message['message_id']}."
        ),
    }

    row = _sanitize_row(row)

    if _candidate_confidence(row) < 3:
        return None

    evidence = {
        "source_type": "ChatGPT-Export",
        "source_file": source_file,
        "conversation_id": message["conversation_id"],
        "conversation_title": message["conversation_title"],
        "message_id": message["message_id"],
        "message_timestamp": message["timestamp"],
        "excerpt": _redact_excerpt(chunk),
        "model_signature": _model_signature(row),
        "listing_signature": _listing_signature(row),
        "confidence_score": _candidate_confidence(row),
    }
    return row, evidence


def _dedupe_export_candidates(
    candidates: list[dict[str, str]], evidence: list[dict[str, Any]]
) -> tuple[list[dict[str, str]], list[dict[str, Any]]]:
    merged: dict[str, dict[str, str]] = {}
    merged_evidence: dict[str, dict[str, Any]] = {}

    for row, evidence_row in zip(candidates, evidence, strict=True):
        key = evidence_row["listing_signature"]
        if key not in merged:
            merged[key] = dict(row)
            merged_evidence[key] = dict(evidence_row)
            continue

        existing = merged[key]
        for field, value in row.items():
            if not _is_populated(existing.get(field)) and _is_populated(value):
                existing[field] = value

        merged_evidence[key]["confidence_score"] = max(
            int(merged_evidence[key]["confidence_score"]),
            int(evidence_row["confidence_score"]),
        )

    return list(merged.values()), list(merged_evidence.values())


def extract_candidates_from_chatgpt_export(export_dir: Path) -> dict[str, Any]:
    """Extract intake-ready candidate rows from a local ChatGPT data export."""
    export_dir = Path(export_dir)
    candidates: list[dict[str, str]] = []
    evidence: list[dict[str, Any]] = []
    conversations_scanned = 0
    messages_scanned = 0
    chunks_scanned = 0

    for conversation_file in sorted(export_dir.glob("conversations-*.json")):
        conversations = json.loads(conversation_file.read_text(encoding="utf-8"))
        for conversation in conversations:
            conversations_scanned += 1
            messages = get_active_conversation_messages(conversation)
            messages_scanned += len(messages)
            for message in messages:
                if not HARDWARE_SIGNAL_RE.search(message["text"]):
                    continue
                for chunk in _candidate_chunks(message["text"]):
                    chunks_scanned += 1
                    extracted = _extract_candidate_from_chunk(
                        chunk, message, conversation_file.name
                    )
                    if not extracted:
                        continue
                    row, evidence_row = extracted
                    candidates.append(row)
                    evidence.append(evidence_row)

    candidates, evidence = _dedupe_export_candidates(candidates, evidence)
    return {
        "candidates": candidates,
        "evidence": evidence,
        "summary": {
            "conversations_scanned": conversations_scanned,
            "messages_scanned": messages_scanned,
            "chunks_scanned": chunks_scanned,
            "candidates_extracted": len(candidates),
            "evidence_rows": len(evidence),
        },
    }


def _is_populated(value: Any) -> bool:
    if value is None:
        return False
    text = str(value).strip()
    return text != "" and text.upper() != "UNKNOWN"


def decide_action(shortlist_row: dict[str, Any] | None) -> str:
    """Choose deterministic action for a candidate vs shortlist row."""
    if not shortlist_row:
        return "append_new"

    required = (
        "MCDA_Total",
        "effective_best_price_aud",
        "current_best_url",
        "in_stock_now",
        "seller_class",
        "source_platform",
    )
    if all(_is_populated(shortlist_row.get(key)) for key in required):
        return "skip_existing"

    return "update_partial"


def dedupe_candidates(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Merge duplicate item names, preferring populated fields from newer entries."""
    merged_candidates: dict[str, dict[str, Any]] = {}
    for candidate in candidates:
        item_name = candidate["item_name"]
        if item_name not in merged_candidates:
            merged_candidates[item_name] = dict(candidate)
            continue
        existing = merged_candidates[item_name]
        for key, value in candidate.items():
            if key == "item_name":
                continue
            if _is_populated(value):
                existing[key] = value
    return list(merged_candidates.values())


def _load_shortlist(path: Path) -> list[dict[str, Any]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def _canonical_item_key(value: str) -> str:
    key = normalize_item_name(value)
    stopwords = {
        "refurb",
        "refurbished",
        "renewed",
        "used",
        "listing",
        "ebay",
        "outlet",
        "open",
        "box",
    }
    parts = [p for p in key.split() if p not in stopwords]
    return " ".join(parts)


def _match_shortlist_row(
    shortlist_rows: list[dict[str, Any]], candidate_item_name: str
) -> dict[str, Any] | None:
    candidate_key = _canonical_item_key(candidate_item_name)
    for row in shortlist_rows:
        source_name = row.get("item_name") or row.get("Machine") or ""
        if normalize_item_name(source_name) == candidate_item_name:
            return row
        if _canonical_item_key(source_name) == candidate_key:
            return row
    return None


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "UNKNOWN") for field in fieldnames})


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")


def _build_review_rows(
    candidates: list[dict[str, str]], evidence: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row, evidence_row in zip(candidates, evidence, strict=True):
        rows.append(
            {
                "candidate": row["item_name"],
                "classification": "Missing",
                "track_pathway": f"{row['track']}/{row['pathway']}",
                "model_signature": evidence_row["model_signature"],
                "listing_signature": evidence_row["listing_signature"],
                "observed_price_aud": row["price_aud"],
                "observed_url": row["url"],
                "conversation_id": evidence_row["conversation_id"],
                "conversation_title": evidence_row["conversation_title"],
                "recommended_action": "Review against existing cards and verify live facts before intake.",
            }
        )
    return rows


def write_chatgpt_export_outputs(
    export_result: dict[str, Any], out_dir: Path, run_date: str
) -> dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    candidates_path = out_dir / f"chatgpt_export_harvest_candidates_{run_date}.csv"
    evidence_path = out_dir / f"chatgpt_export_harvest_evidence_{run_date}.jsonl"
    review_path = out_dir / f"chatgpt_export_harvest_review_{run_date}.csv"
    audit_path = out_dir / f"chatgpt_export_harvest_audit_{run_date}.json"

    candidates = export_result["candidates"]
    evidence = export_result["evidence"]
    review_rows = _build_review_rows(candidates, evidence)

    _write_csv(candidates_path, candidates, CANONICAL_INTAKE_HEADER)
    _write_jsonl(evidence_path, evidence)
    _write_csv(
        review_path,
        review_rows,
        [
            "candidate",
            "classification",
            "track_pathway",
            "model_signature",
            "listing_signature",
            "observed_price_aud",
            "observed_url",
            "conversation_id",
            "conversation_title",
            "recommended_action",
        ],
    )
    audit_path.write_text(
        json.dumps(
            {
                **export_result["summary"],
                "outputs": {
                    "candidates_csv": str(candidates_path),
                    "evidence_jsonl": str(evidence_path),
                    "review_csv": str(review_path),
                },
                "privacy": {
                    "raw_export_text_written": False,
                    "binary_attachments_written": False,
                    "excerpt_cap_chars": 500,
                },
                "defaults": {
                    "verification_status": "Needs Verification",
                    "au_stock_confirmed": "UNKNOWN",
                    "status": "Watchlist",
                },
            },
            indent=2,
            ensure_ascii=True,
        ),
        encoding="utf-8",
    )

    return {
        "candidates_csv": str(candidates_path),
        "evidence_jsonl": str(evidence_path),
        "review_csv": str(review_path),
        "audit_json": str(audit_path),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Harvest LLM recommendations deterministically")
    parser.add_argument("--log", help="Path to markdown log")
    parser.add_argument("--shortlist", help="Path to shortlist CSV")
    parser.add_argument("--out", help="Path to output JSON report")
    parser.add_argument("--chatgpt-export", help="Path to local ChatGPT export directory")
    parser.add_argument("--out-dir", default="output", help="Output directory for export harvest")
    parser.add_argument("--date", default=datetime.now().date().isoformat(), help="Run date for output names")
    args = parser.parse_args()

    if args.chatgpt_export:
        export_result = extract_candidates_from_chatgpt_export(Path(args.chatgpt_export))
        outputs = write_chatgpt_export_outputs(export_result, Path(args.out_dir), args.date)
        print(json.dumps({"summary": export_result["summary"], "outputs": outputs}, indent=2))
        return

    if not args.log or not args.shortlist or not args.out:
        parser.error("--log, --shortlist, and --out are required unless --chatgpt-export is used")

    log_text = Path(args.log).read_text(encoding="utf-8")
    candidates = extract_candidates_from_log(log_text)
    unique_candidates = dedupe_candidates(candidates)

    shortlist_rows = _load_shortlist(Path(args.shortlist))

    actions: list[dict[str, Any]] = []
    counts = {"skip_existing": 0, "append_new": 0, "update_partial": 0}

    for candidate in unique_candidates:
        shortlist_row = _match_shortlist_row(shortlist_rows, candidate["item_name"])
        action = decide_action(shortlist_row=shortlist_row)
        counts[action] += 1
        actions.append({"item_name": candidate["item_name"], "action": action})

    report = {
        "counts": {"total_candidates": len(unique_candidates), **counts},
        "actions": actions,
    }

    out_path = Path(args.out)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
