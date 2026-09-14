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

        self.assertIn("## Target Personas & Core Use Cases", en_content)
        self.assertIn("Multi-Agent Systems Engineers", en_content)
        self.assertIn("Solo Developers & Open-Source Maintainers", en_content)
        self.assertIn("Enterprise Architecture & AI Governance Leads", en_content)
        self.assertIn("Research & Scientific Pipeline Developers", en_content)

        self.assertIn("## Zielgruppen & Kern-Anwendungsfälle", de_content)
        self.assertIn("Multi-Agenten Flotten-Ingenieure", de_content)
        self.assertIn("Solo-Entwickler & Open-Source-Maintainer", de_content)
        self.assertIn("Enterprise Architecture & AI Compliance Leads", de_content)
        self.assertIn("Forschungs- & Pipeline-Entwickler", de_content)

    def test_comparative_architecture_matrix(self) -> None:
        """Verify Comparative Architecture table in both English and German READMEs."""
        en_content = self.readme_en_path.read_text(encoding="utf-8")
        de_content = self.readme_de_path.read_text(encoding="utf-8")

        self.assertIn("## Comparative Architecture", en_content)
        self.assertIn("Generic Markdown Dumps", en_content)
        self.assertIn("Heavy SaaS Wikis", en_content)
        self.assertIn("Rigid Agent Frameworks", en_content)

        self.assertIn("## Architekturvergleich", de_content)
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
        ]
        for pattern in expected_patterns:
            self.assertIn(pattern, content, f"Template .gitignore must defend against {pattern}")

    def test_pyproject_pytest_addopts_and_bug_tracker(self) -> None:
        """Verify pyproject.toml contains standard pytest addopts and Bug Tracker URL."""
        content = self.pyproject_path.read_text(encoding="utf-8")
        self.assertIn('addopts = "-ra -v"', content, "pyproject.toml must configure addopts = '-ra -v'")
        self.assertIn('"Bug Tracker" =', content, "pyproject.toml must contain Bug Tracker URL")


if __name__ == "__main__":
    unittest.main()
