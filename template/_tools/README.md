# _tools/ — Admin-Utilities außerhalb der Haupt-Pipeline

> **Lokale Konventionen** für Utility-Scripts in diesem Ordner.
<!-- profiles:FULL -->
> **Router im Root:** [`../TOOLS.md`](../TOOLS.md) — enthält die
> „Welches Tool wofür"-Übersicht.
<!-- /profiles -->

---

## Zweck

Sammlung von Shell-/Python-Utilities die **außerhalb** der Haupt-Pipeline
laufen (nicht aus `run.py` aufgerufen), aber für den Dev-/Admin-Workflow
nützlich sind.

Im Gegensatz zu `core/` (Module die von `run.py` orchestriert werden) sind
die Scripts hier **direkt per Hand aufrufbar** — gedacht für seltene,
manuelle Admin-Eingriffe oder Notfall-Tooling.

## Konventionen für neue Tools

### Naming

- **Verb-Pattern**, ohne `.sh`-Extension
- **Lowercase** mit Bindestrich: `git-force-admin-push`, `todo-archive`
- **Sprechend**, nicht kryptisch: `health-check` ja, `hc` nein
- **Als Git-Subcommand installierbar** (Namen mit `git-*` Prefix werden
  automatisch als `git <subcommand>` erkennbar wenn im PATH)

### Shebang

```bash
#!/usr/bin/env bash    # für Bash-Scripts
#!/usr/bin/env python3 # für Python-Scripts
```

### Executable

```bash
chmod +x _tools/your-tool
```

### Header-Kommentar (Pflicht)

```bash
#!/usr/bin/env bash
# your-tool — [einzeiler was das Tool macht]
#
# Usage:
#   _tools/your-tool [OPTIONS] [ARGS]
#
# Options:
#   -y, --yes        [Beschreibung]
#   -h, --help       Show this help
#
# Arguments:
#   ARG              [Beschreibung]
#
# Requirements:
#   - [Was wird vorausgesetzt]
#
# Safety features:
#   - [Welche Safeguards sind eingebaut]
```

### Safety-Standards

**Für bash-Scripts:**
```bash
set -euo pipefail
```
- `-e` — exit bei Fehler
- `-u` — exit bei ungesetzter Variable
- `-o pipefail` — Pipe-Errors propagieren

**Für destructive Operationen**: `trap cleanup EXIT INT TERM`
```bash
cleanup() {
    local exit_code=$?
    # revert temporäre Änderungen
    exit $exit_code
}
trap cleanup EXIT INT TERM
```

**Für interaktive Operationen**: Confirmation-Prompt (außer `--yes`)
```bash
if [[ $SKIP_CONFIRM -eq 0 ]]; then
    read -r -p "Continue? [y/N] " reply
    [[ "$reply" =~ ^[Yy]$ ]] || { echo "Aborted."; exit 1; }
fi
```

### Dokumentations-Pflicht

Bei neuem Tool:

1. **Dieser README.md** → neuer H2-Abschnitt mit:
   - Zweck
   - Warum es existiert (konkrete Entstehungssituation)
   - Nutzung + Beispiel-Output
   - Voraussetzungen
   - Safety-Features
   - Technische Funktionsweise
   - Bekannte Limitierungen
   - Geschichte

- Dokumentation im Projekt aktualisieren.
<!-- profiles:FULL -->
- **`../TOOLS.md`** → Eintrag in der Router-Tabelle
<!-- /profiles -->
<!-- profiles:STANDARD,FULL -->
- **`../CHANGELOG.md`** → Eintrag beim ersten Anlegen
- **`../DECISIONS.md`** → nur bei Architektur-relevanten Entscheidungen
   (z.B. „warum bash statt Python", „warum Tool statt Config-Änderung")
<!-- /profiles -->

## Beispiel: Minimal-Template für neues Tool

```bash
#!/usr/bin/env bash
# example-tool — short description
#
# Usage:
#   _tools/example-tool [OPTIONS] [ARG]
#
# Options:
#   -y, --yes    Skip confirmation
#   -h, --help   Show help
#
# Requirements:
#   - bash, git
#
# Safety:
#   - set -euo pipefail
#   - trap on EXIT for cleanup

set -euo pipefail

SKIP_CONFIRM=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    -y|--yes) SKIP_CONFIRM=1; shift ;;
    -h|--help) sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) break ;;
  esac
done

# ... tool logic ...
```

---

## Verfügbare Tools

*(Wird bei jedem neuen Tool hier erweitert)*

<!-- profiles:REPOSITORY -->
### Projekt-Bootstrap

#### `init-project` (python, PRODUKTIV)

**Zweck:** Template-Instantiator — kopiert project-docs-Template in einen
neuen Ordner, ersetzt Platzhalter, optional git init.

**Inspiriert von:** BACHs `tools/skill_generator.py` (4-Profil-System)

**Unser Profil-System:**
- `MINIMAL` (7 Root-Files + `_tools/`): AGENTS, CLAUDE, README, START, STATE, TODO, DONE
- `STANDARD` (12 Root-Files + `_tools/`): + CHANGELOG, HEADER-RULES, CUT-AND-CLUE, DECISIONS, PATTERNS
- `FULL` (16 Files + Ordner): + ARCHITECTURE, HEADER-RULES, CUT-AND-CLUE, WORKFLOWS, TOOLS, GLOSSARY + `workflows/`, `_tools/`, `.github/`

**Status:** Produktiv. Transaktionale Erzeugung, profilabhängige Inhalte,
Link-/Platzhalterprüfung und echte optionale Git-Initialisierung sind getestet.
<!-- /profiles -->

---

### Living Documentation

#### `doc-lint` (python, PRODUKTIV)

**Zweck:** Validiert YAML-Frontmatter in Meta-Files (CLAUDE.md, START.md,
STATE.md), prüft Staleness (last_verified), listet Fehler/Warnings.

**Inspiriert von:** BACHs `tools/skill_header_gen.py`

**Was es prüft:**
- Pflichtfelder pro File-Typ (`name`, `type`, `version`, `updated`, `last_verified`, ...)
- `type`-Match (CLAUDE.md muss `type: project-docs` haben, etc.)
- Staleness: `last_verified` > 30 Tage alt → WARN
- Felder-Reihenfolge (für `--fix`)

**Usage:**
```bash
doc-lint                    # Check aller Meta-Files im cwd
doc-lint --file CLAUDE.md   # Einzelnes File
doc-lint --fix              # Fehlende Felder einfügen
doc-lint --update-dates     # Timestamps auf heute setzen
doc-lint --strict           # Exit != 0 auch bei Warnings
```

**Status:** Produktiv. CLI, Parsing, atomarer `--fix`, Re-Lint und
`--update-dates` sind durch die Repository-Tests abgedeckt.

---

<!-- profiles:FULL -->
#### `workflows-sync` (python, PRODUKTIV)

**Zweck:** Generiert `WORKFLOWS.md`-Router aus `workflows/*.md`. Scannt alle
Workflow-Dateien, extrahiert Title + Purpose + Frequency + Duration, schreibt
kategorisierte Tabelle in AUTOGEN-Block.

**Inspiriert von:** BACHs `tools/workflows_export.py` (aber ohne DB)

**Pattern:** Dateisystem ist Source of Truth. `WORKFLOWS.md` hat einen
AUTOGEN-Block zwischen `<!-- @auto-generated:workflow-index -->` und
`<!-- @end:workflow-index -->`. Nur dieser Block wird ersetzt, Rest bleibt
unangetastet.

**Kategorisierung:** Automatisch nach Ordner-Struktur. Root-Level-Files →
"general", Unterordner → Kategorie-Name.

**Usage:**
```bash
workflows-sync              # Scan workflows/, update WORKFLOWS.md
workflows-sync --dry-run    # Plan anzeigen
workflows-sync --check      # CI-Mode: exit != 0 falls veraltet
```

**Status:** Produktiv. Tabellen-Metadaten werden maskiert, der AUTOGEN-Block
wird atomar und ohne Regex-Replacement-Nebenwirkungen aktualisiert.
<!-- /profiles -->

---

<!-- profiles:REPOSITORY -->
#### `arch-update` (python, GEPLANT)

**Zweck:** Parst `core/*.py` (o.ä.), generiert Module-Graph (mermaid) und
Module-Tabelle, ersetzt AUTOGEN-Blöcke in `ARCHITECTURE.md`.

**Status:** Noch nicht implementiert. Design siehe `DECISIONS.md` Diskussion
zu "Living Architecture".
<!-- /profiles -->

---

<!-- profiles:REPOSITORY -->
### Admin / Notfall

#### `git-force-admin-push` (bash + python)

**Zweck:** Temporärer Force-Push auf Branch-protected main/master für Admins,
ohne die BP dauerhaft zu schwächen. Unlock → Push → Relock mit trap-safety.

**Siehe:** [Details → TOOLS.md](../TOOLS.md)

**Status:** Produktiv (GithubBot-Kontext). Hier nur als Referenz erwähnt,
nicht im Template enthalten (kontext-spezifisch).
<!-- /profiles -->

---

#### `todo-archive` (python, PRODUKTIV)

**Zweck:** Verschiebt `[x]`-Einträge aus `TODO.md` mit heutigem Datum nach
`DONE.md`. Automatisierte Lösung gegen TODO.md-Wachstum.

**Status:** Produktiv. Dry-run und `--apply` sind implementiert; beide
Zieldateien werden vorgestaged und bei einem Schreibfehler zurückgerollt. Ein
atomisches Journal beendet nach einem Prozessabbruch den halben Pair-Commit,
ohne wiederkehrende gleichlautende Aufgaben aus der Historie zu verwerfen.

---

## Tool-Reifegrade

| Reifegrad | Bedeutung |
|---|---|
| **PRODUKTIV** | Der dokumentierte Vertrag ist durch das Repository-Gate abgedeckt |
| **CONCEPT (funktional)** | CLI läuft, Kern-Logik implementiert, TODO-Marker für Edge-Cases |
| **CONCEPT (Skizze)** | CLI-Interface + Dokumentation vorhanden, Kern-Logik als TODO |
| **GEPLANT** | Design fertig, noch nicht geschrieben |

Aktueller Stand im erzeugten Template-Bundle:
- `doc-lint` — PRODUKTIV
- `todo-archive` — PRODUKTIV
<!-- profiles:FULL -->
- `workflows-sync` — PRODUKTIV
<!-- /profiles -->
