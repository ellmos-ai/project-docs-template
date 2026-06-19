# PATTERNS.md — Do/Don't mit Code-Beispielen

> **Format:** Gepaarte ✅ RIGHT + ❌ WRONG Beispiele mit konkretem Code.
> **Zweck:** Wiederkehrende Fehler vermeiden, wiederverwendbare Idiome festhalten.
> **Abgrenzung zu DECISIONS.md:** Patterns sind **wiederholbar** (Code-Level),
> Decisions sind **einmalig** (System-Level).

---

## Template-Beispiel: Config-Merge mit Defaults

**Kontext:** Beim Laden einer JSON-Config soll das Merge mit Default-Werten
so geschehen, dass fehlende Keys die Defaults behalten.

### ❌ WRONG
```python
self.settings = cfg.get("settings", {})
```
**Problem:** Wenn `cfg["settings"]` nur 2 von 5 Keys hat, gehen die anderen 3
Default-Werte verloren.

### ✅ RIGHT
```python
self.settings = {**DEFAULT_SETTINGS, **cfg.get("settings", {})}
```
**Warum:** Spread-Merge — Defaults bleiben, Config überschreibt nur wo gesetzt.
**Siehe:** `core/config.py:42`
**Historie:** [YYYY-MM-DD] bei [Projekt-Kontext] gelernt

---

## Template-Beispiel: Git Force-Push

### ❌ WRONG
```bash
git push --force origin main
```
**Problem:** Überschreibt fremde Commits blind. Wenn zwischenzeitlich jemand
anderer (oder ein Bot wie Dependabot) gepusht hat, geht deren Arbeit verloren.

### ✅ RIGHT
```bash
git push --force-with-lease origin main
```
**Warum:** `--force-with-lease` schlägt fehl falls die Remote-Ref sich seit
dem letzten Fetch geändert hat — schützt vor Blind-Überschreibungen.
**Historie:** [YYYY-MM-DD] — Lesson learned nach [Incident]

---

## Template-Beispiel: `git commit <file>` Falle

### ❌ WRONG
```bash
git rm --cached sensitive_file.txt
git commit sensitive_file.txt -m "untrack file"
```
**Problem:** `git commit <pathspec>` macht einen **partial commit** der die
Working-Tree-Version der Datei nimmt — **überschreibt** das `git rm --cached`!
Das File wird committed statt gelöscht.

### ✅ RIGHT
```bash
git rm --cached sensitive_file.txt
git commit -m "untrack file"   # kein Pathspec!
```
**Warum:** Ohne Pathspec committet git was im Index steht (= die Deletion).
**Historie:** [YYYY-MM-DD] — Fehler live erlebt, Commit musste rebased werden

---

## Reminders per Kontext

### Bei Git-Operationen
- ⚠️ IMMER vor destructive: `git status` + `git log --oneline -5`
- ⚠️ Bei `git rm --cached`: **kein Pathspec** im folgenden Commit
- ⚠️ Bei `--force-with-lease`: prüft Remote-State, nicht blind

### Bei Python auf Windows
- ⚠️ `PYTHONIOENCODING=utf-8` vor jedem Call (cp1252-Default ist ein Gift)
- ⚠️ Pfade in subprocess: Windows-nativ (`C:\...`), nicht Bash (`/c/...`)
- ⚠️ `&&` funktioniert in Git Bash, aber nicht in cmd/PowerShell

### Bei npm Publish
- ⚠️ Version vorher bumpen, nicht erst im `prepublishOnly`
- ⚠️ `package-lock.json` mit committen
- ⚠️ Bei `overrides` für transitive Deps: `npm install --package-lock-only` triggert lock sync

---

## Format-Hinweis

> **Jeder Pattern-Eintrag sollte enthalten:**
> - Kontext (was war die Situation)
> - ❌ WRONG mit konkretem Code
> - ✅ RIGHT mit konkretem Code
> - **Warum** (die Erkenntnis)
> - **Siehe** (Verweis auf echten Code wo möglich)
> - **Historie** (Datum + Kontext wann gelernt)
>
> **Patterns ohne WRONG-Paar sind schwächer** — ohne den Kontrast lernt
> man nicht warum das Pattern existiert.
>
> **Staleness:** Was 2024 wrong war, kann 2026 right sein. Bei Zweifel
> Datum prüfen und neu bewerten.
