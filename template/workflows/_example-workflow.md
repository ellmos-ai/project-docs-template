# Workflow: Release neue npm-Paket-Version

> **Last verified:** [YYYY-MM-DD]
> **Frequency:** pro Release (ad-hoc)
> **Duration:** ~5 min

## Purpose

Eine neue Version eines npm-Pakets veröffentlichen, inkl. Version-Bump, Build,
Test, Git-Tag, Push und Verify. Mit Dependabot-Upstream-Sync falls nötig.

## Preconditions

- `npm whoami` zeigt dich als authentifizierten User
- Du bist auf dem richtigen Branch (meist `main` oder `master`)
- `git status` ist clean außer den geplanten Änderungen
- Du bist Admin des Repos (für Branch Protection Bypass falls nötig)

## Steps

1. **Version bumpen** in `package.json`
   ```bash
   # Manuell oder via:
   npm version patch   # oder minor/major
   ```

2. **package-lock.json syncen**
   ```bash
   npm install --package-lock-only
   ```

3. **Build**
   ```bash
   npm run build
   ```

4. **Tests** (falls vorhanden)
   ```bash
   npm test
   ```

5. **Commit**
   ```bash
   git add package.json package-lock.json dist/
   git commit -m "chore: bump version to $(node -p "require('./package.json').version")"
   ```

6. **Rebase falls behind**
   ```bash
   git fetch origin
   git status -b --porcelain=v1 | head -1
   # Wenn "behind": git pull --rebase
   ```

7. **Push**
   ```bash
   git push
   ```

8. **Publish**
   ```bash
   npm publish --access public
   ```

9. **Verify**
   ```bash
   npm view $(node -p "require('./package.json').name") version
   ```

## Exit-Criteria

- [ ] `git status` ist clean
- [ ] `npm view ... version` zeigt die neue Version
- [ ] Kein offener Branch-Protection-Error
- [ ] `CHANGELOG.md` Eintrag aktualisiert (falls release-worthy)
- [ ] `STATE.md` aktualisiert

## Fallstricke

- ⚠️ **Branch 2 Commits behind**: Das passiert oft wenn ein Bot zwischenzeitlich
  gepusht hat (z.B. Dependabot, CI-Workflow-Sync). Immer `git pull --rebase`
  vor dem eigenen Push.
- ⚠️ **`prepublishOnly` schlägt fehl**: Oft wegen ungesetzter NODE_OPTIONS bei
  TypeScript-OOM. Fix: `NODE_OPTIONS="--max-old-space-size=8192" npm publish`
- ⚠️ **Force-Push nötig wegen fehlerhaftem Commit**: Nutze ein geprüftes
  projektspezifisches Admin-Playbook, nicht `git push --force` direkt.

## Verwandte

- `workflows/security-audit.md` — falls das Projekt dafür ein eigenes
  Security-Playbook anlegt
- [`../PATTERNS.md`](../PATTERNS.md) — Do/Don't bei npm/git

## Historie

- **[YYYY-MM-DD]** — Workflow erstellt aus [Projekt-Kontext]
- **[YYYY-MM-DD]** — Schritt 6 (rebase-check) hinzugefügt nach Reibungs-Vorfall
