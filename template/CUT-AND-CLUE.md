# CUT-AND-CLUE — Pointer-, Split- und Archivverfahren für zu lange Dateien

**Version:** 1.2
**Aktualisiert:** 2026-11-21
**Grund:** Relative Pfade (Portabilität), Indexdatei-Split für TODOs/Register, Vorrang von `_tools/todo-archive` sowie Alters-vs.-Längenregel für Logs ergänzt
**Zweck:** Hält lange Steuerdateien, Aufgabenlisten und Logs navigierbar, ohne Inhalte, Herkunft oder Verweise zu verlieren.

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt (z. B. durch Sync-Konflikte), zuerst vollständig diffen und verlustfrei in die kanonische Datei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang; Archive bleiben getrennt.

> **Dateigröße:** Wenn `CUT-AND-CLUE.md` zu lang wird: diese Datei ist selbstreferenziell — wende das Verfahren auf sich selbst an.

<!-- profiles:FULL -->
> **Abgrenzung zu [`MOVED-STUB.md`](./MOVED-STUB.md):** Cut-and-Clue teilt eine zu lang gewordene Datei in zwei Teile (Inhalt bleibt an **beiden** Orten bestehen). Ein `*.MOVED.md`-Stub markiert dagegen einen **kompletten Umzug** (Inhalt existiert nur noch am neuen Ort).
<!-- /profiles -->

---

## Was ist das Cut-and-Clue-Verfahren?

**Synonyme:** Pointer-Verfahren, Cut and Clue

Wenn eine Datei zu lang oder für ein LLM unhandlich wird, wird sie geteilt. Beide Teile verweisen mit **relativen, portablen Pfaden** (niemals lokale Benutzerpfade) aufeinander.

**Grundsatz:** **Alter allein ist nur bei Logs ein Cut-Trigger.** Konzepte, Policies, Pläne, aktive Aufgaben und Register werden wegen Umfang, Rolle, Abschluss oder sinkender Navigationsrelevanz geteilt oder archiviert — nicht, weil ihr Inhalt alt ist.

---

## Variante A — Logs & Register (Archivierung)

Für: Chronologische Logs (`CHECKS-LOG.txt`), selbstwachsende Registries.

### 1. Vorläufer archivieren
```text
DATEINAME.md  →  _archive/DATEINAME_ARCHIV_v1.md
```

### 2. Pointer in den Vorläufer einfügen (ans Ende)
```markdown
---
Pointer / Nachfolger:
Aktive Datei: ../DATEINAME.md
```

### 3. Neue Datei anlegen mit Pointer (nach Header)
```markdown
---
Pointer / Vorläufer:
Archiv: ./_archive/DATEINAME_ARCHIV_v1.md
---
```

### 4. Verweise in `AGENTS.md`, `CLAUDE.md` und weiteren Steuer-Dateien aktualisieren

---

## Variante B — Aufgabenlisten & Index-Split (TODO-Unterlisten oder sequenziell)

Für: `TODO.md` und andere aktive Aufgabenlisten im Projekt.

**Regel: Vor jedem Schnitt erst leeren.**
Sind erledigte Tasks (`[x]`) enthalten, zuerst `_tools/todo-archive --apply` ausführen, um erledigte Einträge nach `DONE.md` zu verschieben.

Bleiben danach > ~150 aktive Tasks (`[ ]`) oder mehrere klar trennbare Arbeitsbereiche:

- **Option B1 — Fachliche/Rollen-Unterlisten (empfohlen bei mehreren Arbeitsbereichen):**
  1. Unterlisten `TODO-<BEREICH>.md` anlegen (Vorlage: `TODO-SUBLIST.md`).
  2. `TODO.md` wird zum **Verzeichnis** (Index mit Unterlisten-Tabelle, Zählern und gemeinsamer Archivierungsregel nach `DONE.md`).
  3. Jede Unterliste verweist im Kopf zurück auf `./TODO.md` und archiviert ebenfalls nach `DONE.md`.
- **Option B2 — Sequenzielle Teilung (bei einem einzigen monolithischen Stream):**
  1. Aktive Tasks in `_reg/todo/TODO_2.md` (oder `TODO_2.md`) übertragen.
  2. Pointer mit relativem Pfad ans Ende von `TODO.md` und an den Anfang von Teil 2 setzen.
  3. Bei Schrumpfung unter ~40 aktive Tasks Teile nach Differenzcheck wieder in `TODO.md` zusammenführen.

---

## Variante C — Policies (sequenzielle Nummerierung, empfohlen)

Für: Regelwerke und Policies, die evolvieren statt archiviert werden.

1. Neue Datei anlegen: `FILENAME_2.md` (mit vollständigem neuem Inhalt).
2. Alte `FILENAME.md` zu reinem Pointer reduzieren:
```markdown
# FILENAME — veraltet, Pointer
Diese Datei wurde ersetzt.
Aktive Version: ./FILENAME_2.md
```
3. Alle Verweise in `AGENTS.md`, `CLAUDE.md` und weiteren Steuerdateien auf `./FILENAME_2.md` umstellen.

---

## Wann schneiden?

| Dateityp | Verfahren | Faustregel |
|---|---|---|
| Logs | A — Archivierung | älter als 6 Monate **oder** > ~300 Zeilen |
| Registries, Status-Snapshots | A — Archivierung / Index | > 200–300 Zeilen |
| Policies, Regelwerke | C — Sequenziell | > 400 Zeilen |
| Aufgaben mit vielen `[x]`-Tasks | — | Zuerst `_tools/todo-archive --apply` (→ `DONE.md`) |
| Aufgaben mit > 150 offenen Tasks | B — Unterlisten oder Sequenziell | > 150 Zeilen aktive Tasks (`[ ]`) |

## Selbstheilungs-Prüfung nach jedem Cut

1. Stimmen Basisdatei, Teile und bidirektionale **relative** Vor-/Nachfolger-Pointer?
2. Existiert genau eine aktive kanonische Quelle ohne ungemergte Dubletten?
3. Sind bekannte Einstiegsdateien (`CLAUDE.md`, `START.md`, ggf. `MASTER-REGISTRY.md`) aktualisiert?

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
