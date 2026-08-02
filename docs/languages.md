<!-- GENERATED FILE. Edit data/languages.json and run scripts/generate_catalog.py. -->
# SPDX header guide for 20 common languages

This guide contains copy-ready header examples. Replace the sample identifier with the exact identifier used by the project. A source-file header supplements a project-level `LICENSE`; it does not replace the complete license text or required notices.

## Coverage matrix

| Language | Extensions | Comment style | Example header |
|---|---|---|---|
| C | `.c`, `.h` | block | `/* SPDX-License-Identifier: MIT */` |
| C++ | `.cc`, `.cpp`, `.cxx`, `.hpp` | block | `/* SPDX-License-Identifier: Apache-2.0 */` |
| C# | `.cs` | line | `// SPDX-License-Identifier: MIT` |
| Java | `.java` | line | `// SPDX-License-Identifier: Apache-2.0` |
| Python | `.py` | hash | `# SPDX-License-Identifier: MIT` |
| JavaScript | `.js`, `.jsx`, `.mjs`, `.cjs` | line | `// SPDX-License-Identifier: MIT` |
| TypeScript | `.ts`, `.tsx` | line | `// SPDX-License-Identifier: Apache-2.0` |
| Go | `.go` | line | `// SPDX-License-Identifier: BSD-3-Clause` |
| Rust | `.rs` | line | `// SPDX-License-Identifier: MIT OR Apache-2.0` |
| PHP | `.php` | line | `// SPDX-License-Identifier: MIT` |
| Ruby | `.rb` | hash | `# SPDX-License-Identifier: MIT` |
| Swift | `.swift` | line | `// SPDX-License-Identifier: Apache-2.0` |
| Kotlin | `.kt`, `.kts` | line | `// SPDX-License-Identifier: Apache-2.0` |
| Dart | `.dart` | line | `// SPDX-License-Identifier: BSD-3-Clause` |
| R | `.r`, `.R` | hash | `# SPDX-License-Identifier: GPL-3.0-or-later` |
| Lua | `.lua` | line | `-- SPDX-License-Identifier: MIT` |
| Perl | `.pl`, `.pm` | hash | `# SPDX-License-Identifier: Artistic-2.0` |
| Haskell | `.hs`, `.lhs` | line | `-- SPDX-License-Identifier: BSD-3-Clause` |
| Scala | `.scala`, `.sc` | line | `// SPDX-License-Identifier: Apache-2.0` |
| Objective-C | `.m`, `.mm`, `.h` | block | `/* SPDX-License-Identifier: MIT */` |

## Language notes

### C

```text
/* SPDX-License-Identifier: MIT */
```

Keep a project-level LICENSE file; headers are useful for individual source files and generated C headers.

### C++

```text
/* SPDX-License-Identifier: Apache-2.0 */
```

Apply the chosen identifier consistently across templates, headers, and compiled library sources.

### C#

```text
// SPDX-License-Identifier: MIT
```

For NuGet packages, also publish the license expression or license file metadata required by the package format.

### Java

```text
// SPDX-License-Identifier: Apache-2.0
```

Maven and Gradle metadata should agree with the repository LICENSE and any bundled dependency notices.

### Python

```text
# SPDX-License-Identifier: MIT
```

Publish the license in project metadata and include it in source distributions and wheels when appropriate.

### JavaScript

```text
// SPDX-License-Identifier: MIT
```

Keep package.json license metadata, source headers, and bundled third-party notices aligned.

### TypeScript

```text
// SPDX-License-Identifier: Apache-2.0
```

Check both TypeScript source and generated JavaScript distribution artifacts for notice handling.

### Go

```text
// SPDX-License-Identifier: BSD-3-Clause
```

Go modules can include dependencies with different licenses; audit go.mod and transitive modules.

### Rust

```text
// SPDX-License-Identifier: MIT OR Apache-2.0
```

Cargo.toml license or license-file metadata should match the source and distribution terms.

### PHP

```text
// SPDX-License-Identifier: MIT
```

Composer package metadata and bundled dependencies should be checked separately.

### Ruby

```text
# SPDX-License-Identifier: MIT
```

Gem metadata, gemspec files, and vendored dependencies may have separate notice obligations.

### Swift

```text
// SPDX-License-Identifier: Apache-2.0
```

Swift Package Manager manifests should describe the same license choice as the repository.

### Kotlin

```text
// SPDX-License-Identifier: Apache-2.0
```

Review Gradle dependency reports and packaged NOTICE files for Android and JVM distributions.

### Dart

```text
// SPDX-License-Identifier: BSD-3-Clause
```

pubspec metadata and Flutter release bundles should preserve third-party license notices.

### R

```text
# SPDX-License-Identifier: GPL-3.0-or-later
```

CRAN package DESCRIPTION metadata and installed source files should use compatible terms.

### Lua

```text
-- SPDX-License-Identifier: MIT
```

Include the license in rockspec or package metadata when publishing a reusable module.

### Perl

```text
# SPDX-License-Identifier: Artistic-2.0
```

CPAN metadata, module headers, and bundled modules can carry different licenses.

### Haskell

```text
-- SPDX-License-Identifier: BSD-3-Clause
```

Cabal or Hackage metadata should remain consistent with source and distribution files.

### Scala

```text
// SPDX-License-Identifier: Apache-2.0
```

sbt or Maven publication metadata should include license and NOTICE information.

### Objective-C

```text
/* SPDX-License-Identifier: MIT */
```

Framework bundles and CocoaPods or Swift Package Manager metadata may need separate notice handling.

## Header practice

- Use the SPDX identifier that matches the complete project license.
- If a file combines differently licensed material, use a precise SPDX expression or a clearly documented file-level arrangement.
- Do not copy a dependency's header into your own original code without understanding the boundary between the works.
- Keep generated files, vendored code, examples, tests, and documentation examples under an intentional licensing policy.
- Keep the repository `LICENSE`, package metadata, release archives, and source headers consistent.
