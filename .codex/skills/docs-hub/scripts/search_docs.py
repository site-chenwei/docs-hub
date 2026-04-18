"""查询外部 DocsHub 索引。

用法示例：
    python3 scripts/search_docs.py --hub-root /path/to/hub --list-docsets
    python3 scripts/search_docs.py --hub-root /path/to/hub 输入法 --top 10
    python3 scripts/search_docs.py 光标 跟随 --match all --docset harmonyos --top 5
    python3 scripts/search_docs.py pdd.mall.info.get --docset pinduoduo
    python3 scripts/search_docs.py --rebuild-stale 订单 --top 8

排序权重：bm25(chunks, 10.0, 6.0, 1.0) — title:10 symbols:6 body:1
默认过滤 is_nav=1 的导航页；--include-nav 可带出。
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from _bootstrap import ensure_initialized, resolve_query_hub_root  # noqa: E402
from _common import load_docsets  # noqa: E402
from build_docset_index import DocsetBuildError, build_docset  # noqa: E402


_FTS_SPECIAL = re.compile(r'[()":*\-+\^]')


def fts_escape(token: str) -> str:
    """把用户关键词转成 FTS5 安全的短语表达式。

    trigram tokenizer 要求 token >= 3 字符；短于 3 字的中文词（如"光标"）
    无法被 FTS5 命中，需要标记为 short_token 由调用方降级处理。
    """
    cleaned = _FTS_SPECIAL.sub(" ", token).strip()
    if not cleaned:
        return ""
    return '"' + cleaned.replace('"', ' ') + '"'


def _is_short_token(token: str) -> bool:
    """trigram 要求 >= 3 字符；ASCII 字符按字节计，中文按 unicode 字符计。"""
    return len(token.strip()) < 3


def build_match_expr(keywords: list[str], mode: str) -> tuple[str, list[str]]:
    """返回 (fts_match_expr, short_tokens)。

    short_tokens 是无法进入 FTS5 的短词，调用方用 LIKE 补充过滤。
    """
    long_kws = [k for k in keywords if k.strip() and not _is_short_token(k)]
    short_kws = [k for k in keywords if k.strip() and _is_short_token(k)]
    phrases = [fts_escape(k) for k in long_kws]
    phrases = [p for p in phrases if p]
    if not phrases:
        return "", short_kws
    joiner = " AND " if mode == "all" else " OR "
    return joiner.join(phrases), short_kws


def build_like_clause(tokens: list[str], mode: str) -> tuple[str, list[Any], str, list[Any]]:
    """为短词 fallback 构造 WHERE 条件和加权分数表达式。"""
    if not tokens:
        return "", [], "0.0", []

    token_clauses: list[str] = []
    where_params: list[Any] = []
    score_terms: list[str] = []
    score_params: list[Any] = []
    joiner = " AND " if mode == "all" else " OR "

    for token in tokens:
        pattern = f"%{token}%"
        token_clauses.append(
            "("
            "COALESCE(c.title, '') LIKE ? OR "
            "COALESCE(c.symbols, '') LIKE ? OR "
            "COALESCE(c.body, '') LIKE ?"
            ")"
        )
        where_params.extend([pattern, pattern, pattern])
        score_terms.append(
            "("
            "CASE WHEN COALESCE(c.title, '') LIKE ? THEN 10.0 ELSE 0 END + "
            "CASE WHEN COALESCE(c.symbols, '') LIKE ? THEN 6.0 ELSE 0 END + "
            "CASE WHEN COALESCE(c.body, '') LIKE ? THEN 1.0 ELSE 0 END"
            ")"
        )
        score_params.extend([pattern, pattern, pattern])

    return "(" + joiner.join(token_clauses) + ")", where_params, " + ".join(score_terms), score_params


def snippet_clean(s: str, max_len: int = 200) -> str:
    s = s.replace("\n", " ").strip()
    if len(s) <= max_len:
        return s
    return s[: max_len - 1] + "…"


def _dedupe_terms(keywords: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for keyword in sorted((kw.strip() for kw in keywords if kw.strip()), key=len, reverse=True):
        marker = keyword.casefold()
        if marker in seen:
            continue
        seen.add(marker)
        ordered.append(keyword)
    return ordered


def build_highlighted_snippet(text: str, keywords: list[str], max_len: int = 200) -> str:
    compact = text.replace("\n", " ").strip()
    if not compact:
        return ""

    terms = _dedupe_terms(keywords)
    if not terms:
        return snippet_clean(compact, max_len)

    folded = compact.casefold()
    hit_index: int | None = None
    for term in terms:
        idx = folded.find(term.casefold())
        if idx >= 0 and (hit_index is None or idx < hit_index):
            hit_index = idx

    if hit_index is None:
        return snippet_clean(compact, max_len)

    # 优先保留命中点前后文，避免总是返回 chunk 开头。
    before = max_len // 3
    start = max(0, hit_index - before)
    end = min(len(compact), start + max_len)
    if end - start < max_len:
        start = max(0, end - max_len)

    snippet = compact[start:end].strip()
    if start > 0:
        snippet = "…" + snippet.lstrip()
    if end < len(compact):
        snippet = snippet.rstrip() + "…"

    pattern = re.compile("|".join(re.escape(term) for term in terms), re.IGNORECASE)
    return pattern.sub(lambda match: f"【{match.group(0)}】", snippet)


def list_docsets(hub_root: Path) -> None:
    cfg = load_docsets(hub_root)
    for d in cfg.get("docsets", []):
        db = hub_root / "index" / f"{d['id']}.sqlite"
        status = "indexed" if db.exists() else "no-index"
        extra = ""
        if db.exists():
            try:
                conn = sqlite3.connect(db)
                n_doc = conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
                n_chunk = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
                extra = f" docs={n_doc} chunks={n_chunk}"
                conn.close()
            except sqlite3.Error as e:
                extra = f" (read error: {e})"
        print(f"- {d['id']:<12} {d['name']:<20} root={d['root']}  [{status}]{extra}")


def ensure_index_ready(
    hub_root: Path,
    docset: dict[str, Any],
    defaults: dict[str, Any],
    rebuild_stale: bool,
) -> Path | None:
    """返回可用的 db 路径；不可用返回 None。rebuild_stale=True 时允许触发 build。"""
    docset_id = docset["id"]
    db = hub_root / "index" / f"{docset_id}.sqlite"
    if db.exists() and not rebuild_stale:
        return db
    if not db.exists() and not rebuild_stale:
        print(
            f"[error] docset '{docset_id}' 索引缺失: {db}\n"
            f"  可手动运行: python3 {Path(__file__).parent / 'build_docset_index.py'} --hub-root {hub_root} --docset {docset_id}",
            file=sys.stderr,
        )
        return None
    # refresh 模式：直接调用 build_docset 函数，免去起子进程 + 重新 import 的启动开销。
    action = "增量刷新" if db.exists() else "先构建"
    print(f"[build] {docset_id} 索引{action}…", file=sys.stderr)
    try:
        stats = build_docset(hub_root, docset, defaults, rebuild=False)
    except DocsetBuildError as exc:
        print(f"[error] 构建失败 docset={docset_id}: {exc}", file=sys.stderr)
        return None
    except Exception as exc:  # noqa: BLE001
        print(f"[error] 构建失败 docset={docset_id}: {exc}", file=sys.stderr)
        return None
    if not db.exists():
        print(f"[error] 构建失败 docset={docset_id}", file=sys.stderr)
        return None
    print(f"  stats: {stats}", file=sys.stderr)
    return db


def query_like(
    conn: sqlite3.Connection,
    short_tokens: list[str],
    mode: str,
    section: str | None,
    top: int,
    include_nav: bool,
) -> list[sqlite3.Row]:
    like_clause, like_params, like_score_expr, like_score_params = build_like_clause(short_tokens, mode)
    if not like_clause:
        return []

    where = [like_clause]
    where_params = list(like_params)
    if not include_nav:
        where.append("d.is_nav = 0")
    if section:
        where.append("d.section = ?")
        where_params.append(section)

    sql = f"""
        SELECT rel_path, title, section, doc_type, source_url, is_nav, chunk_idx, body, chunk_title, -like_score AS score
        FROM (
            SELECT d.rel_path, d.title, d.section, d.doc_type, d.source_url, d.is_nav,
                   c.chunk_idx, c.body, c.title AS chunk_title,
                   ({like_score_expr}) AS like_score
            FROM chunks c JOIN documents d ON d.id = c.doc_id
            WHERE {' AND '.join(where)}
        )
        ORDER BY like_score DESC, rel_path ASC, chunk_idx ASC
        LIMIT ?
    """
    params = like_score_params + where_params + [top * 3]
    return conn.execute(sql, params).fetchall()


def query_fts(
    conn: sqlite3.Connection,
    match_expr: str,
    section: str | None,
    top: int,
    include_nav: bool,
    required_short_tokens: list[str],
) -> list[sqlite3.Row]:
    where = ["chunks MATCH ?"]
    where_params: list[Any] = [match_expr]
    score_expr = "bm25(chunks, 10.0, 6.0, 1.0)"
    score_params: list[Any] = []

    if required_short_tokens:
        # `match=all` 且混有短词时，短词必须作为过滤条件参与，而不是只做加权。
        like_clause, like_params, like_score_expr, like_score_params = build_like_clause(required_short_tokens, "all")
        where.append(like_clause)
        where_params.extend(like_params)
        # 短词只提供轻量加权，避免压过 bm25 主排序。
        score_expr = f"bm25(chunks, 10.0, 6.0, 1.0) - (({like_score_expr}) / 1000.0)"
        score_params.extend(like_score_params)

    if not include_nav:
        where.append("d.is_nav = 0")
    if section:
        where.append("d.section = ?")
        where_params.append(section)

    sql = f"""
        SELECT d.rel_path, d.title, d.section, d.doc_type, d.source_url, d.is_nav,
               c.chunk_idx, c.body, c.title AS chunk_title,
               {score_expr} AS score
        FROM chunks c JOIN documents d ON d.id = c.doc_id
        WHERE {' AND '.join(where)}
        ORDER BY score ASC
        LIMIT ?
    """
    params = score_params + where_params + [top * 3]
    return conn.execute(sql, params).fetchall()


def search_one(
    db_path: Path,
    match_expr: str,
    short_tokens: list[str],
    keywords: list[str],
    mode: str,
    section: str | None,
    top: int,
    include_nav: bool,
) -> list[dict[str, Any]]:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        rows: list[sqlite3.Row] = []
        if match_expr:
            required_short_tokens = short_tokens if mode == "all" else []
            rows.extend(query_fts(conn, match_expr, section, top, include_nav, required_short_tokens))
        if short_tokens and (mode == "or" or not match_expr):
            rows.extend(query_like(conn, short_tokens, mode, section, top, include_nav))
    finally:
        conn.close()

    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    rows.sort(key=lambda r: (r["score"], r["rel_path"], r["chunk_idx"]))
    for r in rows:
        if r["rel_path"] in seen:
            continue
        seen.add(r["rel_path"])
        # heading_path = chunk_title 去掉文档 title 前缀
        chunk_title = r["chunk_title"] or ""
        heading_path = chunk_title
        if chunk_title.startswith((r["title"] or "") + " "):
            heading_path = chunk_title[len((r["title"] or "")) + 1 :]
        out.append({
            "rel_path": r["rel_path"],
            "title": r["title"],
            "heading_path": heading_path,
            "section": r["section"],
            "doc_type": r["doc_type"],
            "source_url": r["source_url"],
            "is_nav": bool(r["is_nav"]),
            "score": round(r["score"], 3),
            "snippet": build_highlighted_snippet(r["body"], keywords, 200),
        })
        if len(out) >= top:
            break
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hub-root", default=None, help="DocsHub 根目录；未传时按 env/祖先目录自动发现")
    ap.add_argument("--docset", default=None, help="限定 docset id；不指定则跨 docset 查询")
    ap.add_argument("--section", default=None, help="限定 section（如 指南/API参考/FAQ）")
    ap.add_argument("--match", default="or", choices=["or", "all"], help="多关键词匹配策略")
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--include-nav", action="store_true")
    ap.add_argument("--rebuild-stale", action="store_true", help="查询前先做一次增量刷新（refresh 模式）")
    ap.add_argument("--list-docsets", action="store_true")
    ap.add_argument("--json", action="store_true", help="输出 JSON 而非纯文本")
    ap.add_argument("keywords", nargs="*")
    args = ap.parse_args()

    state = ensure_initialized("查询文档")
    hub_root = resolve_query_hub_root(args.hub_root, str(state.get("hub_root") or ""))

    if args.list_docsets:
        list_docsets(hub_root)
        return

    if not args.keywords:
        ap.error("需要至少一个关键词")

    match_expr, short_tokens = build_match_expr(args.keywords, args.match)
    if not match_expr and not short_tokens:
        ap.error("关键词清洗后为空")

    cfg = load_docsets(hub_root)
    defaults = cfg.get("defaults", {})
    all_docsets = cfg.get("docsets", [])
    targets = all_docsets if not args.docset else [d for d in all_docsets if d["id"] == args.docset]
    if not targets:
        raise SystemExit(f"未找到 docset: {args.docset}")

    all_results: list[dict[str, Any]] = []
    for ds in targets:
        db = ensure_index_ready(hub_root, ds, defaults, args.rebuild_stale)
        if db is None:
            continue
        try:
            rows = search_one(db, match_expr, short_tokens, args.keywords, args.match, args.section, args.top, args.include_nav)
        except sqlite3.OperationalError as e:
            print(f"[warn] docset={ds['id']} 查询失败: {e}", file=sys.stderr)
            continue
        for r in rows:
            r["docset"] = ds["id"]
            r["doc_root"] = str((hub_root / ds["root"]).resolve())
            r["abs_path"] = str((hub_root / ds["root"] / r["rel_path"]).resolve())
        all_results.extend(rows)

    # 跨 docset 合并后按 score 再排，取 top
    all_results.sort(key=lambda x: x["score"])
    all_results = all_results[: args.top]

    if args.json:
        print(json.dumps(all_results, ensure_ascii=False, indent=2))
        return

    if not all_results:
        print("(无结果)")
        return

    for i, r in enumerate(all_results, 1):
        print(f"[{i}] ({r['docset']}) {r['abs_path']}")
        if r.get("heading_path"):
            print(f"    # {r['heading_path']}")
        if r.get("source_url"):
            print(f"    url: {r['source_url']}")
        meta_bits = []
        if r.get("section"):
            meta_bits.append(f"section={r['section']}")
        if r.get("doc_type"):
            meta_bits.append(f"type={r['doc_type']}")
        meta_bits.append(f"score={r['score']}")
        print(f"    meta: {' '.join(meta_bits)}")
        print(f"    » {r['snippet']}")
        print()


if __name__ == "__main__":
    main()
