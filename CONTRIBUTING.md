# Contributing to project-docs-template

[English](#english) | [Deutsch](#deutsch)

---

<a id="english"></a>
## English

Thank you for your interest in contributing to **project-docs-template**!

### Architectural Principles & Quality Invariants

`project-docs-template` is an agent-ready project documentation and memory template engineered for autonomous AI coding agents, multi-agent swarms, and human maintainers. All contributions must respect our foundational architectural and governance invariants:

1. **Local-First & Zero-Egress (`INV-LOCAL-01`)**: `SECURITY.md` documents local-disk operation without telemetry or outbound network calls for template generation and the listed maintenance tools. This is the documented tool scope, not an operating-system network sandbox.
2. **Caller Process Context (`INV-SEC-02`)**: These scripts inherit the invoking process context; the CLI does not request privilege elevation. A privileged caller remains privileged; no standard-user enforcement or certification is claimed.
3. **Detected-Conflict Checks (`INV-FAIL-03`)**: Generation rejects an existing target that is not empty. Profile upgrades reject detected edits to managed files and unowned collisions before commit. Generation creates parent and staging directories and writes staged files before promotion; there is no blanket no-write-before-failure guarantee.
4. **Staged Profile Upgrades (`INV-STG-04`)**: Upgrades verify manifest hashes, stage the next profile, and back up files. Hash-guarded restoration is attempted after certain commit failures; it is conditional and can fail if files change concurrently or further filesystem errors occur.
5. **Shared Session Records (`INV-HANDOFF-05`)**: Plain-text files (`CLAUDE.md`, `AGENTS.md`, `START.md`, `STATE.md`) provide project and session context for agents and maintainers. The template cannot ensure that an agent reads, follows, or retains those records.
6. **Tiered Profiles (`INV-TIER-06`)**: The template provides three documentation profiles (`MINIMAL`, `STANDARD`, `FULL`), and profile upgrades proceed one step at a time.
7. **Conflict-Copy Ignore Patterns (`INV-SYNC-07`)**: The repository and scaffold `.gitignore` files list patterns for known synchronization conflict copies and lock files. Ignore patterns do not coordinate concurrent writers or provide a live distributed lock.
8. **Journaled Task Archival (`INV-AUDIT-08`)**: `todo-archive` stages updates to `TODO.md` and `DONE.md`, records a journal, attempts restoration after replacement errors, and can recover an interrupted pair update. Divergent files can leave the journal for manual review.
9. **Runtime Dependencies (`INV-LIC-09`)**: The project declares `dependencies = []` and uses the Python standard library at runtime. Development and test tools are separate from this runtime-dependency statement. `THIRD_PARTY_LICENSES.md` and `THIRD_PARTY_LICENSES.txt` list the documented dependency and license entries; no independent audit claim is made here.
10. **Security Reporting Policy (`INV-SLA-10`)**: `SECURITY.md` prioritizes security fixes and provides best-effort maintenance for supported `0.1.x` versions on `main`; it does not guarantee response times. Versions below `0.1.0` are unsupported.

### Development Guidelines

- **Plan D Architecture**: Development, git operations, and tests occur strictly in the local git repository clone (`C:\_Local_DEV\repos\project-docs-template`).
- **Version Freeze Discipline**: Version `0.1.2` is strictly frozen per `T-20260920-167562623`. Do not bump the package version; document all modifications under `## [Unreleased]` in `CHANGELOG.md`.
- **Python Version Support**: Compatible with Python 3.10 through 3.13.
- **Pre-commit Quality Gates**:
  - Bytecode compilation: `python -m compileall -q .`
  - Linting: `ruff check .`
  - Automated test suite: `python -m pytest -ra -v` (100% green required)
- **Security Vulnerabilities**: Use the private GitHub Security Advisory (preferred) or the direct contacts listed in [SECURITY.md](SECURITY.md): `security@ellmos.ai`, `support@lukasgeiger.com`, and `lukas@open-bricks.org`. Do not report unpatched vulnerabilities in public issues; the policy requests coordinated disclosure until a patch is released.

---

<a id="deutsch"></a>
## Deutsch

Vielen Dank für Ihr Interesse an einer Mitarbeit an **project-docs-template**!

### Architektur-Prinzipien & Qualitäts-Invarianten

`project-docs-template` ist eine agenten-optimierte Projektdokumentations- und Gedächtnisvorlage für autonome KI-Agenten, Multi-Agenten-Schwärme und Entwickler. Alle Beiträge müssen unsere grundlegenden Invarianten einhalten:

1. **Local-First-Betrieb (`INV-LOCAL-01`)**: `SECURITY.md` beschreibt den lokalen Betrieb ohne Telemetrie oder ausgehende Netzaufrufe für die Vorlagenerzeugung und die dort aufgeführten Wartungsskripte. Das ist der dokumentierte Umfang dieser Werkzeuge, keine Netzwerksandbox des Betriebssystems.
2. **Prozesskontext des Aufrufers (`INV-SEC-02`)**: Die Skripte übernehmen den Prozesskontext des Aufrufers; die CLI fordert keine Rechteerhöhung an. Ein bereits privilegierter Aufrufer bleibt privilegiert. Eine Durchsetzung des Standardbenutzermodus oder eine Zertifizierung wird nicht behauptet.
3. **Prüfungen mit Abbruch bei erkannten Konflikten (`INV-FAIL-03`)**: Die Generierung lehnt ein vorhandenes, nicht leeres Zielverzeichnis ab. Profil-Upgrades weisen erkannte Änderungen an verwalteten Dateien und nicht verwaltete Kollisionen vor dem Commit zurück. Die Generierung legt Zielpfad und Staging an und schreibt Dateien ins Staging, bevor die Promotion beginnt; eine allgemeine Garantie, dass zuvor nichts geschrieben wird, gibt es nicht.
4. **Profil-Upgrades mit Staging (`INV-STG-04`)**: Upgrades prüfen Manifest-Hashes, bereiten das nächste Profil im Staging vor und erstellen Backups. Nach bestimmten Commit-Fehlern wird eine hash-geschützte Wiederherstellung versucht. Sie ist bedingt und kann bei parallelen Änderungen oder weiteren Dateisystemfehlern scheitern.
5. **Gemeinsame Sitzungsnotizen (`INV-HANDOFF-05`)**: Klartextdateien (`CLAUDE.md`, `AGENTS.md`, `START.md`, `STATE.md`) halten Projekt- und Sitzungskontext für Agenten und Maintainer:innen fest. Die Vorlage kann nicht sicherstellen, dass ein Agent diese Einträge liest, befolgt oder behält.
6. **Gestaffelte Profile (`INV-TIER-06`)**: Die Vorlage bietet drei Dokumentationsprofile (`MINIMAL`, `STANDARD`, `FULL`); Profil-Upgrades erfolgen schrittweise.
7. **Ignore-Muster für Konfliktkopien (`INV-SYNC-07`)**: Die `.gitignore`-Dateien im Repository und in der Vorlage listen Muster für bekannte Synchronisationskonfliktkopien und Sperrdateien auf. Sie koordinieren keine parallelen Schreibvorgänge und bieten keine verteilte Live-Sperre.
8. **Journalgestützte Aufgabenarchivierung (`INV-AUDIT-08`)**: `todo-archive` stagt Änderungen an `TODO.md` und `DONE.md`, schreibt ein Journal, versucht nach Ersetzungsfehlern die Wiederherstellung und kann einen unterbrochenen Paar-Austausch fortsetzen. Abweichende Dateien können das Journal zur manuellen Prüfung zurücklassen.
9. **Laufzeitabhängigkeiten (`INV-LIC-09`)**: Das Projekt deklariert `dependencies = []` und verwendet zur Laufzeit die Python-Standardbibliothek. Entwicklungs- und Testwerkzeuge sind davon getrennt. `THIRD_PARTY_LICENSES.md` und `THIRD_PARTY_LICENSES.txt` listen die dokumentierten Abhängigkeits- und Lizenzeinträge auf; eine unabhängige Prüfung wird hier nicht behauptet.
10. **Richtlinie für Sicherheitsmeldungen (`INV-SLA-10`)**: `SECURITY.md` priorisiert Sicherheitskorrekturen und sieht für unterstützte Versionen `0.1.x` auf `main` Wartung nach bestem Bemühen vor. Eine Antwortzeit ist nicht garantiert. Versionen unter `0.1.0` werden nicht unterstützt.

### Richtlinien für Entwickler

- **Plan D Entwicklung**: Entwicklung, Git-Aktionen und Tests erfolgen ausschließlich im lokalen Git-Repository (`C:\_Local_DEV\repos\project-docs-template`).
- **Version-Freeze Disziplin**: Version `0.1.2` bleibt gemäß Richtlinie `T-20260920-167562623` eingefroren; Neuerungen werden unter `## [Unreleased]` im `CHANGELOG.md` gepflegt.
- **Python-Unterstützung**: Python 3.10 bis 3.13.
- **Qualitäts-Tore vor Commits**:
  - Bytecode-Prüfung: `python -m compileall -q .`
  - Linter: `ruff check .`
  - Testsuite: `python -m pytest -ra -v` (100% grün erforderlich)
- **Sicherheitsmeldungen**: Nutze bevorzugt ein privates GitHub Security Advisory oder die direkten Kontakte aus [SECURITY.md](SECURITY.md): `security@ellmos.ai`, `support@lukasgeiger.com` und `lukas@open-bricks.org`. Melde ungepatchte Schwachstellen nicht öffentlich; bis zur Veröffentlichung eines Patches bittet die Richtlinie um koordinierte Offenlegung.