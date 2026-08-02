# License Atlas

**A practical, SPDX-aware comparison of 50 commonly encountered licenses for software, documentation, fonts, content, and data.**

[![Validation](https://github.com/Yunushan/license-atlas/actions/workflows/validate.yml/badge.svg)](https://github.com/Yunushan/license-atlas/actions/workflows/validate.yml)
[![License: 0BSD](https://img.shields.io/badge/license-0BSD-blue.svg)](LICENSE)
[![SPDX](https://img.shields.io/badge/metadata-SPDX--aware-informational.svg)](https://spdx.org/licenses/)

License Atlas is a maintainer-friendly reference for comparing license obligations before choosing a license or adding a dependency. It combines a machine-readable catalog with human-readable comparison tables, practical decision guidance, and SPDX header examples for 20 widely used programming languages.

> This is educational reference material, not legal advice. Read the complete license text, inspect all dependency license expressions, and obtain professional advice for material commercial, distribution, patent, or compliance decisions.

## What is included?

- A curated catalog of **50 commonly encountered SPDX licenses and license families**.
- Side-by-side comparison of commercial use, modification, redistribution, notices, source disclosure, patent language, copyleft scope, and network obligations.
- Clear separation between software licenses and licenses intended for documentation, fonts, content, or databases.
- A top-level distinction between open-source licenses and source-available terms such as BUSL-1.1.
- SPDX identifiers and canonical SPDX references for automation and package metadata.
- Comment/header examples for **20 common programming languages**.
- A dependency-review checklist and compatibility cautions.
- A dependency-free Python validator and GitHub Actions workflow.

## Recommended repository name

`license-atlas` is the recommended name: it is short, descriptive, easy to search, and matches the project’s purpose as a map of license choices and obligations.

## Quick decision guide

| If you need… | Start by reviewing… | Main trade-off |
|---|---|---|
| Maximum simplicity and almost no license conditions | `0BSD`, `MIT-0`, `MIT` | The permissive licenses here do not provide the same express patent language as Apache-2.0. |
| Permissive reuse with an express patent grant | `Apache-2.0` | Preserve notices, mark changes, and understand patent-termination language. |
| A permissive license with a short attribution obligation | `MIT`, `BSD-2-Clause`, `ISC`, `Zlib` | Attribution and disclaimer notices still matter in redistribution. |
| Modifications to covered files to remain open while allowing proprietary files beside them | `MPL-2.0`, `EPL-2.0`, `CDDL-1.0` | File-level or source-file obligations can be easy to miss. |
| A library copyleft model | `LGPL-2.1-or-later`, `LGPL-3.0-or-later`, `CECILL-C` | Static linking, relinking, reverse engineering, and modification rules require careful review. |
| The whole distributed derivative work to remain under a strong copyleft license | `GPL-2.0-or-later`, `GPL-3.0-or-later`, `EUPL-1.2`, `CECILL-2.1` | Distribution triggers source and licensing obligations; compatibility is version-specific. |
| Source availability for users interacting with a network service | `AGPL-3.0-only` | Network interaction can trigger an offer of corresponding source code. |
| Open data with attribution | `ODC-By-1.0`, `CC-BY-4.0` | Choose a data/content license deliberately; software licenses are usually a poor fit for datasets. |
| A font license | `OFL-1.1` | Reserved Font Names and font-specific redistribution rules can apply. |
| A time-delayed or use-limited business license | `BUSL-1.1` | It is source-available, not an OSI-approved open-source license. |

## License catalog

The source of truth is [`data/licenses.json`](data/licenses.json). The readable, generated comparison is [`docs/comparison.md`](docs/comparison.md).

For the most common GPL, LGPL, Apache, MIT, BSD, MPL, EPL, AGPL, Creative Commons, and source-available questions, see the high-level [`docs/compatibility.md`](docs/compatibility.md) guide.

The catalog intentionally uses a **practical reference order**, not a claim that there is one universally accepted popularity ranking. License adoption varies by ecosystem, project type, and the way a dataset counts license families and version variants.

### The 50 entries

| # | SPDX identifier | License | Primary scope |
|---:|---|---|---|
| 1 | `0BSD` | BSD Zero Clause License | Software |
| 2 | `MIT` | MIT License | Software |
| 3 | `MIT-0` | MIT No Attribution | Software |
| 4 | `BSD-2-Clause` | BSD 2-Clause | Software |
| 5 | `BSD-3-Clause` | BSD 3-Clause | Software |
| 6 | `BSD-4-Clause` | BSD 4-Clause | Software |
| 7 | `ISC` | ISC License | Software |
| 8 | `Apache-2.0` | Apache License 2.0 | Software |
| 9 | `Zlib` | zlib License | Software |
| 10 | `PostgreSQL` | PostgreSQL License | Software |
| 11 | `Unlicense` | The Unlicense | Software |
| 12 | `BSL-1.0` | Boost Software License 1.0 | Software |
| 13 | `Artistic-2.0` | Artistic License 2.0 | Software |
| 14 | `Python-2.0` | Python License 2.0 | Software |
| 15 | `PHP-3.01` | PHP License 3.01 | Software |
| 16 | `OpenSSL` | OpenSSL License | Software |
| 17 | `libpng` | libpng License | Software |
| 18 | `NCSA` | University of Illinois/NCSA Open Source License | Software |
| 19 | `AFL-3.0` | Academic Free License 3.0 | Software |
| 20 | `BlueOak-1.0.0` | Blue Oak Model License 1.0.0 | Software |
| 21 | `MS-PL` | Microsoft Public License | Software |
| 22 | `MS-RL` | Microsoft Reciprocal License | Software |
| 23 | `MPL-2.0` | Mozilla Public License 2.0 | Software |
| 24 | `EPL-2.0` | Eclipse Public License 2.0 | Software |
| 25 | `CDDL-1.0` | Common Development and Distribution License 1.0 | Software |
| 26 | `LGPL-2.1-only` | GNU LGPL 2.1 only | Software |
| 27 | `LGPL-2.1-or-later` | GNU LGPL 2.1 or later | Software |
| 28 | `LGPL-3.0-only` | GNU LGPL 3.0 only | Software |
| 29 | `LGPL-3.0-or-later` | GNU LGPL 3.0 or later | Software |
| 30 | `GPL-2.0-only` | GNU GPL 2.0 only | Software |
| 31 | `GPL-2.0-or-later` | GNU GPL 2.0 or later | Software |
| 32 | `GPL-3.0-only` | GNU GPL 3.0 only | Software |
| 33 | `GPL-3.0-or-later` | GNU GPL 3.0 or later | Software |
| 34 | `AGPL-3.0-only` | GNU AGPL 3.0 only | Software |
| 35 | `EUPL-1.2` | European Union Public License 1.2 | Software |
| 36 | `OSL-3.0` | Open Software License 3.0 | Software |
| 37 | `CECILL-2.1` | CeCILL 2.1 | Software |
| 38 | `CECILL-C` | CeCILL-C | Software |
| 39 | `QPL-1.0` | Q Public License 1.0 | Software |
| 40 | `Sleepycat` | Sleepycat License | Software |
| 41 | `GFDL-1.3-only` | GNU Free Documentation License 1.3 only | Documentation |
| 42 | `OFL-1.1` | SIL Open Font License 1.1 | Fonts |
| 43 | `CC0-1.0` | Creative Commons Zero 1.0 | Content/data |
| 44 | `CC-BY-4.0` | Creative Commons Attribution 4.0 | Content/data |
| 45 | `CC-BY-SA-4.0` | Creative Commons Attribution-ShareAlike 4.0 | Content/data |
| 46 | `CC-BY-NC-4.0` | Creative Commons Attribution-NonCommercial 4.0 | Content/data |
| 47 | `CC-BY-ND-4.0` | Creative Commons Attribution-NoDerivatives 4.0 | Content/data |
| 48 | `ODC-By-1.0` | Open Data Commons Attribution 1.0 | Databases |
| 49 | `ODbL-1.0` | Open Data Commons Open Database License 1.0 | Databases |
| 50 | `BUSL-1.1` | Business Source License 1.1 | Source-available |

## Supported languages

The project includes SPDX header templates and packaging notes for 20 common languages. The list is practical ecosystem coverage rather than a claim of a single authoritative global ranking.

| Language | Typical source extensions |
|---|---|
| C | `.c`, `.h` |
| C++ | `.cc`, `.cpp`, `.cxx`, `.hpp` |
| C# | `.cs` |
| Java | `.java` |
| Python | `.py` |
| JavaScript | `.js`, `.jsx`, `.mjs`, `.cjs` |
| TypeScript | `.ts`, `.tsx` |
| Go | `.go` |
| Rust | `.rs` |
| PHP | `.php` |
| Ruby | `.rb` |
| Swift | `.swift` |
| Kotlin | `.kt`, `.kts` |
| Dart | `.dart` |
| R | `.r`, `.R` |
| Lua | `.lua` |
| Perl | `.pl`, `.pm` |
| Haskell | `.hs`, `.lhs` |
| Scala | `.scala`, `.sc` |
| Objective-C | `.m`, `.mm`, `.h` |

See [`docs/languages.md`](docs/languages.md) for copy-ready headers.

## Using the catalog responsibly

1. Identify the exact license identifier and version. `GPL-3.0-only` and `GPL-3.0-or-later` are different choices.
2. Read the complete license text and any exception, notice, `NOTICE`, or contributor terms.
3. Review the complete dependency graph, including transitive dependencies and generated artifacts.
4. Preserve required copyright, license, and attribution notices in the distribution format required by the license.
5. Mark material changes when the license requires it.
6. For copyleft licenses, determine whether your use creates a derivative work, combined work, modified file, linked library, conveyed product, or network interaction covered by the license.
7. Treat patent, trademark, privacy, export-control, and third-party asset obligations as separate review topics.
8. Record the final decision in a `LICENSE`, `COPYING`, `NOTICE`, or third-party notices file appropriate to the project.

### SPDX examples

```text
SPDX-License-Identifier: MIT
SPDX-License-Identifier: Apache-2.0
SPDX-License-Identifier: GPL-3.0-or-later
SPDX-License-Identifier: MIT OR Apache-2.0
```

An SPDX identifier is a precise label; it does not remove the obligation to comply with the full license text. License expressions may also use exceptions, for example `GPL-3.0-only WITH Classpath-exception-2.0`; exceptions are not included as stand-alone entries in this 50-license catalog.

## Development

The project intentionally has no runtime dependencies.

```bash
python3 scripts/validate.py
python3 scripts/generate_catalog.py
python3 scripts/generate_catalog.py --check
```

The GitHub Actions workflow runs the validator and verifies that generated documentation is synchronized with the JSON source data.

## Sources and further reading

- [SPDX License List](https://spdx.org/licenses/) — identifiers, canonical license pages, and license text references.
- [Open Source Initiative approved licenses](https://opensource.org/licenses) — OSI approval and Open Source Definition context.
- [GNU license compatibility guidance](https://www.gnu.org/licenses/license-compatibility.html) — GPL/LGPL compatibility discussion.
- [Choose a License](https://choosealicense.com/) — practical license-selection guidance from GitHub.
- [Choose a License: non-software works](https://choosealicense.com/non-software/) — guidance for data, media, documentation, and fonts.

## Contributing

Contributions are welcome when they improve factual accuracy, source links, readability, validation, or language coverage. See [`CONTRIBUTING.md`](CONTRIBUTING.md). Please update `data/licenses.json` or `data/languages.json` first and regenerate the documentation rather than editing generated files manually.

## License

The License Atlas project is released under the [0BSD License](LICENSE).
