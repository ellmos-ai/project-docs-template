# CUT-AND-CLUE — Pointer-Verfahren für zu lange Dateien

**Version:** 1.0
**Aktualisiert:** 2026-06-02
**Grund:** Aus .SOFTWARE-Pipeline zurückübertragen
**Zweck:** Beschreibt das Pointer-Verfahren (Cut and Clue) zum Archivieren zu langer Dateien mit bidirektionalen Pfad-Verweisen.

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, korrigiere diese Datei autonom.

> **Dateigröße:** Wenn diese Datei zu lang wird: sie ist selbstreferenziell — wende das Verfahren auf sich selbst an.

---

## Was ist das Cut-and-Clue-Verfahren?

**Synonyme:** Pointer-Verfahren, Cut and Clue

Wenn eine Datei zu lang wird, wird sie geteilt. Beide Teile verweisen mit
exakten Pfaden aufeinander. Es gibt drei Varianten je nach Dateityp.

---

## Variante A — Logs & Register (Archivierung)

Für: Chronologische Logs, Registries mit wachsendem Inhalt.

### 1. Vorläufer archivieren
```
DATEINAME.md  →  _archive/DATEINAME_ARCHIV_v1.md
```
(oder projektspezifischen Archiv-Ordner nutzen)

### 2. Pointer in den Vorläufer einfügen (ans Ende)
```
---
Pointer / Nachfolger:
Aktive Datei: [absoluter Pfad zur neuen Datei]
```

### 3. Neue Datei anlegen mit Pointer (nach Header)
```
---
Pointer / Vorläufer:
Archiv: [absoluter Pfad zur archivierten Datei]
---
```

### 4. Verweise in CLAUDE.md und anderen Steuer-Dateien aktualisieren

---

## Variante B — Aufgabenlisten (sequenzielle Nummerierung)

Für: `TODO.md`, `AUFGABEN.md` oder andere aktive Aufgabenlisten im Projekt.

**Regel: Nur schneiden wenn noch aktive Tasks drin sind.**
Sind alle erledigt → stattdessen leeren (erledigte → `DONE.md`).

1. Aktive Tasks in `TODO_2.md` übertragen
2. Pointer ans Ende der alten Datei
3. Pointer an Anfang der neuen Datei
4. Alte Datei bleibt als Archiv (kein Rename)

---

## Variante C — Policies (sequenzielle Nummerierung, empfohlen)

Für: Regelwerke, Policies die evolvieren statt archiviert werden.

1. Neue Datei anlegen: `FILENAME_2.md` (mit vollständigem neuen Inhalt)
2. Alte `FILENAME.md` zu reinem Pointer reduzieren:
```markdown
# FILENAME — veraltet, Pointer
Diese Datei wurde ersetzt.
Aktive Version: [Pfad zu FILENAME_2.md]
```
3. Alle Verweise in CLAUDE.md auf `_2.md` umstellen

---

## Wann schneiden?

| Dateityp | Variante | Faustregel |
|---|---|---|
| Logs, Registries | A — Archivierung | > 200-300 Zeilen |
| Policies, Regelwerke | C — Sequenziell | > 400 Zeilen |
| Aufgaben mit aktiven Tasks | B — Sequenziell | > 150 Zeilen aktive Tasks |
| Aufgaben vollständig erledigt | — | Leeren, erledigte → DONE.md |

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE Ü Ö Ä -->
