---
name: project-docs-template
version: 0.1.2
description: "Scaffold, lint, archive, and upgrade agent-ready project documentation (CLAUDE.md, AGENTS.md, START.md, STATE.md, TODO.md, DONE.md, DECISIONS.md) using pure Python standard library tools."
---

# Project Docs Template Skill

Use this skill when setting up, validating, archiving, or upgrading structured project documentation for AI coding agents and human maintainers with `project-docs-template`.

## Prerequisites

- Python 3.10 or newer (pure Python standard library at runtime; `dependencies = []`).
- Local filesystem access to the repository checkout (`https://github.com/ellmos-ai/project-docs-template`).

## Available Profiles

- **`MINIMAL`**: Core context (`CLAUDE.md`, `AGENTS.md`, `START.md`, `STATE.md`, `TODO.md`, `DONE.md`, `_tools/doc-lint`, `_tools/todo-archive`).
- **`STANDARD`**: Adds `DECISIONS.md`, `PATTERNS.md`, `CHANGELOG.md`, `HEADER-RULES.md`, and `CUT-AND-CLUE.md`.
- **`FULL`**: Adds enterprise routers and governance (`MASTER-REGISTRY.md`, `MOVED-STUB.md`, `WORKFLOWS.md`, `TOOLS.md`, `GLOSSARY.md`, `ARCHITECTURE.md`, `_tools/workflows-sync`, `.github/`).

## Core Workflows

### 1. Dry-Run and Scaffold a New Project

```bash
python template/_tools/init-project --target /path/to/my-project --name "my-project" --profile STANDARD --dry-run
python template/_tools/init-project --target /path/to/my-project --name "my-project" --profile STANDARD
```

Optional `--git` initializes a `main` Git repository with an initial commit.

### 2. Validate Documentation & Frontmatter

```bash
python template/_tools/doc-lint --root template
python /path/to/my-project/_tools/doc-lint --root /path/to/my-project --fix --update-dates
```

### 3. Archive Completed Tasks

```bash
python /path/to/my-project/_tools/todo-archive --todo /path/to/my-project/TODO.md --done /path/to/my-project/DONE.md --apply
```

### 4. Merge-Safe Profile Upgrade

```bash
python template/_tools/init-project --target /path/to/my-project --upgrade --profile FULL
```

## Verification

```bash
python -m pytest -ra -v
```

## Guardrails

- **Fail-Closed Checks**: `init-project` rejects existing non-empty targets; `--upgrade` refuses to overwrite edited managed files or unowned collisions against `.project-docs-template.json`.
- **Zero-Egress**: Template tools run locally on disk without outbound network requests or telemetry.
- **Template Language**: Repository docs (`README.md`, `llms.txt`, `SECURITY.md`) are multilingual/English-led, while generated template bodies under `template/` and CLI messages are currently German; YAML keys and filenames are language-neutral.
