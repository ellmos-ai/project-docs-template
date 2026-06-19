# DONE.md — Erledigte Tasks (Archiv)

> **Zweck:** Fine-grained Task-Level-History. Umgekehrt chronologisch
> (neueste oben).
> **Pflege:** Automatisch via `_tools/todo-archive`. Niemals manuell
> ergänzen, sonst ist das Datumsformat inkonsistent.
> **Rotation:** Einträge älter als 6 Monate → nach `archive/done-YYYY-QX.md`
> verschieben oder in `CHANGELOG.md` unter der entsprechenden Version
> zusammenfassen.

---

## [YYYY-MM-DD]

- [x] [Erledigte Task mit Kontext]
- [x] [Noch eine]

## [YYYY-MM-DD]

- [x] [Erledigte Task]

---

## Abgrenzung zu CHANGELOG.md

| File | Granularität | Zielgruppe |
|---|---|---|
| **DONE.md** | Fine-grained (einzelne Tasks) | Dev-interner Blick zurück |
| **CHANGELOG.md** | Coarse-grained (Features, Versionen) | User / Nutzer / externe Stakeholder |

Bei Release werden die DONE.md-Einträge des Zeitraums zu einem CHANGELOG.md
Unreleased-Block zusammengefasst — **nicht 1:1 kopiert**, sondern destilliert.

## Format-Hinweis

Jeder Eintrag ist ein einzelner Task wie er in TODO.md stand, mit
`[x]`-Markierung erhalten. Das Datum-Header kommt vom Archivierungs-Tool.
Wenn du manuell Einträge hinzufügen musst (z.B. vergessene History), nutze
dasselbe Format für Konsistenz.
