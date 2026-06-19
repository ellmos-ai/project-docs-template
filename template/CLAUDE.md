---
name: "[project-name]"
type: project-docs
profile: "[MINIMAL|STANDARD|FULL]"
version: 0.1.0
created: "[YYYY-MM-DD]"
updated: "[YYYY-MM-DD]"
reason_last_change: "[Was wurde warum geändert]"
last_verified: "[YYYY-MM-DD]"
author: "[author]"
anthropic_compatible: true
description: |
  Project-specific instructions for AI coding agents in [project-name].
  Primary audience: Claude Code. Other agents redirect here via AGENTS.md.
---

# CLAUDE.md — Instructions für AI Coding Agents

> **Für LLM-Agenten (Claude Code, Codex, Cursor, Cline, Aider, Windsurf, Copilot).**
> Diese Datei wird von Claude Code **automatisch** in den Kontext geladen.
> Andere Agents lesen zuerst `AGENTS.md` → Redirect hierher.
>
> **YAML-Header oben** ist maschinenlesbar und wird von `_tools/doc-lint` validiert.
> Bei Änderungen an der Doku: `updated` und `last_verified` nachziehen.

---

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Dateigröße:** Wenn diese Datei zu lang wird, verwende das Cut-and-Clue-Verfahren → `CUT-AND-CLUE.md` (Pointer-Verfahren mit Vorläufer/Nachfolger-Dateien).

## Projekt

**[Projektname]** — [Einzeiler-Beschreibung was das Projekt ist und für wen]

**Pfad:** `[absoluter Pfad zum Projekt]`
**Repository:** `[github.com/owner/repo oder "privat, kein Remote"]`
**Sprache/Stack:** `[Python 3.11, TypeScript, Bash, ...]`

## Rolle & Stil

Arbeite als [Senior Dev / Researcher / ...] mit Fokus auf [correctness / speed / security / ...].

**Kommunikation:**
- Sprache: Deutsch (Code/Identifier bleiben englisch)
- Stil: knapp, direkt, ohne Preamble
- Bei Unsicherheit: fragen statt raten

## Einstieg (Quick Commands)

```bash
# [Haupt-Einstiegspunkt]
[COMMAND HIER]

# [Zweiter typischer Run]
[COMMAND HIER]

# Tests
[TEST-COMMAND HIER]
```

**Für vollständige Session-Bootstrap-Sequenz siehe [`START.md`](./START.md).**
**Für aktuellen Stand siehe [`STATE.md`](./STATE.md).**

## Hard Rules (non-negotiable)

- **NIEMALS** Credentials committen (`.env`, `*.key`, `credentials.json`, tokens)
- **NIEMALS** `git push --force` auf `main`/`master` (wenn unvermeidbar, nur über ein projektspezifisch geprüftes Admin-Playbook)
- **NIEMALS** destructive Operationen ohne explizite User-Bestätigung (`rm -rf`, `DROP TABLE`, `git reset --hard`)
- **IMMER** bei Python auf Windows: `PYTHONIOENCODING=utf-8` vor dem Call
- **IMMER** vor Push: `git status` prüfen

## Soft Guidelines

- Bevorzuge `Edit` vor `Write` für existierende Dateien
- Keine prophylaktischen Features — nur was gerade gebraucht wird
- Keine Kommentare für selbsterklärenden Code
- Bei gleichartigen Dateien: vor Anlegen prüfen ob ein bestehendes erweitert werden kann

## Selbstreflexion vor komplexen Aktionen

Bevor du destructive Git-Operationen ausführst oder Architektur-relevante
Änderungen machst, frage dich:
1. Habe ich den aktuellen State verstanden (`git status`, `git log`)?
2. Gibt es eine weniger destruktive Alternative?
3. Ist `--force-with-lease` statt `--force` möglich?
4. Wird diese Änderung in `DECISIONS.md` dokumentierbar?

## Projekt-Struktur

Details siehe [`ARCHITECTURE.md`](./ARCHITECTURE.md). Kurz:

```
[projekt-root]/
├── [haupt-code-ordner]/
├── [konfig-ordner]/
├── workflows/      # Multi-Step-Playbooks
├── _tools/         # Admin-Utilities
└── .github/        # GitHub-native Config
```

## Wichtige Dateien

| Datei | Zweck |
|---|---|
| [`START.md`](./START.md) | Session-Bootstrap — lies als Erstes beim Session-Start |
| [`STATE.md`](./STATE.md) | Wo-stehen-wir-Snapshot — aktueller Stand |
| [`TODO.md`](./TODO.md) | Aktive Tasks |
| [`DONE.md`](./DONE.md) | Erledigte Tasks (archiviert via `_tools/todo-archive`) |
| [`ARCHITECTURE.md`](./ARCHITECTURE.md) | Struktur & Modul-Graph (auto-generiert) |
| [`DECISIONS.md`](./DECISIONS.md) | Warum-Entscheidungen (ADRs) |
| [`PATTERNS.md`](./PATTERNS.md) | Do/Don't mit Code-Beispielen |
| [`WORKFLOWS.md`](./WORKFLOWS.md) | Router zu Multi-Step-Playbooks |
| [`TOOLS.md`](./TOOLS.md) | Router zu Admin-Utilities |
| [`GLOSSARY.md`](./GLOSSARY.md) | Projekt-Jargon |
| [`CHANGELOG.md`](./CHANGELOG.md) | Chronik |

## Domain-Kontext

[Hier projektspezifische Background-Infos: Was macht das Projekt in welchem
Umfeld, welche externen Abhängigkeiten gibt es, was ist die Zielgruppe, etc.
Alles was der LLM-Agent braucht um Entscheidungen im Kontext zu treffen.]

## Umgebungs-Hinweise

[z.B. OS-Spezifisches, spezielle Shell-Setups, Encoding-Gotchas, Rate-Limits
externer APIs, Lokale vs. Remote-Infrastruktur.]

---

## Multi-Agent-Setup (optional, nur falls relevant)

> **Wann ausfüllen:** Nur wenn dieses Projekt **mehrere AI-Agents** orchestriert
> (Boss-Agent + Experten, oder parallele Agents mit verschiedenen Rollen).
> Bei Solo-Agent-Projekten diesen ganzen Abschnitt löschen.

```yaml
agents:
  primary: claude-code              # Haupt-Tool / Orchestrator
  orchestrator: [agent-name]        # Optional: Boss-Agent
  experts:
    - name: [expert-1]
      role: [Was dieser Expert macht]
      trigger: [Wann wird er gerufen]
    - name: [expert-2]
      role: [...]
      trigger: [...]
  delegation_rules:
    - [Regel 1: wenn X, dann expert-1]
    - [Regel 2: wenn Y, dann expert-2]
  communication:
    inbox: [Pfad oder Channel]
    outbox: [Pfad oder Channel]
```

**Beispiel (fiktives Research-Projekt):**

```yaml
agents:
  primary: claude-code
  orchestrator: research-coordinator
  experts:
    - name: literature-scout
      role: Holt Paper aus arxiv/PubMed
      trigger: Bei neuem Forschungsthema
    - name: fact-checker
      role: Verifiziert Zitate und Referenzen
      trigger: Vor jedem Publication-Commit
    - name: stats-reviewer
      role: Prüft statistische Analysen
      trigger: Bei Methoden-Sektionen
  delegation_rules:
    - "neue Quelle" → literature-scout
    - "prüfe Referenzen" → fact-checker
    - "p-Wert diskussion" → stats-reviewer
  communication:
    inbox: _data/agent_inbox/
    outbox: _data/agent_outbox/
```

**Verweis:** Siehe [`AGENTS.md`](./AGENTS.md) für den tool-agnostischen
Einstiegspunkt, der auf diese Datei verweist.

---

## Meta

- **YAML-Frontmatter oben** wird validiert via `_tools/doc-lint`
- **Staleness-Check**: Wenn `last_verified` älter als 30 Tage → `doc-lint` warnt
- **Bei Version-Bumps** von Projekt-Code: `version` im Frontmatter nachziehen und in `CHANGELOG.md` eintragen

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE Ü Ö Ä -->
