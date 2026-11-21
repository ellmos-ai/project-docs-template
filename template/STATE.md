---
name: "[project-name]-state"
type: state-snapshot
version: 0.1.0
updated: "[YYYY-MM-DD HH:MM]"
updated_by: "[Claude | Gemini | Mensch]"
current_phase: "[phase-name]"
last_verified: "[YYYY-MM-DD]"
description: |
  Current-state snapshot for fast session-start orientation in [project-name].
---

# STATE.md — Aktueller Projekt-Stand

> **Zweck:** Wo-stehen-wir-Snapshot für den schnellen Session-Start.
> **Pflege:** Einmal pro Session am Session-Ende aktualisieren (nicht während).
> **Semantik:** Output-Disziplin — destillierte Essenz, kein Brain-Dump.

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt (z. B. durch Sync-Konflikte), zuerst vollständig diffen und verlustfrei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang.

<!-- profiles:STANDARD,FULL -->
> **Wasserlinie & Dateigröße:** `STATE.md` bleibt ein kompakter Snapshot (~100–200 Zeilen). Ausführliche Prüfchroniken gehören in ein separates Check-Register/Log, nicht hierher. Wächst die Datei über ~200 Zeilen, Vorläufer nach [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md) (Variante A) ins Archiv schneiden und verlinken.
<!-- /profiles -->

---

**Next review:** bei Phasen-Wechsel oder nach 2 Wochen

## Current Phase

[Phase 1 — Initial Setup / Phase 2 — Core Features / Phase 3 — ...]

## Focus gerade

[1-2 Sätze: woran wird aktuell gearbeitet]

## Letzte bedeutsame Aktion

[Was wurde in der letzten Session abgeschlossen? 2-4 Sätze.]

## Next

- [ ] [Nächster konkreter Schritt]
- [ ] [Noch einer]
- [ ] [Maximal 5 — dies ist kein TODO.md-Ersatz, nur Highlights]

## Aktuelle Blocker

- [Blocker mit Kontext, oder „— keine —"]

## Notizen für nächste Session

- [Dinge, die man beim nächsten Start wissen sollte]
- [Laufende Experimente]
- [Offene Fragen an den User]

---

## Historie (letzte 5 State-Updates)

> Kurze Chronik, damit Staleness sichtbar ist. Ältere Einträge werden
> entfernt, in `CHANGELOG.md` verdichtet oder per Cut-and-Clue archiviert.

- **[YYYY-MM-DD]** — [Ein-Zeiler was sich geändert hat]
- **[YYYY-MM-DD]** — [Ein-Zeiler]

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
