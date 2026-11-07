#!/usr/bin/env python3
"""Optional strict gate for projects requiring human sequence approval.

The full-build phase is project-selected. The audience-ready phase must remain
fail-closed before claiming human comprehension, and neither phase decides
whether an untested presentation artifact may be produced.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SECTION_NAMES = {"audience_use_gate", "audience use gate"}
AI_REVIEWER = re.compile(r"\b(ai|agent|assistant|chatgpt|model|llm|unknown)\b", re.I)
PLACEHOLDER_VALUES = {
    "pending",
    "tbd",
    "todo",
    "not_run",
    "not_yet",
    "not_applicable",
    "n/a",
    "na",
    "missing",
    "unknown",
}


def normalize_key(value: str) -> str:
    return re.sub(r"[\s-]+", "_", value.strip().lower())


def is_placeholder(value: str) -> bool:
    return normalize_key(value) in PLACEHOLDER_VALUES


def parse_gate(spec_lock: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    active = False
    for raw in spec_lock.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("## "):
            active = normalize_key(line[3:]) in {
                normalize_key(name) for name in SECTION_NAMES
            }
            continue
        if not active:
            continue
        match = re.match(r"^-\s*([^:]+):\s*(.*)$", line)
        if match:
            values[normalize_key(match.group(1))] = match.group(2).strip()
    return values


def validate(values: dict[str, str], phase: str) -> list[str]:
    errors: list[str] = []
    status = normalize_key(values.get("status", ""))
    allowed = {"sequence_approved", "audience_ready"}
    if phase == "audience-ready":
        allowed = {"audience_ready"}
    if status not in allowed:
        errors.append(f"status must be one of {sorted(allowed)}, got {status or 'missing'}")

    reviewer = values.get("human_reviewer", "")
    if not reviewer:
        errors.append("human_reviewer is required")
    elif is_placeholder(reviewer):
        errors.append("human_reviewer must contain observed human evidence, not a placeholder")
    elif AI_REVIEWER.search(reviewer):
        errors.append("human_reviewer cannot be an AI, agent, model, or unknown reviewer")

    for key in ("sequence", "retell", "loss_points"):
        value = values.get(key, "").strip()
        if not value:
            errors.append(f"{key} is required")
        elif is_placeholder(value):
            errors.append(f"{key} must contain observed evidence, not a placeholder")

    if phase == "audience-ready" and normalize_key(values.get("spoken_run", "")) != "passed":
        errors.append("spoken_run must be passed for audience-ready")
    if phase == "audience-ready":
        for key in ("unseen_transfer", "delayed_reconstruction"):
            value = values.get(key, "").strip()
            if not value:
                errors.append(f"{key} is required for audience-ready")
            elif is_placeholder(value):
                errors.append(f"{key} must contain observed evidence, not a placeholder")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate human sequential-use evidence for a presentation project."
    )
    parser.add_argument(
        "project_or_evidence",
        type=Path,
        help="project directory with spec_lock.md, or an existing Markdown evidence file",
    )
    parser.add_argument(
        "--phase", choices=("full-build", "audience-ready"), required=True
    )
    args = parser.parse_args()

    spec_lock = args.project_or_evidence
    if spec_lock.is_dir():
        spec_lock = spec_lock / "spec_lock.md"
    if not spec_lock.is_file():
        print(f"FAIL audience use gate: missing {spec_lock}")
        return 1

    values = parse_gate(spec_lock)
    if not values:
        print("FAIL audience use gate: missing ## audience_use_gate section")
        return 1

    errors = validate(values, args.phase)
    if errors:
        print(f"FAIL audience use gate ({args.phase}):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"PASS audience use gate ({args.phase}): "
        f"status={normalize_key(values['status'])}; human_reviewer={values['human_reviewer']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
