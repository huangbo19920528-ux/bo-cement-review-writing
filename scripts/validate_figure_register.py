#!/usr/bin/env python3
"""Validate a review-manuscript figure source and permission register."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path


REQUIRED_COLUMNS = {
    "figure",
    "panel",
    "panel_purpose",
    "evidence_claim",
    "role",
    "source_id",
    "source_type",
    "doi_or_url",
    "source_figure_or_page",
    "creator_or_institution",
    "license_or_terms",
    "permission_status",
    "attribution_text",
    "local_asset",
    "duplicate_hash_check",
    "legacy_label_check",
    "completeness_check",
    "scale_bar_or_axes_check",
    "scientific_integrity_check",
    "final_size_legibility",
    "final_visual_check",
}

ALLOWED_PERMISSION = {
    "original",
    "public-domain",
    "open-license",
    "permission-obtained",
    "permission-required",
    "not-used",
}

ALLOWED_CHECK = {"pass", "not-applicable"}

ORIGINAL_SOURCE_TYPES = {
    "original",
    "original-synthesis",
    "replotted-data",
    "author-owned-photo",
    "not-used",
}

PANEL_CHECKS = (
    "duplicate_hash_check",
    "legacy_label_check",
    "completeness_check",
    "scale_bar_or_axes_check",
    "scientific_integrity_check",
    "final_size_legibility",
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check figure provenance, permission status, and duplicate sources."
    )
    parser.add_argument("register", type=Path, help="CSV figure-source register")
    args = parser.parse_args()

    with args.register.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = set(reader.fieldnames or [])
        missing = sorted(REQUIRED_COLUMNS - fieldnames)
        if missing:
            print("ERROR missing columns:", ", ".join(missing))
            return 2
        rows = list(reader)

    errors: list[str] = []
    warnings: list[str] = []
    source_keys: list[str] = []

    for number, row in enumerate(rows, start=2):
        label = f"{row.get('figure', '?')}{row.get('panel', '')}"
        status = row["permission_status"].strip().lower()
        source_type = row["source_type"].strip().lower()
        source_id = row["source_id"].strip()

        if status not in ALLOWED_PERMISSION:
            errors.append(f"line {number} ({label}): invalid permission_status '{status}'")
        if status == "permission-required":
            errors.append(f"line {number} ({label}): permission remains required")
        if status != "not-used":
            for field in ("figure", "panel_purpose", "evidence_claim", "role", "local_asset"):
                if not row[field].strip():
                    errors.append(f"line {number} ({label}): missing {field}")
        if status not in {"original", "not-used"}:
            for field in (
                "source_id",
                "doi_or_url",
                "source_figure_or_page",
                "creator_or_institution",
                "license_or_terms",
                "attribution_text",
            ):
                if not row[field].strip():
                    errors.append(f"line {number} ({label}): missing {field}")
        if source_type not in ORIGINAL_SOURCE_TYPES and source_id:
            source_keys.append(source_id.casefold())
        if status != "not-used":
            for field in PANEL_CHECKS:
                value = row[field].strip().lower()
                if value not in ALLOWED_CHECK:
                    errors.append(
                        f"line {number} ({label}): {field} must be pass or not-applicable"
                    )
        if status != "not-used" and row["final_visual_check"].strip().lower() != "pass":
            warnings.append(f"line {number} ({label}): final visual check not recorded")

    repeated = sorted(key for key, count in Counter(source_keys).items() if count > 1)
    if repeated:
        warnings.append(
            "Repeated source_id values require a documented reason: " + ", ".join(repeated)
        )

    print(f"rows={len(rows)} errors={len(errors)} warnings={len(warnings)}")
    for item in errors:
        print("ERROR", item)
    for item in warnings:
        print("WARNING", item)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

