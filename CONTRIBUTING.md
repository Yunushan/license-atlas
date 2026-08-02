# Contributing to License Atlas

Thank you for improving the catalog.

## Source of truth

- Edit `data/licenses.json` for license entries.
- Edit `data/languages.json` for language coverage.
- Add localized README overviews as `README.<locale>.md`; keep `README.md` as the canonical source.
- Run `python3 scripts/generate_catalog.py` to regenerate the readable documents.
- Do not edit `docs/comparison.md` or `docs/languages.md` manually; CI verifies that they match the data.

## Accuracy standards

- Use the exact SPDX identifier and version.
- Link to a canonical SPDX license page.
- Describe obligations cautiously and avoid absolute legal conclusions.
- Keep software, documentation, font, content, database, and source-available scopes distinct.
- Explain compatibility as a starting point for review, not as a blanket legal guarantee.
- Preserve license identifiers, legal notices, links, and compatibility cautions in translated README files.

## Pull requests

Please include the reason for a change, authoritative references, and the output of:

```bash
python3 scripts/validate.py
python3 scripts/generate_catalog.py --check
```
