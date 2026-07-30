#!/usr/bin/env python3
"""Validate frozen final-size acceptance records for review figures."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path


REQUIRED_COLUMNS = {
    "figure",
    "criteria_frozen_before_render",
    "primary_question",
    "caption_claim",
    "supported_manuscript_claims",
    "source_register_rows",
    "target_width_in",
    "min_text_pt",
    "detailed_panel_count",
    "expected_page_or_section",
    "acceptance_criteria",
    "hard_blockers",
    "round_1_result",
    "round_1_actions",
    "round_2_result",
    "final_decision",
    "author_approval",
    "notes",
}

ALLOWED_ROUND = {"pass", "revise", "split", "replace", "delete", "not-required"}
ALLOWED_FINAL = {"pass", "split", "replace", "delete"}


def parse_positive_float(value: str, label: str) -> float:
    try:
        number = float(value)
    except ValueError as exc:
        raise ValueError(f"{label} must be numeric") from exc
    if number <= 0:
        raise ValueError(f"{label} must be positive")
    return number


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check frozen acceptance criteria and bounded visual-review rounds."
    )
    parser.add_argument("register", type=Path, help="visual-acceptance CSV")
    args = parser.parse_args()

    try:
        with args.register.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames or []))
            if missing:
                print("ERROR missing columns:", ", ".join(missing))
                return 2
            rows = list(reader)
    except OSError as exc:
        print("ERROR", exc)
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    figures: list[str] = []

    for number, row in enumerate(rows, start=2):
        figure = row["figure"].strip() or f"line-{number}"
        if row["figure"].strip():
            figures.append(row["figure"].strip().casefold())

        for field in (
            "figure",
            "primary_question",
            "caption_claim",
            "supported_manuscript_claims",
            "source_register_rows",
            "expected_page_or_section",
            "acceptance_criteria",
            "hard_blockers",
            "round_1_result",
            "round_2_result",
            "final_decision",
        ):
            if not row[field].strip():
                errors.append(f"line {number} ({figure}): missing {field}")

        if row["criteria_frozen_before_render"].strip().lower() not in {"yes", "true"}:
            errors.append(f"line {number} ({figure}): criteria were not frozen")

        try:
            parse_positive_float(row["target_width_in"].strip(), "target_width_in")
            minimum_text = parse_positive_float(
                row["min_text_pt"].strip(), "min_text_pt"
            )
            if minimum_text < 8:
                errors.append(
                    f"line {number} ({figure}): min_text_pt is below 8 pt"
                )
            panel_count = int(row["detailed_panel_count"].strip())
            if panel_count < 0:
                errors.append(
                    f"line {number} ({figure}): detailed_panel_count is negative"
                )
            if panel_count > 2:
                warnings.append(
                    f"line {number} ({figure}): more than two detailed panels; "
                    "document why they remain legible"
                )
        except ValueError as exc:
            errors.append(f"line {number} ({figure}): {exc}")

        round_1 = row["round_1_result"].strip().lower()
        round_2 = row["round_2_result"].strip().lower()
        final = row["final_decision"].strip().lower()
        if round_1 not in ALLOWED_ROUND:
            errors.append(f"line {number} ({figure}): invalid round_1_result")
        if round_2 not in ALLOWED_ROUND:
            errors.append(f"line {number} ({figure}): invalid round_2_result")
        if final not in ALLOWED_FINAL:
            errors.append(f"line {number} ({figure}): invalid final_decision")
        if round_1 == "revise" and not row["round_1_actions"].strip():
            errors.append(
                f"line {number} ({figure}): revision actions not recorded"
            )
        if final == "pass" and round_2 not in {"pass", "not-required"}:
            errors.append(
                f"line {number} ({figure}): final pass conflicts with round 2"
            )
        if row["author_approval"].strip().lower() != "approved":
            warnings.append(f"line {number} ({figure}): author approval not recorded")

    duplicates = sorted(
        figure for figure, count in Counter(figures).items() if count > 1
    )
    if duplicates:
        errors.append("duplicate figure IDs: " + ", ".join(duplicates))

    print(f"rows={len(rows)} errors={len(errors)} warnings={len(warnings)}")
    for item in errors:
        print("ERROR", item)
    for item in warnings:
        print("WARNING", item)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
