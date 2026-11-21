# DONE.md — Erledigte Tasks (Archiv)

**Version:** 0.1.0
**Aktualisiert:** [YYYY-MM-DD]
**Grund:** [Was wurde warum geändert]
**Zweck:** Fine-grained Task-Level-History von [Projektname] (umgekehrt chronologisch, neueste oben).

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt (z. B. durch Sync-Konflikte), zuerst vollständig diffen und verlustfrei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang.

> **Pflege:** Automatisch via `_tools/todo-archive --apply` (auch für optionale `TODO-<BEREICH>.md`-Unterlisten via `--todo TODO-<BEREICH>.md --done DONE.md --apply`). Niemals manuell kürzen.
<!-- profiles:STANDARD,FULL -->
> **Rotation:** Einträge älter als 6 Monate oder > ~300 Zeilen → nach `_archive/done-YYYY-QX.md` schneiden → [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md) (Variante A) oder in `CHANGELOG.md` zusammenfassen.
<!-- /profiles -->

---

## [YYYY-MM-DD]

- [x] [Erledigte Task mit Kontext]
- [x] [Noch eine]

## [YYYY-MM-DD]

- [x] [Erledigte Task]

---

## Abgrenzung zu CHANGELOG.md

| File | Granularität | Zielgruppe |
|---|---|---|
| **DONE.md** | Fine-grained (einzelne Tasks) | Dev-interner Blick zurück |
| **CHANGELOG.md** | Coarse-grained (Features, Versionen) | User / Nutzer / externe Stakeholder |

Bei Release werden die `DONE.md`-Einträge des Zeitraums zu einem `CHANGELOG.md`-Block zusammengefasst — **nicht 1:1 kopiert**, sondern destilliert.

## Format-Hinweis

Jeder Eintrag ist ein einzelner Task wie er in `TODO.md` (oder einer `TODO-<BEREICH>.md`-Unterliste) stand, mit `[x]`-Markierung erhalten. Der Datums-Header kommt vom Archivierungs-Tool. Wenn du manuell Einträge hinzufügen musst (z. B. vergessene History), nutze dasselbe Format für Konsistenz.

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
