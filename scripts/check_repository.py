#!/usr/bin/env python3
"""Check repository-level documentation and localization invariants."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
LICENSE = ROOT / "LICENSE"
README_LANGUAGE_DATA = ROOT / "data" / "readme_languages.json"
LOCAL_LINK_PATTERN = re.compile(r"\]\((?!https?://|#|mailto:)([^)]+)\)")
README_TABLE_ROW = re.compile(r"^\| (.+) \| `([^`]+)` \| \[[^]]+\]\(([^)]+)\) \|$")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_readme_languages(errors: list[str]) -> None:
    try:
        entries = load_json(README_LANGUAGE_DATA)
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"could not load readme language data: {exc}")
        return

    if not isinstance(entries, list) or len(entries) != 20:
        errors.append("readme_languages.json must contain exactly 20 entries")
        return

    locales: list[str] = []
    readmes: list[str] = []
    expected_rows: list[tuple[str, str, str]] = []
    valid_entries: list[dict[str, str]] = []
    required_fields = {"name", "locale", "label", "readme"}
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("every README language entry must be an object")
            continue
        missing = required_fields - entry.keys()
        if missing:
            errors.append(f"README language entry is missing fields: {sorted(missing)}")
            continue
        name = entry["name"]
        locale = entry["locale"]
        readme = entry["readme"]
        if not all(isinstance(entry[field], str) and entry[field].strip() for field in required_fields):
            errors.append(f"README language entry {name!r} has an empty or non-string field")
            continue
        if not re.fullmatch(r"[a-z]{2}(?:-[A-Z]{2})?", locale):
            errors.append(f"README language entry {name!r} has an invalid locale: {locale!r}")
        if Path(readme).is_absolute() or ".." in Path(readme).parts or not readme.endswith(".md"):
            errors.append(f"README language entry {name!r} has an unsafe README path: {readme!r}")
        elif not (ROOT / readme).is_file():
            errors.append(f"README language entry {name!r} points to a missing file: {readme}")
        valid_entries.append(entry)
        locales.append(locale)
        readmes.append(readme)
        expected_rows.append((name, locale, readme))

    if len(locales) != len(set(locales)):
        errors.append("README language locales must be unique")
    if len(readmes) != len(set(readmes)):
        errors.append("README language README paths must be unique")

    readme_text = README.read_text(encoding="utf-8")
    lines = readme_text.splitlines()
    try:
        header_index = lines.index("| Language | Locale | README |")
    except ValueError:
        errors.append("README must contain the generated language support table header")
    else:
        rows: list[tuple[str, str, str]] = []
        for line in lines[header_index + 2 :]:
            if not line.startswith("|"):
                break
            match = README_TABLE_ROW.fullmatch(line)
            if not match:
                errors.append(f"invalid README language support row: {line}")
                continue
            rows.append((match.group(1), match.group(2), match.group(3)))
        if rows != expected_rows:
            errors.append("README language support table does not match data/readme_languages.json")

    for entry in valid_entries:
        readme_text_path = ROOT / entry["readme"]
        if readme_text_path.is_file():
            text = readme_text_path.read_text(encoding="utf-8")
            for required_target in ("README.md", "LICENSE", "docs/comparison.md", "docs/languages.md"):
                if required_target not in text:
                    errors.append(f"{entry['readme']} is missing navigation target {required_target}")


def check_local_links(errors: list[str]) -> None:
    markdown_files = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        for raw_target in LOCAL_LINK_PATTERN.findall(text):
            target = unquote(raw_target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (source.parent / target).resolve()
            if ROOT not in resolved.parents and resolved != ROOT:
                errors.append(f"{source.relative_to(ROOT)} links outside the repository: {raw_target}")
            elif not resolved.is_file():
                errors.append(f"{source.relative_to(ROOT)} links to a missing file: {raw_target}")


def main() -> int:
    errors: list[str] = []
    if not README.is_file():
        errors.append("README.md is missing")
    if not LICENSE.is_file():
        errors.append("LICENSE is missing")
    elif "BSD Zero Clause License" not in LICENSE.read_text(encoding="utf-8"):
        errors.append("LICENSE must identify the BSD Zero Clause License")

    check_readme_languages(errors)
    check_local_links(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("validated repository links, README localization and license metadata")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
