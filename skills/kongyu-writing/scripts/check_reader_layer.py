#!/usr/bin/env python3
"""Check a participant-facing reader layer for audit-register language.

The existing `Machine-identifier scrubbing` rule only covers machine provenance
(message ids, run names, confidence fields). This gate covers the register that
survives that test: sample sizes, field names, the author's own error counts,
analyst nouns, taxonomy labels, and standing schema phrases.

It also checks that the narrative person is consistent, because a body that opens
in second person and reverts to third-person names reads as two stitched
documents -- and because bulk name replacement silently corrupts quoted messages.

Usage:
    python check_reader_layer.py <md-or-html> [--allow-term TERM ...] [--json]

Exit codes: 0 pass (warnings allowed), 1 findings above threshold, 2 bad input.
Only lines inside fenced code blocks and inline code are exempt from the
quote-person check, never from the audit-register check.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Audit-register vocabulary. Tier: 2 = rewrite before delivery, 1 = rewrite if easy.
# Each entry: (term, tier, why it leaks)
TERMS: list[tuple[str, int, str]] = [
    # --- register opened with the reader's first screen ---
    ("材料内无法判定", 2, "standing schema phrase; say what the record cannot show"),
    ("材料无法判定", 2, "standing schema phrase"),
    ("材料答不了", 2, "register shorthand"),
    ("先说材料", 2, "audit register opening"),
    ("硬约束", 2, "internal rule label"),
    ("本节", 2, "internal structure label"),
    ("回表", 2, "internal verification verb"),
    ("原表", 2, "internal data-store reference"),
    ("核验", 1, "verification register; keep only in appendix"),
    ("自查", 1, "verification register"),
    ("台账", 2, "internal artifact name"),
    # --- analyst nouns the participant cannot use in conversation ---
    ("代理", 2, "analyst noun"),
    ("子代理", 2, "analyst noun"),
    ("subagent", 2, "analyst noun"),
    ("prompt", 1, "analyst noun unless quoted"),
    ("派发", 2, "analyst noun"),
    ("分派", 1, "analyst noun"),
    ("skill", 1, "tool noun"),
    ("工作流", 1, "process noun"),
    # --- taxonomy labels used as headings or in prose ---
    ("骨架", 1, "internal structure label"),
    ("分界依据", 1, "internal column label"),
    ("暴露度", 2, "abstract metric not defined for the reader"),
    ("置信度", 2, "confidence field"),
    ("可信度", 2, "confidence field"),
    ("覆盖率", 1, "audit metric"),
    ("字段", 1, "data field name"),
    ("元数据", 1, "machine provenance"),
    # --- analyst-facing scaffolding ---
    ("附录", 0, "allowed; but the appendix carries what the body may not"),
    ("反讽", 3, "tone marker"),
]

# Third-person names that must not survive in a second-person body.
NAME_TOKENS = ("流云", "benny", "Benny", "罗贝妮")

FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`\n]+`")


def strip_fenced(text: str) -> list[tuple[int, str, bool]]:
    """Return (lineno, line, inside_fence) triples."""
    out, inside = [], False
    for i, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            inside = not inside
            out.append((i, line, True))
            continue
        out.append((i, line, inside))
    return out


def check_terms(lines) -> list[dict]:
    findings = []
    for lineno, line, _ in lines:
        for term, tier, why in TERMS:
            if tier == 0:
                continue
            if term in line:
                findings.append({
                    "kind": "register", "line": lineno, "term": term,
                    "tier": tier, "why": why, "excerpt": line.strip()[:110],
                })
    return findings


def check_person(lines) -> list[dict]:
    """Narrative person must be consistent; quotes exempt via inline code."""
    findings = []
    for lineno, line, inside in lines:
        if inside:
            continue
        bare = INLINE_CODE.sub(" ", line)
        hits = [t for t in NAME_TOKENS if t in bare]
        if hits:
            findings.append({
                "kind": "person", "line": lineno, "terms": hits,
                "tier": 1, "why": "third-person name in a second-person body",
                "excerpt": line.strip()[:110],
            })
    return findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--allow-term", action="append", default=[])
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    p = Path(args.path)
    if not p.is_file():
        print(f"not a file: {p}", file=sys.stderr)
        return 2
    raw = p.read_text(encoding="utf-8", errors="replace")
    if p.suffix.lower() in (".html", ".htm"):
        # Strip script/style; keep the visible body only.
        raw = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", raw)
        raw = re.sub(r"(?s)<[^>]+>", " ", raw)

    lines = strip_fenced(raw)
    findings = check_terms(lines) + check_person(lines)

    for f in findings:
        if f["kind"] == "register" and f["term"] in args.allow_term:
            continue
        if f["kind"] == "person":
            if any(t in args.allow_term for t in f["terms"]):
                continue

    blocking = [f for f in findings if f["tier"] >= 2 and f["term"] not in args.allow_term]
    warn = [f for f in findings if f["tier"] < 2]

    if args.json:
        print(json.dumps({
            "path": str(p), "ok": not blocking,
            "blocking": blocking, "warnings": warn,
        }, ensure_ascii=False, indent=2))
        return 1 if blocking else 0

    print(f"# reader-layer gate: {p.name}\n")
    if blocking:
        print(f"BLOCKING {len(blocking)}\n")
        for f in blocking:
            print(f"- L{f['line']} [{f['term']}] {f['why']}")
            print(f"    {f['excerpt']}")
    else:
        print("PASS blocking: 0")
    if warn:
        print(f"\nWARN {len(warn)} (rewrite if easy)\n")
        for f in warn:
            print(f"- L{f['line']} [{f.get('term') or ','.join(f.get('terms', []))}] {f['why']}")
    print("\nOnly the body must pass. An appendix may carry method and error counts;")
    print("move findings there rather than deleting the underlying claim.")
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())