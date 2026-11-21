# <REGISTER-NAME> — <Zuständigkeit in einem Satz>

**Version:** 1.0
**Aktualisiert:** <YYYY-MM-DD>
**Grund:** Erstausgabe aus `REG-TEMPLATE.md` angelegt
**Zweck:** <Welche Information wird hier kanonisch geführt? Welcher Parallel-Wildwuchs wird damit verhindert?>

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt (z. B. durch Sync-Konflikte), zuerst vollständig diffen und verlustfrei in die kanonische Datei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang; Archive bleiben getrennt.

> **Dateigröße:** Wenn diese Datei zu lang wird (> ~200 Zeilen): Verwende das Cut-and-Clue-Verfahren → [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md).

---

> **Kopiervorlage (nicht direkt im Template-Repo ausfüllen):** Kopiere diese Datei als `<THEMA>-REG.md` (im Root oder unter `_reg/`) ins Zielprojekt, ersetze die `<...>`-Platzhalter und registriere das neue Register in [`MASTER-REGISTRY.md`](./MASTER-REGISTRY.md).

## Registry-Regel & Abgrenzung

- **Kanonische Quelle:** Dieses Register ist die einzige aktive Wahrheitsquelle für `<Gegenstand>`.
- **Abgrenzung:** Keine Duplikation in `CLAUDE.md`, `START.md` oder `STATE.md` (dort nur Kurzverweis).
- **Zählstände:** Falls Summen oder Zähler angegeben werden, immer Messdatum und Quelle nennen (z. B. `12 Einträge, Stand <YYYY-MM-DD>`).
- **Laufzeit-Logs:** Ausführliche chronologische Rohprotokolle gehören in ein separates Log (`_logs/<name>.txt` oder `CHECKS-LOG.txt`), nicht in diese Tabelle.

---

## Aktive Einträge

> Beispiel-Struktur (Spalten an den konkreten Zweck anpassen, z. B. für Komponenten, Policies, Checks oder Releases):

| ID / Name | Status | Verantwortlich / Scope | Nachweis / Zielpfad | Aktualisiert |
|---|---|---|---|---|
| `<Eintrag-1>` | `aktiv` | `<Bereich>` | `<relativer-pfad>` | `<YYYY-MM-DD>` |
| `<Eintrag-2>` | `geplant` | `<Bereich>` | `<relativer-pfad>` | `<YYYY-MM-DD>` |

---

## Historie / Archivierte Segmente

- **Vorläuferarchiv:** `<keines | _archive/<REGISTER-NAME>_ARCHIV_v1_<YYYY-MM-DD>.md>`
- Abgeschlossene oder veraltete Einträge nicht stillschweigend löschen, wenn Nachvollziehbarkeit nötig ist — stattdessen Status auf `archiviert` / `ersetzt` setzen oder per Cut-and-Clue (Variante A) ins Archiv auslagern.

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
