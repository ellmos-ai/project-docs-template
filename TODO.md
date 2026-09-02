# TODO

Project-level maintenance checklist for `project-docs-template`.

## STATUS

| Category | Status | Notes |
|------|--------|-------|
| Release gate | Green again since 2026-09-02 | The matrix was red on all eight Windows and macOS jobs from 2026-08-23 to 2026-09-02; see the entry below. |
| Template profiles | Verified | `MINIMAL`, `STANDARD`, and `FULL` generate profile-correct files without dead local links. |
| Tooling | Verified | Generator, linter, archive transaction, and workflow synchronization have focused regression tests. |
| Security hygiene | Documented | Root/template ignore rules and private vulnerability-reporting guidance are present. |

## Open Items

- [ ] **Provide an English template set.** The repository presents itself in
  English, but the generated documentation is German: the bodies under
  `template/` and the CLI output of `init-project`, `doc-lint`, `todo-archive`
  and `workflows-sync`. There is no i18n mechanism of any kind — no `locales/`,
  no catalogue, no switch. Next step: extract the CLI strings of the four tools
  into a catalogue and add a `--lang` flag with system-locale detection, then
  translate the template bodies. Disclosed in the READMEs and `llms.txt` in the
  meantime so the mismatch is at least honest.
- [ ] **Cut tags and GitHub releases for 0.1.1 and 0.1.2.** `pyproject.toml`,
  `ellmos-module.v2.json`, the README badge and `CHANGELOG.md` all say `0.1.2`,
  but `v0.1.0` is the only tag that exists and the repository has no GitHub
  release at all. Every version carrier except the tag has moved.
- [ ] **Make the release gate enforce itself.** `RELEASE_GATE.md` states that a
  release must not be created while any matrix job is failing; `0.1.2` was
  released on 2026-08-23 with eight of twelve jobs red, and its changelog entry
  claimed "34 tests passed, 7 subtests, 100% green". Consider a required status
  check on `main` so the written gate and the enforced gate are the same thing.
- [ ] **Reconcile `RELEASE_GATE.md` with the workflow.** The documented gate runs
  `compileall`, `unittest`, `doc-lint` and `git diff --check`; CI runs `ruff`,
  `compileall` and `pytest` and never invokes `doc-lint`.
- [ ] **Set the missing back-links.** The "Ecosystem & Sibling Tools" matrix
  points at fourteen sibling repositories; an org-wide code search on
  2026-09-02 found no repository in any of the ten own organizations that links
  back. The matrix is currently a one-way street.
- [x] Decide when the first semantic version tag should be cut — `v0.1.0` was
  tagged on 2026-07-28; the open work is the missing follow-up tags above.
- [x] Add an explicit profile-upgrade command with a merge-safe manifest/hash
  contract for existing project files; covered by the upgrade regression tests.
- [x] Fix the cross-platform CI failure: the upgrade rollback test compared an
  unresolved temporary path against the resolved manifest path, so the injected
  failure never fired on macOS (`/var` symlink) or Windows (8.3 short paths).
- [x] Stop tracking `BEFUNDE.md` — an internal maintenance journal that
  published the local working path and stale test counts.
- [x] Restore the SHA-pinned Node 24 GitHub Actions that the `0.1.2` "CI
  hardening" commit replaced with the floating, Node 20 tags `@v4` and `@v5`.
- [x] Remove the private `dev-bricks/automation-master` from the public sibling
  matrix; a contract test had been requiring the 404 link.
- [x] Correct the `clutch` entry — it is an LLM router, not a Git wrapper — and
  restore the missing MIT line in the English README's license section.

## Notes

- Root `CHANGELOG.md` describes this repository and its tooling. A generated
  project's `CHANGELOG.md` remains independent by design.
- Inside generated projects, use `_tools/todo-archive` for completed tasks.
