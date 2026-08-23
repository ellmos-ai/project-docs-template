# Security Policy

## Supported Versions

Security fixes are actively applied to the current `main` branch.

| Version | Supported | Security Policy |
|---|---|---|
| `0.1.x` (`main`) | :white_check_mark: | Full active support & immediate hotfixes |
| `< 0.1.0` | :x: | Unsupported |

## Reporting a Vulnerability

If you discover a potential security vulnerability, please report it responsibly:

1. **GitHub Private Security Advisory (Preferred):** [Submit an Advisory](https://github.com/ellmos-ai/project-docs-template/security/advisories/new)
2. **Direct Maintainer Contacts:**
   - Primary: `security@ellmos.ai`
   - Secondary: `support@lukasgeiger.com`
   - Umbrella: `lukas@open-bricks.org`

Please include the affected profile (`MINIMAL`, `STANDARD`, `FULL`), reproduction steps, expected impact, and a minimal sanitized example. Reports are handled with high priority. Coordinated disclosure is requested until a patch is released.

## Security Architecture & Invariants

- **Local-First & Zero-Egress**: The template generation tool (`init-project`) and maintenance scripts (`doc-lint`, `todo-archive`, `workflows-sync`) operate entirely on local disk. Zero outbound telemetry, network calls, or egress traffic occur during template instantiation or upgrading.
- **Deterministic Staging Isolation**: Template generation stages files in a temporary sidecar directory beside the target. Output files are promoted atomically only after link validation and placeholder verification pass. Existing non-empty targets are protected from accidental destruction.
- **SHA-256 Manifest Integrity & Fail-Closed Upgrades**: Upgrades verify `.project-docs-template.json` checksums against disk state. If any managed file has been modified by the user or an unowned file collision occurs, the upgrade operation fails closed and aborts without modifying target files.
- **Non-Elevation & User-Mode Safety**: All scripts execute in standard user context without requiring administrative or root elevation.

---

# Sicherheitsrichtlinie (Deutsche Fassung)

## Unterstützte Versionen

Sicherheitsupdates werden auf dem aktuellen `main`-Branch bereitgestellt.

| Version | Unterstützt | Status |
|---|---|---|
| `0.1.x` (`main`) | :white_check_mark: | Vollständige aktive Pflege & sofortige Patches |
| `< 0.1.0` | :x: | Nicht unterstützt |

## Sicherheitslücken melden

Bitte melden Sie Sicherheitslücken diskret und verantwortungsvoll:

1. **GitHub Private Security Advisory (Bevorzugt):** [Sicherheitsbericht einreichen](https://github.com/ellmos-ai/project-docs-template/security/advisories/new)
2. **Direkter Kontakt zum Maintainer-Team:**
   - Primär: `security@ellmos.ai`
   - Sekundär: `support@lukasgeiger.com`
   - Dachverband: `lukas@open-bricks.org`

Bitte nennen Sie das betroffene Profil (`MINIMAL`, `STANDARD`, `FULL`), Schritte zur Reproduktion sowie ein bereinigtes Minimalbeispiel. Bitte öffnen Sie keine öffentlichen GitHub-Issues für ungepatchte Schwachstellen.

## Sicherheits- und Architektur-Invarianten

- **Local-First- & Zero-Egress-Garantie**: Die Vorlagengenerierung (`init-project`) sowie alle Begleitwerkzeuge (`doc-lint`, `todo-archive`, `workflows-sync`) laufen vollständig lokal und offline ab. Es werden keinerlei Telemetrie- oder Netzwerkverbindungen aufgebaut.
- **Deterministische Staging-Isolation**: Vorlagendateien werden zuerst in einem isolierten Staging-Ordner neben dem Zielverzeichnis aufgebaut und auf Integrität geprüft. Ein bestehendes, nicht-leeres Zielverzeichnis wird niemals versehentlich überschrieben.
- **SHA-256-Manifest-Integrität & Fail-Closed-Upgrade**: Profil-Upgrades gleichen Prüfsummen in `.project-docs-template.json` bitgenau ab. Bei Benutzeranpassungen oder Dateikollisionen bricht der Prozess deterministisch ab (*Fail-Closed*), ohne das Zielverzeichnis zu beschädigen.
- **Standard-Benutzerkontext**: Alle Werkzeuge laufen ohne Administrator- oder Root-Rechte.

