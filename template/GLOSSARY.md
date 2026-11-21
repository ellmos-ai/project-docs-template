# GLOSSARY.md — Projekt-Jargon

**Version:** 0.1.0
**Aktualisiert:** [YYYY-MM-DD]
**Grund:** [Was wurde warum geändert]
**Zweck:** Begriffs-, Symbol- und Kürzel-Definitionen für projektspezifische Termini in [Projektname].

> **Selbstkorrektur:** Wenn du einen Begriff nachschlagen musstest und er hier fehlte, trage ihn ein. Wenn du einen neuen Begriff einführst, trage ihn im selben Arbeitsgang ein — prüfe vorab, damit keine zweite Bezeichnung für dasselbe entsteht.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt (z. B. durch Sync-Konflikte), zuerst vollständig diffen und verlustfrei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang.

> **Dateigröße:** Wenn diese Datei zu lang wird: Verwende das Cut-and-Clue-Verfahren → [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md).

> **Wann anlegen:** Wenn das Projekt mehr als ~5 eigene Begriffe hat, die nicht sofort selbst-erklärend sind.
> **Wann NICHT:** Für Standard-Technik-Begriffe, die jeder Entwickler kennt.

---

## Regeln

1. **Ein Glossar definiert, es beweist nichts.** Kein Eintrag ist ein Status- oder Evidenz-Nachweis.
2. **Fundstelle nennen:** Jeder Begriff verweist auf Datei/Abschnitt oder Code-Referenz.
3. **Namenskollisionen ausweisen:** Trägt ein Symbol oder Kürzel in zwei Modulen/Quellen unterschiedliche Bedeutungen, beide nebeneinander aufführen.
4. **Zählstände nur datiert:** Zahlenangaben immer mit Messdatum und Quelle versehen.

---

## A

**[Begriff A]**
[Definition. Was bedeutet der Begriff in diesem Projekt-Kontext? Warum
wurde er so gewählt?]
*Beispiel:* [Kurzes Beispiel]
*Siehe auch:* [Verwandter Begriff]

## B

**[Begriff B]**
[Definition]

## C

**[Begriff C]**
[Definition]

---

## Format-Regeln

- **Alphabetisch** sortiert, mit Überschriften pro Buchstabe
- **Cross-Links** zu verwandten Begriffen
- **Code-Referenz** wo möglich (`core/file.py:42`)
- **Datum bei neuen Einträgen** optional (`[2026-04-08] Begriff X`)

## Wann Begriffe hierher gehören

- ✅ Domain-spezifische Kunstwörter (z. B. „Reciprocity-Score“)
- ✅ Abkürzungen und Akronyme die nur in diesem Projekt Sinn machen
- ✅ Technik-Begriffe mit einer projekt-spezifischen Bedeutung
- ❌ Standard-Begriffe (REST, API, JSON, Git) — die kennt jeder
- ❌ Vollständige Konzept-Erklärungen — das ist `ARCHITECTURE.md`
- ❌ Entscheidungs-Rationale — das ist `DECISIONS.md`

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
