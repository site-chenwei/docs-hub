from __future__ import annotations

import json
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = REPO_ROOT / "scripts" / "build_docset_index.py"
SEARCH_SCRIPT = REPO_ROOT / "scripts" / "search_docs.py"
INIT_SCRIPT = REPO_ROOT / "scripts" / "local_doc_init.py"
INIT_STATE = REPO_ROOT / ".local-doc-init.json"
REQ_FILE = REPO_ROOT / "requirements-build.txt"


class DocsHubScriptsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            ["python3", str(INIT_SCRIPT), "--hub-root", str(REPO_ROOT)],
            check=True,
            capture_output=True,
            text=True,
        )
        cls.shared_init_state = json.loads(INIT_STATE.read_text(encoding="utf-8"))

    def make_hub(self) -> Path:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        hub_root = Path(tmpdir.name)
        (hub_root / "docs" / "testset").mkdir(parents=True, exist_ok=True)
        (hub_root / "index").mkdir(parents=True, exist_ok=True)
        (hub_root / "requirements-build.txt").write_text(REQ_FILE.read_text(encoding="utf-8"), encoding="utf-8")
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
        init_state = dict(self.shared_init_state)
        init_state["hub_root"] = str(hub_root)
        (hub_root / ".local-doc-init.json").write_text(
            json.dumps(init_state, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return hub_root

    def write_doc(self, hub_root: Path, rel_path: str, content: str) -> Path:
        path = hub_root / "docs" / "testset" / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")
        return path

    def run_build(self, hub_root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python3", str(BUILD_SCRIPT), "--hub-root", str(hub_root), "--docset", "testset"],
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

    def test_missing_init_prompts_user_to_initialize(self) -> None:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        hub_root = Path(tmpdir.name)
        (hub_root / "docs").mkdir(parents=True, exist_ok=True)
        (hub_root / "requirements-build.txt").write_text(REQ_FILE.read_text(encoding="utf-8"), encoding="utf-8")
        (hub_root / "docsets.json").write_text(json.dumps({"version": 1, "defaults": {}, "docsets": []}), encoding="utf-8")

        proc = subprocess.run(
            ["python3", str(SEARCH_SCRIPT), "--hub-root", str(hub_root), "输入法"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(0, proc.returncode)
        self.assertIn("请先手动运行", proc.stderr)

    def test_root_level_markdown_is_indexed(self) -> None:
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

        results = self.run_search(hub_root, "hello", "--docset", "testset")
        self.assertEqual(["root.md"], [item["rel_path"] for item in results])

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

        results = self.run_search(hub_root, "--rebuild-stale", "updated", "--docset", "testset")
        self.assertEqual(["sub/a.md"], [item["rel_path"] for item in results])

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

        results = self.run_search(hub_root, "光标", "跟随", "--match", "or", "--docset", "testset")
        self.assertEqual(["sub/a.md", "sub/b.md"], [item["rel_path"] for item in results])

    def test_short_tokens_can_match_title_and_symbols(self) -> None:
        hub_root = self.make_hub()
        self.write_doc(
            hub_root,
            "sub/ui-guide.md",
            """
            ---
            title: "UI 规范"
            source_url: "https://example.com/ui"
            menu_path:
              - "指南"
            ---

            # 设计系统

            This page talks about design systems.
            """,
        )
        self.run_build(hub_root)

        results = self.run_search(hub_root, "UI", "--docset", "testset")
        self.assertEqual(["sub/ui-guide.md"], [item["rel_path"] for item in results])

    def test_short_body_without_menu_path_is_marked_as_nav(self) -> None:
        hub_root = self.make_hub()
        self.write_doc(
            hub_root,
            "sub/nav.md",
            """
            ---
            title: "临时目录"
            source_url: "https://example.com/nav"
            ---

            # 临时目录

            navmarker
            """,
        )
        self.run_build(hub_root)

        default_results = self.run_search(hub_root, "navmarker", "--docset", "testset")
        self.assertEqual([], default_results)

        include_nav_results = self.run_search(
            hub_root,
            "navmarker",
            "--docset",
            "testset",
            "--include-nav",
        )
        self.assertEqual(["sub/nav.md"], [item["rel_path"] for item in include_nav_results])

    def test_markdown_it_ignores_fake_headings_inside_code_fence(self) -> None:
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

        results = self.run_search(hub_root, "codesentinel", "--docset", "testset")
        self.assertEqual(["sub/code-fence.md"], [item["rel_path"] for item in results])
        self.assertEqual("Real Heading", results[0]["heading_path"])


if __name__ == "__main__":
    unittest.main()
