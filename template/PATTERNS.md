# PATTERNS.md — Do/Don't mit Code-Beispielen

**Version:** 0.1.0
**Aktualisiert:** [YYYY-MM-DD]
**Grund:** [Was wurde warum geändert]
**Zweck:** Hält wiederkehrende Do/Don't-Idiome, Fehlerbilder und Qualitäts-Checks für [Projektname] fest.

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt (z. B. durch Sync-Konflikte), zuerst vollständig diffen und verlustfrei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang.

> **Dateigröße:** Wenn diese Datei zu lang wird: Verwende das Cut-and-Clue-Verfahren → [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md).

> **Format:** Gepaarte ✅ RIGHT + ❌ WRONG Beispiele mit konkretem Code.
> **Abgrenzung zu `DECISIONS.md`:** Patterns sind **wiederholbar** (Code-/Prozess-Level),
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

## Template-Beispiel: Mess- & Falsifizierungs-Disziplin (daten-/forschungsnahe Repos)

**Kontext:** Bei eigenen Messungen, Benchmarks oder Modellen genügen positive Einzelwerte nicht.

### ❌ WRONG
- Einen Testbereich so eng wählen, dass der Test die Vorhersage gar nicht widerlegen kann.
- Strukturmerkmale ohne Vergleich gegen ein Zufalls-/Nullmodell als Signal deuten.
- Trefferquoten („6/10 richtig“) ohne Basisrate der Mehrheitsklasse berichten.

### ✅ RIGHT
1. **Falsifizierbarkeit:** Testbereich so wählen, dass er die erwartete Grenze **beidseitig** überdeckt.
2. **Nullmodell:** Jede Struktur- oder Muster-Aussage gegen eine Zufallskontrolle prüfen.
3. **Bezugsgröße:** Jede Kennzahl mit Basisrate, Nullmodellwert oder Normierung angeben.

---

## Reminders per Kontext

### Bei Git-Operationen & Multi-Writer-Betrieb
- ⚠️ IMMER vor destructive: `git status` + `git log --oneline -5` + aktive `LOCK*.txt` prüfen
- ⚠️ Bei `git rm --cached`: **kein Pathspec** im folgenden Commit
- ⚠️ Bei `--force-with-lease`: prüft Remote-State, nicht blind
- ⚠️ Sync-Konfliktkopien niemals blind löschen — zuerst diffen und verlustfrei mergen

### Bei Python auf Windows
- ⚠️ `PYTHONIOENCODING=utf-8` bzw. `python -X utf8` vor jedem Call (cp1252-Default vermeiden)
- ⚠️ Pfade in subprocess: plattformnativ (`pathlib.Path`), keine hardcodierten Benutzerpfade
- ⚠️ `&&` funktioniert in Git Bash, aber nicht in cmd/PowerShell 5.1 (in `pwsh` 7 ja)

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
> **Staleness:** Was früher richtig war, kann später überholt sein — veraltete Stellen nicht still löschen, sondern mit `NACHTRAG` oder datiertem Vermerk aktualisieren.

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
