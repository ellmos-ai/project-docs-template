# HEADER-RULES — Standard-Kopfzeilen für Steuer-Dateien

**Version:** 1.2
**Aktualisiert:** 2026-11-21
**Grund:** 2-Ebenen-Header-System, vollständiger Selbstheilungs-Passus (Multi-Writer-/Konflikt-Merge & Lock-Vorrang) sowie datierte Zählstände integriert
**Zweck:** Definiert den Standard-Header und -Footer für alle Projekt-Steuerdateien — sorgt für Konsistenz, Maschinenlesbarkeit, Konflikt-Resilienz und autonome Selbstkorrektur.

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt (z. B. durch Sync-Konflikte), zuerst vollständig diffen und verlustfrei in die kanonische Datei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang; Archive bleiben getrennt. Kodierungs- oder Formatkorrekturen vor dem Schreiben trocken prüfen und echte Umlaute bewahren.

> **Dateigröße:** Wenn diese Datei zu lang wird: Verwende das Cut-and-Clue-Verfahren → [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md).

---

## Das 2-Ebenen-Header-System

Um sowohl automatisierte Tool-Validierung als auch unmittelbare Lesbarkeit im Agenten-Kontext zu verbinden, unterscheidet das Template zwei Header-Ebenen:

### Ebene 1: Maschinenlesbares YAML-Frontmatter (Session-Kernset)

Gilt verbindlich für die drei zentralen Session-Steuerdateien:

- `CLAUDE.md` (Primär-Instruktionen, zusätzlich `created` und `reason_last_change`)
- `START.md` (Session-Bootstrap, imperativ)
- `STATE.md` (Aktueller Snapshot, zusätzlich `updated_by` und `current_phase`)

Diese Dateien beginnen mit YAML-Frontmatter (`--- ... ---`), das von `_tools/doc-lint` auf Pflichtfelder, Typ und Staleness (`last_verified`) geprüft wird. Direkt unter dem Titel folgt der Selbstkorrektur-, Selbstheilungs- und Cut-and-Clue-Block.

### Ebene 2: Strukturierter Markdown-Header (Governance-, Register- & Referenzdateien)

Gilt für alle weiteren Steuer-, Register-, Architektur- und Governance-Dokumente (`ARCHITECTURE.md`, `CHANGELOG.md`, `CUT-AND-CLUE.md`, `DECISIONS.md`, `DONE.md`, `GLOSSARY.md`, `HEADER-RULES.md`, `MASTER-REGISTRY.md`, `MOVED-STUB.md`, `PATTERNS.md`, `REG-TEMPLATE.md`, `TODO.md`, `TODO-SUBLIST.md`, `TOOLS.md`, `WORKFLOWS.md`):

```markdown
# DATEINAME — Zweck in einem Satz

**Version:** <X.Y>
**Aktualisiert:** <YYYY-MM-DD>
**Grund:** <Kurze Beschreibung der letzten Änderung>
**Zweck:** <Ein Satz: Was ist diese Datei? Welche Frage beantwortet sie?>

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt (z. B. durch Sync-Konflikte), zuerst vollständig diffen und verlustfrei in die kanonische Datei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang; Archive bleiben getrennt.

> **Dateigröße:** Wenn diese Datei zu lang wird: Verwende das Cut-and-Clue-Verfahren → [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md).

---
[Inhalt]
---
<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
```

## Qualitätsregel: Datierte Zählstände

Zählstände in Steuertexten (z. B. Anzahl von Modulen, Tests oder offenen Punkten) werden nur **mit Messdatum und Quelle** angegeben (z. B. `14 Module, Stand <YYYY-MM-DD> laut MASTER-REGISTRY.md`). Undatierte Zahlen veralten unbemerkt und erzeugen Scheindivergenzen.

## Pflicht-Footer

```markdown
---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
```

## Versionierung

- Patch (`X.Y` → `X.Y+1`): Kleine Korrekturen, Verweise, Tippfehler
- Minor (`X.Y` → `X+1.0`): Neue Abschnitte, strukturelle Änderungen
- Für übergroße Dateien: Cut-and-Clue statt Major-Version

## Dateiendungs-Konvention

| Typ | Endung | Beispiele |
|---|---|---|
| Policies, Regelwerke, Multi-Agent-Einstiege | `.md` | `AGENTS.md`, `CLAUDE.md`, `DECISIONS.md` |
| Projekt-Steuerdateien, Register und Aufgabenlisten | `.md` | `START.md`, `STATE.md`, `TODO.md`, `DONE.md`, `MASTER-REGISTRY.md` |
| Einfache Export-/Maschinen-Logs | `.txt` | `CHECKS-LOG.txt`, `export.txt` |

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
