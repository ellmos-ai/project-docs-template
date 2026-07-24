# HEADER-RULES — Standard-Kopfzeilen für Steuer-Dateien

**Version:** 1.0
**Aktualisiert:** 2026-06-02
**Grund:** Erprobt in einer produktiven Projekt-Pipeline und in den Template-Standard übernommen
**Zweck:** Definiert den Standard-Header für alle Projekt-Steuerdateien — sorgt für Konsistenz, Maschinenlesbarkeit und autonome Selbstkorrektur.

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom.

> **Dateigröße:** Wenn diese Datei zu lang wird, verwende das Cut-and-Clue-Verfahren → `CUT-AND-CLUE.md`.

---

## Pflicht-Header (jede Steuerdatei)

```markdown
# DATEINAME — Zweck in einem Satz

**Version:** X.Y
**Aktualisiert:** YYYY-MM-DD
**Grund:** [Kurze Beschreibung der letzten Änderung]
**Zweck:** [Ein Satz: Was ist diese Datei? Welche Frage beantwortet sie?]

> Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet
> wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder
> erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du
> gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht,
> setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> Wenn diese Datei zu lang wird: Verwende das Cut-and-Clue-Verfahren → CUT-AND-CLUE.md

---
[Inhalt]
---
<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE Ü Ö Ä -->
```

## Pflicht-Footer

```markdown
---
<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE Ü Ö Ä -->
```

## Versionierung

- Patch (X.Y → X.Y+1): Kleine Korrekturen, Verweise, Tippfehler
- Minor (X.Y → X+1.0): Neue Abschnitte, strukturelle Änderungen
- Für übergroße Dateien: Cut-and-Clue statt Major-Version

## Dateiendungs-Konvention

| Typ | Endung | Beispiele |
|---|---|---|
| Policies, Regelwerke, Dokumentation | `.md` | CLAUDE.md, DECISIONS.md |
| Projekt-Steuerdateien und Aufgabenlisten im Root | `.md` | START.md, STATE.md, TODO.md, DONE.md |
| Einfache Export-/Maschinen-Logs | `.txt` | CHECKS-LOG.txt, export.txt |

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE Ü Ö Ä -->
