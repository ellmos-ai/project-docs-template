# Release Gate

The repository is release-ready only when all commands below pass from the
repository root with Python 3.10 or newer:

```bash
python -m compileall -q tests
python -m unittest discover -s tests -v
python template/_tools/doc-lint --root template
git diff --check
```

The regression suite must prove:

- MINIMAL, STANDARD, and FULL generate without unresolved generator metadata
  or dead local Markdown links.
- Generated project frontmatter passes `doc-lint`.
- `--git` creates a clean `main` repository with an initial commit.
- A non-empty target is rejected without mutation.
- FULL generation leaves `WORKFLOWS.md` synchronized.
- Markdown table metadata cannot corrupt workflow synchronization.
- A successful TODO archival is idempotent on rerun, recurring task text is
  retained as a new event, aliased paths are rejected, and both input files
  are restored when the second replacement fails.

GitHub Actions repeats compilation and the full suite on Linux, Windows, and
macOS with Python 3.10 and 3.13. A release or tag must not be created while any
matrix job is failing.
