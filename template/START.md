---
name: "[project-name]-start"
type: session-bootstrap
version: 0.1.0
updated: "[YYYY-MM-DD]"
last_verified: "[YYYY-MM-DD]"
description: |
  Imperative bootstrap sequence for new sessions in [project-name].
---

# START.md — Session-Bootstrap für [Projektname]

> **Wann lesen:** Zu Beginn jeder Arbeitssession in diesem Projekt.
> **Semantik:** Imperativ, aktiv. Befehle, keine Beschreibungen.

---

## Bootstrap-Sequenz

Führe diese Schritte **in dieser Reihenfolge** aus, wenn du eine neue Session
in diesem Projekt beginnst:

1. **CLAUDE.md** ist auto-loaded (Claude Code) — andere Tools: öffne sie jetzt
2. **`git status`** prüfen — irgendwelche hängenden Änderungen aus der vorherigen Session?
3. **`STATE.md`** lesen — wo standen wir beim letzten Mal?
4. **`TODO.md`** lesen — was ist aktiver Fokus?
5. **`CHANGELOG.md`** letzter Eintrag — was war die letzte bedeutsame Aktion?
6. **Wenn unsicher:** User fragen „Woran wollen wir weitermachen?"

## Quick Commands

```bash
# [Haupt-Run]
[COMMAND]

# [Test]
[COMMAND]

# [Deploy/Publish]
[COMMAND]
```

## Session-Ende-Ritual

Am Ende jeder bedeutsamen Session:

1. Commit alle relevanten Änderungen
2. **`STATE.md` aktualisieren** — was wurde gemacht, was ist next, Blocker?
3. **`TODO.md` pflegen** — neue Tasks [ ], erledigte markieren [x]
4. Optional: `_tools/todo-archive` ausführen (verschiebt [x] nach DONE.md)
5. **`CHANGELOG.md` Eintrag** wenn Release-relevant

## Bei Problemen

| Problem | Wohin |
|---|---|
| Ich verstehe die Struktur nicht | [`ARCHITECTURE.md`](./ARCHITECTURE.md) |
| Warum wurde X so gemacht? | [`DECISIONS.md`](./DECISIONS.md) |
| Wie führe ich Prozess Y aus? | [`WORKFLOWS.md`](./WORKFLOWS.md) |
| Welches Tool macht Z? | [`TOOLS.md`](./TOOLS.md) |
| Was bedeutet Begriff Q? | [`GLOSSARY.md`](./GLOSSARY.md) |
| Ich mache immer wieder denselben Fehler | [`PATTERNS.md`](./PATTERNS.md) |
