# DECISIONS.md — Architekturentscheidungen

**Version:** 0.1.0
**Aktualisiert:** [YYYY-MM-DD]
**Grund:** [Was wurde warum geändert]
**Zweck:** Architecture Decision Records (ADRs) von [Projektname] — chronologisch (neueste oben), append-only und nachvollziehbar begründet.

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt (z. B. durch Sync-Konflikte), zuerst vollständig diffen und verlustfrei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang.

> **Dateigröße:** Wenn diese Datei zu lang wird: Verwende das Cut-and-Clue-Verfahren → [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md).

> **ADR-Pattern:** Append-only — alte Entscheidungen werden nicht stillschweigend gelöscht, sondern durch neue ersetzt oder an Ort und Stelle per `NACHTRAG` markiert.

---

## [YYYY-MM-DD]: [Kurze Entscheidungs-Überschrift]

**Status:** `PROPOSED | ACCEPTED | SUPERSEDED | REJECTED`
**Beteiligte / Akteur:** `[Mensch | Agent]`

### Kontext

[Was war die Situation? Welches Problem mussten wir lösen? Was waren die
Rahmenbedingungen?]

### Optionen

| Option | Ansatz | Bewertung |
|---|---|---|
| **A** | [Alternative 1] | [Warum verworfen] |
| **B** | [Alternative 2] | **Gewählt** — [Warum] |
| **C** | [Alternative 3] | [Warum verworfen] |

### Entscheidung

[Welche Option wurde gewählt? Konkret beschreiben was umgesetzt wurde.]

### Kern-Prinzipien

1. [Prinzip 1, mit Begründung]
2. [Prinzip 2, mit Begründung]
3. [Prinzip 3, mit Begründung]

### Technische Details

- [Konkrete Implementierung]
- [Verwendete Libraries/Tools]
- [Schnittstellen zu anderen Modulen]

### Limitationen (bewusst akzeptiert)

- [Was diese Entscheidung NICHT löst]
- [Welche Trade-offs wir eingehen]
- [Was bei Änderung der Rahmenbedingungen neu bewertet werden müsste]

### Revisit-Trigger

Diese Entscheidung ist gültig solange:
- [Bedingung 1]
- [Bedingung 2]

Bei [Ereignis X] sollte die Entscheidung neu bewertet werden.

### Folge-Aktionen

- [x] [Erledigte Schritte]
- [ ] [Offene Schritte]

---

## [YYYY-MM-DD]: [Nächste Entscheidung]

[Gleiche Struktur wiederholen]

---

## Nachträge statt stiller Korrektur (bei widerlegten/überholten Aussagen)

Erweist sich eine dokumentierte Annahme, Zahl oder Entscheidung im Nachhinein als falsch, irreführend oder überholt, wird der Originaltext **nicht stillschweigend gelöscht** (sonst geht die Lerngeschichte verloren), sondern unmittelbar darunter mit einem strukturierten Nachtrag versehen:

```markdown
> **NACHTRAG [<Kürzel> YYYY-MM-DD] — <WIDERLEGT | IRREFÜHREND | ÜBERHOLT | PRÄZISIERT>**
> <1–3 Sätze: Was stimmt nicht und warum?>
> **Beleg:** <Pfad / Commit / Messung>
```

Sobald ein Dokument mindestens einen Nachtrag enthält, steht direkt unter der Titelzeile ein kurzer Hinweis (`NACHTRAGS-HINWEIS: N Nachträge, schwerste Stufe ...`).

## Format-Hinweis

> **Wann etwas hierher gehört:** Wenn du eine Entscheidung triffst, die
> **schwer rückgängig zu machen** ist, **systemisch** wirkt, oder deren
> **Warum** in Zukunft jemand (oder du selbst) verstehen muss.
>
> **Wann NICHT:** Kleine Refactorings, Style-Entscheidungen, reversible
> Optimierungen. Dafür ist `PATTERNS.md` da.
>
> **Commits zeigen nur „was"**, `DECISIONS.md` zeigt „warum".

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
