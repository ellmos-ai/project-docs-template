from __future__ import annotations

import json
import re
import unittest
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


class MetadataAndManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.pyproject_path = REPO_ROOT / "pyproject.toml"
        self.module_json_path = REPO_ROOT / "ellmos-module.v2.json"
        self.changelog_path = REPO_ROOT / "CHANGELOG.md"
        self.readme_en_path = REPO_ROOT / "README.md"
        self.readme_de_path = REPO_ROOT / "README_de.md"
        self.security_path = REPO_ROOT / "SECURITY.md"
        self.llms_txt_path = REPO_ROOT / "llms.txt"
        self.ci_workflow_path = REPO_ROOT / ".github" / "workflows" / "ci.yml"

    def _extract_pyproject_version(self) -> str:
        content = self.pyproject_path.read_text(encoding="utf-8")
        match = re.search(r'version\s*=\s*"([^"]+)"', content)
        self.assertIsNotNone(match, "version not found in pyproject.toml")
        return match.group(1)

    def _extract_module_version(self) -> str:
        data = json.loads(self.module_json_path.read_text(encoding="utf-8"))
        return data.get("version", "")

    def test_version_parity_across_manifests(self) -> None:
        pyproject_ver = self._extract_pyproject_version()
        module_ver = self._extract_module_version()
        self.assertEqual(
            pyproject_ver,
            module_ver,
            f"pyproject.toml version ({pyproject_ver}) != ellmos-module.v2.json version ({module_ver})",
        )
        changelog_content = self.changelog_path.read_text(encoding="utf-8")
        self.assertIn(pyproject_ver, changelog_content, f"Version {pyproject_ver} missing in CHANGELOG.md")

    def test_required_root_documents_exist(self) -> None:
        required_files = [
            "README.md",
            "README_de.md",
            "LICENSE",
            "SECURITY.md",
            "RELEASE_GATE.md",
            "CHANGELOG.md",
            "llms.txt",
            "pyproject.toml",
            "ellmos-module.v2.json",
            "THIRD_PARTY_LICENSES.md",
            "MARKETING-LOG.txt",
        ]
        for filename in required_files:
            file_path = REPO_ROOT / filename
            self.assertTrue(file_path.is_file(), f"Required file missing: {filename}")
            self.assertGreater(file_path.stat().st_size, 0, f"File is empty: {filename}")

    def test_ellmos_module_manifest_validity(self) -> None:
        data = json.loads(self.module_json_path.read_text(encoding="utf-8"))
        self.assertEqual(data.get("schema"), "ellmos.module.v2")
        self.assertEqual(data.get("id"), "project-docs-template")
        self.assertEqual(data.get("kind"), "template")
        self.assertEqual(data.get("status"), "released")
        self.assertEqual(data.get("visibility"), "public")
        self.assertIn("minimal", data.get("profiles", []))
        self.assertIn("standard", data.get("profiles", []))
        self.assertIn("full", data.get("profiles", []))
        self.assertIn("quality.project-docs", data.get("provides", []))

    def test_llms_txt_integrity(self) -> None:
        content = self.llms_txt_path.read_text(encoding="utf-8")
        self.assertTrue(content.startswith("## Last-checked:"), "llms.txt must start with ## Last-checked:")
        # Assert the shape of the stamp, not one frozen day. Hard-coding a date
        # here meant every refresh of llms.txt broke the suite, which invites
        # bumping the assertion instead of checking the stamp is real.
        stamp = re.match(r"## Last-checked: (\d{4})-(\d{2})-(\d{2})\n", content)
        self.assertIsNotNone(stamp, "llms.txt must carry an ISO Last-checked date")
        date(int(stamp.group(1)), int(stamp.group(2)), int(stamp.group(3)))
        self.assertIn("https://github.com/ellmos-ai/project-docs-template", content)
        self.assertIn("## Search Phrases", content)
        self.assertIn("## Disambiguation", content)
        self.assertIn("Primary audience:", content)

    def test_readme_bilingual_structural_parity(self) -> None:
        en_content = self.readme_en_path.read_text(encoding="utf-8")
        de_content = self.readme_de_path.read_text(encoding="utf-8")

        # Badges
        for badge_pattern in [
            "pytest",
            "license-MIT",
            "Language-",
            "Ecosystem-ellmos",
            "Umbrella-open",
            "LLM--Ready",
            "zero--dependency",
            "marketing-",
        ]:
            self.assertIn(badge_pattern, en_content, f"Badge {badge_pattern} missing in README.md")
            self.assertIn(badge_pattern, de_content, f"Badge {badge_pattern} missing in README_de.md")
        self.assertIn("last%20checked", en_content)
        self.assertIn("letzte%20pr%C3%BCfung", de_content)
        self.assertIn("licenses-zero--dependency", en_content)
        self.assertIn("lizenzen-zero--dependency", de_content)

        # Mermaid diagrams (2 diagrams in each)
        self.assertEqual(en_content.count("```mermaid"), 2, "README.md must contain 2 Mermaid diagrams")
        self.assertEqual(de_content.count("```mermaid"), 2, "README_de.md must contain 2 Mermaid diagrams")

        # Profiles
        for profile in ["MINIMAL", "STANDARD", "FULL"]:
            self.assertIn(profile, en_content, f"Profile {profile} missing in README.md")
            self.assertIn(profile, de_content, f"Profile {profile} missing in README_de.md")

    def test_security_policy_bilingual_parity_and_contacts(self) -> None:
        content = self.security_path.read_text(encoding="utf-8")
        self.assertIn("# Security Policy", content, "SECURITY.md missing English heading")
        self.assertIn("Sicherheitsrichtlinie", content, "SECURITY.md missing German section")
        self.assertIn("security@ellmos.ai", content, "SECURITY.md missing security@ellmos.ai contact")
        self.assertIn("support@lukasgeiger.com", content, "SECURITY.md missing support@lukasgeiger.com contact")
        self.assertIn("lukas@open-bricks.org", content, "SECURITY.md missing lukas@open-bricks.org contact")
        self.assertIn("Zero-Egress", content, "SECURITY.md missing Zero-Egress invariant")
        self.assertIn("Local-First", content, "SECURITY.md missing Local-First invariant")

    def test_sibling_tools_ecosystem_matrix(self) -> None:
        en_content = self.readme_en_path.read_text(encoding="utf-8")
        de_content = self.readme_de_path.read_text(encoding="utf-8")

        # Only publicly reachable repositories belong here. `automation-master`
        # was required by this list while being private, so the contract test
        # actively kept a 404 link in a public README.
        key_siblings = [
            "policy-registry",
            "companion-for-agy",
            "lock-master",
            "system-gap-master",
            "open-bricks",
        ]
        for sibling in key_siblings:
            self.assertIn(sibling, en_content, f"Sibling tool {sibling} missing in README.md matrix")
            self.assertIn(sibling, de_content, f"Sibling tool {sibling} missing in README_de.md matrix")

    def test_ci_workflow_and_ruff_configuration(self) -> None:
        self.assertTrue(self.ci_workflow_path.is_file(), "CI workflow file missing")
        ci_content = self.ci_workflow_path.read_text(encoding="utf-8")
        self.assertIn("ubuntu-latest", ci_content)
        self.assertIn("windows-latest", ci_content)
        self.assertIn("macos-latest", ci_content)
        self.assertIn("3.10", ci_content)
        self.assertIn("3.11", ci_content)
        self.assertIn("3.12", ci_content)
        self.assertIn("3.13", ci_content)
        # Contract is supply-chain pinning, not a specific major. Asserting
        # "@v4"/"@v5" literally froze the workflow onto the deprecated Node 20
        # actions and blocked the upgrade it was supposed to protect.
        for action in ("actions/checkout", "actions/setup-python"):
            self.assertRegex(
                ci_content,
                rf"uses: {action}@[0-9a-f]{{40}}\b",
                f"{action} must be pinned to a full 40-character commit SHA",
            )
        self.assertIn("ruff check", ci_content)
        self.assertIn("compileall", ci_content)
        self.assertIn("pytest", ci_content)

        pyproject_content = self.pyproject_path.read_text(encoding="utf-8")
        self.assertIn("[tool.ruff]", pyproject_content)
        self.assertIn("[tool.ruff.lint]", pyproject_content)

    def test_pyproject_pep621_classifiers_and_urls(self) -> None:
        content = self.pyproject_path.read_text(encoding="utf-8")
        self.assertIn("Operating System :: OS Independent", content)
        self.assertIn("Operating System :: Microsoft :: Windows", content)
        self.assertIn("Operating System :: POSIX :: Linux", content)
        self.assertIn("Operating System :: MacOS", content)
        self.assertIn("Documentation =", content)
        self.assertIn("Security =", content)
        self.assertIn("Umbrella =", content)
        self.assertIn("https://open-bricks.org", content)
        self.assertIn('"Third-Party Licenses" =', content)
        self.assertIn('"Marketing Log" =', content)
        self.assertIn('"LLM Ready" =', content)
        for kw in ["multi-agent", "zero-egress", "governance", "session-handoff"]:
            self.assertIn(f'"{kw}"', content, f"Keyword {kw} missing in pyproject.toml")

    def test_offline_and_privacy_invariants(self) -> None:
        sec_content = self.security_path.read_text(encoding="utf-8")
        readme_en = self.readme_en_path.read_text(encoding="utf-8")
        readme_de = self.readme_de_path.read_text(encoding="utf-8")

        self.assertIn("Zero-Egress", sec_content)
        self.assertIn("Local-First", sec_content)
        self.assertIn("Deterministic Staging", sec_content)
        self.assertIn("Fail-Closed", sec_content)
        self.assertIn("Non-Elevation", sec_content)

        self.assertIn("100%25%20Offline", readme_en)
        self.assertIn("Zero--Egress", readme_en)
        self.assertIn("100%25%20Offline", readme_de)
        self.assertIn("Zero--Egress", readme_de)

    def test_template_directory_completeness(self) -> None:
        template_dir = REPO_ROOT / "template"
        self.assertTrue(template_dir.is_dir(), "template/ directory missing")

        core_templates = [
            "CLAUDE.md",
            "AGENTS.md",
            "START.md",
            "STATE.md",
            "TODO.md",
            "DONE.md",
            "DECISIONS.md",
            "PATTERNS.md",
            "CHANGELOG.md",
            "HEADER-RULES.md",
            "CUT-AND-CLUE.md",
            "ARCHITECTURE.md",
            "WORKFLOWS.md",
            "TOOLS.md",
            "GLOSSARY.md",
            "TEMPLATE.md",
        ]
        for tpl in core_templates:
            self.assertTrue((template_dir / tpl).is_file(), f"Template file missing: template/{tpl}")

        tools_dir = template_dir / "_tools"
        self.assertTrue(tools_dir.is_dir(), "template/_tools directory missing")
        for tool in ["init-project", "doc-lint", "todo-archive", "workflows-sync"]:
            self.assertTrue((tools_dir / tool).is_file(), f"Tool script missing: template/_tools/{tool}")

    def test_quick_navigation_anchors(self) -> None:
        """Verify quick navigation links resolve to headers in READMEs."""
        for filename in ["README.md", "README_de.md"]:
            content = (REPO_ROOT / filename).read_text(encoding="utf-8")
            self.assertTrue("Quick Navigation" in content or "Schnellnavigation" in content)

            anchor_links = re.findall(r"\[([^\]]+)\]\(#([^\)]+)\)", content)
            self.assertGreaterEqual(len(anchor_links), 8, f"Expected at least 8 quick nav links in {filename}")

            headers = re.findall(r"^#{2,4}\s+(.+)$", content, re.MULTILINE)
            normalized_headers = [
                re.sub(r"[^\w\s-]", "", h).strip().lower().replace(" ", "-") for h in headers
            ]

            for _text, anchor in anchor_links:
                self.assertTrue(
                    anchor in normalized_headers or any(anchor in nh for nh in normalized_headers),
                    f"Anchor #{anchor} in {filename} does not match any header",
                )

    def test_target_personas_and_use_cases_section(self) -> None:
        """Verify Target Personas section in both English and German READMEs."""
        en_content = self.readme_en_path.read_text(encoding="utf-8")
        de_content = self.readme_de_path.read_text(encoding="utf-8")

        self.assertTrue("Target Personas & Core Use Cases" in en_content or "Target Personas" in en_content)
        self.assertIn("Multi-Agent Systems Engineers", en_content)
        self.assertIn("Solo Developers & Open-Source Maintainers", en_content)
        self.assertIn("Enterprise Architecture & AI Governance Leads", en_content)
        self.assertIn("Research & Scientific Pipeline Developers", en_content)

        self.assertTrue("Zielgruppen & Kern-Anwendungsfälle" in de_content or "Zielgruppen" in de_content)
        self.assertIn("Multi-Agenten Flotten-Ingenieure", de_content)
        self.assertIn("Solo-Entwickler & Open-Source-Maintainer", de_content)
        self.assertIn("Enterprise Architecture & AI Compliance Leads", de_content)
        self.assertIn("Forschungs- & Pipeline-Entwickler", de_content)

    def test_comparative_architecture_matrix(self) -> None:
        """Verify Comparative Architecture table in both English and German READMEs."""
        en_content = self.readme_en_path.read_text(encoding="utf-8")
        de_content = self.readme_de_path.read_text(encoding="utf-8")

        self.assertTrue("Comparative Architecture" in en_content)
        self.assertIn("Generic Markdown Dumps", en_content)
        self.assertIn("Heavy SaaS Wikis", en_content)
        self.assertIn("Rigid Agent Frameworks", en_content)

        self.assertTrue("Architekturvergleich" in de_content or "Vergleichsmatrix" in de_content)
        self.assertIn("Generische Markdown-Ablage", de_content)
        self.assertIn("Schwere SaaS-Wikis", de_content)
        self.assertIn("Starre Agenten-Frameworks", de_content)

    def test_third_party_licenses_content(self) -> None:
        """Verify THIRD_PARTY_LICENSES.md structure and invariants."""
        tpl_path = REPO_ROOT / "THIRD_PARTY_LICENSES.md"
        self.assertTrue(tpl_path.is_file(), "THIRD_PARTY_LICENSES.md missing")
        content = tpl_path.read_text(encoding="utf-8")
        self.assertIn("Third-Party Licenses & Software Bill of Materials", content)
        self.assertIn("Zero-Runtime-Dependency invariant", content)
        self.assertIn("Zero-Egress & Local-First Invariant", content)
        self.assertIn("pytest", content)
        self.assertIn("ruff", content)
        self.assertIn("MIT License", content)

    def test_marketing_log_structure(self) -> None:
        """Verify MARKETING-LOG.txt presence and Pfad B sections."""
        mlog_path = REPO_ROOT / "MARKETING-LOG.txt"
        self.assertTrue(mlog_path.is_file(), "MARKETING-LOG.txt missing")
        content = mlog_path.read_text(encoding="utf-8")
        self.assertIn("MARKETING-LOG — Discoverability, SEO & Positioning Register", content)
        self.assertIn("Pfad B: Discoverability, Target Personas", content)
        self.assertIn("Bilingual High-Intent Keyword Matrix", content)
        self.assertIn("Comparative Architecture & Differentiation", content)

    def test_ci_workflow_timeouts_concurrency_and_runner(self) -> None:
        """Verify CI workflow has runaway timeouts, concurrency cancellation, and pytest flags."""
        ci_content = self.ci_workflow_path.read_text(encoding="utf-8")
        self.assertIn("timeout-minutes: 15", ci_content, "CI test job must specify timeout-minutes: 15")
        self.assertIn("concurrency:", ci_content, "CI workflow must specify concurrency")
        self.assertIn("cancel-in-progress: true", ci_content, "CI concurrency must cancel in-progress runs")
        self.assertIn("-ra -v", ci_content, "CI pytest command must include -ra -v flags")

    def test_stale_workflow_present_and_safe(self) -> None:
        """Verify stale.yml automation exists with timeouts and concurrency."""
        stale_path = REPO_ROOT / ".github" / "workflows" / "stale.yml"
        self.assertTrue(stale_path.is_file(), "stale.yml workflow must exist")
        content = stale_path.read_text(encoding="utf-8")
        self.assertIn("timeout-minutes: 10", content, "stale workflow must have timeout-minutes: 10")
        self.assertIn("concurrency:", content, "stale workflow must specify concurrency")
        self.assertIn("actions/stale", content, "stale workflow must use actions/stale")

    def test_gitignore_canonical_locks_and_multihost_defense(self) -> None:
        """Verify root .gitignore defends against multi-host conflict copies and locks."""
        content = (REPO_ROOT / ".gitignore").read_text(encoding="utf-8")
        expected_patterns = [
            "* (kopie)*",
            "* (copy)*",
            "*-WORKSTATION*",
            "*-ASUS-GEI*",
            "LOCK",
            "LOCK.*",
            "LOCK.permissions.json",
            "uv.lock",
            "!package-lock.json",
            ".coverage.*",
            ".tox/",
            ".turbo/",
            ".nyc_output/",
            ".hypothesis/",
            "MARKETING-LOG.txt",
        ]
        for pattern in expected_patterns:
            self.assertIn(pattern, content, f"Root .gitignore must defend against {pattern}")

    def test_template_gitignore_inherits_defense(self) -> None:
        """Verify scaffold template/.gitignore also protects generated repositories."""
        content = (REPO_ROOT / "template" / ".gitignore").read_text(encoding="utf-8")
        expected_patterns = [
            "* (kopie)*",
            "* (copy)*",
            "*-WORKSTATION*",
            "*-ASUS-GEI*",
            "LOCK",
            "LOCK.*",
            "LOCK.permissions.json",
            "uv.lock",
            "!package-lock.json",
            ".coverage.*",
            ".tox/",
            ".turbo/",
            ".nyc_output/",
            ".hypothesis/",
            "MARKETING-LOG.txt",
        ]
        for pattern in expected_patterns:
            self.assertIn(pattern, content, f"Template .gitignore must defend against {pattern}")

    def test_pyproject_pytest_addopts_and_bug_tracker(self) -> None:
        """Verify pyproject.toml contains standard pytest addopts and Bug Tracker URL."""
        content = self.pyproject_path.read_text(encoding="utf-8")
        self.assertIn('addopts = "-ra -v"', content, "pyproject.toml must configure addopts = '-ra -v'")
        self.assertIn('"Bug Tracker" =', content, "pyproject.toml must contain Bug Tracker URL")

    def test_root_notice_attribution(self) -> None:
        """Verify root NOTICE file exists and contains canonical attribution and copyright."""
        notice_path = REPO_ROOT / "NOTICE"
        self.assertTrue(notice_path.is_file(), "NOTICE file must exist in repository root")
        notice_content = notice_path.read_text(encoding="utf-8")
        self.assertIn("project-docs-template", notice_content)
        self.assertIn("Copyright (c) 2026 Lukas Geiger", notice_content)
        self.assertIn("ellmos-ai", notice_content)
        self.assertIn("open-bricks", notice_content)
        self.assertIn("MIT License", notice_content)

    def test_pep639_license_files_contract(self) -> None:
        """Verify PEP 639 license-files declaration in pyproject.toml and file existence."""
        pyproject_content = self.pyproject_path.read_text(encoding="utf-8")
        self.assertIn('license = "MIT"', pyproject_content)
        self.assertIn(
            'license-files = ["LICENSE", "NOTICE", "THIRD_PARTY_LICENSES.md", "THIRD_PARTY_LICENSES.txt"]',
            pyproject_content,
        )
        self.assertTrue((REPO_ROOT / "LICENSE").is_file(), "LICENSE file missing")
        self.assertTrue((REPO_ROOT / "NOTICE").is_file(), "NOTICE file missing")
        self.assertTrue((REPO_ROOT / "THIRD_PARTY_LICENSES.md").is_file(), "THIRD_PARTY_LICENSES.md file missing")
        self.assertTrue((REPO_ROOT / "THIRD_PARTY_LICENSES.txt").is_file(), "THIRD_PARTY_LICENSES.txt file missing")

    def test_level1_sbom_and_invariants_table(self) -> None:
        """Verify Level 1 SBOM, Invariants table, RunAsInvoker, and Zero-Copyleft in THIRD_PARTY_LICENSES.md."""
        tpl_content = (REPO_ROOT / "THIRD_PARTY_LICENSES.md").read_text(encoding="utf-8")
        self.assertIn("Level 1 Software Bill of Materials (SBOM)", tpl_content)
        self.assertIn("INV-LOCAL-01", tpl_content)
        self.assertIn("INV-SEC-02", tpl_content)
        self.assertIn("INV-FAIL-03", tpl_content)
        self.assertIn("INV-STG-04", tpl_content)
        self.assertIn("INV-HANDOFF-05", tpl_content)
        self.assertIn("INV-TIER-06", tpl_content)
        self.assertIn("INV-SYNC-07", tpl_content)
        self.assertIn("INV-AUDIT-08", tpl_content)
        self.assertIn("INV-LIC-09", tpl_content)
        self.assertIn("INV-SLA-10", tpl_content)
        self.assertIn("RunAsInvoker", tpl_content)
        self.assertIn("Zero-Copyleft Isolation Guarantee", tpl_content)

    def test_quick_navigation_18_points_parity(self) -> None:
        """Verify both README.md and README_de.md implement an 18-point quick navigation structure."""
        for filename in ["README.md", "README_de.md"]:
            content = (REPO_ROOT / filename).read_text(encoding="utf-8")
            nav_match = re.search(r"(?:### 🧭 Quick Navigation|### 🧭 Schnellnavigation)\s+((?:\d+\.\s+\[[^\]]+\]\(#[^\)]+\)\s*)+)", content)
            self.assertIsNotNone(nav_match, f"Quick navigation block not found in {filename}")
            nav_block = nav_match.group(1)
            links = re.findall(r"\d+\.\s+\[([^\]]+)\]\(#([^\)]+)\)", nav_block)
            self.assertEqual(len(links), 18, f"Expected exactly 18 quick nav links in {filename}, found {len(links)}")

    def test_mermaid_diagrams_syntax_and_semicolon_free(self) -> None:
        """Verify README Mermaid diagrams contain valid syntax, autonumber, and strictly zero semicolons."""
        for filename in ["README.md", "README_de.md"]:
            content = (REPO_ROOT / filename).read_text(encoding="utf-8")
            blocks = re.findall(r"```mermaid\s+(.+?)```", content, re.DOTALL)
            self.assertEqual(len(blocks), 2, f"Expected exactly 2 Mermaid blocks in {filename}, found {len(blocks)}")

            flowchart_block = blocks[0]
            self.assertTrue(
                "flowchart TD" in flowchart_block or "graph TD" in flowchart_block,
                f"First diagram in {filename} must be flowchart TD",
            )

            sequence_block = blocks[1]
            self.assertIn("sequenceDiagram", sequence_block, f"Second diagram in {filename} must be sequenceDiagram")
            self.assertIn("autonumber", sequence_block, f"Sequence diagram in {filename} must have autonumber")
            self.assertNotIn(";", sequence_block, f"Sequence diagram in {filename} must contain zero semicolons")

    def test_statutory_notice_521_bgb(self) -> None:
        """Verify statutory notice and limitation of liability under § 521 BGB in both READMEs."""
        en_content = self.readme_en_path.read_text(encoding="utf-8")
        de_content = self.readme_de_path.read_text(encoding="utf-8")

        self.assertIn("§ 521 BGB", en_content)
        self.assertIn("Gefälligkeit", en_content)
        self.assertIn("intent and gross negligence", en_content)

        self.assertIn("§ 521 BGB", de_content)
        self.assertIn("Gefälligkeit", de_content)
        self.assertIn("Vorsatz und grobe Fahrlässigkeit", de_content)

    def test_comparative_matrix_10_dimensions(self) -> None:
        """Verify all 10 invariant IDs are present across READMEs."""
        en_content = self.readme_en_path.read_text(encoding="utf-8")
        de_content = self.readme_de_path.read_text(encoding="utf-8")

        for inv in [
            "INV-LOCAL-01",
            "INV-SEC-02",
            "INV-FAIL-03",
            "INV-STG-04",
            "INV-HANDOFF-05",
            "INV-TIER-06",
            "INV-SYNC-07",
            "INV-AUDIT-08",
            "INV-LIC-09",
            "INV-SLA-10",
        ]:
            self.assertIn(inv, en_content, f"{inv} missing from README.md")
            self.assertIn(inv, de_content, f"{inv} missing from README_de.md")

    def test_ci_explicit_permissions_guard(self) -> None:
        """Verify CI workflows declare least-privilege explicit permissions."""
        ci_content = self.ci_workflow_path.read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", ci_content, "ci.yml must declare unprivileged contents: read")

        stale_content = (REPO_ROOT / ".github" / "workflows" / "stale.yml").read_text(encoding="utf-8")
        self.assertIn("issues: write", stale_content, "stale.yml must declare issues: write")
        self.assertIn("pull-requests: write", stale_content, "stale.yml must declare pull-requests: write")

    def test_extended_gitignore_patch_and_cache_defense(self) -> None:
        """Verify root and template gitignore include patch reject and temp debugging defenses."""
        for path in [REPO_ROOT / ".gitignore", REPO_ROOT / "template" / ".gitignore"]:
            content = path.read_text(encoding="utf-8")
            for pattern in ["*.rej", "*.tmp", "pytestdebug.log"]:
                self.assertIn(pattern, content, f"{path.name} must ignore {pattern}")

    def test_changelog_recent_pfad_a_entry(self) -> None:
        """Verify CHANGELOG.md documents recent Pfad A repository hygiene and CI security audit."""
        content = self.changelog_path.read_text(encoding="utf-8")
        self.assertIn("## 2026-09-25 - Pfad A", content, "CHANGELOG.md must contain 2026-09-25 Pfad A entry")

    def test_changelog_unreleased_pfad_b_entry(self) -> None:
        """Verify CHANGELOG.md documents Pfad B 2026-09-29 discoverability improvements."""
        content = self.changelog_path.read_text(encoding="utf-8")
        self.assertIn("## [Unreleased]", content, "CHANGELOG.md must contain ## [Unreleased] section")
        self.assertIn("2026-09-29", content, "CHANGELOG.md must contain 2026-09-29 entry")
        self.assertIn("ASCII Vier-Ansichten-Architekturprojektion", content)
        self.assertIn("Level 1 SBOM Plain-Text Companion", content)

    def test_bilateral_sec_navigation_anchors(self) -> None:
        """Verify README.md and README_de.md maintain bilateral sec-01..18 navigation anchors."""
        readme_en = self.readme_en_path.read_text(encoding="utf-8")
        readme_de = self.readme_de_path.read_text(encoding="utf-8")
        for i in range(1, 19):
            anchor = f'<a id="sec-{i:02d}"></a>'
            self.assertIn(anchor, readme_en, f"Missing anchor {anchor} in README.md")
            self.assertIn(anchor, readme_de, f"Missing anchor {anchor} in README_de.md")

    def test_ascii_four_view_topology_projection(self) -> None:
        """Verify README.md and README_de.md include the 4 architectural projection views."""
        readme_en = self.readme_en_path.read_text(encoding="utf-8")
        readme_de = self.readme_de_path.read_text(encoding="utf-8")

        # English README views
        self.assertIn("VIEW 1: CLI COCKPIT", readme_en)
        self.assertIn("VIEW 2: TIERED PROFILE ENGINE", readme_en)
        self.assertIn("VIEW 3: RUNTIME PERSISTENCE", readme_en)
        self.assertIn("VIEW 4: SECURITY BOUNDARY", readme_en)

        # German README views
        self.assertIn("SICHT 1: CLI-COCKPIT", readme_de)
        self.assertIn("SICHT 2: GESTAFFELTE PROFIL-ENGINE", readme_de)
        self.assertIn("SICHT 3: LAUFZEIT-PERSISTENZ", readme_de)
        self.assertIn("SICHT 4: SICHERHEITSPERIMETER", readme_de)

    def test_level1_sbom_plaintext_companion_contract(self) -> None:
        """Verify THIRD_PARTY_LICENSES.txt exists and meets all compliance invariants."""
        sbom_txt = REPO_ROOT / "THIRD_PARTY_LICENSES.txt"
        self.assertTrue(sbom_txt.is_file(), "Missing root THIRD_PARTY_LICENSES.txt")
        content = sbom_txt.read_text(encoding="utf-8")

        for inv in [
            "INV-LOCAL-01",
            "INV-SEC-02",
            "INV-FAIL-03",
            "INV-STG-04",
            "INV-HANDOFF-05",
            "INV-TIER-06",
            "INV-SYNC-07",
            "INV-AUDIT-08",
            "INV-LIC-09",
            "INV-SLA-10",
        ]:
            self.assertIn(inv, content, f"Missing invariant {inv} in THIRD_PARTY_LICENSES.txt")

        self.assertIn("RunAsInvoker", content)
        self.assertIn("Zero-Runtime-Dependency", content)
        self.assertIn("dependencies = []", content)
        self.assertIn("MIT License", content)
        self.assertIn("PSFL-2.0", content)
        self.assertIn("Apache License Version 2.0", content)
        self.assertIn("§ 521 BGB", content)

    def test_pep621_twenty_topics_saturation(self) -> None:
        """Verify pyproject.toml keywords list matches all 20 saturated GitHub topics."""
        pyproject = self.pyproject_path.read_text(encoding="utf-8")
        expected_topics = [
            "agent-ready",
            "antigravity",
            "claude-code",
            "codex",
            "developer-tools",
            "documentation-template",
            "documentation-tools",
            "ellmos",
            "ellmos-ai",
            "governance",
            "llm-agents",
            "llm-documentation",
            "local-first",
            "markdown",
            "multi-agent",
            "open-bricks",
            "project-docs",
            "project-template",
            "session-handoff",
            "zero-egress",
        ]
        self.assertEqual(len(expected_topics), 20)
        for topic in expected_topics:
            self.assertIn(f'"{topic}"', pyproject, f"Missing topic '{topic}' in pyproject.toml keywords")

    def test_marketing_log_recency_pfad_b(self) -> None:
        """Verify MARKETING-LOG.txt contains the 2026-09-29 Pfad B audit record."""
        mlog_path = REPO_ROOT / "MARKETING-LOG.txt"
        self.assertTrue(mlog_path.is_file(), "Missing MARKETING-LOG.txt")
        content = mlog_path.read_text(encoding="utf-8")
        self.assertIn("2026-09-29 — Pfad B", content)
        self.assertIn("ASCII 4-View Architecture Topology", content)
        self.assertIn("THIRD_PARTY_LICENSES.txt", content)


if __name__ == "__main__":
    unittest.main()
