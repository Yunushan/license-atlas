# High-level compatibility guide

This guide is intentionally directional. License compatibility depends on the exact license version, SPDX expression, exception, work boundary, linking model, distribution method, and jurisdiction. `Generally yes` below means “often possible after preserving conditions,” not “automatically approved for every project.”

## Common combinations

| Combination | High-level result | What still needs review |
|---|---|---|
| MIT, MIT-0, 0BSD, ISC, BSD-2-Clause into GPL-2.0 | Generally yes | Preserve notices; BSD-4-Clause and advertising-style variants are different. |
| MIT, MIT-0, 0BSD, ISC, BSD-2-Clause into GPL-3.0 | Generally yes | Preserve notices and follow GPL source/distribution obligations. |
| BSD-3-Clause into GPL-2.0 or GPL-3.0 | Generally yes | Preserve the non-endorsement clause and the original notices. |
| BSD-4-Clause into GPL-2.0 or GPL-3.0 | No automatic compatibility | The advertising clause can add terms that conflict with copyleft requirements. |
| Apache-2.0 into GPL-3.0 | Generally yes | Preserve Apache notices, mark changes, and account for patent terms. |
| Apache-2.0 into GPL-2.0-only | Not automatically compatible | Apache-2.0’s additional terms, especially patent language, are not accepted by GPL-2.0-only. |
| GPL-2.0-only with GPL-3.0-only | Generally incompatible | The “only” versions cannot simply be mixed or relicensed without permission from all relevant copyright holders. |
| GPL-2.0-or-later with GPL-3.0 | Often possible | The or-later option can allow GPL-3.0 selection, but every component and exception must permit the same result. |
| LGPL-2.1 with GPL-2.0 | Often possible in the permitted cases | Library relinking, source, reverse-engineering, and combined-work rules still apply. |
| LGPL-3.0 with GPL-3.0 | Often possible in the permitted cases | The LGPL-3.0 and GPL-3.0 terms control the resulting work; preserve the library obligations. |
| MPL-2.0 with proprietary files | Often possible | Keep MPL-covered files under MPL-2.0 and provide source for covered modifications. |
| MPL-2.0 with GPL-family code | Sometimes possible | MPL-2.0’s secondary-license option and the exact file boundary must be checked. |
| EPL-2.0 with GPL-family code | Sometimes possible | EPL-2.0 has a secondary-license pathway, but it is not a blanket compatibility promise. |
| CDDL-1.0 with GPL-2.0-only | Commonly treated as incompatible | Do not combine based only on both being open source; analyze the file-level terms. |
| AGPL-3.0 with a hosted service | Network obligations may apply | Users interacting with a modified service may need access to corresponding source. |
| GPL-3.0 with AGPL-3.0 | Not interchangeable by default | AGPL-3.0 includes network-use obligations beyond GPL-3.0. |
| CC-BY or CC-BY-SA with documentation | Often appropriate | Preserve attribution and indicate changes; document what material is covered. |
| CC-BY-NC or CC-BY-ND with software | Not recommended | NonCommercial and NoDerivatives terms conflict with common software freedom and modification goals. |
| ODbL database with software using the database | Fact-dependent | Separate the database, its contents, and produced works; apply the correct database terms. |
| BUSL-1.1 with an open-source project | Not an OSI open-source combination | Read the Use Limitation, Additional Use Grant, Change Date, and Change License. |

## GPLv2 versus GPLv3

`GPL-2.0-only` and `GPL-3.0-only` are separate licenses, not interchangeable labels. GPLv3 adds or changes provisions concerning patents, anti-tivoization, DRM-related restrictions, and other distribution conditions. A project using GPL-2.0-or-later may have more options than one using GPL-2.0-only, because copyright holders have authorized use under later GPL versions.

Before combining GPL code:

1. Record the exact SPDX expression for every GPL component.
2. Check whether the component is `only`, `or-later`, or paired with an exception.
3. Identify which work is being distributed and whether it is linked, combined, or merely shipped alongside another independent work.
4. Confirm that all copyright holders have granted the permissions needed for the final license.

## MIT versus Apache-2.0

Both are permissive and commonly used for commercial-friendly software. MIT is shorter and mainly requires preserving copyright and permission notices. Apache-2.0 is longer and adds an express patent license, patent-termination language, NOTICE handling, change marking, and trademark limitations. Choose Apache-2.0 when its explicit patent and notice framework is valuable; choose MIT when minimal text and broad familiarity are the priority.

## File-level versus project-level copyleft

MPL-2.0, EPL-2.0, CDDL-1.0, MS-PL, and MS-RL are often described as file-level or weak copyleft. That does not mean “no source obligations.” It means the reciprocal obligation is usually focused on covered files or modifications rather than every file in a larger combined application. The exact definition of a covered file, modification, executable, or larger work controls the result.

## Open-source status matters

Creative Commons licenses are designed primarily for content, media, and data—not software. BUSL-1.1 is source-available during its restricted period, not an OSI-approved open-source license. A license can be generous in some contexts and still be unsuitable for an open-source software project, package ecosystem, or downstream compliance policy.

## References

- [SPDX License List](https://spdx.org/licenses/)
- [GNU license compatibility](https://www.gnu.org/licenses/license-compatibility.html)
- [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.html)
- [Open Source Initiative licenses](https://opensource.org/licenses)
- [Choose a License: non-software](https://choosealicense.com/non-software/)
