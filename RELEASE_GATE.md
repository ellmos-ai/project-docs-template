# Release Gate

The repository is release-ready only when all commands below pass from the
repository root with Python 3.10 or newer:

```bash
ruff check .
python template/_tools/doc-lint --root template
python -m compileall -q tests template
python -m pytest -ra -v
git diff --check
```

The regression suite must prove:

- MINIMAL, STANDARD, and FULL generate without unresolved generator metadata
  or dead local Markdown links.
- Generated project frontmatter passes `doc-lint`.
- `--git` creates a clean `main` repository with an initial commit.
- A non-empty target is rejected without mutation.
- Every generated project records a `.project-docs-template.json` ownership
  manifest, and the next profile upgrade replaces only unchanged managed files,
  rejects changed/unowned collisions without mutation, and rolls back on
  commit failure.
- FULL generation leaves `WORKFLOWS.md` synchronized.
- Markdown table metadata cannot corrupt workflow synchronization.
- A successful TODO archival is idempotent on rerun, recurring task text is
  retained as a new event, aliased paths are rejected, and both input files
  are restored when the second replacement fails.

GitHub Actions repeats compilation, template linting, and the full test suite
on Linux, Windows, and macOS across Python 3.10, 3.11, 3.12, and 3.13. A release
or tag must not be created while any matrix job is failing.
