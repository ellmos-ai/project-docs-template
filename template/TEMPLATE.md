# TEMPLATE.md — Meta-Info zu diesem Template

> **Nicht ins Zielprojekt kopieren.** Diese Datei ist die Bedienungsanleitung
> für das Template selbst und wird beim Ausrollen weggelassen oder gelöscht.

## Was ist dieses Template

Ein **Doku-Skelett** für neue Projekte, das die aus langer Diskussion
herauskristallisierten „Gold-Set"-Dateien enthält. Jede Datei hat eine
**eindeutige, nicht-überlappende Rolle** und wurde gewählt nach dem Kriterium:
maximaler Nutzen für LLM-Agenten bei minimaler Pflegelast.

Das Template ist **Doku-fokussiert**, nicht System-fokussiert. Für
Agent-/Skill-OS-Strukturen (`_boot/`, `_memory/`, `_registry/`, etc.) sollte
ein separates OS-/Runtime-Template verwendet werden. Die Ebenen ergänzen sich,
sie konkurrieren nicht.

## Wann dieses Template nutzen

- Neues Software-Projekt, das von einem LLM-Agent mitgepflegt wird
- Bestehendes Projekt, das unorganisierte .md-Files im Root hat
- Referenz-Punkt wenn du dich fragst „welches File soll ich anlegen"
- Als Argument wenn jemand ein 16. Root-.md-File vorschlägt

## Wie das Template nutzen

### Variante A: Copy-Paste
```bash
# Von hier ins Zielprojekt kopieren (nur die relevanten Files)
git clone https://github.com/ellmos-ai/project-docs-template.git
cp -r project-docs-template/template/* /path/to/new/project/
cd /path/to/new/project
rm TEMPLATE.md           # Diese Meta-Datei raus
# Dann Platzhalter [...] in jeder Datei ersetzen
```

### Variante B: Profil-basiert (empfohlen)

Das Template definiert **3 Profile** (inspiriert vom BACH-Skill-Generator-Pattern).
Wähle das Profil, das zum Projekt-Umfang passt:

#### Profil **MINIMAL** (7 Root-Files + `_tools/`)
Für kleine Projekte, Proof-of-Concepts, Experimente, Ein-Wochen-Hacks —
aber schon mit dem vollständigen Session-Kernset.

```
AGENTS.md       # Redirect auf CLAUDE.md für andere Agent-Tools
CLAUDE.md       # Pflicht — auto-loaded von Claude Code
README.md       # Pflicht — Human-first für GitHub
START.md        # Session-Bootstrap
STATE.md        # Wo-stehen-wir-Snapshot
TODO.md         # Aktive Tasks
DONE.md         # Erledigte Tasks

_tools/         # Mindestens `todo-archive` + `doc-lint`
```

**Wann:** <500 LOC, Solo-Dev, klarer Scope, wenig Zusatz-Doku nötig, aber
kein paralleler Minimal-Standard ohne Start-/State-/Done-Dateien.

#### Profil **STANDARD** (12 Root-Files + `_tools/`)
Für ernsthafte Projekte mit mehrmonatiger Lebensdauer.

```
AGENTS.md        # Redirect für agent-agnostische Tools
CLAUDE.md        # Instructions (mit YAML-Frontmatter)
README.md        # Human-first
START.md         # Session-Bootstrap (aktiv, imperativ)
STATE.md         # Wo-stehen-wir-Snapshot
CHANGELOG.md     # Zeit-Achse
HEADER-RULES.md  # Header-/Footer-Konventionen für Steuer-Dateien
CUT-AND-CLUE.md  # Pointer-Verfahren für zu lange Dateien
DECISIONS.md     # Warum-Entscheidungen (ADR-Pattern)
PATTERNS.md      # Do/Don't mit Code-Beispielen
TODO.md          # Aktiv
DONE.md          # Erledigt (optional: mit _tools/todo-archive)
```

**Wann:** Multi-Monats-Projekt, potenziell mehrere Mitwirkende, komplexe Entscheidungen.

#### Profil **FULL** (16 Root-Files + 3 Ordner + Tools)
Für komplexe Projekte mit Multi-Agent-Orchestrierung oder langfristiger Wartung.

```
CLAUDE.md          # + Multi-Agent-Section ausgefüllt
AGENTS.md          # Stub-Redirect (Cross-Tool-Kompatibilität)
README.md
START.md
STATE.md
ARCHITECTURE.md    # Mit AUTOGEN-Markern
CHANGELOG.md
HEADER-RULES.md    # Header-/Footer-Konventionen für Steuer-Dateien
CUT-AND-CLUE.md    # Pointer-Verfahren für zu lange Dateien
DECISIONS.md
PATTERNS.md
WORKFLOWS.md       # Router → workflows/
TOOLS.md           # Router → _tools/
TODO.md
DONE.md
GLOSSARY.md        # Jargon

workflows/         # Multi-Step-Playbooks
├── README.md
└── <sprechende-namen>.md

_tools/            # Admin-Utilities + Generatoren
├── README.md
├── init-project       # Template-Instantiator
├── doc-lint           # Frontmatter-Validator
├── workflows-sync     # Router-Generator
└── <weitere>

.github/           # GitHub-native
```

**Wann:** Multi-Monat+ Projekt, mehrere Agents, umfangreiche Automatisierung,
Living-Documentation mit Auto-Generatoren.

### Profil-Upgrade-Pfad

Projekte wachsen. Ein MINIMAL-Projekt kann später STANDARD werden, STANDARD
kann FULL werden. **Reihenfolge für Upgrades:**

1. `MINIMAL → STANDARD`: Beim ersten Mal wenn du zusätzlich belastbare
   Entscheidungs- und Historien-Doku brauchst → `CHANGELOG.md`,
   `DECISIONS.md` und `PATTERNS.md` ergänzen.

2. `STANDARD → FULL`: Beim ersten Mal wenn Architektur, Workflows, GitHub-
   Scaffolding oder Glossar eigene Router brauchen → `ARCHITECTURE.md`,
   `WORKFLOWS.md`, `TOOLS.md`, `GLOSSARY.md`, `workflows/` und `.github/`
   ergänzen.

**Niemals prophylaktisch upgraden.** Bis der konkrete Bedarf da ist, ist die
Zusatzdatei nur Wartungsballast.

## Die Gold-Set-Logik in 6 Sätzen

1. **Jede Datei hat eine eigene, nicht-überlappende Rolle** — keine Dubletten wie DECISIONS.md + DECIDED.md
2. **Disziplin wird automatisiert statt erzwungen** — TODO→DONE via Tool, ARCHITECTURE via Generator, WORKFLOWS.md via `workflows-sync`
3. **Router-Pattern für Skalierbarkeit** — `WORKFLOWS.md` + `workflows/*`, `TOOLS.md` + `_tools/*`
4. **CLAUDE.md ist privilegiert weil auto-loaded** — was garantiert gelesen werden muss, gehört dort rein
5. **Profile statt Fixed-Sets** — MINIMAL/STANDARD/FULL für verschiedene Projektgrößen, niedrige Einstiegshürde
6. **YAML-Frontmatter für Maschinenlesbarkeit** — jedes Meta-File hat einen parsebaren Header, validierbar via `_tools/doc-lint`

## Dateien im Template

### Root-Files (16)

| File | Rolle | Zeit-Dimension |
|---|---|---|
| `CLAUDE.md` | Primary instructions, auto-loaded | stabil |
| `AGENTS.md` | Stub-Redirect für tool-agnostische Agent-Files | stabil |
| `START.md` | Session-Bootstrap, imperativ, aktiv | stabil |
| `STATE.md` | Wo-stehen-wir-Snapshot, pro Session | volatil (Tage/Wochen) |
| `README.md` | Human-first, für GitHub-Besucher | stabil |
| `ARCHITECTURE.md` | Struktur mit AUTOGEN-Markern | semi-stabil (Code-getrieben) |
| `CHANGELOG.md` | Zeit-Achse, append-only | append-only |
| `HEADER-RULES.md` | Header-/Footer-Regeln für Steuer-Dateien | stabil |
| `CUT-AND-CLUE.md` | Pointer-Verfahren für übergroße Dateien | stabil |
| `DECISIONS.md` | Warum-Achse, ADR-Pattern | append-only |
| `PATTERNS.md` | Do/Don't mit Code-Beispielen, Reminders | append-only |
| `WORKFLOWS.md` | Router → `workflows/*.md` | stabil (Router) |
| `TOOLS.md` | Router → `_tools/*` | stabil (Router) |
| `TODO.md` | Aktive Tasks (nur `[ ]`) | volatil |
| `DONE.md` | Erledigte Tasks (automatisiert via `_tools/todo-archive`) | append-only |
| `GLOSSARY.md` | Jargon, Begriffs-Definitionen | stabil |

### Strukturierte Ordner (3)

```
workflows/    # Multi-Step-Playbooks mit Side-Effects
├── README.md # Lokale Konventionen
└── <name>.md # Einzelne Workflows (sprechende Namen!)

_tools/       # Admin-Utilities außerhalb der Haupt-Pipeline
├── README.md # Lokale Konventionen
└── <name>   # Executable scripts (bash/python)

.github/      # GitHub-native (workflows, templates, ISSUE_TEMPLATE, etc.)
```

## Bewusst weggelassen (Anti-Patterns)

- `DECIDED.md`, `DECISION-GROUND-TRUTH.md`, `ONLY-TRUTH.md` → Dubletten von DECISIONS.md
- `RULES.md`, `GUIDELINES.md`, `BESTPRACTICES.md` → gehören als Abschnitte in CLAUDE.md
- `INFO.md`, `START.md` als Alternative zu CLAUDE.md → zu generisch / Redundanz
- `SELF-CHECKS.md`, `BETWEEN-TASK-CHECKS.md` etc. → gehören als Hooks in `.claude/settings.json`
- `SCRATCH.md`, `WORKING-MEMORY.md` → Input-Disziplin scheitert real, STATE.md (Output-Disziplin) ersetzt es
- `SNAP.md` → kryptischer Name
- `DONE.md` **ohne** Automation → wird selbst zum Moloch. Template enthält Hinweis auf `_tools/todo-archive`
- `BOOT.md`, `BOOTING.md` → schlechter Sprach-Trigger als START.md
- Pro-Workflow getrennte Files mit Buchstaben-Suffix (`WORKFLOW-A.md`, `WORKFLOW-B.md`) → Namens-Explosion

## Philosophie

**Template ist Vorschlag, nicht Gesetz.** Wenn dein Projekt eine Datei nicht
braucht, lass sie weg. Wenn du eine Datei brauchst die nicht hier ist, füge sie
hinzu — aber nur wenn du eine **eindeutige Rolle** benennen kannst, die keine
existierende Datei hat. „Ich könnte mir vorstellen das wäre nützlich" ist kein
Grund. „Ohne dieses File kann ich X nicht erreichen" ist einer.

**Wenn eine Datei nicht gepflegt wird, ist sie ein Risiko, kein Vorteil.**
Veraltete Doku ist schlechter als keine Doku, weil sie Vertrauen erzeugt das
nicht gerechtfertigt ist. Lieber ein ehrliches „hier gibt's noch keine" als ein
falsches „stand 2024-01-05".

## Innovationen aus .SOFTWARE-Pipeline (2026-06-02)

Diese Konzepte wurden aus der aktiven .SOFTWARE-Pipeline zurückübertragen
und sind nun Teil des Template-Standards:

### Selbstheilungs-Passus (in alle Steuer-Dateien)

Jede Root-Steuerdatei bekommt diesen Blockquote-Block direkt nach dem Header:

```markdown
> Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet
> wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder
> erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du
> gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht,
> setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> Wenn diese Datei zu lang wird: Verwende das Cut-and-Clue-Verfahren → CUT-AND-CLUE.md
```

**Warum:** Verhindert Doku-Fäulnis. Gibt dem Agenten explizite Erlaubnis und Pflicht,
veraltete Stellen selbst zu korrigieren — ohne auf menschliche Code-Reviews zu warten.

### REMEMBER-Footer

Am Ende jeder Steuerdatei:
```
<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE Ü Ö Ä -->
```

**Warum:** Einfache, persistente Erinnerung die kein Extra-Dokument braucht.

### Header-Felder: Zweck und Grund

Jede Steuerdatei (`.md`) bekommt im Markdown-Header (nicht nur YAML):
```
**Version:** X.Y
**Aktualisiert:** YYYY-MM-DD
**Grund:** [Was wurde warum geändert]
**Zweck:** [Ein Satz was diese Datei tut]
```

**Warum:** Das YAML-Frontmatter ist für Maschinen. Die Markdown-Felder sind für
Agenten die die Datei im Chat-Kontext lesen ohne YAML zu parsen.

### Cut-and-Clue-Verfahren (`CUT-AND-CLUE.md`)

Drei Varianten für übergroße Dateien:
- **A (Archivierung):** Logs/Registries → `_archive/DATEI_ARCHIV_v1.md`
- **B (Sequenziell):** Aufgabenlisten mit aktiven Tasks → `TODO_2.txt`
- **C (Sequenziell, Policies):** Regelwerke → `POLICY_2.md`, alte wird Pointer

**Warum:** Verhindert monolithische Dateien (>200-400 Zeilen) die langsam werden
und Kontext-Fenster verstopfen.

### Neue Template-Dateien

| Datei | Profil | Zweck |
|---|---|---|
| `HEADER-RULES.md` | STANDARD/FULL | Konsolidiert alle Header-Konventionen |
| `CUT-AND-CLUE.md` | STANDARD/FULL | Pointer-Verfahren für übergroße Dateien |

## Historie

- **2026-06-02** — Innovationen aus .SOFTWARE-Pipeline zurückübertragen
  - Selbstheilungs-Passus, REMEMBER-Footer, Header-Felder Zweck/Grund
  - Neue Template-Dateien: `HEADER-RULES.md`, `CUT-AND-CLUE.md`
  - `reason_last_change` ins YAML-Frontmatter von `CLAUDE.md` aufgenommen

- **2026-04-08** — Template erstellt aus Diskussion zur Doku-Architektur
  - Ursprung: Umfrage zu Doku-File-Pattern mit durchlaufenen Kandidaten
    (DONE, RULES, SELF-CHECKS, BOOT, SNAP, WORKING-MEMORY, …)
  - Gold-Set destilliert nach Eliminierungs-Kriterien: eindeutige Rolle,
    niedriger Pflegeaufwand, LLM-Freundlichkeit, Team-Ready
  - Ergebnis: 14 Root-Files + 3 strukturierte Ordner

- **2026-06-12** — Profil- und Tooling-Konsistenz nachgezogen
  - `HEADER-RULES.md` und `CUT-AND-CLUE.md` sind jetzt auch in `STANDARD` und `FULL` generatorisch hinterlegt
  - Profilzählungen und Root-File-Liste auf den aktuellen 16-Dateien-Stand angeglichen
  - `doc-lint` bewahrt `reason_last_change` in `CLAUDE.md` jetzt auch bei `--fix`/`--update-dates`
