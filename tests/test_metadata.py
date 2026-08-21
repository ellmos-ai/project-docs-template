from __future__ import annotations

import json
import re
import unittest
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
        self.assertIn("2026-08-21", content, "llms.txt must reflect current verification date 2026-08-21")
        self.assertIn("https://github.com/ellmos-ai/project-docs-template", content)
        self.assertIn("## Search Phrases", content)
        self.assertIn("## Disambiguation", content)
        self.assertIn("Primary audience:", content)

    def test_readme_bilingual_structural_parity(self) -> None:
        en_content = self.readme_en_path.read_text(encoding="utf-8")
        de_content = self.readme_de_path.read_text(encoding="utf-8")

        # Badges
        for badge_pattern in ["pytest", "license-MIT", "Language-", "Ecosystem-ellmos", "Umbrella-open", "LLM--Ready"]:
            self.assertIn(badge_pattern, en_content, f"Badge {badge_pattern} missing in README.md")
            self.assertIn(badge_pattern, de_content, f"Badge {badge_pattern} missing in README_de.md")

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
        self.assertIn("Zero-Egress", content, "SECURITY.md missing Zero-Egress invariant")
        self.assertIn("Local-First", content, "SECURITY.md missing Local-First invariant")

    def test_sibling_tools_ecosystem_matrix(self) -> None:
        en_content = self.readme_en_path.read_text(encoding="utf-8")
        de_content = self.readme_de_path.read_text(encoding="utf-8")

        key_siblings = [
            "policy-registry",
            "automation-master",
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
        self.assertIn("3.13", ci_content)

        pyproject_content = self.pyproject_path.read_text(encoding="utf-8")
        self.assertIn("[tool.ruff]", pyproject_content)
        self.assertIn("[tool.ruff.lint]", pyproject_content)

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


if __name__ == "__main__":
    unittest.main()
