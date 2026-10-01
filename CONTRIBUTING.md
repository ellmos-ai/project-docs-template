# Contributing to project-docs-template

[English](#english) | [Deutsch](#deutsch)

---

<a id="english"></a>
## English

Thank you for your interest in contributing to **project-docs-template**!

### Architectural Principles & Quality Invariants

`project-docs-template` is an agent-ready project documentation and memory template engineered for autonomous AI coding agents, multi-agent swarms, and human maintainers. All contributions must respect our foundational architectural and governance invariants:

1. **Local-First & Zero-Egress (`INV-LOCAL-01`)**: Operates entirely on local filesystems and local storage mounts; zero telemetry, zero analytics, zero external network calls by default.
2. **Unprivileged User-Mode Execution (`RunAsInvoker` / `INV-SEC-02`)**: Executes safely in unprivileged user space (`RunAsInvoker`) without requiring root, sudo, or UAC administrator elevation.
3. **Fail-Closed Default Semantics (`INV-FAIL-03`)**: When generation or upgrade encounters dirty directories, collision states, or unparseable YAML frontmatter, execution aborts safely without mutating existing project assets.
4. **Transactional & Merge-Safe Staging (`INV-STG-04`)**: Profile upgrades verify SHA-256 hashes against `.project-docs-template.json` manifests; any modified or unowned collision file triggers a clean rollback rather than silent corruption.
5. **Multi-Agent Session Handoff & Memory (`INV-HANDOFF-05`)**: Predictable plain-text contracts (`CLAUDE.md`, `AGENTS.md`, `START.md`, `STATE.md`) guarantee deterministic agent context and session handoffs.
6. **Tiered Scalable Profiles (`INV-TIER-06`)**: Three curated documentation profiles (`MINIMAL`, `STANDARD`, `FULL`) prevent documentation bloat and scale with project complexity.
7. **Multi-Host Cloud-Sync Defense (`INV-SYNC-07`)**: Both repository and scaffold template `.gitignore` files defend against cloud synchronization conflicts (`* (kopie)*`, `*-WORKSTATION*`, `*-ASUS-GEI*`, `*-IDEAPAD*`) and canonical lock files.
8. **Human-Readable Backlog & Atomic Archival (`INV-AUDIT-08`)**: Plain-text Markdown task tracking (`TODO.md`, `DONE.md`) with transactional two-file atomic archival (`todo-archive`).
9. **100% Permissive Audited Dependency Stack (`INV-LIC-09`)**: Zero runtime dependencies (`dependencies = []`), clean MIT/PSFL-2.0/Apache-2.0 stack audited in `THIRD_PARTY_LICENSES.md` and `THIRD_PARTY_LICENSES.txt`, zero copyleft or AGPL contamination.
10. **Dual Security Response & Triage SLA (`INV-SLA-10`)**: Committed 48-hour response and 5-business-day triage commitment via canonical security channels.

### Development Guidelines

- **Plan D Architecture**: Development, git operations, and tests occur strictly in the local git repository clone (`C:\_Local_DEV\repos\project-docs-template`).
- **Version Freeze Discipline**: Version `0.1.2` is strictly frozen per `T-20260920-167562623`. Do not bump the package version; document all modifications under `## [Unreleased]` in `CHANGELOG.md`.
- **Python Version Support**: Compatible with Python 3.10 through 3.13.
- **Pre-commit Quality Gates**:
  - Bytecode compilation: `python -m compileall -q .`
  - Linting: `ruff check .`
  - Automated test suite: `python -m pytest -ra -v` (100% green required)
- **Security Vulnerabilities**: Please do not report security vulnerabilities publicly. Follow our [SECURITY.md](SECURITY.md) guidelines for responsible disclosure (48h response SLA via security@ellmos.ai).

---

<a id="deutsch"></a>
## Deutsch

Vielen Dank für Ihr Interesse an einer Mitarbeit an **project-docs-template**!

### Architektur-Prinzipien & Qualitäts-Invarianten

`project-docs-template` ist eine agenten-optimierte Projektdokumentations- und Gedächtnisvorlage für autonome KI-Agenten, Multi-Agenten-Schwärme und Entwickler. Alle Beiträge müssen unsere grundlegenden Invarianten einhalten:

1. **100% Local-First & Zero-Egress (`INV-LOCAL-01`)**: Vollständige lokale Ausführung auf lokalen Dateisystemen und Mounts; null Telemetrie, null Cloud-Zwang, null Egress-Aufrufe.
2. **Unprivilegierter Ausführungsmodus (`RunAsInvoker` / `INV-SEC-02`)**: Läuft sicher im normalen Benutzerkontext (`RunAsInvoker`) ohne Root-, Sudo- oder Administrator-Elevation.
3. **Fail-Closed Standard-Semantik (`INV-FAIL-03`)**: Bei unsauberen Verzeichnissen, Kollisionen oder unparsebarem YAML-Frontmatter bricht das Tooling fail-closed ab, ohne vorhandene Dateien zu beschädigen.
4. **Transaktionales & merge-sicheres Staging (`INV-STG-04`)**: Profil-Upgrades prüfen SHA-256 Hashes gegen das Manifest (`.project-docs-template.json`); modifizierte oder fremde Kollisionsdateien lösen saubere Rollbacks aus.
5. **Multi-Agenten Session-Handoff (`INV-HANDOFF-05`)**: Standardisierte Klartext-Verträge (`CLAUDE.md`, `AGENTS.md`, `START.md`, `STATE.md`) sichern deterministische Kontext-Übergaben zwischen Agenten.
6. **Gestaffelte skalierbare Profile (`INV-TIER-06`)**: Drei kuratierte Dokumentationsprofile (`MINIMAL`, `STANDARD`, `FULL`) verhindern Dokumentations-Wildwuchs und skalieren mit der Projektgröße.
7. **Multi-Host Cloud-Sync Schutz (`INV-SYNC-07`)**: Sowohl Repo- als auch Scaffold-`.gitignore` schützen vor Cloud-Sync-Konfliktkopien (`* (kopie)*`, `*-WORKSTATION*`, `*-ASUS-GEI*`, `*-IDEAPAD*`) und Lock-Dateien.
8. **Klartext-Backlog & atomare Archivierung (`INV-AUDIT-08`)**: Menschenlesbares Markdown-Aufgabenmanagement (`TODO.md`, `DONE.md`) mit atomarem Journaling-Archivierer (`todo-archive`).
9. **100% permissiver Lizenz-Stack (`INV-LIC-09`)**: Null externe Laufzeit-Abhängigkeiten (`dependencies = []`), rein MIT-/PSFL-2.0-/Apache-2.0-lizenziert, auditiert in `THIRD_PARTY_LICENSES.md` und `THIRD_PARTY_LICENSES.txt`, null Copyleft.
10. **Zweisprachige Sicherheits-SLA (`INV-SLA-10`)**: Verbindliche 48-Stunden-Reaktionszeit und 5 Tage Triage-Zusage über offizielle Sicherheitskontakte (`security@ellmos.ai`).

### Richtlinien für Entwickler

- **Plan D Entwicklung**: Entwicklung, Git-Aktionen und Tests erfolgen ausschließlich im lokalen Git-Repository (`C:\_Local_DEV\repos\project-docs-template`).
- **Version-Freeze Disziplin**: Version `0.1.2` bleibt gemäß Richtlinie `T-20260920-167562623` eingefroren; Neuerungen werden unter `## [Unreleased]` im `CHANGELOG.md` gepflegt.
- **Python-Unterstützung**: Python 3.10 bis 3.13.
- **Qualitäts-Tore vor Commits**:
  - Bytecode-Prüfung: `python -m compileall -q .`
  - Linter: `ruff check .`
  - Testsuite: `python -m pytest -ra -v` (100% grün erforderlich)
- **Sicherheitsmeldungen**: Sicherheitslücken bitte nicht öffentlich melden, sondern gemäß [SECURITY.md](SECURITY.md) vertraulich einreichen (48h Reaktions-SLA via security@ellmos.ai).
