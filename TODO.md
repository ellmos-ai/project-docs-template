# TODO

Project-level maintenance checklist for `project-docs-template`.

## STATUS

| Category | Status | Notes |
|------|--------|-------|
| Release gate | Passing locally | The 2026-07-17 regression suite covers all profiles and tools; the GitHub matrix is the remote gate. |
| Template profiles | Verified | `MINIMAL`, `STANDARD`, and `FULL` generate profile-correct files without dead local links. |
| Tooling | Verified | Generator, linter, archive transaction, and workflow synchronization have focused regression tests. |
| Security hygiene | Documented | Root/template ignore rules and private vulnerability-reporting guidance are present. |

## Open Items

- [ ] Decide when the first semantic version tag should be cut; do not infer a
  version from generated projects' independent changelogs.
- [ ] Add an explicit profile-upgrade command only after a merge-safe contract
  for existing project files has been designed and tested.

## Notes

- Root `CHANGELOG.md` describes this repository and its tooling. A generated
  project's `CHANGELOG.md` remains independent by design.
- Inside generated projects, use `_tools/todo-archive` for completed tasks.
