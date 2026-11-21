# TODO.md — Aktive Tasks

**Version:** 0.1.0
**Aktualisiert:** [YYYY-MM-DD]
**Grund:** [Was wurde warum geändert]
**Zweck:** Zentrale Liste aller offenen Aufgaben (`[ ]`) von [Projektname] — bzw. Index-Verzeichnis auf bereichsbezogene Unterlisten bei wachsendem Umfang.

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt (z. B. durch Sync-Konflikte), zuerst vollständig diffen und verlustfrei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang.

> **Regel:** Nur **offene** Tasks (`[ ]`). Erledigtes (`[x]`) wird via `_tools/todo-archive` nach [`DONE.md`](./DONE.md) verschoben.
> **Pflege:** Während der Arbeit laufend, am Session-Ende aufräumen.
<!-- profiles:STANDARD,FULL -->
> **Dateigröße:** Vor jedem Teilen erst via `_tools/todo-archive --apply` leeren. Bleiben > 150 offene Tasks oder wachsen Bereiche stark auseinander, in Unterlisten aufspalten → [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md).
<!-- /profiles -->

---

## Active

- [ ] [Nächster konkreter Task mit klarer Exit-Bedingung]
- [ ] [Weiterer Task]

## Backlog

- [ ] [Späterer Task, noch nicht aktueller Fokus]

## Blocked

- [ ] [Blockierter Task] — wartet auf [Entscheidung/Dependency/Zugang]

---

## Aufspalt-Regel: Unter-TODO-Listen (optional bei Wachstum)

Solange das Projekt überschaubar ist (< ~80–150 offene Tasks), bleibt diese einzelne `TODO.md` die einzige Aufgabenliste.

**Wann aufspalten:**
1. Zuerst alle `[x]`-Einträge per `_tools/todo-archive --apply` nach `DONE.md` auslagern.
2. Bleiben danach **> ~150 offene Tasks** oder arbeiten mehrere Bereiche/Rollen dauerhaft parallel (z. B. IT, Dokumentation, Recht/Compliance, manuelle User-Aufgaben), nach Bereichen aufspalten: `TODO-<BEREICH>.md` (Kopiervorlage im Template-Repo: `template/TODO-SUBLIST.md`).
3. Diese `TODO.md` bleibt dann der **stabile Einstieg und Index** im Root:

```markdown
> **Unterlisten (aktiv):** `TODO-DEV.md` | `TODO-DOCS.md` | `TODO-OPS.md` (als relative Markdown-Links auf existierende Unterlisten)

| Unterliste | Zuständigkeit / Inhalt | Offen | Blockiert |
|---|---|---:|---:|
| `TODO-DEV.md` | Entwicklung, Tests, Bugfixes | 0 | 0 |
| `TODO-DOCS.md` | Dokumentation, Releases | 0 | 0 |
```

4. **Gemeinsames Archiv & Rückführung:** Auch Unterlisten archivieren per `_tools/todo-archive --todo TODO-<BEREICH>.md --done DONE.md --apply` in das eine zentrale `DONE.md`. Sinkt die Summe über alle Unterlisten dauerhaft unter ~40 offene Tasks, Unterlisten wieder hier zusammenführen.

---

## Format-Regeln

- **Pro Task eine Zeile**, klare Exit-Bedingung.
- **Verweise auf Kontext:** `(siehe DECISIONS.md §3)` oder `(Issue #42)`.
- **Datum bei lang offenen Tasks:** `[ ] 2026-02-15 Task X` zeigt Alter.
- **Keine Kategorien-Explosion:** Active / Backlog / Blocked reichen.

## Archivierung

Am Session-Ende oder wöchentlich:

```bash
_tools/todo-archive --apply
```

Das verschiebt alle `[x]`-Einträge aus dieser Datei mit heutigem Datum nach `DONE.md` und entfernt sie hier. **Nie manuell löschen** — dadurch verlierst du die History. Erledigte Tasks und Laufprotokolle gehören niemals in `CLAUDE.md` oder `AGENTS.md`.

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
