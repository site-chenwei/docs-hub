from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills" / "docs-hub"
BUILD_SCRIPT = SKILL_ROOT / "scripts" / "build_docset_index.py"
SEARCH_SCRIPT = SKILL_ROOT / "scripts" / "search_docs.py"
INIT_SCRIPT = SKILL_ROOT / "scripts" / "local_doc_init.py"


class DocsHubSearchSkillTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._shared_tmpdir = tempfile.TemporaryDirectory()
        cls.shared_hub_root = Path(cls._shared_tmpdir.name)
        (cls.shared_hub_root / "docs" / "bootstrap").mkdir(parents=True, exist_ok=True)
        (cls.shared_hub_root / "index").mkdir(parents=True, exist_ok=True)
        (cls.shared_hub_root / "docsets.json").write_text(
            json.dumps(
                {
                    "version": 1,
                    "defaults": {
                        "include": ["*.md", "**/*.md"],
                        "exclude": [],
                        "section_from": ["menu_path[0]", "rel_path[0]"],
                        "doc_type_rules": [],
                        "nav_rules": {
                            "filenames": ["README.md", "catalog.md", "index.md"],
                            "min_body_chars": 300,
                        },
                        "chunk": {
                            "target_chars": 1200,
                            "max_chars": 1500,
                            "overlap_chars": 150,
                        },
                    },
                    "docsets": [
                        {
                            "id": "bootstrap",
                            "name": "Bootstrap",
                            "root": "docs/bootstrap",
                        }
                    ],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        subprocess.run(
            ["python3", str(INIT_SCRIPT), "--skill-root", str(SKILL_ROOT), "--hub-root", str(cls.shared_hub_root)],
            check=True,
            capture_output=True,
            text=True,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls._shared_tmpdir.cleanup()

    def make_hub(self) -> Path:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        hub_root = Path(tmpdir.name)
        (hub_root / "docs" / "testset").mkdir(parents=True, exist_ok=True)
        (hub_root / "index").mkdir(parents=True, exist_ok=True)
        (hub_root / "docsets.json").write_text(
            json.dumps(
                {
                    "version": 1,
                    "defaults": {
                        "include": ["*.md", "**/*.md"],
                        "exclude": [],
                        "section_from": ["menu_path[0]", "rel_path[0]"],
                        "doc_type_rules": [],
                        "nav_rules": {
                            "filenames": ["README.md", "catalog.md", "index.md"],
                            "min_body_chars": 300,
                        },
                        "chunk": {
                            "target_chars": 1200,
                            "max_chars": 1500,
                            "overlap_chars": 150,
                        },
                    },
                    "docsets": [
                        {
                            "id": "testset",
                            "name": "Test",
                            "root": "docs/testset",
                        }
                    ],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        return hub_root

    def write_doc(self, hub_root: Path, rel_path: str, content: str) -> Path:
        path = hub_root / "docs" / "testset" / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")
        return path

    def run_build(self, hub_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python3", str(BUILD_SCRIPT), "--hub-root", str(hub_root), "--docset", "testset", *args],
            check=True,
            capture_output=True,
            text=True,
        )

    def run_search(self, hub_root: Path, *args: str) -> list[dict]:
        proc = subprocess.run(
            ["python3", str(SEARCH_SCRIPT), "--hub-root", str(hub_root), *args, "--json"],
            check=True,
            capture_output=True,
            text=True,
        )
        return json.loads(proc.stdout)

    def test_explicit_query_hub_root_overrides_saved_init_hub_root(self) -> None:
        hub_root = self.make_hub()
        self.write_doc(
            hub_root,
            "root.md",
            """
            ---
            title: "root doc"
            source_url: "https://example.com/root"
            menu_path:
              - "指南"
            ---

            # root doc

            hello root file
            """,
        )
        self.run_build(hub_root)
        proc = subprocess.run(
            ["python3", str(SEARCH_SCRIPT), "--hub-root", str(hub_root), "hello", "--docset", "testset", "--json"],
            check=True,
            capture_output=True,
            text=True,
        )
        rows = json.loads(proc.stdout)
        self.assertEqual(["root.md"], [row["rel_path"] for row in rows])
        self.assertTrue(rows[0]["abs_path"].endswith("/docs/testset/root.md"))

    def test_rebuild_stale_refreshes_existing_index(self) -> None:
        hub_root = self.make_hub()
        doc_path = self.write_doc(
            hub_root,
            "sub/a.md",
            """
            ---
            title: "alpha"
            source_url: "https://example.com/a"
            menu_path:
              - "指南"
            ---

            # alpha

            original content
            """,
        )
        self.run_build(hub_root)
        doc_path.write_text(
            textwrap.dedent(
                """
                ---
                title: "alpha"
                source_url: "https://example.com/a"
                menu_path:
                  - "指南"
                ---

                # alpha

                updated content only
                """
            ).lstrip(),
            encoding="utf-8",
        )

        rows = self.run_search(hub_root, "--rebuild-stale", "updated", "--docset", "testset")
        self.assertEqual(["sub/a.md"], [row["rel_path"] for row in rows])

    def test_short_tokens_respect_or_semantics(self) -> None:
        hub_root = self.make_hub()
        self.write_doc(
            hub_root,
            "sub/a.md",
            """
            ---
            title: "doc-a"
            source_url: "https://example.com/a"
            menu_path:
              - "FAQ"
            ---

            # doc-a

            光标
            """,
        )
        self.write_doc(
            hub_root,
            "sub/b.md",
            """
            ---
            title: "doc-b"
            source_url: "https://example.com/b"
            menu_path:
              - "FAQ"
            ---

            # doc-b

            跟随
            """,
        )
        self.run_build(hub_root)
        rows = self.run_search(hub_root, "光标", "跟随", "--match", "or", "--docset", "testset")
        self.assertEqual(["sub/a.md", "sub/b.md"], [row["rel_path"] for row in rows])

    def test_code_fence_fake_heading_is_ignored(self) -> None:
        hub_root = self.make_hub()
        self.write_doc(
            hub_root,
            "sub/code-fence.md",
            """
            ---
            title: "Code Fence"
            source_url: "https://example.com/code-fence"
            menu_path:
              - "指南"
            ---

            # Real Heading

            ```md
            # fake heading
            codesentinel
            ```

            ## Later

            later-sentinel
            """,
        )
        self.run_build(hub_root)
        rows = self.run_search(hub_root, "codesentinel", "--docset", "testset")
        self.assertEqual(["sub/code-fence.md"], [row["rel_path"] for row in rows])
        self.assertEqual("Real Heading", rows[0]["heading_path"])

    def test_init_fails_without_resolvable_hub_root(self) -> None:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        proc = subprocess.run(
            ["python3", str(INIT_SCRIPT), "--skill-root", str(SKILL_ROOT)],
            check=False,
            cwd=tmpdir.name,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(0, proc.returncode)
        self.assertIn("未找到可用的 DocsHub 根目录", proc.stderr)

    def test_init_with_explicit_invalid_hub_root_fails_immediately(self) -> None:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        invalid_root = Path(tmpdir.name) / "not-a-hub"
        invalid_root.mkdir(parents=True, exist_ok=True)
        valid_hub = self.make_hub()
        proc = subprocess.run(
            ["python3", str(INIT_SCRIPT), "--skill-root", str(SKILL_ROOT), "--hub-root", str(invalid_root)],
            check=False,
            capture_output=True,
            text=True,
            env={"CODEX_DOC_HUB": str(valid_hub), **dict(os.environ)},
        )
        self.assertNotEqual(0, proc.returncode)
        self.assertIn("指定路径不是有效的 DocsHub 根目录", proc.stderr)

    def test_init_auto_builds_missing_indexes(self) -> None:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        isolated_skill_root = Path(tmpdir.name) / "docs-hub"
        shutil.copytree(SKILL_ROOT, isolated_skill_root)
        hub_root = self.make_hub()
        self.write_doc(
            hub_root,
            "sub/auto.md",
            """
            ---
            title: "auto build"
            source_url: "https://example.com/auto"
            menu_path:
              - "指南"
            ---

            # auto build

            content for auto build
            """,
        )
        subprocess.run(
            ["python3", str(isolated_skill_root / "scripts" / "local_doc_init.py"), "--skill-root", str(isolated_skill_root), "--hub-root", str(hub_root)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertTrue((hub_root / "index" / "testset.sqlite").exists())

    def test_init_accepts_workspace_root_with_nested_docsearch(self) -> None:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        isolated_skill_root = Path(tmpdir.name) / "docs-hub"
        shutil.copytree(SKILL_ROOT, isolated_skill_root)
        workspace_root = Path(tmpdir.name) / "workspace"
        hub_root = workspace_root / "doc-search"
        (hub_root / "docs" / "testset").mkdir(parents=True, exist_ok=True)
        (hub_root / "index").mkdir(parents=True, exist_ok=True)
        (hub_root / "docsets.json").write_text(
            json.dumps(
                {
                    "version": 1,
                    "defaults": {
                        "include": ["*.md", "**/*.md"],
                        "exclude": [],
                        "section_from": ["menu_path[0]", "rel_path[0]"],
                        "doc_type_rules": [],
                        "nav_rules": {"filenames": ["README.md"], "min_body_chars": 300},
                        "chunk": {"target_chars": 1200, "max_chars": 1500, "overlap_chars": 150},
                    },
                    "docsets": [{"id": "testset", "name": "Test", "root": "docs/testset"}],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        subprocess.run(
            ["python3", str(isolated_skill_root / "scripts" / "local_doc_init.py"), "--skill-root", str(isolated_skill_root), "--hub-root", str(workspace_root)],
            check=True,
            capture_output=True,
            text=True,
        )
        state = json.loads((isolated_skill_root / ".skill-init.json").read_text(encoding="utf-8"))
        self.assertEqual(str(hub_root.resolve()), state["hub_root"])

    def test_missing_skill_init_mentions_doc_hub_init(self) -> None:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        isolated_skill_root = Path(tmpdir.name) / "docs-hub"
        shutil.copytree(SKILL_ROOT, isolated_skill_root)
        init_state = isolated_skill_root / ".skill-init.json"
        if init_state.exists():
            init_state.unlink()
        hub_root = self.make_hub()
        proc = subprocess.run(
            ["python3", str(isolated_skill_root / "scripts" / "search_docs.py"), "--hub-root", str(hub_root), "输入法"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(0, proc.returncode)
        self.assertIn("$docs-hub init", proc.stderr)

    def test_query_prefers_saved_init_hub_root(self) -> None:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        isolated_skill_root = Path(tmpdir.name) / "docs-hub"
        shutil.copytree(SKILL_ROOT, isolated_skill_root)
        hub_root = self.make_hub()
        self.write_doc(
            hub_root,
            "sub/a.md",
            """
            ---
            title: "alpha"
            source_url: "https://example.com/a"
            menu_path:
              - "指南"
            ---

            # alpha

            reusable content
            """,
        )
        subprocess.run(
            ["python3", str(isolated_skill_root / "scripts" / "local_doc_init.py"), "--skill-root", str(isolated_skill_root), "--hub-root", str(hub_root)],
            check=True,
            capture_output=True,
            text=True,
        )
        proc = subprocess.run(
            ["python3", str(isolated_skill_root / "scripts" / "search_docs.py"), "reusable", "--docset", "testset", "--json"],
            check=True,
            capture_output=True,
            text=True,
            cwd=tmpdir.name,
        )
        rows = json.loads(proc.stdout)
        self.assertEqual(["sub/a.md"], [row["rel_path"] for row in rows])

    def test_refresh_prefers_saved_init_hub_root(self) -> None:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        isolated_skill_root = Path(tmpdir.name) / "docs-hub"
        shutil.copytree(SKILL_ROOT, isolated_skill_root)
        hub_root = self.make_hub()
        doc_path = self.write_doc(
            hub_root,
            "sub/a.md",
            """
            ---
            title: "alpha"
            source_url: "https://example.com/a"
            menu_path:
              - "指南"
            ---

            # alpha

            original refresh content
            """,
        )
        subprocess.run(
            ["python3", str(isolated_skill_root / "scripts" / "local_doc_init.py"), "--skill-root", str(isolated_skill_root), "--hub-root", str(hub_root)],
            check=True,
            capture_output=True,
            text=True,
        )
        doc_path.write_text(
            textwrap.dedent(
                """
                ---
                title: "alpha"
                source_url: "https://example.com/a"
                menu_path:
                  - "指南"
                ---

                # alpha

                refreshed content only
                """
            ).lstrip(),
            encoding="utf-8",
        )
        proc = subprocess.run(
            ["python3", str(isolated_skill_root / "scripts" / "search_docs.py"), "--rebuild-stale", "refreshed", "--docset", "testset", "--json"],
            check=True,
            capture_output=True,
            text=True,
            cwd=tmpdir.name,
        )
        rows = json.loads(proc.stdout)
        self.assertEqual(["sub/a.md"], [row["rel_path"] for row in rows])


if __name__ == "__main__":
    unittest.main()
