#!/usr/bin/env python3
"""Validate review-figure briefs and visual-precedent links."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path


BRIEF_REQUIRED = {
    "figure",
    "primary_question",
    "scientific_role",
    "section",
    "evidence_claim",
    "why_visual_needed",
    "planned_panels",
    "source_class_by_panel",
    "precedent_ids",
    "final_width_or_layout",
    "min_readable_text",
    "caption_draft",
    "permission_route",
    "retain_revise_replace_delete",
    "author_approval",
}

PRECEDENT_REQUIRED = {
    "precedent_id",
    "citation",
    "doi",
    "journal",
    "year",
    "source_figure",
    "scientific_question",
    "figure_role",
    "evidence_type",
    "why_it_works",
    "practice_to_learn",
    "practice_not_to_copy",
    "license_or_permission_note",
    "verification_status",
}

ALLOWED_DECISIONS = {"retain", "revise", "replace", "delete"}


def read_csv(path: Path, required: set[str]) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise ValueError(f"{path.name}: missing columns: {', '.join(missing)}")
        return list(reader)


def split_ids(value: str) -> set[str]:
    return {
        item.strip()
        for item in value.replace(";", ",").split(",")
        if item.strip()
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check figure briefs against a visual-precedent matrix."
    )
    parser.add_argument("briefs", type=Path, help="CSV figure-brief file")
    parser.add_argument("precedents", type=Path, help="CSV visual-benchmark matrix")
    args = parser.parse_args()

    try:
        briefs = read_csv(args.briefs, BRIEF_REQUIRED)
        precedents = read_csv(args.precedents, PRECEDENT_REQUIRED)
    except (OSError, ValueError) as exc:
        print("ERROR", exc)
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    precedent_ids = {
        row["precedent_id"].strip()
        for row in precedents
        if row["precedent_id"].strip()
    }

    duplicate_precedents = sorted(
        key
        for key, count in Counter(
            row["precedent_id"].strip()
            for row in precedents
            if row["precedent_id"].strip()
        ).items()
        if count > 1
    )
    if duplicate_precedents:
        errors.append("duplicate precedent IDs: " + ", ".join(duplicate_precedents))

    figure_ids: list[str] = []
    for number, row in enumerate(briefs, start=2):
        figure = row["figure"].strip() or f"line-{number}"
        decision = row["retain_revise_replace_delete"].strip().lower()
        if decision not in ALLOWED_DECISIONS:
            errors.append(f"line {number} ({figure}): invalid decision '{decision}'")
            continue
        if row["figure"].strip():
            figure_ids.append(row["figure"].strip().casefold())
        if decision != "delete":
            for field in (
                "primary_question",
                "scientific_role",
                "section",
                "evidence_claim",
                "why_visual_needed",
                "planned_panels",
                "source_class_by_panel",
                "final_width_or_layout",
                "min_readable_text",
                "caption_draft",
                "permission_route",
            ):
                if not row[field].strip():
                    errors.append(f"line {number} ({figure}): missing {field}")
            missing_links = sorted(split_ids(row["precedent_ids"]) - precedent_ids)
            if missing_links:
                errors.append(
                    f"line {number} ({figure}): unknown precedent IDs "
                    + ", ".join(missing_links)
                )
            if not split_ids(row["precedent_ids"]):
                warnings.append(f"line {number} ({figure}): no visual precedent linked")
            if row["author_approval"].strip().lower() != "approved":
                warnings.append(f"line {number} ({figure}): author approval not recorded")

    duplicate_figures = sorted(
        key for key, count in Counter(figure_ids).items() if count > 1
    )
    if duplicate_figures:
        errors.append("duplicate figure IDs: " + ", ".join(duplicate_figures))

    print(
        f"briefs={len(briefs)} precedents={len(precedents)} "
        f"errors={len(errors)} warnings={len(warnings)}"
    )
    for item in errors:
        print("ERROR", item)
    for item in warnings:
        print("WARNING", item)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
