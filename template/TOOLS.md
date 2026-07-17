# TOOLS.md — Router zu Admin-Utilities

> **Zweck:** Navigation. „Welches Tool macht was?"
> **Content:** Siehe `_tools/*` — hier steht **kein** Implementierungs-Detail.
> **Abgrenzung zu `core/`:** `core/` wird von der Haupt-Pipeline (`run.py` o.ä.)
> orchestriert. `_tools/` wird **manuell per Hand** aufgerufen — seltene
> Admin-Eingriffe, Notfall-Tooling, Dev-Utilities.

---

## Im Template gebündelte Tools

### Projekt-Bootstrap

| Tool | Zweck | Sprache | Häufigkeit |
|---|---|---|---|
| [`_tools/init-project`](./_tools/init-project) | Instanziiert das project-docs-Template in einem neuen Ordner mit gewähltem Profil (MINIMAL/STANDARD/FULL) | python | einmalig pro Projekt |

### Living Documentation

| Tool | Zweck | Sprache | Häufigkeit |
|---|---|---|---|
| [`_tools/doc-lint`](./_tools/doc-lint) | Validiert YAML-Frontmatter in Meta-Files (CLAUDE/START/STATE), prüft Staleness | python | bei Commit / regelmäßig |
| [`_tools/workflows-sync`](./_tools/workflows-sync) | Generiert `WORKFLOWS.md`-Router aus `workflows/*.md` (AUTOGEN-Block) | python | bei neuem Workflow |
| [`_tools/todo-archive`](./_tools/todo-archive) | Verschiebt `[x]`-Einträge aus `TODO.md` nach `DONE.md` mit Datum | python | regelmäßig |

## Optionale Referenzen, nicht im Template gebündelt

| Tool | Status | Hinweis |
|---|---|---|
| `_tools/arch-update` | geplant | Architektur-AUTOGEN ist als Muster vorbereitet, das konkrete Tool gehört aber noch nicht zum Template-Bundle. |
| `_tools/git-force-admin-push` | extern | Projektspezifisches Admin-Tool; bewusst nicht Teil des generischen `project-docs`-Templates. |

## Wann welches Tool?

- **Neues Projekt anlegen** → `init-project` (Profil wählen, loslegen)
- **Vor jedem Commit von Doku-Änderungen** → `doc-lint` (Frontmatter + Staleness)
- **Nach neuem Workflow in `workflows/`** → `workflows-sync` (Router updaten)
- **Am Session-Ende** (Cleanup) → `todo-archive`
- **Für Architektur-AUTOGEN später nachrüsten** → projektspezifisches `arch-update`, falls das Projekt diesen Generator wirklich braucht
- **Für Admin-Force-Pushes** → eigenes projektspezifisches Playbook statt generischer Template-Pflicht

## BACH-Inspiration

Drei der gebündelten Tools sind **konzeptionell adaptiert** aus dem BACH-System
(lokale Referenzimplementierung im BACH-Tooling):

| Unser Tool | BACH-Original | Adaption |
|---|---|---|
| `init-project` | `skill_generator.py` | 3-Profile-System statt 4 (MICRO/LIGHT/STANDARD/EXTENDED → MINIMAL/STANDARD/FULL) |
| `doc-lint` | `skill_header_gen.py` | Generisches project-docs statt BACH-spezifisches Skill-Manifest |
| `workflows-sync` | `workflows_export.py` | Nur Dateisystem statt Dateisystem + DB (kein bach.db nötig) |

Die BACH-Originale sind produktionserprobt und bleiben für die Wartung unserer
produktiven lokalen Ports die erste Referenz.

## Wann ein neues Tool anlegen

Ein neues Tool ist gerechtfertigt wenn:
- Die Operation **reproduzierbar** ist (gleicher Input → gleiches Ergebnis)
- Sie **manuell unbequem** ist (mehr als 3 Schritte, Fehler-anfällig)
- Sie **Side-Effects** hat, die im Fehlerfall aufwändig zu reparieren sind
- Ein **Trap-Safe-Mechanismus** möglich und nötig ist (Cleanup bei Abbruch)

Wenn einer dieser Punkte fehlt: **kein eigenes Tool**, sondern Workflow in
`workflows/` oder Alias in `.bashrc`.

## Konventionen

Siehe [`_tools/README.md`](./_tools/README.md) für:
- Naming (Verb-Pattern, ohne `.sh`-Extension, lowercase mit Bindestrich)
- Header-Kommentar-Format (Zweck, Usage, Requirements, Safety)
- Safety-Standards (`set -euo pipefail`, trap-Handler)
- Dokumentations-Pflicht (Eintrag hier + in `_tools/README.md`)
