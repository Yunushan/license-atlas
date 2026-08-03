#!/usr/bin/env python3
"""Unit tests for the catalog validator."""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate  # noqa: E402


class ValidateDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.licenses = json.loads((ROOT / "data" / "licenses.json").read_text(encoding="utf-8"))
        cls.languages = json.loads((ROOT / "data" / "languages.json").read_text(encoding="utf-8"))

    def test_current_catalog_is_valid(self) -> None:
        self.assertEqual(validate.validate_data(self.licenses, self.languages), [])

    def test_rejects_invalid_source_availability(self) -> None:
        licenses = copy.deepcopy(self.licenses)
        licenses[0]["source_availability"] = "unknown"
        errors = validate.validate_data(licenses, self.languages)
        self.assertTrue(any("source_availability" in error for error in errors))

    def test_rejects_reference_url_for_the_wrong_identifier(self) -> None:
        licenses = copy.deepcopy(self.licenses)
        licenses[0]["reference_url"] = "https://spdx.org/licenses/MIT.html"
        errors = validate.validate_data(licenses, self.languages)
        self.assertTrue(any("reference URL" in error for error in errors))

    def test_rejects_non_object_entries(self) -> None:
        licenses = copy.deepcopy(self.licenses)
        licenses[0] = "not an object"
        errors = validate.validate_data(licenses, self.languages)
        self.assertTrue(any("must be a JSON object" in error for error in errors))

    def test_rejects_duplicate_language_names(self) -> None:
        languages = copy.deepcopy(self.languages)
        languages[1]["name"] = languages[0]["name"]
        errors = validate.validate_data(self.licenses, languages)
        self.assertTrue(any("language names must be unique" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
