# .github/ — GitHub-native Konfiguration

Dieser Ordner enthält GitHub-spezifische Dateien die außerhalb des normalen
Doku-Sets leben:

## Typische Inhalte

```
.github/
├── workflows/              # GitHub Actions (CI/CD)
│   ├── ci.yml
│   ├── release.yml
│   └── stale.yml
├── ISSUE_TEMPLATE/         # Issue-Vorlagen
│   ├── bug_report.md
│   └── feature_request.md
├── PULL_REQUEST_TEMPLATE.md
├── CODEOWNERS              # Auto-Reviewer-Zuweisung
├── CONTRIBUTING.md         # Beiträge-Guide
├── CODE_OF_CONDUCT.md      # Verhaltenskodex
├── SECURITY.md             # Security-Reporting
├── FUNDING.yml             # Sponsoring-Links
└── dependabot.yml          # Dependabot-Config
```

## Abgrenzung zum Root

| Wo | Was |
|---|---|
| **Root** (CLAUDE.md, DECISIONS.md, etc.) | Entwicklungs-Doku, LLM-Agenten, interne Prozesse |
| **.github/** | GitHub-spezifische Features, externe Contributor-Onboarding, CI/CD |

## Tipp

- **`CONTRIBUTING.md`** kann auf `../CLAUDE.md` und `../WORKFLOWS.md`
  verweisen — **nicht duplizieren**, nur für externe Contributors eine
  schmale Einstiegs-Perspektive bieten
- **`SECURITY.md`** sollte ein Kontakt-Channel sein, keine
  Policy-Ausformulierung
- **`dependabot.yml`** konfiguriert wie Alerts kommen — die
  Reaktion darauf gehört in ein projektspezifisches Security-Playbook oder
  den Router [`../WORKFLOWS.md`](../WORKFLOWS.md)
