"""为外部 DocsHub 的单个 docset 构建 SQLite FTS5 索引。

索引布局：
    index/<docset_id>.sqlite
        documents      — 每篇文档一行（rel_path, title, section, doc_type, source_url, is_nav, sha256, mtime）
        chunks (FTS5)  — 每块一行（title, symbols, body, doc_id, chunk_idx）tokenize=trigram

增量规则：按 rel_path 的 mtime+sha256 判断是否变更；未变更跳过分块/入库。
过滤规则：
    - 排除 *:Zone.Identifier、catalog.md、README.md（源自 docsets.json.defaults.exclude）
    - nav 页仍入库但打 is_nav=1，默认 search 时过滤；加 --include-nav 可带出

用法：
    python3 scripts/build_docset_index.py --hub-root /path/to/hub --docset harmonyos
    python3 scripts/build_docset_index.py --docset all --rebuild
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import sys
import time
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from _bootstrap import ensure_initialized, resolve_query_hub_root  # noqa: E402
from _common import (  # noqa: E402
    FrontMatterError,
    WarningSink,
    derive_doc_type,
    derive_section,
    extract_symbols,
    is_nav_page,
    load_docsets,
    parse_front_matter,
    read_text_safely,
    sha256_text,
    split_markdown,
)


SCHEMA = """
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY,
    rel_path TEXT NOT NULL UNIQUE,
    title TEXT,
    section TEXT,
    doc_type TEXT,
    source_url TEXT,
    is_nav INTEGER NOT NULL DEFAULT 0,
    mtime REAL,
    size INTEGER,
    sha256 TEXT,
    chunk_count INTEGER NOT NULL DEFAULT 0
);

CREATE INDEX IF NOT EXISTS idx_documents_section ON documents(section);
CREATE INDEX IF NOT EXISTS idx_documents_doctype ON documents(doc_type);
CREATE INDEX IF NOT EXISTS idx_documents_isnav ON documents(is_nav);

CREATE VIRTUAL TABLE IF NOT EXISTS chunks USING fts5(
    title,
    symbols,
    body,
    doc_id UNINDEXED,
    chunk_idx UNINDEXED,
    tokenize = 'trigram'
);

CREATE TABLE IF NOT EXISTS meta (
    key TEXT PRIMARY KEY,
    value TEXT
);
"""

BUILD_LOGIC_VERSION = "4"


def compile_pathspec(patterns: list[str]):
    from pathspec import PathSpec

    return PathSpec.from_lines("gitwildmatch", patterns)


def match_any(rel: str, patterns: list[str]) -> bool:
    return compile_pathspec(patterns).match_file(rel)


def iter_candidate_files(root: Path, includes: list[str], excludes: list[str]):
    include_spec = compile_pathspec(includes)
    exclude_spec = compile_pathspec(excludes)
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        # 用相对于 root 的 posix 路径做 glob 匹配
        rel = p.relative_to(root).as_posix()
        if not include_spec.match_file(rel):
            continue
        # 兜底：再次显式过滤掉 Zone.Identifier（即便 includes 没限制）
        if rel.endswith(":Zone.Identifier"):
            continue
        if exclude_spec.match_file(rel):
            continue
        yield p


def merge_config(defaults: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    out = dict(defaults)
    for k, v in override.items():
        if k in ("include", "exclude") and isinstance(v, list) and isinstance(defaults.get(k), list):
            out[k] = defaults[k] + v
        else:
            out[k] = v
    return out


def compute_build_signature(cfg: dict[str, Any]) -> str:
    payload = {
        "build_logic_version": BUILD_LOGIC_VERSION,
        "config": cfg,
    }
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    return conn


def meta_value(conn: sqlite3.Connection, key: str) -> str | None:
    row = conn.execute("SELECT value FROM meta WHERE key=?", (key,)).fetchone()
    return row[0] if row else None


def existing_sha(conn: sqlite3.Connection, rel_path: str) -> tuple[int | None, str | None]:
    cur = conn.execute("SELECT id, sha256 FROM documents WHERE rel_path=?", (rel_path,))
    row = cur.fetchone()
    return (row[0], row[1]) if row else (None, None)


def upsert_document(
    conn: sqlite3.Connection,
    rel_path: str,
    title: str,
    section: str,
    doc_type: str,
    source_url: str,
    is_nav: bool,
    mtime: float,
    size: int,
    sha: str,
    chunk_count: int,
) -> int:
    cur = conn.execute(
        """
        INSERT INTO documents(rel_path, title, section, doc_type, source_url, is_nav, mtime, size, sha256, chunk_count)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(rel_path) DO UPDATE SET
            title=excluded.title,
            section=excluded.section,
            doc_type=excluded.doc_type,
            source_url=excluded.source_url,
            is_nav=excluded.is_nav,
            mtime=excluded.mtime,
            size=excluded.size,
            sha256=excluded.sha256,
            chunk_count=excluded.chunk_count
        RETURNING id
        """,
        (rel_path, title, section, doc_type, source_url, int(is_nav), mtime, size, sha, chunk_count),
    )
    return cur.fetchone()[0]


def delete_chunks(conn: sqlite3.Connection, doc_id: int) -> None:
    conn.execute("DELETE FROM chunks WHERE doc_id=?", (doc_id,))


def build_docset(hub_root: Path, docset: dict[str, Any], defaults: dict[str, Any], rebuild: bool) -> dict[str, Any]:
    cfg = merge_config(defaults, docset)
    root = hub_root / docset["root"]
    if not root.exists():
        raise SystemExit(f"docset root 不存在: {root}")

    db_path = hub_root / "index" / f"{docset['id']}.sqlite"
    warn_path = hub_root / "index" / f"{docset['id']}.warnings.jsonl"

    if rebuild and db_path.exists():
        db_path.unlink()
        for suffix in ("-wal", "-shm"):
            extra = db_path.with_name(db_path.name + suffix)
            if extra.exists():
                extra.unlink()

    conn = connect(db_path)
    warn = WarningSink(warn_path)
    build_signature = compute_build_signature(cfg)
    force_reindex = rebuild or meta_value(conn, "build_signature") != build_signature

    stats = {"scanned": 0, "indexed": 0, "skipped_unchanged": 0, "failed": 0, "nav": 0, "warnings": 0}
    t0 = time.time()

    # 收集磁盘上现存的 rel_path 集合，末尾清理已删除文档
    seen_rel: set[str] = set()

    for path in iter_candidate_files(root, cfg["include"], cfg["exclude"]):
        stats["scanned"] += 1
        rel = path.relative_to(root).as_posix()
        seen_rel.add(rel)

        text, err = read_text_safely(path)
        if text is None:
            warn.add(rel, "read_error", err or "")
            stats["failed"] += 1
            continue

        sha = sha256_text(text)
        doc_id, prev_sha = existing_sha(conn, rel)
        if doc_id is not None and prev_sha == sha and not force_reindex:
            stats["skipped_unchanged"] += 1
            continue

        fm: dict[str, Any] = {}
        try:
            fm, body = parse_front_matter(text)
        except FrontMatterError as e:
            warn.add(rel, "front_matter_error", str(e))
            body = text  # 降级：整篇当 body
            stats["warnings"] += 1

        title = str(fm.get("title") or "").strip()
        if not title:
            # 从首个 # 标题派生
            for line in body.splitlines():
                line = line.strip()
                if line.startswith("# "):
                    title = line[2:].strip()
                    break
            if not title:
                title = Path(rel).stem
                warn.add(rel, "missing_title", f"fallback to filename stem: {title}")
                stats["warnings"] += 1

        source_url = str(fm.get("source_url") or "").strip()
        if not source_url:
            warn.add(rel, "missing_source_url", "")
            stats["warnings"] += 1

        rel_path_obj = Path(rel)
        section = derive_section(fm, rel_path_obj, cfg.get("section_from", ["menu_path[0]", "rel_path[0]"]))
        doc_type = derive_doc_type(rel_path_obj, cfg.get("doc_type_rules", []))
        nav = is_nav_page(rel_path_obj, fm, body, cfg.get("nav_rules", {}))
        if nav:
            stats["nav"] += 1

        symbols = extract_symbols(rel_path_obj, fm)

        chunk_cfg = cfg.get("chunk", {})
        chunks = split_markdown(
            body,
            doc_title=title,
            target_chars=int(chunk_cfg.get("target_chars", 1200)),
            max_chars=int(chunk_cfg.get("max_chars", 1500)),
            overlap_chars=int(chunk_cfg.get("overlap_chars", 150)),
        )
        if not chunks:
            warn.add(rel, "empty_body", "")
            stats["warnings"] += 1

        st = path.stat()
        # 写文档元信息
        if doc_id is not None:
            delete_chunks(conn, doc_id)
        new_doc_id = upsert_document(
            conn,
            rel_path=rel,
            title=title,
            section=section,
            doc_type=doc_type,
            source_url=source_url,
            is_nav=nav,
            mtime=st.st_mtime,
            size=st.st_size,
            sha=sha,
            chunk_count=len(chunks),
        )
        # 写 chunks
        rows = []
        for c in chunks:
            # title 列用 文档 title + heading_path 拼接，最大化命中概率
            t_col = title
            if c.heading_path and c.heading_path != title:
                t_col = f"{title} {c.heading_path}"
            rows.append((t_col, symbols, c.body, new_doc_id, c.idx))
        if rows:
            conn.executemany(
                "INSERT INTO chunks(title, symbols, body, doc_id, chunk_idx) VALUES (?, ?, ?, ?, ?)",
                rows,
            )
        stats["indexed"] += 1

        if stats["indexed"] % 500 == 0:
            conn.commit()

    # 清理已从磁盘删除的文档
    cur = conn.execute("SELECT id, rel_path FROM documents")
    removed = 0
    for doc_id, rel in cur.fetchall():
        if rel not in seen_rel:
            delete_chunks(conn, doc_id)
            conn.execute("DELETE FROM documents WHERE id=?", (doc_id,))
            removed += 1
    stats["removed"] = removed

    # 记录 meta
    conn.execute(
        "INSERT INTO meta(key, value) VALUES('built_at', ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
        (str(int(time.time())),),
    )
    conn.execute(
        "INSERT INTO meta(key, value) VALUES('docset_id', ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
        (docset["id"],),
    )
    conn.execute(
        "INSERT INTO meta(key, value) VALUES('build_signature', ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
        (build_signature,),
    )
    conn.execute(
        "INSERT INTO meta(key, value) VALUES('build_logic_version', ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
        (BUILD_LOGIC_VERSION,),
    )
    conn.commit()
    # FTS5 优化
    try:
        conn.execute("INSERT INTO chunks(chunks) VALUES('optimize')")
        conn.commit()
    except sqlite3.OperationalError:
        pass
    conn.close()

    warn.flush()
    stats["elapsed_sec"] = round(time.time() - t0, 2)
    stats["db_path"] = str(db_path)
    stats["warnings_path"] = str(warn_path) if warn.items else ""
    stats["warnings_count"] = len(warn.items)
    return stats


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hub-root", default=None, help="DocsHub 根目录；未传时按 env/祖先目录自动发现")
    ap.add_argument("--docset", required=True, help="docset id 或 all")
    ap.add_argument("--rebuild", action="store_true", help="丢弃旧索引重建")
    args = ap.parse_args()

    state = ensure_initialized("构建索引")
    hub_root = resolve_query_hub_root(args.hub_root, str(state.get("hub_root") or ""))
    cfg = load_docsets(hub_root)
    defaults = cfg.get("defaults", {})
    docsets = cfg.get("docsets", [])

    targets = docsets if args.docset == "all" else [d for d in docsets if d["id"] == args.docset]
    if not targets:
        raise SystemExit(f"未找到 docset: {args.docset}")

    for ds in targets:
        print(f"[build] docset={ds['id']} root={ds['root']}")
        stats = build_docset(hub_root, ds, defaults, args.rebuild)
        print(f"  stats: {stats}")


if __name__ == "__main__":
    main()
