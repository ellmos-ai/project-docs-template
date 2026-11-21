# MASTER-REGISTRY.md — Verzeichnis der Projekt-Register

**Version:** 0.1.0
**Aktualisiert:** [YYYY-MM-DD]
**Grund:** [Was wurde warum geändert]
**Zweck:** Zentraler Index aller Register, Verzeichnisse und Status-Quellen von [Projektname]. Diese Datei benennt Zuständigkeiten, ohne Fachinhalte zu duplizieren.

> **Selbstkorrektur:** Wenn du veraltete Passagen oder Verweise entdeckst, oder sogar missgeleitet wirst, korrigiere diese Datei autonom. Wenn du etwas Neues gebaut oder erstellt hast, prüfe: Hättest du es durch das Lesen der Dateien, die du gelesen hast, bereits gefunden und/oder richtig verstanden? Wenn nicht, setze dort an und behebe es, sodass du es gefunden und verstanden hättest.

> **Selbstheilung:** Werden mehrere aktive Dateien derselben Rolle oder Nummer nebeneinander erkannt (z. B. durch Sync-Konflikte), zuerst vollständig diffen und verlustfrei in die kanonische Datei zusammenführen; nichts Einzigartiges stillschweigend löschen. Aktive Locks (`LOCK*.txt`) haben Vorrang; Archive bleiben getrennt.

> **Dateigröße:** Wenn diese Datei zu lang wird: Verwende das Cut-and-Clue-Verfahren → [`CUT-AND-CLUE.md`](./CUT-AND-CLUE.md).

---

## Kanonische Projekt-Register

| Register | Zuständigkeit | Wann lesen oder ändern |
|---|---|---|
| [`WORKFLOWS.md`](./WORKFLOWS.md) | Index aller Multi-Step-Playbooks in `workflows/` (auto-generiert via `_tools/workflows-sync`) | Wenn ein wiederkehrender Prozess angelegt, geändert oder gesucht wird. |
| [`TOOLS.md`](./TOOLS.md) | Index aller Admin- und Hilfs-Scripts in `_tools/` | Wenn ein Utility-Script angelegt, geändert oder gesucht wird. |
| [`DECISIONS.md`](./DECISIONS.md) | Architekturentscheidungen (ADR-Format, append-only) | Bei schwer rückgängig zu machenden oder systemischen Entscheidungen. |
| [`PATTERNS.md`](./PATTERNS.md) | Wiederkehrende Code-/Betriebsmuster (Do/Don't) | Bei wiederkehrenden Fehlerbildern oder Best-Practice-Regeln. |
| [`GLOSSARY.md`](./GLOSSARY.md) | Projektspezifische Begriffe, Abkürzungen und Symbole | Wenn domänenspezifische Begriffe nachgeschlagen oder eingeführt werden. |
| [`TODO.md`](./TODO.md) | Aktive Aufgaben (optional als Index auf `TODO-<BEREICH>.md`-Unterlisten) | Bei jeder Aufgabenplanung, Statusänderung oder Session-Übergabe. |
| [`DONE.md`](./DONE.md) | Chronologisches Archiv erledigter Aufgaben (`_tools/todo-archive`) | Über `_tools/todo-archive --apply` am Session-Ende. |

### Optionale Fach- und Betriebsregister (bei Bedarf aus `REG-TEMPLATE.md` anlegen)

| Beispiel-Register | Typische Zuständigkeit | Ablage-Empfehlung |
|---|---|---|
| `CHECKS-REG.md` | Chronik geprüfter Komponenten, Audits oder Testläufe | Root oder `_reg/CHECKS-REG.md` |
| `POLICY-REG.md` | Verzeichnis projektspezifischer Richtlinien und Freigabegates | Root oder `_reg/POLICY-REG.md` |
| `RELEASES-REG.md` | Plattform-/Zielmatrix, Release-Artefakte und Checksummen | Root oder `_reg/RELEASES-REG.md` |

---

## Nicht als Registry verwenden

| Datei | Tatsächliche Rolle |
|---|---|
| [`CLAUDE.md`](./CLAUDE.md) | Boot-, Regel- und Überblicksdatei; verweist auf Register, ersetzt sie aber nicht. |
| [`AGENTS.md`](./AGENTS.md) | Tool-agnostischer Redirect auf `CLAUDE.md`. |
| [`START.md`](./START.md) | Imperative Session-Start- und Session-Ende-Checkliste. |
| [`STATE.md`](./STATE.md) | Kurzfristiger aktueller Projekt-Snapshot (keine vollständige Chronik). |
| [`README.md`](./README.md) | Menschlicher Einstieg und Kurzorientierung. |

---

## Root-Ablage & Unterverzeichnis-Regel

Damit das Projekt-Root übersichtlich bleibt, wenn Register oder Aufgabenlisten wachsen:

1. **Stabile Einstiege im Root:** Kanonische Einstiegsdateien (`TODO.md`, `MASTER-REGISTRY.md`, aktive Hauptregister) behalten ihren Namen im Root.
2. **Unterteile und Fortsetzungen auslagern:** Nummerierte Fortsetzungen und thematische Unterregister gehören nach `_reg/` (z. B. `_reg/todo/TODO_<N>.md` oder `_reg/<bereich>-reg.md`) oder in klar benannte Unterlisten, abgeschlossene Segmente nach `_archive/`.
3. **Keine unregistrierten Schattenregister:** Jedes neue Register wird sofort hier eingetragen — ein nicht registriertes Register existiert für nachfolgende Agenten praktisch nicht.

## Pflege-Regel

Wenn ein neues Register angelegt wird:

1. Aus der Vorlage `REG-TEMPLATE.md` (im Template-Repository unter `template/REG-TEMPLATE.md`) erstellen und Rolle sowie Zuständigkeit in einem Satz festlegen.
2. In dieser `MASTER-REGISTRY.md` mit Zuständigkeit und Trigger („Wann lesen oder ändern“) eintragen.
3. Falls es für den Session-Start relevant ist, auch in `START.md` / `CLAUDE.md` verlinken.
4. Wenn ein neues Register ein älteres ablöst, im alten Dokument einen eindeutigen Verweis auf die neue Zuständigkeit (oder bei komplettem Umzug einen `*.MOVED.md`-Stub nach [`MOVED-STUB.md`](./MOVED-STUB.md)) hinterlassen.

---

<!-- REMEMBER: ENDUSERTEXTE BEKOMMEN ECHTE UMLAUTE ä ö ü Ä Ö Ü ß -->
