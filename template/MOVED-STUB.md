# MOVED-STUB.md — Standard für Umzugs-Pointer bei Datei-/Ordner-Umzügen

**Version:** 0.1.0
**Aktualisiert:** [YYYY-MM-DD]
**Grund:** [Was wurde warum geändert]
**Zweck:** Kompakter Pointer für den Fall „Ordner oder Datei X liegt jetzt woanders“ — kein Log, kein Wrapper, kein Archiv.

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt, zuerst vollständig diffen und verlustfrei in die kanonische Datei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang; Archive bleiben getrennt.

> **Dateigröße:** Wenn diese Datei zu lang wird: Verwende das Cut-and-Clue-Verfahren → [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md).

> **Abgrenzung zu [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md):** Cut-and-Clue teilt eine zu lang gewordene Datei in zwei Teile (Inhalt bleibt an **beiden** Orten bestehen, beide referenzieren sich). Ein `*.MOVED.md`-Stub markiert einen **kompletten Umzug** (Inhalt existiert nur noch am neuen Ort).

---

## Wann diesen Stub anlegen

Ein **ganzer Ordner** oder eine **einzelne Datei** ist an einen anderen Ort umgezogen (Konsolidierung, Umbenennung, Reorganisation) und der alte Ort soll nicht kommentarlos verschwinden.

**Nicht verwenden für:** Dateiteilung bei Überlänge (→ [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md)).

## Name und Ablageort

- **Ordner-Umzug:** `<alter-Ordnername>.MOVED.md` liegt im **alten Elternordner**, dort wo der Ordner vorher lag.
- **Datei-Umzug:** `<alter-Dateiname-ohne-Endung>.MOVED.md` liegt **neben dem alten Dateipfad**.

## Pflichtfelder (`key: value`, in dieser Reihenfolge)

```text
moved_to: <relativer Pfad oder <projekt-root>/... zum neuen Ziel>
moved_on: YYYY-MM-DD
reason: <1 Zeile: warum umgezogen wurde>
moved_by: <agent|maintainer>
ref: <optional: Issue-, PR- oder Ticket-Referenz>
remove_when: 90 Tage UND 0 lebende Referenzen
```

Danach **1–3 Zeilen Klartext** für Menschen (was umgezogen ist, wohin, warum). **Kein weiterer Inhalt** — kein Log, keine Tabelle, keine Duplizierung von Historie.

### Portabilität

- Verwende bevorzugt **relative Pfade** oder einen generischen Platzhalter (`<projekt-root>/...`) statt lokaler absoluter Benutzerpfade.

## Beispiel

```markdown
moved_to: ../docs/architecture/DECISIONS.md
moved_on: 2026-06-01
reason: Konsolidierung der Architekturdokumentation unter docs/architecture/
moved_by: maintainer
ref: PR #42
remove_when: 90 Tage UND 0 lebende Referenzen

Die Architekturentscheidungen liegen jetzt gebündelt unter `docs/architecture/DECISIONS.md`.
```

## Rückbau

Der Stub wird beim Rückbau **gelöscht, nicht archiviert**, sobald beide Bedingungen von `remove_when` erfüllt sind:

1. Mindestalter erreicht (Default: 90 Tage nach `moved_on`), **und**
2. 0 lebende Referenzen im Repository (vor dem Löschen per Suche verifizieren).

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
