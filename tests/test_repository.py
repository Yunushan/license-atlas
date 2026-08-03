#!/usr/bin/env python3
"""Unit tests for repository-level invariants."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_repository  # noqa: E402


class RepositoryInvariantTests(unittest.TestCase):
    def test_current_repository_has_no_invariant_errors(self) -> None:
        errors: list[str] = []
        check_repository.check_readme_languages(errors)
        check_repository.check_local_links(errors)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
