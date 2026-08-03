# Release and maintenance runbook

License Atlas is a documentation and reference repository. A release publishes a reviewed snapshot of the catalog and its generated documentation; it does not deploy a runtime service.

## Required release gates

Run these commands from a clean checkout before opening a release pull request:

```bash
python3 scripts/validate.py
python3 scripts/check_repository.py
python3 scripts/generate_catalog.py --check
python3 -m compileall -q scripts tests
python3 -m unittest discover -s tests -v
```

The GitHub Actions `Validate catalog` workflow must pass on the release commit. Review the generated diff after changing either source JSON file, and verify every new external reference against an authoritative source.

## Versioning

Use semantic version tags in the form `vMAJOR.MINOR.PATCH`. Before tagging:

1. Move the relevant `Unreleased` changelog entries into a dated release section.
2. Review license identifiers, canonical SPDX links, generated documents, and localized README navigation.
3. Merge through a reviewed pull request after the required status check passes.
4. Create a GitHub release pointing to the exact release tag and summarize content or accuracy changes.

## Repository settings

The default `main` branch should require pull requests, CODEOWNERS review, and the successful `validate` status check. Force-push and branch deletion should be disabled. Keep Dependabot updates enabled for GitHub Actions and use private GitHub security advisories for security reports.

## Recovery

Because the repository has no runtime state, recovery is version-control based: revert the offending commit or restore the previous release tag, then rerun every release gate before publishing a replacement release.
