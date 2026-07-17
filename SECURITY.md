# Security Policy

## Supported Version

Security fixes are applied to the current `main` branch. This repository does
not yet publish separately supported release branches.

## Reporting a Vulnerability

Please use [GitHub's private vulnerability report form](https://github.com/ellmos-ai/project-docs-template/security/advisories/new).
Do not open a public issue for an unpatched vulnerability or include secrets,
tokens, personal data, or a vulnerable third-party project in a report.

Include the affected tool and profile, reproduction steps, expected impact,
and a minimal sanitized example. Reports are handled as maintainer capacity
allows. Coordinated disclosure is preferred until a fix is available.

## Scope

Relevant reports include unsafe file replacement, path traversal, command
execution beyond the documented `--git` operation, secret exposure, and data
loss in `todo-archive`, `doc-lint`, `workflows-sync`, or `init-project`.

Template wording, documentation typos, and project-specific commands that a
user deliberately inserts after generation are not security vulnerabilities;
they may be reported as ordinary issues.
