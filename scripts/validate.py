#!/usr/bin/env python3
"""Validate the License Atlas source data without third-party dependencies."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LICENSE_DATA = ROOT / "data" / "licenses.json"
LANGUAGE_DATA = ROOT / "data" / "languages.json"

REQUIRED_LICENSE_FIELDS = {
    "rank",
    "id",
    "name",
    "family",
    "category",
    "scope",
    "commercial_use",
    "private_use",
    "modification",
    "redistribution",
    "source_availability",
    "notice",
    "patent",
    "copyleft",
    "conditions",
    "best_for",
    "watch_out",
    "compatibility",
    "reference_url",
}
REQUIRED_LANGUAGE_FIELDS = {"name", "extensions", "comment_style", "header", "ecosystem_note"}
ALLOWED_CATEGORIES = {
    "permissive",
    "weak-copyleft",
    "library-copyleft",
    "strong-copyleft",
    "network-copyleft",
    "documentation",
    "font",
    "content-data",
    "database",
    "source-available",
}
ALLOWED_VALUES = {"yes", "no", "conditional", "limited", "not-applicable", "modification", "no-for-distribution"}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    try:
        licenses = json.loads(LICENSE_DATA.read_text(encoding="utf-8"))
        languages = json.loads(LANGUAGE_DATA.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"data loading failed: {exc}", file=sys.stderr)
        return 1

    if len(licenses) != 50:
        fail(f"expected exactly 50 licenses, found {len(licenses)}", errors)
    if len(languages) != 20:
        fail(f"expected exactly 20 languages, found {len(languages)}", errors)

    ids = [item.get("id") for item in licenses]
    if len(ids) != len(set(ids)):
        fail("license SPDX identifiers must be unique", errors)
    ranks = [item.get("rank") for item in licenses]
    if ranks != list(range(1, len(licenses) + 1)):
        fail("license ranks must be sequential starting at 1", errors)

    for item in licenses:
        missing = REQUIRED_LICENSE_FIELDS - item.keys()
        if missing:
            fail(f"{item.get('id', '<unknown>')} is missing fields: {sorted(missing)}", errors)
        if item.get("category") not in ALLOWED_CATEGORIES:
            fail(f"{item.get('id', '<unknown>')} has an unknown category", errors)
        for field in ("commercial_use", "private_use", "modification", "redistribution"):
            if item.get(field) not in ALLOWED_VALUES:
                fail(f"{item.get('id', '<unknown>')} has an invalid {field} value", errors)
        if not item.get("conditions") or not all(isinstance(value, str) and value for value in item["conditions"]):
            fail(f"{item.get('id', '<unknown>')} must have non-empty condition strings", errors)
        if not str(item.get("reference_url", "")).startswith("https://spdx.org/licenses/"):
            fail(f"{item.get('id', '<unknown>')} must use a canonical SPDX reference URL", errors)

    language_names = [item.get("name") for item in languages]
    if len(language_names) != len(set(language_names)):
        fail("language names must be unique", errors)
    for item in languages:
        missing = REQUIRED_LANGUAGE_FIELDS - item.keys()
        if missing:
            fail(f"{item.get('name', '<unknown>')} is missing fields: {sorted(missing)}", errors)
        if not item.get("extensions") or not all(str(ext).startswith(".") for ext in item["extensions"]):
            fail(f"{item.get('name', '<unknown>')} must list dotted file extensions", errors)
        if not item.get("header", "").strip():
            fail(f"{item.get('name', '<unknown>')} must have a header example", errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"validated {len(licenses)} licenses and {len(languages)} languages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
