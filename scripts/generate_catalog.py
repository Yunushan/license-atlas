#!/usr/bin/env python3
"""Generate the human-readable License Atlas documents from JSON data."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LICENSE_DATA = ROOT / "data" / "licenses.json"
LANGUAGE_DATA = ROOT / "data" / "languages.json"
COMPARISON_DOC = ROOT / "docs" / "comparison.md"
LANGUAGE_DOC = ROOT / "docs" / "languages.md"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def display(value: str) -> str:
    return {
        "yes": "Yes",
        "no": "No",
        "conditional": "Conditional",
        "limited": "Limited",
        "no-for-distribution": "No for distributed adaptations",
        "not-applicable": "N/A",
        "not-required": "Not required",
        "required-on-distribution": "Required on distribution",
        "required-for-covered-source": "Required for covered source",
        "required-for-covered-files": "Required for covered files",
        "required-for-covered-modifications": "Required for covered modifications",
        "required-on-distribution-and-network-use": "Required on distribution and network use",
        "required-on-distribution-and-external-deployment": "Required on distribution and external deployment",
        "required-for-database-derivatives": "Required for database derivatives",
        "none": "None",
        "none-stated": "None stated",
        "explicit": "Explicit",
        "limited": "Limited",
        "copyright-and-license": "Copyright and license",
        "copyright-license-and-notice": "Copyright, license, and NOTICE",
        "copyright-license-and-disclaimer": "Copyright, license, and disclaimer",
        "copyright-license-and-acknowledgement": "Copyright, license, and acknowledgement",
        "copyright-license-and-changes": "Copyright, license, and changes",
        "copyright-license-and-source": "Copyright, license, and source",
        "copyright-license-and-font-name": "Copyright, license, and font name",
        "attribution": "Attribution",
        "limited": "Limited",
    }.get(value, value.replace("-", " ").capitalize())


def markdown_list(values: list[str]) -> str:
    return "\n".join(f"- {value}" for value in values)


def build_comparison(licenses: list[dict]) -> str:
    lines = [
        "<!-- GENERATED FILE. Edit data/licenses.json and run scripts/generate_catalog.py. -->",
        "# License Atlas: detailed comparison",
        "",
        "This document is generated from [`data/licenses.json`](../data/licenses.json). It is a practical summary, not a replacement for the complete license text.",
        "",
        "## How to read the matrix",
        "",
        "- **Commercial use** describes whether the license generally permits commercial use, not whether a product is free of other legal or contractual obligations.",
        "- **Source availability** describes when source or editable material must be supplied. It does not mean every user must receive source code in every scenario.",
        "- **Copyleft** is a simplified classification. The exact trigger depends on the license definitions, the work structure, linking, modification, distribution, and sometimes network access.",
        "- **Patent** records whether the license contains an express patent grant, not whether the project has no patent risk.",
        "- **N/A** means the field is not a meaningful software-license axis for the primary scope of the entry.",
        "",
        "## Comparison matrix",
        "",
        "| # | SPDX | Name | Category | Commercial | Modify | Redistribute | Source availability | Notice | Patent | Copyleft | Scope |",
        "|---:|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for item in licenses:
        lines.append(
            "| {rank} | [`{id}`]({reference_url}) | {name} | {category} | {commercial} | {modification} | {redistribution} | {source} | {notice} | {patent} | {copyleft} | {scope} |".format(
                rank=item["rank"],
                id=item["id"],
                reference_url=item["reference_url"],
                name=item["name"],
                category=item["category"],
                commercial=display(item["commercial_use"]),
                modification=display(item["modification"]),
                redistribution=display(item["redistribution"]),
                source=display(item["source_availability"]),
                notice=display(item["notice"]),
                patent=display(item["patent"]),
                copyleft=display(item["copyleft"]),
                scope=item["scope"],
            )
        )

    lines.extend(["", "## Detailed profiles", ""])
    for item in licenses:
        lines.extend(
            [
                f"### {item['rank']}. {item['name']} (`{item['id']}`)",
                "",
                f"- **Reference:** [{item['id']}]({item['reference_url']})",
                f"- **Family:** {item['family']}",
                f"- **Primary scope:** {item['scope']}",
                f"- **Category:** {item['category']}",
                f"- **Commercial use:** {display(item['commercial_use'])}",
                f"- **Private use:** {display(item['private_use'])}",
                f"- **Modification:** {display(item['modification'])}",
                f"- **Redistribution:** {display(item['redistribution'])}",
                f"- **Source availability:** {display(item['source_availability'])}",
                f"- **Notice:** {display(item['notice'])}",
                f"- **Patent language:** {display(item['patent'])}",
                f"- **Copyleft scope:** {display(item['copyleft'])}",
                "- **Conditions:**",
                markdown_list(item["conditions"]),
                f"- **Best for:** {item['best_for']}",
                f"- **Watch out:** {item['watch_out']}",
                f"- **Compatibility note:** {item['compatibility']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Compatibility checklist",
            "",
            "1. Compare the exact SPDX identifiers, including `only` versus `or-later` variants.",
            "2. Check whether the dependency is modified, linked, combined, distributed, embedded, or only used as an independent service.",
            "3. Preserve copyright, license, NOTICE, attribution, and source-offer material in the correct distribution location.",
            "4. Review license exceptions and SPDX expressions; an exception can change the result materially.",
            "5. Confirm patent, trademark, privacy, export, and third-party asset obligations independently.",
            "6. Use the complete license text and qualified legal review for high-risk or commercial decisions.",
            "",
        ]
    )
    return "\n".join(lines)


def build_languages(languages: list[dict]) -> str:
    lines = [
        "<!-- GENERATED FILE. Edit data/languages.json and run scripts/generate_catalog.py. -->",
        "# SPDX header guide for 20 common languages",
        "",
        "This guide contains copy-ready header examples. Replace the sample identifier with the exact identifier used by the project. A source-file header supplements a project-level `LICENSE`; it does not replace the complete license text or required notices.",
        "",
        "## Coverage matrix",
        "",
        "| Language | Extensions | Comment style | Example header |",
        "|---|---|---|---|",
    ]
    for item in languages:
        lines.append(
            f"| {item['name']} | {', '.join(f'`{ext}`' for ext in item['extensions'])} | {item['comment_style']} | `{item['header']}` |"
        )

    lines.extend(["", "## Language notes", ""])
    for item in languages:
        lines.extend(
            [
                f"### {item['name']}",
                "",
                f"```text\n{item['header']}\n```",
                "",
                f"{item['ecosystem_note']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Header practice",
            "",
            "- Use the SPDX identifier that matches the complete project license.",
            "- If a file combines differently licensed material, use a precise SPDX expression or a clearly documented file-level arrangement.",
            "- Do not copy a dependency's header into your own original code without understanding the boundary between the works.",
            "- Keep generated files, vendored code, examples, tests, and documentation examples under an intentional licensing policy.",
            "- Keep the repository `LICENSE`, package metadata, release archives, and source headers consistent.",
            "",
        ]
    )
    return "\n".join(lines)


def write_or_check(path: Path, content: str, check: bool) -> bool:
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            print(f"out of date: {path.relative_to(ROOT)}", file=sys.stderr)
            return False
        return True
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail when generated files are not synchronized")
    args = parser.parse_args()

    licenses = load_json(LICENSE_DATA)
    languages = load_json(LANGUAGE_DATA)
    ok = write_or_check(COMPARISON_DOC, build_comparison(licenses), args.check)
    ok = write_or_check(LANGUAGE_DOC, build_languages(languages), args.check) and ok
    if not args.check:
        print(f"generated {COMPARISON_DOC.relative_to(ROOT)}")
        print(f"generated {LANGUAGE_DOC.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
