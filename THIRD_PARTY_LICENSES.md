# Third-Party Licenses & Software Bill of Materials (SBOM)

> **Project:** `ellmos-ai/project-docs-template`
> **Audit Date:** 2026-09-20
> **Repository License:** [MIT License](LICENSE)
> **Attribution:** [NOTICE](NOTICE)
> **Architecture & Privacy:** 100% Local-First, Zero-Egress, Unprivileged User-Mode (`RunAsInvoker`), Fail-Closed

---

## 1. Executive Summary & Compliance Assurance

`project-docs-template` operates under strict architectural and governance invariants: **100% Local-First, Zero-Egress by default, unprivileged user-mode execution (`RunAsInvoker`), and fail-closed staging semantics**. All scaffold generation, profile upgrade management, doc linting, workflow synchronization, and task archival routines operate entirely within local process and filesystem boundaries.

The repository operates under a strict **Zero-Runtime-Dependency invariant** (`dependencies = []`). All runtime generation and maintenance tools rely exclusively on the Python standard library (3.10+).

All direct, development, build, and test dependencies utilized across `project-docs-template` are distributed under strictly **permissive and free open-source licenses** (MIT, Apache-2.0, PSFL). There are **zero AGPL, GPL, or restrictive copyleft constraints**, ensuring maximum portability for multi-device setups, corporate environments, air-gapped workstations, and automated multi-agent fleets.

Furthermore, `project-docs-template` guarantees:
1. **Zero-Egress & Local-First Invariant (INV-LOCAL-01):** Operates entirely on local filesystems and local storage mounts. Zero network telemetry, zero phone-home calls, and zero external analytical tracking.
2. **Unprivileged User-Mode Execution (`RunAsInvoker` / INV-SEC-02):** Executes safely in unprivileged user space without requiring root or administrator elevation.
3. **Fail-Closed Staging Semantics (INV-FAIL-03):** When a generation or upgrade encounters dirty directories, collision states, or unparseable YAML frontmatter, execution aborts safely without mutating existing project assets.
4. **Transactional & Merge-Safe Staging (INV-STG-04):** Upgrades verify SHA-256 hashes against `.project-docs-template.json` manifests. Any modified or unowned file triggers a clean rollback rather than silent corruption.
5. **Multi-Agent Session Handoff & Memory (INV-HANDOFF-05):** Predictable plain-text contracts (`CLAUDE.md`, `AGENTS.md`, `START.md`, `STATE.md`) guarantee deterministic agent context and session handoffs.
6. **Tiered Scalable Profiles (INV-TIER-06):** Three curated documentation profiles (`MINIMAL`, `STANDARD`, `FULL`) prevent documentation bloat and scale with project complexity.
7. **Multi-Host Cloud-Sync Defense (INV-SYNC-07):** Both root and scaffold `.gitignore` files defend against cloud synchronization conflicts (`* (kopie)*`, `*-WORKSTATION*`, `*-ASUS-GEI*`) and canonical lock files.
8. **Human-Readable Backlog & Atomic Archival (INV-AUDIT-08):** Plain-text Markdown task tracking (`TODO.md`, `DONE.md`) with transactional two-file atomic archival (`todo-archive`).
9. **100% Permissive Audited Dependency Stack (INV-LIC-09):** Zero external runtime dependencies; development and testing tools are strictly MIT/PSFL/Apache-2.0 audited.
10. **Dual Security Response SLA (INV-SLA-10):** Committed 48-hour response and 5-business-day triage window via canonical security contacts (`security@ellmos.ai`, `security@open-bricks.org`, `support@lukasgeiger.com`).

---

## 2. Level 1 Software Bill of Materials (SBOM)

| Component / Artifact | Type | Declared License | Upstream Source | Copyleft / AGPL | Role & Scope |
|:---|:---|:---|:---|:---|:---|
| **Python Standard Library** | Runtime Core | [PSFL-2.0](https://docs.python.org/3/license.html) | [python/cpython](https://github.com/python/cpython) | **None** (100% Permissive) | CLI, filesystem, json, re, ast, tempfile, staging, tests |
| **pytest** | Development / Test | [MIT](https://github.com/pytest-dev/pytest/blob/main/LICENSE) | [pytest-dev/pytest](https://github.com/pytest-dev/pytest) | **None** (100% Permissive) | Automated test execution and contract verification runner |
| **ruff** | Development / QA | [MIT / Apache-2.0](https://github.com/astral-sh/ruff/blob/main/LICENSE-MIT) | [astral-sh/ruff](https://github.com/astral-sh/ruff) | **None** (100% Permissive) | Static analysis, linting, and formatting gate |
| **setuptools** | Build Backend | [MIT](https://github.com/pypa/setuptools/blob/main/LICENSE) | [pypa/setuptools](https://github.com/pypa/setuptools) | **None** (100% Permissive) | PEP 517 / PEP 621 packaging build backend |

### Zero-Runtime-Dependency & Zero-Copyleft Isolation Guarantee

The core runtime and scaffolding tools of `project-docs-template` execute with **zero external dependencies** (`dependencies = []` in `pyproject.toml`):
- **Zero-Runtime-Dependency Guarantee**: Pure Python standard library (3.10+) provides 100% of all template generation, manifest checking, doc linting, workflow sync, and task archival logic.
- **Zero-Copyleft Isolation Guarantee**: 0% GPL, 0% LGPL, 0% AGPL, and 0% reciprocal licenses at runtime or in build paths. All dependencies are MIT, Apache-2.0, or PSFL-2.0.
- **Unprivileged User-Mode Execution (`RunAsInvoker`)**: Never attempts administrative privilege escalation, UAC prompts, or root filesystem writes. Operates strictly within user-invoked directories.

---

## 3. Invariant Cross-Reference Matrix

| Invariant ID | Name & Semantic Contract | Verification Mechanism & Implementation Component |
|:---|:---|:---|
| **INV-LOCAL-01** | 100% Local-First & Zero-Egress | `template/_tools/*`, `tests/test_metadata.py::test_offline_and_privacy_invariants` |
| **INV-SEC-02** | Unprivileged User-Mode (`RunAsInvoker`) | `template/_tools/init-project`, user-space filesystem writes only |
| **INV-FAIL-03** | Fail-Closed Default Semantics | `template/_tools/init-project`, refuses existing dirty or unowned collisions |
| **INV-STG-04** | Transactional & Merge-Safe Staging | `template/_tools/init-project --upgrade`, SHA-256 manifest rollback |
| **INV-HANDOFF-05** | Multi-Agent Session Handoff & Memory | `template/START.md`, `template/STATE.md`, predictable plain-text contracts |
| **INV-TIER-06** | Tiered Scalable Profiles | `template/TEMPLATE.md`, `MINIMAL`, `STANDARD`, `FULL` profiles |
| **INV-SYNC-07** | Multi-Host Cloud-Sync Defense | `.gitignore`, `template/.gitignore`, lock and conflict copy filters |
| **INV-AUDIT-08** | Human-Readable Backlog & Archival | `template/TODO.md`, `template/DONE.md`, `template/_tools/todo-archive` |
| **INV-LIC-09** | Permissive Audited Dependency Stack | `THIRD_PARTY_LICENSES.md`, `tests/test_metadata.py::test_third_party_licenses_content` |
| **INV-SLA-10** | Dual Security Response SLA | `SECURITY.md`, `tests/test_metadata.py::test_security_policy_bilingual_parity_and_contacts` |

---

## 4. Full License Texts (Excerpts & Notices)

### 1. Python Software Foundation License Version 2 (PSFL-2.0)
Python standard library modules are used under the PSF License Agreement.
Copyright (c) 2001-2026 Python Software Foundation. All rights reserved.

### 2. MIT License (MIT)
Used by `project-docs-template`, `pytest`, and `setuptools`.

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### 3. Apache License Version 2.0 (Apache-2.0)
Dual-license option used by `ruff`.
Licensed under the Apache License, Version 2.0. You may obtain a copy of the License at `http://www.apache.org/licenses/LICENSE-2.0`.
