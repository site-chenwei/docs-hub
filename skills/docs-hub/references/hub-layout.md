# DocsHub Layout

The bundled scripts expect an external DocsHub root with this shape:

```text
<hub-root>/
├── docsets.json
├── docs/
│   └── <docset folders>
└── index/                 # created on demand
```

## `docsets.json`

Minimal shape:

```json
{
  "version": 1,
  "defaults": {
    "include": ["*.md", "**/*.md"],
    "exclude": ["**/*:Zone.Identifier", "**/README.md", "**/catalog.md"],
    "section_from": ["menu_path[0]", "rel_path[0]"],
    "doc_type_rules": [],
    "nav_rules": {
      "filenames": ["README.md", "catalog.md", "index.md"],
      "min_body_chars": 300
    },
    "chunk": {
      "target_chars": 1200,
      "max_chars": 1500,
      "overlap_chars": 150
    }
  },
  "docsets": [
    {
      "id": "example",
      "name": "Example Docs",
      "root": "docs/example"
    }
  ]
}
```

## Commands

Read-only search:

```bash
python3 <skill_root>/scripts/search_docs.py --hub-root <hub_root> 输入法 --top 8
python3 <skill_root>/scripts/search_docs.py --hub-root <hub_root> 光标 跟随 --match all --docset harmonyos --top 5
```

Refresh only on explicit user request:

```bash
python3 <skill_root>/scripts/search_docs.py --hub-root <hub_root> --rebuild-stale 输入法 --top 8
python3 <skill_root>/scripts/build_docset_index.py --hub-root <hub_root> --docset harmonyos
```

## Notes

- Search results include `abs_path`, which is the path to open for verification.
- The skill bundle keeps its own `.deps/` and init state; do not write initialization state into the external hub.
