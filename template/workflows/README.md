# workflows/ — Multi-Step-Playbooks

> **Lokale Konventionen** für Workflow-Dateien in diesem Ordner.
> **Router im Root:** [`../WORKFLOWS.md`](../WORKFLOWS.md) — enthält die
> „Welcher Workflow wofür"-Übersicht.

---

## Was gehört hier rein

Playbooks für **wiederholbare Multi-Step-Prozesse** mit Side-Effects. Jeder
Workflow ist eine eigene Datei mit sprechendem Namen (NICHT `WORKFLOW-A.md`).

**Beispiele für gute Workflows:**
- `release.md` — Versions-Bump, Build, Test, Tag, Push, Publish, Verify
- `hotfix.md` — Branch, Fix, Test, Merge, Cherry-Pick, Deploy
- `security-audit.md` — Dependabot-Scan, Update, Test, Commit, Push
- `add-module.md` — Gerüst, Tests, Wire-Up, Doku, Commit

**Beispiele für schlechte Workflows (gehören anderswo):**
- ❌ „Wie installiere ich das Projekt" → das ist `README.md`
- ❌ „Warum haben wir X so entschieden" → das ist `DECISIONS.md`
- ❌ „Ein 2-Schritt-Prozess" → zu klein, gehört als Bash-Alias oder in PATTERNS.md

## Datei-Struktur eines Workflows

```markdown
# Workflow: [Kurzer Imperativ-Titel]

> **Last verified:** [YYYY-MM-DD]
> **Frequency:** [täglich / wöchentlich / pro Release / ad-hoc]
> **Duration:** [~5 min / ~30 min]

## Purpose

[1-2 Sätze: Wann brauche ich diesen Workflow? Was ist das Ziel?]

## Preconditions

- [Was muss vor dem Start wahr sein]
- [Welche Tools/Permissions braucht der Workflow]

## Steps

1. **[Schritt 1]** — [Beschreibung]
   ```bash
   [konkreter Befehl]
   ```

2. **[Schritt 2]** — [Beschreibung]
   ```bash
   [konkreter Befehl]
   ```

...

## Exit-Criteria (vor Abschluss prüfen)

- [ ] [Bedingung 1 — was muss wahr sein damit wir „fertig" sind]
- [ ] [Bedingung 2]
- [ ] [Optional: STATE.md aktualisiert, CHANGELOG.md Eintrag]

## Fallstricke

- ⚠️ [Häufiger Fehler 1 mit Lösungsansatz]
- ⚠️ [Häufiger Fehler 2]

## Verwandte

- `Workflow X` (`workflows/x.md`, sobald angelegt) — wenn Y der Fall ist
- [PATTERNS.md#sektion](../PATTERNS.md) — für Do/Don't

## Historie

- **[YYYY-MM-DD]** — Erstellt
- **[YYYY-MM-DD]** — Schritt 3 erweitert um [Fallstrick X]
```

## Naming

- **Sprechend**, nicht Buchstaben-Suffix: `release.md`, `hotfix.md` — nicht `WORKFLOW-A.md`
- **Imperativ** wo möglich: `add-module.md` statt `module-adding.md`
- **Kurz**: max. 3 Wörter, mit Bindestrich: `security-audit.md`, `force-push.md`
- **Kleinbuchstaben**: im Unterordner ist das Konvention

## Wann einen Workflow aktualisieren

- Beim **ersten Mal** dass der alte Workflow einen Fehler produziert → Root-Cause in „Fallstricke" dokumentieren
- Bei **Tool-Updates** die den Ablauf ändern → Version prüfen, Last verified bumpen
- Bei **Abwicklungs-Änderung** (z.B. neuer Registry, neue Auth) → Steps überarbeiten

**Staleness-Check:** Jeder Workflow hat `Last verified`-Datum. Wenn älter als
6 Monate und du stehst grad vor dem Lauf → erst verifizieren, dann nutzen.
