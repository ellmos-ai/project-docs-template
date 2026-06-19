# TODO.md — Aktive Tasks

> **Regel:** Nur **offene** Tasks (`[ ]`). Erledigtes (`[x]`) wird via
> `_tools/todo-archive` nach [`DONE.md`](./DONE.md) verschoben.
> **Pflege:** Während der Arbeit laufend, am Session-Ende aufräumen.

---

## Active

- [ ] [Nächster konkreter Task mit klarer Exit-Bedingung]
- [ ] [Weiterer Task]

## Backlog

- [ ] [Späterer Task, noch nicht aktueller Fokus]

## Blocked

- [ ] [Blockierter Task] — wartet auf [Entscheidung/Dependency/Zugang]

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

Das verschiebt alle `[x]`-Einträge aus dieser Datei mit heutigem Datum nach
`DONE.md` und entfernt sie hier. **Nie manuell löschen** — dadurch verlierst
du die History.
