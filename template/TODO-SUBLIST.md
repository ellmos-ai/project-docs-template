# TODO-<BEREICH> — Aufgaben für <Bereich / Rolle>

**Version:** 1.0
**Aktualisiert:** <YYYY-MM-DD>
**Grund:** Auslagerung aus `TODO.md` zur Begrenzung der Dateigröße
**Zweck:** Fokussierte Aufgabenliste für `<Bereich / Rolle>`. Erledigte Tasks wandern gemeinsam mit der Hauptliste nach [`DONE.md`](./DONE.md).

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt (z. B. durch Sync-Konflikte), zuerst vollständig diffen und verlustfrei in die kanonische Datei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang; Archive bleiben getrennt.

> **Dateigröße:** Wenn diese Unterliste > 150 offene Tasks überschreitet: erst per `_tools/todo-archive --todo TODO-<BEREICH>.md --done DONE.md --apply` leeren, danach ggf. weiter teilen → [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md).

---

> **Übergeordneter Index:** [`TODO.md`](./TODO.md) | **Zuständig:** `<Rolle / Team / Maintainer>`
> **Schreibregel:** Neue Aufgaben aus diesem Bereich direkt hier eintragen und den Bereichszähler in `TODO.md` bei größeren Änderungen mitpflegen.
> **Rückführung:** Sinkt die Summe offener Tasks über alle Unterlisten dauerhaft unter ~40 Einträge, Unterlisten nach Differenzprüfung wieder in `TODO.md` zusammenführen.

---

## Active

- [ ] [<Nächster konkreter Task in diesem Bereich mit klarer Exit-Bedingung>]

## Backlog

- [ ] [<Späterer Task in diesem Bereich>]

## Blocked

- [ ] [<Blockierter Task>] — wartet auf [<Entscheidung / Dependency / Zugang>]

---

## Format & Archivierung

- **Eine Zeile pro Task**, klare Exit-Bedingung, optional Datum bei lang offenen Tasks (`- [ ] <YYYY-MM-DD> Task ...`).
- **Gemeinsames Archivziel:** Erledigte `[x]`-Einträge werden nicht manuell gelöscht und nicht in eine zweite `DONE-*.md` verschoben, sondern gesammelt ins zentrale `DONE.md` überführt:

```bash
_tools/todo-archive --todo TODO-<BEREICH>.md --done DONE.md --apply
```

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
