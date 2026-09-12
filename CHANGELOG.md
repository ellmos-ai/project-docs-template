# Changelog

All notable public-facing changes to this repository are documented here.

## 2026-09-12 - Pfad B Discoverability, Target Personas & Comparative Architecture

- **Quick Navigation & Readme Badges**: Added Shields.io badges for Last Checked (`2026-09-12`), Zero-Dependency MIT Licenses, and Marketing Log. Added reciprocal `🧭 Quick Navigation` / `🧭 Schnellnavigation` anchors across `README.md` and `README_de.md`.
- **Target Personas & Core Use Cases**: Documented explicit value propositions for 4 target groups: Multi-Agent Systems Engineers, Solo Developers & Open-Source Maintainers, Enterprise Architecture & AI Governance Leads, and Research & Scientific Pipeline Developers.
- **Comparative Architecture Matrix**: Added a 7-dimension comparative analysis contrasting `project-docs-template` against generic markdown dumps, heavyweight SaaS wikis (Notion, Confluence), and rigid agent frameworks.
- **Software Bill of Materials (SBOM)**: Created `THIRD_PARTY_LICENSES.md` formally validating the zero-runtime-dependency architecture (`dependencies = []`), standard library usage, and MIT licensing.
- **Marketing Register (`MARKETING-LOG.txt`)**: Documented Pfad B discoverability audit, bilingual high-intent keyword matrix, and differentiation rationale.
- **PEP 621 Metadata Expansion**: Added `multi-agent`, `zero-egress`, `governance`, and `session-handoff` keywords, and declared extended project URLs in `pyproject.toml`.
- **Automated Contract Tests (`tests/test_metadata.py`)**: Added test coverage for quick navigation anchor integrity, persona presence, comparative architecture matrix, and PEP 621 extended URLs.

## 2026-09-02 - Cross-platform CI repair and documentation correction

- **Fixed the red matrix.** `test_profile_upgrade_rolls_back_when_manifest_commit_fails`
  compared an unresolved temporary path against the manifest path that
  `upgrade()` resolves. On Linux `/tmp` is a real directory and the comparison
  matched; on macOS the temporary directory sits under the `/var` -> `/private/var`
  symlink and on Windows it can be an 8.3 short path, so the injected failure
  never fired and the test failed with `OSError not raised`. All eight Windows
  and macOS jobs had been red since 2026-08-23 while the four Ubuntu jobs stayed
  green. Reproduced locally by pointing `TMPDIR` at a symlinked directory.
- **Corrected the 0.1.2 entry below.** It claimed "34 tests passed, 7 subtests,
  100% green"; that held on Ubuntu only. `RELEASE_GATE.md` forbids releasing
  while any matrix job fails, and `0.1.2` was released while eight were failing.
- **Restored the SHA-pinned Node 24 actions.** The 0.1.2 change described as CI
  hardening replaced `actions/checkout` and `actions/setup-python`, pinned to
  full commit SHAs of the v6 majors since 2026-07-17, with the floating tags
  `@v4` and `@v5`, which still target the deprecated Node 20. The contract test
  now asserts SHA pinning instead of a specific major, which is what it meant.
- **Disclosed the template language.** The repository documents itself in
  English while the generated template bodies and all CLI output are German.
  `README.md`, `README_de.md` and `llms.txt` now say so; an English template set
  is an open item in `TODO.md`.
- **Ecosystem matrix corrections.** Removed the private
  `dev-bricks/automation-master` (a 404 for every reader, and a contract test
  had been requiring it), corrected the `clutch` entry from "Safe Git operation
  wrapper" to the LLM router it actually is, and aligned the `DevCenter`
  description with its repository description.
- **Restored the missing MIT line** in the English README's license section; the
  German README had it, the English one did not.
- **Stopped tracking `BEFUNDE.md`**, an internal maintenance journal that
  exposed the local working path and stale test counts.
- **Added a trademark and independence notice.** The project names Claude Code,
  Codex, Antigravity and Gemini thirteen times across both READMEs and again in
  the package keywords, the GitHub topics and the discoverability blocks, with
  no statement of independence anywhere. A legal first look found the naming
  itself covered by the referential-use exception, with the one open point being
  the impression of a business relationship — so both READMEs now carry a
  Trademarks section plus a short notice next to the two blocks that create that
  impression.
- **Sharpened the liability paragraph** so the Section 521 BGB limitation is
  conditioned rather than asserted, and mandatory liability is reserved.
- **Stated that the package is not on PyPI.** A `pyproject.toml` naming
  `project-docs-template` invites `pip install project-docs-template`, and the
  name is unregistered — a dependency-confusion opening that a third party could
  take at any time.
- **Replaced the "full active support & immediate hotfixes" promise** in
  `SECURITY.md` with a best-effort formulation, and "Zero-Egress guarantee" with
  "architecture"; both contradicted the project's own liability disclaimer.

## 2026-08-23 - 0.1.2 (Multi-OS CI Hardening, PEP 621 Classifiers & Metadata Contract Expansion)

- **Version Bump & Manifest Parity**: Released `0.1.2` across `pyproject.toml` and `ellmos-module.v2.json`.
- **PEP 621 Metadata & URLs**: Added `Operating System :: OS Independent`, Windows, Linux, and macOS classifiers, along with `Documentation`, `Security`, and `Umbrella` URLs in `pyproject.toml`.
- **Hardened GitHub Actions CI (`.github/workflows/ci.yml`)**: Updated actions to `actions/checkout@v4` and `actions/setup-python@v5` with `cache: 'pip'`; expanded matrix across Python `3.10`, `3.11`, `3.12`, and `3.13` on `ubuntu-latest`, `windows-latest`, and `macos-latest`; added explicit `ruff check .` linting step before test discovery.
- **Contract & Metadata Test Expansion (`tests/test_metadata.py`)**: Added automated contract tests for PEP 621 classifiers, offline/zero-egress invariants, and full CI matrix parity (34 tests, 7 subtests). *Corrected on 2026-09-02: the original entry said "100% green". That was true on Ubuntu only — the eight Windows and macOS jobs were failing when this version was released, contrary to `RELEASE_GATE.md`.*
- **Security & Umbrella Governance (`SECURITY.md`)**: Added direct umbrella contact `lukas@open-bricks.org` in both German and English vulnerability disclosure policies.
- **LLM Discovery Index (`llms.txt`)**: Updated `Last-checked: 2026-08-23` and synchronized verification status.

## 2026-08-21 - 0.1.1 (Discoverability & Security Parity)

- **Shields.io Badges & Discoverability**: Synchronized badges across `README.md` and `README_de.md` (32 passed tests, 100% green, version `0.1.1`, Python `3.10 | 3.11 | 3.12 | 3.13`, `Windows | Linux | macOS`, `100% Offline / Zero-Egress`, `Local-First / Deterministic Staging`, `ellmos-ai` ecosystem, `open-bricks` umbrella, `llms.txt` discovery).
- **Interactive Mermaid Lifecycle Sequence Diagrams**: Added bilingual Mermaid sequence diagrams illustrating the staged, hash-verified profile upgrade lifecycle with fail-closed safeguards, unowned file collision prevention, and zero implicit merges.
- **Bilingual Hardened Security Policy (`SECURITY.md`)**: Implemented full German and English security policies with Local-First & Zero-Egress invariants, deterministic staging isolation, SHA-256 manifest integrity, non-elevation execution, and direct security contacts (`security@ellmos.ai` & `support@lukasgeiger.com`) alongside GitHub Private Security Advisories.
- **Ecosystem & Sibling Tools Matrix**: Expanded cross-linking matrix across 16 sibling repositories in `ellmos-ai`, `dev-bricks`, and `open-bricks`.
- **Contract & Parity Test Suite (`tests/test_metadata.py`)**: Added 3 new comprehensive test cases (32 passed tests total) asserting bilingual README badge and diagram parity, SECURITY.md invariants/contacts, and CI matrix/Ruff configuration consistency.
- **LLM Discovery Index (`llms.txt`)**: Updated `Last-checked: 2026-08-21` and refreshed verification status.

## 2026-08-16 - 0.1.1

- Bumped package and manifest version to `0.1.1` across `pyproject.toml` and `ellmos-module.v2.json`.
- Added automated metadata, schema, and manifest parity test suite in `tests/test_metadata.py` (29 total tests, 7 subtests, 100% green).
- Integrated `[tool.ruff]` and `[tool.ruff.lint]` configuration in `pyproject.toml` (`target-version = "py310"`, `line-length = 120`, `ruff check` 100% clean).
- Cleaned unused import in `tests/test_tools.py`.
- Synchronized Shields.io badges in `README.md` and `README_de.md` (`pytest 29 passed`, `ellmos-ai` ecosystem, `open-bricks` umbrella, `LLM-Ready`).
- Added Ecosystem & Sibling Tools cross-link matrix to English and German documentation.
- Updated `llms.txt` verification timestamp to 2026-08-16 with comprehensive verification summary.

## 2026-08-13

- Added `init-project --upgrade --profile <STANDARD|FULL>` with a staged,
  manifest/hash-verified contract for existing generated projects.
- Profile upgrades are one-step only, never implicitly merge user changes,
  reject unowned filename collisions before mutation, and roll back their own
  writes if the final manifest commit fails.
- Added regression coverage for successful upgrades, dry-run/no-write safety,
  modified-file conflicts, unowned collisions, and legacy projects without a
  manifest.

## 2026-08-12

- Updated `llms.txt` verification timestamp to 2026-08-12.
- Re-verified the complete 18-test regression suite (`pytest` and `unittest`,
  including 7 subtests), `compileall`, `doc-lint`, and `git diff --check`.
- Recorded the current local branch divergence in `BEFUNDE.md`; no merge or
  push was performed.

## 2026-08-10

- Updated `llms.txt` verification timestamp to 2026-08-10.
- Re-verified the complete 18-test regression suite (`pytest` and `unittest`,
  including 7 subtests), `compileall`, `doc-lint`, and `git diff --check`.

## 2026-08-01

- Updated `llms.txt` verification timestamp to 2026-08-01.
- Re-verified the complete 18-test regression suite (`pytest` and `unittest`,
  including 7 subtests), `compileall`, and `doc-lint`.

## 2026-07-30

- Updated `llms.txt` verification timestamp to 2026-07-30.
- Re-verified complete 18-test regression suite across all template generation profiles (`pytest` / 18 passed).

## 2026-07-29

- Updated `llms.txt` verification timestamp to 2026-07-29.
- Re-verified complete 18-test regression suite across all template generation profiles (`pytest` / 18 passed).

## 2026-07-27

- Updated `llms.txt` verification timestamp to 2026-07-27.
- Re-verified complete 18-test regression suite across all template generation profiles (`pytest` / `unittest`).

## 2026-07-26

- Added German documentation `README_de.md` for multi-language access and international discoverability.
- Added Mermaid System Architecture & Flow diagram (`Architecture & Flow`) to `README.md` and `README_de.md`.
- Updated `llms.txt` verification timestamp to 2026-07-26.
- Re-verified complete 18-test regression suite across all template generation profiles.

## 2026-07-25

- Added PEP 621 `pyproject.toml` with project metadata, Python >=3.10 requirement, and pytest configuration (`tool.pytest.ini_options`).
- Updated `llms.txt` verification timestamp to 2026-07-25.
- Added Pytest status badge and GFM LLM orientation callout (`> [!NOTE]`) to `README.md`.
- Re-verified complete 18-test regression suite across template generation profiles.

## 2026-07-17

- Promoted `init-project` from a concept to a staged generator with real Git
  initialization, author fallback, profile rendering, and output validation.
- Made MINIMAL, STANDARD, and FULL documentation self-consistent: optional
  sections are profile-aware and generated relative links must resolve.
- Hardened `doc-lint` with canonical-template detection, safe YAML scalars,
  atomic writes, placeholder repair, and a post-fix verification pass.
- Hardened `todo-archive` with distinct-path validation, idempotent retries,
  staged pair replacement, and rollback after partial failure.
- Hardened `workflows-sync` with atomic writes and safe Markdown/regex escaping.
- Added an 18-test regression suite, a six-job Linux/Windows/macOS CI matrix,
  `SECURITY.md`, and an explicit `RELEASE_GATE.md`.

## 2026-07-02

- Added root `llms.txt` with canonical search phrases, audience notes, and
  disambiguation for LLM/crawler discovery.
- Expanded the root `README.md` with template-use cases, profile comparison,
  badges, and canonical discovery phrases.
