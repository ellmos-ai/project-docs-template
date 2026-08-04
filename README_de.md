# Project Docs Template (Deutsche Dokumentation)

[![Template](https://img.shields.io/badge/template-agent--ready_project_docs-2f6f5e)](https://github.com/ellmos-ai/project-docs-template)
[![CI](https://github.com/ellmos-ai/project-docs-template/actions/workflows/ci.yml/badge.svg)](https://github.com/ellmos-ai/project-docs-template/actions/workflows/ci.yml)
[![Pytest](https://img.shields.io/badge/pytest-18%20passed-brightgreen.svg)](./tests/test_tools.py)
[![Language: English](https://img.shields.io/badge/Language-English-blue.svg)](./README.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

Agenten-optimierte Projektdokumentations-Vorlage mit START/STATE/TODO/DONE,
Workflows, leichtgewichtigen Tools und KI-freundlichem Projektgedächtnis.

> [!NOTE]
> Dieses Repository ist maschinenlesbar und für KI-Agenten optimiert. KI-Coding-Assistenten (Claude Code, Antigravity/Gemini, Codex) können [`llms.txt`](./llms.txt) als schnellen Kontext-Index nutzen und `pytest` (18 bestandene Tests) ausführen, um die Integrität der Vorlagengenerierung zu überprüfen.

Dieses Repository enthält ein kompaktes Dokumentations-Scaffold für Software-, Forschungs- und Betriebsprojekte, die mit LLM-Agenten gepflegt werden. Die Vorlage konzentriert sich auf klaren Projektstatus, Übergaben zwischen Sitzungen, Aufgabenhistorie, Entscheidungsaufzeichnungen und Workflows, ohne das Projekt in ein schwerfälliges Betriebssystem zu verwandeln.

## Architektur & Ablauf

```mermaid
graph TD
    A["LLM Coding Agent<br>(Claude Code / Antigravity / Codex)"] --> B["init-project CLI / Staging"]
    B --> C{"Profil wählen"}
    C -->|MINIMAL| D["Kern-Dokumente<br>(CLAUDE.md, START.md, STATE.md, TODO.md)"]
    C -->|STANDARD| E["Standard-Suite<br>(Minimal + DECISIONS.md, CHANGELOG.md)"]
    C -->|FULL| F["Enterprise Router<br>(Standard + WORKFLOWS.md, TOOLS.md, GLOSSARY.md)"]
    D --> G["Validierte Projekt-Vorlage"]
    E --> G
    F --> G
    G --> H["Deterministische Agenten-Übergabe & Sitzungsspeicher"]
```

## Verwendungsszenarien

| Situation | Vorteil |
|---|---|
| Ein neues Projekt wird von Claude Code, Codex, Gemini CLI oder einem anderen Agenten betreut | Bietet dem Agenten einen vorhersehbaren Bootstrap-Pfad und eine aktuelle Statusdatei. |
| Ein bestehendes Repo hat verstreute Notizen oder keine Übergabespur | Trennt aktive Arbeit, abgeschlossene Arbeit, Entscheidungen und Sitzungsstatus sauber. |
| Mehrere Agenten oder Entwickler müssen die Arbeit sicher fortsetzen | Hält Anweisungen, Status, Workflows und Tools in dedizierten Dateien. |

## Was enthalten ist

- `CLAUDE.md` und `AGENTS.md` für Agenten-Anweisungen
- `START.md` und `STATE.md` für den Sitzungs-Bootstrap und den aktuellen Status
- `TODO.md` und `DONE.md` mit optionaler Archivierungsunterstützung
- `DECISIONS.md`, `PATTERNS.md`, `CHANGELOG.md` und `HEADER-RULES.md`
- Optionale FULL-Profil-Router: `WORKFLOWS.md`, `TOOLS.md`, `GLOSSARY.md`
- Lokale Helfer unter `_tools/`, darunter `init-project`, `doc-lint`, `todo-archive` und `workflows-sync`

Die eigentlichen Vorlagendateien befinden sich in [`template/`](./template/).

## Schnellstart

Repository klonen und ein Projektprofil instanziieren:

```bash
git clone https://github.com/ellmos-ai/project-docs-template.git
cd project-docs-template
python template/_tools/init-project --target ../mein-projekt --name MeinProjekt --profile STANDARD
```

Optionale Flag `--author "Ihr Name"` zur Festlegung des Autors oder `--git` zur Erstellung eines `main`-Repositories mit Initial-Commit.

Verfügbare Profile:

- `MINIMAL`: 7 Stammdateien plus essentielle Werkzeuge
- `STANDARD`: 12 Stammdateien plus Entscheidungen & Changelog
- `FULL`: 16 Stammdateien plus Workflow-, Tool- und Glossar-Router

Alternativ können einzelne Dateien auch manuell aus [`template/`](./template/)
kopiert werden, wenn nur ausgewählte Teile benötigt werden.

Erfordert Python 3.10 oder neuer. Git wird nur für `--git` benötigt.

## Profil-Vergleich

| Profil | Bestes Szenario | Kopierte Dateien |
|---|---|---|
| `MINIMAL` | Kleine Repos, Experimente, kurze Tools | Core Agenten-Instruktionen, Start/State, TODO/DONE, Basis-Tools |
| `STANDARD` | Ernsthafte Projekte mit Entscheidungs- & Pflegebedarf | Minimal-Set plus Changelog, Entscheidungen, Muster & Regeln |
| `FULL` | Multi-Agenten- & Langzeitprojekte mit Routern & Workflows | Standard-Set plus Architektur, Workflow/Tool-Router & Glossar |

## Design-Prinzipien

- Jede Datei hat eine klar abgegrenzte Aufgabe.
- Die Übergabe zwischen Sitzungen ist explizit und kurz.
- Der Pflegeaufwand zählt mehr als die Vollständigkeit aller denkbaren Dokumente.
- Router wie `WORKFLOWS.md` und `TOOLS.md` verweisen auf Details an anderer Stelle.
- Abgeschlossene Aufgaben können automatisch archiviert werden, statt `TODO.md` aufzublähen.

Die vollständige Begründung und eine Erklärung Datei für Datei bietet
[`template/TEMPLATE.md`](./template/TEMPLATE.md).

## Verifizierung

```bash
python -m unittest discover -s tests -v
```

Die Testsuite prüft alle Profile, reale Git-Initialisierung, Frontmatter-Reparatur und TODO/DONE Rollback-Verhalten auf Windows, Linux und macOS; siehe [`RELEASE_GATE.md`](./RELEASE_GATE.md).

Sicherheitsmeldungen gehören in den privaten Kanal, der in
[`SECURITY.md`](./SECURITY.md) beschrieben ist, nicht in öffentliche Issues.

<!-- BEGIN ELLMOS BUNDLE DISCOVERY DE -->

## Bundles und Partner

Geprüfte Discovery-Projektion für `module:project-docs-template` aus
`catalog:v4-bundles`
(`546290dafbaafd810df1d59ef5a3d7183738472b48cd5a8a81f1e8f2b64d852e`).
Das Ziel-Repository ist `public`. Die Bundle-Manifeste bleiben die Autorität
für Mitgliedschaften; dieser Abschnitt installiert oder aktiviert keine
Komponenten. Die Freigabe beruht auf einem öffentlichen Modul-Registry-Eintrag
und einer ausdrücklichen Default-deny-Allowlist für Bundles.

### `ellmos-dev-lifecycle-bundle`

- Sichtbarkeit des Bundle-Rezepts: `private`; Rolle: `declared-component`;
  Anforderung: `required`.
- Modulpartner: `module:bundle-installer`, `module:ellmos-code-tools`,
  `module:ellmos-tests`, `module:github-onedrive-mirror`,
  `module:stack-system-installer`.
- Skill-Partner: `skill:bugfix-protocol`, `skill:bugsweep`, `skill:dev-cycle`,
  `skill:encoding-fix`, `skill:github-repo-care`, `skill:migrate-rename`,
  `skill:nulcleaner`, `skill:pipeline-optimizer`, `skill:plugin-system`,
  `skill:project-onboarding`, `skill:trampelpfadanalyse`.

### `ellmos-knowledge-bundle`

- Sichtbarkeit des Bundle-Rezepts: `private`; Rolle: `declared-component`;
  Anforderung: `recommended`.
- Modulpartner: `module:KnowledgeDigest`, `module:WikiStub-Seed`,
  `module:report-forge`, `module:web-scraper`.
- Skill-Partner: `skill:bilingual-doc-sync`, `skill:docs-analysis`,
  `skill:document-chunker`.

Kompositions- und Runtime-Details werden bewusst nicht offengelegt.

<!-- END ELLMOS BUNDLE DISCOVERY DE -->

## Auffindbarkeit (SEO)

Suchbegriffe:

```text
agent-ready project documentation template
LLM project docs template START STATE TODO DONE
Claude Code Codex project documentation scaffold
multi-agent repo handoff documentation template
```

Für crawler- und LLM-orientierte Metadaten siehe [`llms.txt`](./llms.txt).

## Lizenz

MIT Lizenz. Siehe [LICENSE](./LICENSE).

Dieses Projekt ist eine unentgeltliche Open-Source-Spende. Die Haftung ist gemäß § 521 BGB auf Vorsatz und grobe Fahrlässigkeit beschränkt. Die Nutzung erfolgt auf eigene Gefahr.
