# Changelog

All notable public-facing changes to this repository are documented here.

## [Unreleased]

### 2026-10-02 - Pfad A CI Lifecycle Workflows, Lock Defense, Bilingual Contributing & Metadata Contracts

- **Version-Freeze Disziplin (T-20260920-167562623)**: Version `0.1.2` strikt unverändert beibehalten; alle Modifikationen unter `## [Unreleased]` geführt.
- **CI/CD Lifecycle Workflows Provisioning (`.github/workflows/auto-assign.yml`, `label-sync.yml`, `.github/labels.yml`)**:
  - `.github/workflows/auto-assign.yml` neu angelegt mit `actions/github-script@v7`, `timeout-minutes: 5`, Concurrency `cancel-in-progress: true` (`auto-assign-${{ github.ref }}`) und least-privilege permissions (`pull-requests: write`, `issues: write`).
  - `.github/workflows/label-sync.yml` neu angelegt mit `EndBug/label-sync@v2`, `timeout-minutes: 5`, Concurrency `cancel-in-progress: true` (`label-sync-${{ github.ref }}`) und least-privilege permissions (`issues: write`).
  - `.github/labels.yml` mit 11 kanonischen Standard-Labels gemäß GOVERNANCE.md §4.2 provisioniert.
- **Bilinguale Contributing Guidelines (`CONTRIBUTING.md`)**: Vollständiger Leitfaden auf Deutsch und Englisch mit Spezifikation aller 10 Governance- und Laufzeitinvarianten (`INV-LOCAL-01` bis `INV-SLA-10`), unprivilegiertem `RunAsInvoker` Modus (`INV-SEC-02`), Plan D Klon-Setup (`C:\_Local_DEV\repos\project-docs-template`), Version-Freeze-Disziplin, Pre-Commit Quality Gates und 48h Security Response SLA.
- **Multi-Host Cloud-Sync-, Lock- und Cache-Härtung (`.gitignore` & `template/.gitignore`)**: Gehärtet gegen Multi-Host-Tokens (`*-IDEAPAD*`, `*-IDEAPAD-GEI*`), Betriebssystem-Caches (`Desktop.ini`, `ehthumbs.db`), Agenten-Planungsdateien (`TASKPLAN_*.md`) sowie kanonische Entwicklungs- und Agenten-Locks (`LOCK.dev.*`, `LOCK.antigravity.*`, `LOCK.bugsearch.*`, `LOCK.user.*`, `LOCK.until.*`, `LOCK.condition.*`).
- **PEP 621 Standardisierung in `pyproject.toml`**: `Contributing` URL unter `[project.urls]` registriert; `[tool.pytest.ini_options]` mit `addopts = "-ra -v --basetemp=.pytest_temp"` und gehärtetem `norecursedirs` (.turbo, .nyc_output) standardisiert.
- **Level 1 SBOM Text-Companion Re-Audit (`THIRD_PARTY_LICENSES.md` & `THIRD_PARTY_LICENSES.txt`)**: Re-Audit Stand `2026-10-02` mit unprivileged `RunAsInvoker` Non-Elevation-Garantie, § 521 BGB Haftungsausschluss, Zero-Copyleft und Zero-Runtime-Dependencies.
- **Dokumentations- & Kontext-Parität**:
  - `README.md` und `README_de.md`: Last-Checked Badge auf `2026-10-02` aktualisiert, `Contributing` Badge ergänzt, Test-Counter auf neue Gesamtzahl synchronisiert unter striktem Erhalt aller 18 bilateralen Schnellnavigations-Anker `sec-01`..`sec-18`.
  - `llms.txt`: `## Last-checked: 2026-10-02`, Verweise auf `CONTRIBUTING.md` und `THIRD_PARTY_LICENSES.txt` ergänzt, Test-Baseline aktualisiert.
  - `MARKETING-LOG.txt`: Section 13 Pfad A Revisionsbericht Stand 2026-10-02 dokumentiert.
- **Automatisierte Vertragstest-Erweiterung (`tests/test_metadata.py`)**: 8 neue automatisierte Contract-Tests für `CONTRIBUTING.md`, CI Lifecycle Workflows, Standard-Labels, PEP 621 URLs, erweiterte .gitignore Lock-Defense und Re-Audit Stand 2026-10-02.

### 2026-09-29 - Pfad B Discoverability, Dual HTML Anchors, ASCII 4-View Architecture Topology, Level 1 SBOM Text Companion & 20 Topics Saturation

- **Version-Freeze Disziplin (T-20260920-167562623)**: Version `0.1.2` strikt unverändert beibehalten; kein vorzeitiger Release-Bump.
- **Bilinguale 18-Punkte-Navigationsparität & wechselseitige HTML-Anker**: Vollständige 18-Punkte-Schnellnavigation in `README.md` und `README_de.md` mit reziproken dualen HTML-Ankern (`<a id="sec-01"></a>`..`<a id="sec-18"></a>`) und synchronisierten Shields.io-Badges (`last checked-2026--09--29`, `Level 1 SBOM: Audited | Plain Text`).
- **ASCII Vier-Ansichten-Architekturprojektion**: Ergänzung von Section 2 in beiden READMEs um standardisierte 4-Ebenen-ASCII-Topologie (`[VIEW 1: CLI COCKPIT, LINTER & AGENT INTERFACE HARNESS]`, `[VIEW 2: TIERED PROFILE ENGINE & MERGE-SAFE STAGING]`, `[VIEW 3: RUNTIME PERSISTENCE, REPOSITORY MEMORY & AUDIT]`, `[VIEW 4: SECURITY BOUNDARY, AIR-GAP & RUNASINVOKER ZERO-EGRESS]`; deutsche Entsprechung `[SICHT 1]`..`[SICHT 4]`).
- **Level 1 SBOM Plain-Text Companion (`THIRD_PARTY_LICENSES.txt`)**: Neue Plain-Text-Begleitdatei mit vollständigem Permissive-Inventar (PSFL-2.0, MIT, Apache-2.0), Zero-Runtime-Dependency-Garantie, `RunAsInvoker` Non-Elevation-Zertifizierung, Invarianten-Kreuzreferenzmatrix (`INV-LOCAL-01` bis `INV-SLA-10`) und gesetzlichem Haftungsausschluss gem. § 521 BGB.
- **PEP 621 Metadaten- & GitHub Topics Sättigung**: GitHub Remote Topics via `gh repo edit` auf 20/20 gesättigt; alle 20 Topics in sortierter Reihenfolge in `keywords` von `pyproject.toml` synchronisiert; `license-files` Whitelist um `THIRD_PARTY_LICENSES.txt` erweitert; `"Level 1 SBOM"`, `"Third-Party Licenses (Text)"` und `"Plain-Text License"` URLs in `[project.urls]` registriert; `[tool.pytest.ini_options]` mit `--basetemp=.pytest_temp` und erweitertem `norecursedirs` gehärtet.
- **Automatisierte Vertragstests (`tests/test_metadata.py`)**: Neue Contract-Tests für bilaterale 18-Punkte-Navigationsanker `sec-01`..`sec-18`, ASCII Vier-Ansichten-Topologie-Projektion, Level 1 SBOM Text-Companion und PEP 621 20-Keywords-Sättigung.

## 2026-09-25 - Pfad A Repository Hygiene, CI Security Hardening & Contract Test Expansion

- **CI Workflow Security Hardening (`.github/workflows/ci.yml`)**: Verified explicit unprivileged permissions (`contents: read`), runaway execution guardrail (`timeout-minutes: 15`), concurrency dedup, and pinned Node 24 action SHAs.
- **Multi-Host Defense & Patch Hygiene (`.gitignore` & `template/.gitignore`)**: Hardened root and template ignore specifications with patch rejection artifacts (`*.rej`), temporary debug logs (`pytestdebug.log`), and multi-host conflict patterns.
- **Context & Badge Synchronization**: Synchronized test badge baselines (54 passed, 7 subtests | 100% green), updated verification timestamps to `2026-09-25` across `README.md`, `README_de.md`, and `llms.txt`.
- **Automated Contract Tests Expansion (`tests/test_metadata.py`)**: Added 3 new regression contract tests covering explicit CI workflow permissions, patch artifact ignore defenses, and changelog hygiene auditing (54 collected tests, 100% green).

## 2026-09-20 - Pfad B Discoverability, 18-Point Navigation Parity, Level 1 SBOM, NOTICE & Visual Architecture Overhaul

- **18-Point Bilingual Navigation Parity**: Standardized both `README.md` and `README_de.md` into 18 identically numbered sections with dual reciprocal HTML anchors (`<a id="..."></a>`) guaranteeing seamless deep linking.
- **Visual Architecture & Lifecycle Flowcharts**: Added dual Mermaid diagrams to both language editions: a 4-tier decoupled architecture flowchart (`flowchart TD`) and a 4-phase end-to-end multi-agent session lifecycle (`sequenceDiagram` with `autonumber` and strictly 0 semicolons).
- **Level 1 Software Bill of Materials (SBOM)**: Overhauled `THIRD_PARTY_LICENSES.md` to include a full Level 1 SBOM table, Zero-Runtime-Dependency & Zero-Copyleft Isolation Guarantee, unprivileged user-mode execution (`RunAsInvoker`) certification, and Invariant Cross-Reference Matrix (`INV-LOCAL-01` to `INV-SLA-10`).
- **Canonical Root NOTICE File**: Created root `NOTICE` file asserting copyright 2026 Lukas Geiger, ellmos-ai, and open-bricks umbrella attribution.
- **PEP 639 License Files Standard**: Configured `license-files = ["LICENSE", "NOTICE", "THIRD_PARTY_LICENSES.md"]` and ecosystem discoverability keywords (`ellmos-ai`, `open-bricks`) in `pyproject.toml`.
- **10-Dimension Comparative Matrix**: Expanded Section 5 matrix evaluating 4 alternatives across all 10 governance invariants (`INV-LOCAL-01` to `INV-SLA-10`).
- **Section 18 Statutory Notice (§ 521 BGB)**: Documented statutory courtesy disclaimer (*Gefälligkeit / unentgeltliche Schenkung* pursuant to § 521 BGB, liability limited to intent and gross negligence).
- **Automated Contract Tests (`tests/test_metadata.py`)**: Added test assertions for root `NOTICE` existence, PEP 639 `license-files`, Level 1 SBOM / `RunAsInvoker`, 18-point quick navigation, 10-dimension matrix, and semicolon-free Mermaid syntax.

## 2026-09-14 - Pfad A Repository Hygiene, CI Timeout Hardening & Multi-Host Defense

- **CI Workflow Hardening (`.github/workflows/ci.yml`)**: Added `timeout-minutes: 15` runaway guardrail to the matrix test job, concurrency cancellation for in-flight pushes, and standardized pytest runner invocation to `python -m pytest -ra -v`.
- **Stale Management Automation (`.github/workflows/stale.yml`)**: Added automated issue and pull-request stale lifecycle management with concurrency control and `timeout-minutes: 10`.
- **Multi-Host Cloud-Sync & Lock Defense (`.gitignore` & `template/.gitignore`)**: Hardened both the repository root `.gitignore` and the scaffold template `.gitignore` against cloud sync conflict copies (`* (kopie)*`, `* (copy)*`, `*-WORKSTATION*`, `*-ASUS-GEI*`), canonical lock files (`LOCK`, `LOCK.*`, `LOCK*.txt`, `LOCK.permissions.json`, `uv.lock`), and temporary test/cache artifacts (`.coverage.*`, `.tox/`, `.turbo/`, `.nyc_output/`, `.hypothesis/`, `*.orig`).
- **PEP 621 Metadata & Pytest Standardization**: Configured `addopts = "-ra -v"` in `[tool.pytest.ini_options]` and declared explicit `"Bug Tracker"` project URL in `pyproject.toml`.
- **SBOM & License Audit Refresh (`THIRD_PARTY_LICENSES.md`)**: Re-audited zero-runtime-dependency invariant and updated audit timestamp to 2026-09-14.
- **Metadata, Badges & LLM-Context Freshness**: Synchronized shields.io badges in `README.md` and `README_de.md` to latest test baseline (44 tests, 7 subtests, 100% green) and updated Last Checked to `2026-09-14`; refreshed `llms.txt` timestamp and test counts.
- **Automated Contract Tests Expansion (`tests/test_metadata.py`)**: Added 5 new contract tests verifying CI timeouts, concurrency settings, stale workflow presence, multi-host .gitignore defense across both root and template, and pytest options.

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
