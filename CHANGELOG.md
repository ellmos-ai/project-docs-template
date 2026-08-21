# Changelog

All notable public-facing changes to this repository are documented here.

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
