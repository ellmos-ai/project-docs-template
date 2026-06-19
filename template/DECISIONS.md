# DECISIONS.md — Architekturentscheidungen

> **ADR-Pattern:** Architecture Decision Records.
> **Chronologisch**, neueste oben.
> **Append-only** — alte Entscheidungen werden nicht gelöscht, sondern
> durch neue ersetzt (mit Verweis).

---

## [YYYY-MM-DD]: [Kurze Entscheidungs-Überschrift]

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

## Format-Hinweis

> **Wann etwas hierher gehört:** Wenn du eine Entscheidung triffst, die
> **schwer rückgängig zu machen** ist, **systemisch** wirkt, oder deren
> **Warum** in Zukunft jemand (oder du selbst) verstehen muss.
>
> **Wann NICHT:** Kleine Refactorings, Style-Entscheidungen, reversible
> Optimierungen. Dafür ist `PATTERNS.md` da.
>
> **Commits zeigen nur „was"**, DECISIONS.md zeigt „warum".
