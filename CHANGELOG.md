# Changelog

All notable public-facing changes to this repository are documented here.

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
