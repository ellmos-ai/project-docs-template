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

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt (z. B. durch Sync-Konflikte), zuerst vollständig diffen und verlustfrei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang.

<!-- profiles:STANDARD,FULL -->
> **Dateigröße:** Wenn diese Datei zu lang wird: Verwende das Cut-and-Clue-Verfahren → [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md).
<!-- /profiles -->

---

## Bootstrap-Sequenz

Führe diese Schritte **in dieser Reihenfolge** aus, wenn du eine neue Session
in diesem Projekt beginnst:

1. **`CLAUDE.md`** ist auto-loaded (Claude Code) — andere Tools: öffne sie jetzt (oder über [`AGENTS.md`](./AGENTS.md))
1. **Lock-Status & `git status`** prüfen — liegen aktive Sperren (`LOCK*.txt`) im Arbeitsbereich vor? Falls ja: Bereich nicht verändern (Fail-Closed). Zusätzlich hängende Git-Änderungen aus der vorherigen Session prüfen.
1. **[`STATE.md`](./STATE.md)** lesen — wo standen wir beim letzten Mal?
1. **[`TODO.md`](./TODO.md)** lesen — was ist aktiver Fokus (inkl. verlinkter `TODO-<BEREICH>.md`-Unterlisten, falls vorhanden)?
<!-- profiles:FULL -->
1. **[`MASTER-REGISTRY.md`](./MASTER-REGISTRY.md)** bei Bedarf prüfen — welches Register oder welche Statusdatei ist zuständig?
<!-- /profiles -->
<!-- profiles:STANDARD,FULL -->
1. **[`CHANGELOG.md`](./CHANGELOG.md)** letzter Eintrag — was war die letzte bedeutsame Aktion?
<!-- /profiles -->
1. **Wenn unsicher:** User fragen „Woran wollen wir weitermachen?“

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

1. Commit alle relevanten Änderungen (nur bei freiem Lock)
1. **[`STATE.md`](./STATE.md) aktualisieren** — was wurde gemacht, was ist next, Blocker?
1. **[`TODO.md`](./TODO.md) pflegen** — neue Tasks `[ ]`, erledigte markieren `[x]` (ggf. in Unterlisten)
1. Optional: `_tools/todo-archive --apply` ausführen (verschiebt `[x]` nach [`DONE.md`](./DONE.md))
<!-- profiles:STANDARD,FULL -->
1. **[`CHANGELOG.md`](./CHANGELOG.md) Eintrag** wenn Release-relevant
<!-- /profiles -->
1. **Protokolltrennung wahren** — reine Laufprotokolle gehören in `DONE.md`, `CHANGELOG.md` oder dedizierte Logs, niemals in `CLAUDE.md` oder `AGENTS.md`. Eigene temporäre Locks wieder entfernen.

## Bei Problemen

| Problem | Wohin |
|---|---|
| Was ist als Nächstes dran? | [`TODO.md`](./TODO.md) und [`STATE.md`](./STATE.md) |
<!-- profiles:FULL -->
| Welches Register ist wofür zuständig? | [`MASTER-REGISTRY.md`](./MASTER-REGISTRY.md) |
| Ich verstehe die Struktur nicht | [`ARCHITECTURE.md`](./ARCHITECTURE.md) |
<!-- /profiles -->
<!-- profiles:STANDARD,FULL -->
| Warum wurde X so gemacht? | [`DECISIONS.md`](./DECISIONS.md) |
| Wie sind Header und Footer aufgebaut? | [`HEADER-RULES.md`](./HEADER-RULES.md) |
| Eine Steuerdatei wird zu lang | [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md) |
<!-- /profiles -->
<!-- profiles:FULL -->
| Eine Datei oder ein Ordner ist umgezogen | [`MOVED-STUB.md`](./MOVED-STUB.md) |
| Wie führe ich Prozess Y aus? | [`WORKFLOWS.md`](./WORKFLOWS.md) |
| Welches Tool macht Z? | [`TOOLS.md`](./TOOLS.md) |
| Was bedeutet Begriff Q? | [`GLOSSARY.md`](./GLOSSARY.md) |
<!-- /profiles -->
<!-- profiles:STANDARD,FULL -->
| Ich mache immer wieder denselben Fehler | [`PATTERNS.md`](./PATTERNS.md) |
<!-- /profiles -->

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
