from __future__ import annotations

import ast
import importlib.util
import os
import re
import subprocess
import sys
import tempfile
import unittest
from importlib.machinery import SourceFileLoader
from pathlib import Path
from unittest import mock
from urllib.parse import unquote


REPO = Path(__file__).resolve().parents[1]
TEMPLATE = REPO / "template"
INIT = TEMPLATE / "_tools" / "init-project"
DOC_LINT = TEMPLATE / "_tools" / "doc-lint"
TODO_ARCHIVE = TEMPLATE / "_tools" / "todo-archive"
WORKFLOWS_SYNC = TEMPLATE / "_tools" / "workflows-sync"
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
GENERATOR_PLACEHOLDERS = (
    "[project-name]", "[Projektname]", "[MINIMAL|STANDARD|FULL]",
    "[YYYY-MM-DD]", "[YYYY-MM-DD HH:MM]", "[author]",
)

PROFILE_ROOT_FILES = {
    "MINIMAL": {
        "AGENTS.md", "CLAUDE.md", "README.md", "START.md", "STATE.md",
        "TODO.md", "DONE.md", ".gitignore",
    },
    "STANDARD": {
        "AGENTS.md", "CLAUDE.md", "README.md", "START.md", "STATE.md",
        "CHANGELOG.md", "HEADER-RULES.md", "CUT-AND-CLUE.md",
        "DECISIONS.md", "PATTERNS.md", "TODO.md", "DONE.md", ".gitignore",
    },
    "FULL": {
        "CLAUDE.md", "AGENTS.md", "README.md", "START.md", "STATE.md",
        "ARCHITECTURE.md", "CHANGELOG.md", "HEADER-RULES.md",
        "CUT-AND-CLUE.md", "DECISIONS.md", "PATTERNS.md", "WORKFLOWS.md",
        "TOOLS.md", "TODO.md", "DONE.md", "GLOSSARY.md", ".gitignore",
    },
}


def run(*args: str | Path, cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [str(arg) for arg in args],
        cwd=cwd or REPO,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if check and result.returncode != 0:
        raise AssertionError(
            f"command failed ({result.returncode}): {' '.join(map(str, args))}\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return result


def load_script(name: str, path: Path):
    loader = SourceFileLoader(name, str(path))
    spec = importlib.util.spec_from_loader(name, loader)
    if spec is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


def assert_no_dead_markdown_links(testcase: unittest.TestCase, root: Path) -> None:
    for path in root.rglob("*.md"):
        content = path.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(content):
            link = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not link or link.startswith(("#", "http://", "https://", "mailto:")):
                continue
            relative = unquote(link.split("#", 1)[0].split("?", 1)[0])
            testcase.assertTrue(
                (path.parent / relative).resolve().exists(),
                f"dead link in {path.relative_to(root)}: {link}",
            )


def assert_markdown_structure(testcase: unittest.TestCase, root: Path) -> None:
    for path in root.rglob("*.md"):
        lines = path.read_text(encoding="utf-8").splitlines()
        fences = sum(line.lstrip().startswith("```") for line in lines)
        testcase.assertEqual(0, fences % 2, f"unbalanced code fence in {path.relative_to(root)}")
        for index, line in enumerate(lines):
            if line.strip() or index == 0 or not lines[index - 1].startswith("|"):
                continue
            next_nonempty = next(
                (candidate for candidate in lines[index + 1:] if candidate.strip()),
                "",
            )
            testcase.assertFalse(
                next_nonempty.startswith("|"),
                f"blank line splits Markdown table in {path.relative_to(root)}",
            )


class InitProjectTests(unittest.TestCase):
    def generate(self, base: Path, profile: str, *extra: str) -> Path:
        target = base / profile.lower()
        run(
            sys.executable, INIT,
            "--target", target,
            "--name", f"Example-{profile}",
            "--profile", profile,
            "--author", "CI Tester",
            *extra,
        )
        return target

    def test_all_profiles_are_self_consistent(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            for profile in PROFILE_ROOT_FILES:
                with self.subTest(profile=profile):
                    target = self.generate(base, profile)
                    actual_files = {path.name for path in target.iterdir() if path.is_file()}
                    self.assertEqual(PROFILE_ROOT_FILES[profile], actual_files)
                    for path in target.rglob("*"):
                        if not path.is_file() or path.suffix.lower() != ".md":
                            continue
                        content = path.read_text(encoding="utf-8")
                        for placeholder in GENERATOR_PLACEHOLDERS:
                            self.assertNotIn(placeholder, content, f"{path}: {placeholder}")
                    assert_no_dead_markdown_links(self, target)
                    assert_markdown_structure(self, target)
                    run(sys.executable, target / "_tools" / "doc-lint", "--root", target)
                    if profile == "FULL":
                        run(
                            sys.executable,
                            target / "_tools" / "workflows-sync",
                            "--root", target,
                            "--check",
                        )

    def test_git_option_creates_main_with_initial_commit(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = self.generate(Path(temp), "MINIMAL", "--git")
            self.assertEqual("main", run("git", "branch", "--show-current", cwd=target).stdout.strip())
            self.assertEqual(
                "docs: initialize project documentation",
                run("git", "log", "-1", "--pretty=%s", cwd=target).stdout.strip(),
            )
            self.assertFalse(run("git", "status", "--porcelain", cwd=target).stdout.strip())

    def test_author_fallback_never_leaves_template_placeholder(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "fallback"
            run(
                sys.executable, INIT,
                "--target", target,
                "--name", "Fallback",
                "--profile", "MINIMAL",
            )
            self.assertNotIn("[author]", (target / "CLAUDE.md").read_text(encoding="utf-8"))

    def test_quoted_metadata_is_yaml_safe(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "quoted"
            run(
                sys.executable, INIT,
                "--target", target,
                "--name", 'Project "Quoted"',
                "--profile", "MINIMAL",
                "--author", 'Ada "Ace" \\ Lovelace',
            )
            run(sys.executable, target / "_tools" / "doc-lint", "--root", target)
            content = (target / "CLAUDE.md").read_text(encoding="utf-8")
            self.assertIn(r'name: "Project \"Quoted\""', content)
            self.assertIn(r'author: "Ada \"Ace\" \\ Lovelace"', content)

    def test_nonempty_target_is_unchanged(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "occupied"
            target.mkdir()
            sentinel = target / "keep.txt"
            sentinel.write_text("untouched", encoding="utf-8")
            result = run(
                sys.executable, INIT,
                "--target", target,
                "--name", "Nope",
                check=False,
            )
            self.assertEqual(1, result.returncode)
            self.assertEqual("untouched", sentinel.read_text(encoding="utf-8"))
            self.assertEqual({"keep.txt"}, {path.name for path in target.iterdir()})

    def test_dry_run_does_not_create_target(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "dry"
            run(
                sys.executable, INIT,
                "--target", target,
                "--name", "Dry",
                "--dry-run",
                "--git",
            )
            self.assertFalse(target.exists())

    def test_multiline_metadata_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "unsafe"
            result = run(
                sys.executable, INIT,
                "--target", target,
                "--name", "Bad\nName",
                check=False,
            )
            self.assertEqual(1, result.returncode)
            self.assertFalse(target.exists())


class DocLintTests(unittest.TestCase):
    def test_canonical_template_is_recognized(self) -> None:
        result = run(sys.executable, DOC_LINT, "--root", TEMPLATE)
        self.assertIn("template-source", result.stdout)

    def test_fix_repairs_placeholder_and_rechecks(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "project"
            run(
                sys.executable, INIT,
                "--target", target,
                "--name", "LintFix",
                "--profile", "MINIMAL",
                "--author", "Tester",
            )
            claude = target / "CLAUDE.md"
            content = claude.read_text(encoding="utf-8").replace('author: "Tester"', 'author: "[author]"')
            claude.write_text(content, encoding="utf-8")
            result = run(sys.executable, target / "_tools" / "doc-lint", "--root", target, "--fix")
            self.assertIn("Re-checking", result.stdout)
            self.assertNotIn("[author]", claude.read_text(encoding="utf-8"))

    def test_fix_preserves_unknown_valid_frontmatter(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "project"
            run(
                sys.executable, INIT,
                "--target", target,
                "--name", "CustomHeader",
                "--profile", "MINIMAL",
                "--author", "Tester",
            )
            claude = target / "CLAUDE.md"
            content = claude.read_text(encoding="utf-8")
            content = re.sub(
                r'^reason_last_change:.*$',
                'custom_owner_data: "KEEP-ME"',
                content,
                count=1,
                flags=re.MULTILINE,
            )
            claude.write_text(content, encoding="utf-8")
            run(sys.executable, target / "_tools" / "doc-lint", "--root", target, "--fix")
            self.assertIn('custom_owner_data: "KEEP-ME"', claude.read_text(encoding="utf-8"))

    def test_fix_refuses_unparseable_yaml_without_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "project"
            run(
                sys.executable, INIT,
                "--target", target,
                "--name", "BrokenHeader",
                "--profile", "MINIMAL",
                "--author", "Tester",
            )
            claude = target / "CLAUDE.md"
            broken = claude.read_text(encoding="utf-8").replace(
                'author: "Tester"',
                'author: "Tester" broken\ncustom_owner_data: "KEEP-ME"',
            )
            claude.write_text(broken, encoding="utf-8")
            result = run(
                sys.executable,
                target / "_tools" / "doc-lint",
                "--root", target,
                "--fix",
                check=False,
            )
            self.assertEqual(1, result.returncode)
            self.assertEqual(broken, claude.read_text(encoding="utf-8"))


class WorkflowSyncTests(unittest.TestCase):
    def test_special_table_text_and_replacement_are_safe(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            workflows = root / "workflows"
            workflows.mkdir()
            (workflows / "special.md").write_text(
                "# Workflow: Back\\g | Pipe\n\n"
                "## Purpose\n\nUse \\g | safely.\n\n"
                "**Frequency:** now | later\n"
                "**Duration:** 5 \\ min\n",
                encoding="utf-8",
            )
            (workflows / "routine (safe).md").write_text(
                "# Workflow: Routine\n\n## Purpose\n\nSafe filename test.\n",
                encoding="utf-8",
            )
            (root / "WORKFLOWS.md").write_text(
                "# Router\n\n<!-- @auto-generated:workflow-index -->\nold\n"
                "<!-- @end:workflow-index -->\n",
                encoding="utf-8",
            )
            run(sys.executable, WORKFLOWS_SYNC, "--root", root)
            run(sys.executable, WORKFLOWS_SYNC, "--root", root, "--check")
            output = (root / "WORKFLOWS.md").read_text(encoding="utf-8")
            self.assertIn(r"Back\\g \| Pipe", output)
            self.assertIn(r"Use \\g \| safely.", output)
            self.assertIn("routine%20%28safe%29.md", output)
            assert_no_dead_markdown_links(self, root)


class TodoArchiveTests(unittest.TestCase):
    def test_apply_and_retry_are_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            todo = root / "TODO.md"
            done = root / "DONE.md"
            todo.write_text("# TODO\n\n- [x] finished\n- [ ] open\n", encoding="utf-8")
            run(sys.executable, TODO_ARCHIVE, "--todo", todo, "--done", done, "--apply")
            self.assertNotIn("finished", todo.read_text(encoding="utf-8"))
            first_done = done.read_text(encoding="utf-8")
            self.assertEqual(1, first_done.count("- [x] finished"))
            run(sys.executable, TODO_ARCHIVE, "--todo", todo, "--done", done, "--apply")
            self.assertEqual(first_done, done.read_text(encoding="utf-8"))

    def test_recurring_task_text_is_archived_again(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            todo = root / "TODO.md"
            done = root / "DONE.md"
            todo.write_text("# TODO\n\n- [x] run release checklist\n", encoding="utf-8")
            done.write_text(
                "# DONE\n\n## 2000-01-01\n\n- [x] run release checklist\n",
                encoding="utf-8",
            )
            run(sys.executable, TODO_ARCHIVE, "--todo", todo, "--done", done, "--apply")
            self.assertEqual(
                2,
                done.read_text(encoding="utf-8").count("- [x] run release checklist"),
            )

    def test_same_path_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "tasks.md"
            path.write_text("- [x] done\n", encoding="utf-8")
            result = run(
                sys.executable, TODO_ARCHIVE,
                "--todo", path,
                "--done", path,
                "--apply",
                check=False,
            )
            self.assertEqual(2, result.returncode)
            self.assertEqual("- [x] done\n", path.read_text(encoding="utf-8"))

    def test_second_replace_failure_rolls_back_both_files(self) -> None:
        module = load_script("todo_archive_for_test", TODO_ARCHIVE)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            todo = root / "TODO.md"
            done = root / "DONE.md"
            original_todo = "# TODO\n- [x] finished\n"
            original_done = "# DONE\n"
            todo.write_text(original_todo, encoding="utf-8")
            done.write_text(original_done, encoding="utf-8")
            real_replace = module.os.replace
            failed = False

            def fail_todo_once(src, dst):
                nonlocal failed
                if Path(dst) == todo and not failed:
                    failed = True
                    raise OSError("injected second replace failure")
                return real_replace(src, dst)

            with mock.patch.object(module.os, "replace", side_effect=fail_todo_once):
                with self.assertRaises(RuntimeError):
                    module.commit_pair(
                        todo,
                        original_todo,
                        "# TODO\n",
                        done,
                        original_done,
                        "# DONE\n- [x] finished\n",
                    )
            self.assertEqual(original_todo, todo.read_text(encoding="utf-8"))
            self.assertEqual(original_done, done.read_text(encoding="utf-8"))

    def test_process_crash_is_completed_from_journal(self) -> None:
        module = load_script("todo_archive_crash_test", TODO_ARCHIVE)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            todo = root / "TODO.md"
            done = root / "DONE.md"
            original_todo = "# TODO\n- [x] finished\n"
            original_done = "# DONE\n"
            new_todo = "# TODO\n"
            new_done = module.append_to_done(original_done, ["- [x] finished"], "2026-07-17")
            todo.write_text(original_todo, encoding="utf-8")
            done.write_text(original_done, encoding="utf-8")
            real_replace = module.os.replace
            crashed = False

            def crash_on_todo(src, dst):
                nonlocal crashed
                if Path(dst) == todo and not crashed:
                    crashed = True
                    raise SystemExit("injected process crash")
                return real_replace(src, dst)

            with mock.patch.object(module.os, "replace", side_effect=crash_on_todo):
                with self.assertRaises(SystemExit):
                    module.commit_pair(
                        todo,
                        original_todo,
                        new_todo,
                        done,
                        original_done,
                        new_done,
                    )

            self.assertEqual(original_todo, todo.read_text(encoding="utf-8"))
            self.assertEqual(new_done, done.read_text(encoding="utf-8"))
            self.assertTrue(module.journal_path(todo, done).exists())
            run(sys.executable, TODO_ARCHIVE, "--todo", todo, "--done", done, "--apply")
            self.assertEqual(new_todo, todo.read_text(encoding="utf-8"))
            self.assertEqual(1, done.read_text(encoding="utf-8").count("- [x] finished"))
            self.assertFalse(module.journal_path(todo, done).exists())


class SourceSyntaxTests(unittest.TestCase):
    def test_extensionless_python_tools_parse(self) -> None:
        for path in (INIT, DOC_LINT, TODO_ARCHIVE, WORKFLOWS_SYNC):
            with self.subTest(tool=path.name):
                ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


if __name__ == "__main__":
    unittest.main()
