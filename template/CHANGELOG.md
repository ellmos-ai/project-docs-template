# Changelog

Alle nennenswerten Änderungen an diesem Projekt werden hier dokumentiert.

Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.1.0/),
dieses Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

---

## [Unreleased]

### Hinzugefügt
- [Neue Features]

### Geändert
- [Änderungen an bestehenden Features]

### Behoben
- `_tools/doc-lint` erkennt das kanonische `project-docs`-Quelltemplate jetzt als Placeholder-Modus, damit der strikte Root-Check nicht an absichtlichen Template-Platzhaltern scheitert.
- YAML-Frontmatter-Platzhalter in `CLAUDE.md`, `START.md` und `STATE.md` als gültige Strings gequotet, damit Template-Instanzen keine Parser-Fallen im Header erben.
- `_tools/init-project` kopiert `_tools/` jetzt profilgerecht statt den Generator selbst und weitere Template-Helfer ungefragt in neue Projekte zu legen.
- `_tools/doc-lint` bewahrt das Feld `reason_last_change` in `CLAUDE.md` jetzt auch bei `--fix` und `--update-dates`, statt es versehentlich aus dem Header zu verlieren.

### Geändert
- `STANDARD` und `FULL` rollen `HEADER-RULES.md` und `CUT-AND-CLUE.md` jetzt konsistent mit aus; Profilzählungen und Root-Doku wurden auf den aktuellen 16-Dateien-Stand nachgezogen.
- `HEADER-RULES.md` beschreibt für Projekt-Steuerdateien und Aufgabenlisten jetzt wieder eindeutig den `.md`-Standard statt eines konkurrierenden `.txt`-Schemas.

### Entfernt
- [Entfernte Features]

---

## [0.1.0] — [YYYY-MM-DD]

### Hinzugefügt
- Initiale Projekt-Struktur
- [Erstes Feature]
- [Zweites Feature]

---

## Format-Hinweis

> **Fine-grained Task-Level-Historie** (einzelne erledigte TODO-Einträge)
> lebt in [`DONE.md`](./DONE.md). **CHANGELOG.md** ist für Release-Level
> und bedeutsame Ereignisse — nicht für jeden einzelnen Task.
>
> Bei Release: erledigte DONE.md-Einträge werden zu einem Unreleased-Block
> zusammengefasst und hier archiviert.
