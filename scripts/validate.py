#!/usr/bin/env python3
"""Validate the License Atlas source data without third-party dependencies."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LICENSE_DATA = ROOT / "data" / "licenses.json"
LANGUAGE_DATA = ROOT / "data" / "languages.json"

EXPECTED_LICENSE_COUNT = 50
EXPECTED_LANGUAGE_COUNT = 20

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

ALLOWED_LICENSE_VALUES = {
    "category": {
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
    },
    "scope": {"software", "documentation", "fonts", "content-and-data", "databases"},
    "commercial_use": {"yes", "no", "conditional"},
    "private_use": {"yes", "no", "conditional"},
    "modification": {"yes", "no", "conditional", "no-for-distribution"},
    "redistribution": {"yes", "no", "conditional"},
    "source_availability": {
        "conditional",
        "not-applicable",
        "not-required",
        "required-for-covered-files",
        "required-for-covered-modifications",
        "required-for-covered-source",
        "required-for-database-derivatives",
        "required-on-distribution",
        "required-on-distribution-and-external-deployment",
        "required-on-distribution-and-network-use",
    },
    "notice": {
        "attribution",
        "copyright-and-license",
        "copyright-license-and-acknowledgement",
        "copyright-license-and-changes",
        "copyright-license-and-disclaimer",
        "copyright-license-and-font-name",
        "copyright-license-and-notice",
        "copyright-license-and-source",
        "limited",
        "none",
    },
    "patent": {"explicit", "limited", "none-stated", "not-applicable"},
    "copyleft": {
        "content-share-alike",
        "database-share-alike",
        "documentation-share-alike",
        "file-level",
        "library",
        "network",
        "none",
        "project-level",
    },
}
ALLOWED_COMMENT_STYLES = {"block", "line", "hash"}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_data(licenses: Any, languages: Any) -> list[str]:
    """Return actionable validation errors for loaded catalog data."""

    errors: list[str] = []
    if not isinstance(licenses, list):
        fail("licenses.json must contain a JSON array", errors)
        licenses = []
    if not isinstance(languages, list):
        fail("languages.json must contain a JSON array", errors)
        languages = []

    if len(licenses) != EXPECTED_LICENSE_COUNT:
        fail(f"expected exactly {EXPECTED_LICENSE_COUNT} licenses, found {len(licenses)}", errors)
    if len(languages) != EXPECTED_LANGUAGE_COUNT:
        fail(f"expected exactly {EXPECTED_LANGUAGE_COUNT} languages, found {len(languages)}", errors)

    license_ids: list[str] = []
    ranks: list[int] = []
    license_text_fields = (
        "id",
        "name",
        "family",
        "category",
        "scope",
        "best_for",
        "watch_out",
        "compatibility",
        "reference_url",
    )
    for index, item in enumerate(licenses, start=1):
        label = f"license #{index}"
        if not isinstance(item, dict):
            fail(f"{label} must be a JSON object", errors)
            continue

        identifier = item.get("id", label)
        missing = REQUIRED_LICENSE_FIELDS - item.keys()
        if missing:
            fail(f"{identifier} is missing fields: {sorted(missing)}", errors)

        for field in license_text_fields:
            if not non_empty_string(item.get(field)):
                fail(f"{identifier} must have a non-empty string {field}", errors)

        rank = item.get("rank")
        if not isinstance(rank, int) or isinstance(rank, bool):
            fail(f"{identifier} must have an integer rank", errors)
        else:
            ranks.append(rank)

        if isinstance(item.get("id"), str):
            license_ids.append(item["id"])
            expected_url = f"https://spdx.org/licenses/{item['id']}.html"
            if item.get("reference_url") != expected_url:
                fail(f"{identifier} must use reference URL {expected_url}", errors)

        for field, allowed in ALLOWED_LICENSE_VALUES.items():
            value = item.get(field)
            if value not in allowed:
                fail(f"{identifier} has an invalid {field} value: {value!r}", errors)

        conditions = item.get("conditions")
        if not isinstance(conditions, list) or not conditions or not all(non_empty_string(value) for value in conditions):
            fail(f"{identifier} must have a non-empty list of condition strings", errors)

    if len(license_ids) != len(set(license_ids)):
        fail("license SPDX identifiers must be unique", errors)
    if ranks != list(range(1, len(licenses) + 1)):
        fail("license ranks must be sequential integers starting at 1", errors)

    language_names: list[str] = []
    for index, item in enumerate(languages, start=1):
        label = f"language #{index}"
        if not isinstance(item, dict):
            fail(f"{label} must be a JSON object", errors)
            continue

        name = item.get("name", label)
        missing = REQUIRED_LANGUAGE_FIELDS - item.keys()
        if missing:
            fail(f"{name} is missing fields: {sorted(missing)}", errors)
        if isinstance(item.get("name"), str):
            language_names.append(item["name"])
        for field in ("name", "comment_style", "header", "ecosystem_note"):
            if not non_empty_string(item.get(field)):
                fail(f"{name} must have a non-empty string {field}", errors)

        if item.get("comment_style") not in ALLOWED_COMMENT_STYLES:
            fail(f"{name} has an invalid comment_style value: {item.get('comment_style')!r}", errors)

        extensions = item.get("extensions")
        if not isinstance(extensions, list) or not extensions or not all(
            non_empty_string(extension) and extension.startswith(".") for extension in extensions
        ):
            fail(f"{name} must list non-empty dotted file extensions", errors)
        elif len(extensions) != len(set(extensions)):
            fail(f"{name} must not repeat a file extension", errors)

    if len(language_names) != len(set(language_names)):
        fail("language names must be unique", errors)

    return errors


def load_data() -> tuple[Any, Any]:
    return (
        json.loads(LICENSE_DATA.read_text(encoding="utf-8")),
        json.loads(LANGUAGE_DATA.read_text(encoding="utf-8")),
    )


def main() -> int:
    try:
        licenses, languages = load_data()
    except (OSError, json.JSONDecodeError) as exc:
        print(f"data loading failed: {exc}", file=sys.stderr)
        return 1

    errors = validate_data(licenses, languages)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"validated {len(licenses)} licenses and {len(languages)} languages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
