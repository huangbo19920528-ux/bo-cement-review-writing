#!/usr/bin/env python3
"""Validate the high-ambition journal target ladder."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


REQUIRED_COLUMNS = {
    "level",
    "journal",
    "official_scope_url",
    "guide_url",
    "policy_check_date",
    "review_eligibility",
    "proposal_or_invitation",
    "readership",
    "synthesis_profile",
    "closest_recent_reviews",
    "novelty_reason",
    "required_upgrades",
    "visual_program",
    "method_and_data_requirements",
    "transfer_changes",
    "status",
}
LEVELS = {"stretch", "best-fit", "floor"}
ELIGIBILITY = {"yes", "no", "invited", "proposal-required", "priority-only", "unknown"}
PROFILES = {
    "mechanism-to-performance",
    "application-to-performance",
    "evidence-to-design",
    "hybrid",
}
STATUSES = {"pending", "verified", "ineligible", "selected"}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = REQUIRED_COLUMNS - fields
        if missing:
            return [f"missing columns: {', '.join(sorted(missing))}"]
        rows = list(reader)

    by_level = {row["level"].strip(): row for row in rows}
    if set(by_level) != LEVELS:
        errors.append("ladder must contain exactly one stretch, best-fit, and floor row")

    for index, row in enumerate(rows, start=2):
        level = row["level"].strip()
        eligibility = row["review_eligibility"].strip()
        profile = row["synthesis_profile"].strip()
        status = row["status"].strip()
        if eligibility not in ELIGIBILITY:
            errors.append(f"row {index}: invalid review_eligibility {eligibility!r}")
        if profile and profile not in PROFILES:
            errors.append(f"row {index}: invalid synthesis_profile {profile!r}")
        if status not in STATUSES:
            errors.append(f"row {index}: invalid status {status!r}")
        if status in {"verified", "selected"}:
            for field in (
                "journal",
                "official_scope_url",
                "guide_url",
                "policy_check_date",
                "readership",
                "synthesis_profile",
                "novelty_reason",
                "required_upgrades",
                "visual_program",
                "method_and_data_requirements",
            ):
                if not row[field].strip():
                    errors.append(f"row {index}: {field} is required for status {status}")
        if level == "stretch" and status == "selected" and eligibility in {"no", "unknown"}:
            errors.append("stretch target cannot be selected when review eligibility is no/unknown")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    errors = validate(args.csv_path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("journal target ladder: valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())

