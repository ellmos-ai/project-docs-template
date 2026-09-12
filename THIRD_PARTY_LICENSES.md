# Third-Party Licenses & Software Bill of Materials (SBOM)

**Repository:** `ellmos-ai/project-docs-template`  
**License:** MIT License  
**Audit Date:** 2026-09-12  
**Status:** Clean — Zero Runtime Dependencies  

---

## 1. Runtime Dependencies Overview

`project-docs-template` operates under a **strict Zero-Runtime-Dependency invariant** (`dependencies = []`).
At runtime, project generation, upgrade management, validation, and archival rely exclusively on the Python standard library.

| Package | Version Range | License | Direct/Transitive | Purpose |
|---|---|---|---|---|
| *(none)* | — | — | — | Pure Python standard library implementation |

### Standard Library Modules Utilized
- `argparse`, `sys`, `pathlib`, `shutil`, `tempfile` (CLI arguments, filesystem, staging)
- `json`, `re`, `ast`, `importlib` (Manifest parsing, link verification, syntax validation)
- `subprocess`, `unittest`, `datetime` (Subprocess invocation, testing, time anchors)

---

## 2. Development, Test & Build Dependencies

These tools are utilized exclusively for development, automated contract testing, release gate validation, and packaging. They are never distributed or loaded at template execution time.

| Package | Ecosystem | License | Primary Purpose |
|---|---|---|---|
| `pytest` | PyPI | MIT License | Test discovery and test runner |
| `ruff` | PyPI / Rust | MIT / Apache-2.0 | Fast static analysis, linting, and style enforcement |
| `setuptools` | PyPI | MIT License | PEP 517/518 build system backend |

---

## 3. Dependency-Confusion & Supply-Chain Invariant

1. **Unregistered PyPI Namespace Disclaimer:**  
   `project-docs-template` is maintained as a template repository and developer scaffold. It is not published to the public PyPI index. Installing via `pip install project-docs-template` without explicit private repository configuration must be avoided to eliminate dependency-confusion attack vectors.

2. **Supply-Chain Pinning in CI:**  
   All automated GitHub Actions workflows (`.github/workflows/ci.yml`) strictly pin external actions to full 40-character commit SHAs rather than mutable tags or branches.

3. **Zero-Egress & Local-First Invariant:**  
   No external telemetry, web beacons, remote calls, or phone-home requests are initiated by the template or its maintenance utilities. Execution is 100% local-first and air-gap compliant.
