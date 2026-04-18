"""docs-hub 共用工具。

包含：
- front matter 解析器（PyYAML safe_load）
- Markdown 分块（markdown-it-py 标题树 + 滑窗续切）
- 元信息派生（section / doc_type / is_nav）
- 符号抽取（用于 FTS5 symbols 列加权匹配 API 名/错误码）
- warnings 收集器
- 文件 sha256

设计原则：主路径严格，边界处才降级，降级时必须留 warning。
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


class FrontMatterError(ValueError):
    """front matter 语法不在支持子集内。调用方决定是否降级。"""


_FM_FENCE = "---"
def _normalize_front_matter_value(value: Any) -> Any:
    if isinstance(value, list):
        return [str(item) for item in value]
    if value is None:
        return None
    if isinstance(value, (str, int, float, bool)):
        return str(value)
    return value


def parse_front_matter(text: str) -> tuple[dict[str, Any], str]:
    """解析 front matter；返回 (fm_dict, body)。

    支持子集：
        key: "value" | key: value
        key:
          - "item"
          - item

    子集之外的结构（嵌套映射、内联 JSON、多行字符串、!tag 等）一律抛 FrontMatterError。
    没有 front matter 时返回 ({}, text)。
    """
    if not text.startswith(_FM_FENCE + "\n") and not text.startswith(_FM_FENCE + "\r\n"):
        return {}, text

    lines = text.splitlines(keepends=False)
    if not lines or lines[0].strip() != _FM_FENCE:
        return {}, text

    # 找结束 fence
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == _FM_FENCE:
            end_idx = i
            break
    if end_idx is None:
        raise FrontMatterError("front matter 未闭合")

    fm_lines = lines[1:end_idx]
    body = "\n".join(lines[end_idx + 1 :])
    # 保留原 body 末尾换行语义
    if text.endswith("\n") and not body.endswith("\n"):
        body += "\n"

    try:
        import yaml
    except ImportError as exc:
        raise FrontMatterError(f"缺少 PyYAML: {exc}") from exc

    raw_meta = "\n".join(fm_lines)
    try:
        parsed = yaml.safe_load(raw_meta) if raw_meta.strip() else {}
    except yaml.YAMLError as exc:  # type: ignore[attr-defined]
        raise FrontMatterError(f"front matter YAML 解析失败: {exc}") from exc

    if parsed is None:
        parsed = {}
    if not isinstance(parsed, dict):
        raise FrontMatterError("front matter 顶层必须是映射")

    result = {str(key): _normalize_front_matter_value(value) for key, value in parsed.items()}
    return result, body

@dataclass
class Chunk:
    heading_path: str  # "H1 > H2 > H3"
    body: str
    idx: int = 0


def _split_by_length(text: str, target: int, max_len: int, overlap: int) -> list[str]:
    """按目标长度切分，优先在换行/句号/空格处断开；块之间保留 overlap 字符重叠。"""
    text = text.strip()
    if len(text) <= max_len:
        return [text] if text else []
    chunks: list[str] = []
    start = 0
    n = len(text)
    while start < n:
        end = min(start + target, n)
        if end < n:
            # 在 [start+target*0.6, start+max_len] 区间找最近的换行/句号
            search_end = min(start + max_len, n)
            window = text[start:search_end]
            candidates = [window.rfind("\n\n"), window.rfind("\n"), window.rfind("。"), window.rfind(". ")]
            best = max(candidates)
            if best >= int(target * 0.6):
                end = start + best + 1
        chunks.append(text[start:end].strip())
        if end >= n:
            break
        start = max(end - overlap, start + 1)
    return [c for c in chunks if c]


def _segment_by_markdown_ast(body: str) -> list[tuple[str, str]]:
    """基于 markdown-it-py token 流提取 (heading_path, segment_text)。"""
    try:
        from markdown_it import MarkdownIt
    except ImportError as exc:
        raise RuntimeError(f"缺少 markdown-it-py: {exc}") from exc

    lines = body.splitlines()
    parser = MarkdownIt("commonmark")
    tokens = parser.parse(body)

    headings: list[tuple[int, str, int, int]] = []
    for idx, token in enumerate(tokens):
        if token.type != "heading_open":
            continue
        if not token.tag.startswith("h"):
            continue
        line_map = token.map or []
        if len(line_map) != 2:
            continue
        title = ""
        if idx + 1 < len(tokens) and tokens[idx + 1].type == "inline":
            title = tokens[idx + 1].content.strip()
        level = int(token.tag[1:])
        headings.append((level, title, line_map[0], line_map[1]))

    if not headings:
        whole = body.strip()
        return [("", whole)] if whole else []

    segments: list[tuple[str, str]] = []
    if headings[0][2] > 0:
        preface = "\n".join(lines[: headings[0][2]]).strip()
        if preface:
            segments.append(("", preface))

    stack: list[tuple[int, str]] = []
    for idx, (level, title, start_line, content_start_line) in enumerate(headings):
        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, title))
        next_start_line = headings[idx + 1][2] if idx + 1 < len(headings) else len(lines)
        seg_text = "\n".join(lines[content_start_line:next_start_line]).strip()
        if not seg_text:
            continue
        heading_path = " > ".join(text for _, text in stack if text)
        segments.append((heading_path, seg_text))
    return segments


def split_markdown(
    body: str,
    doc_title: str | None,
    target_chars: int = 1200,
    max_chars: int = 1500,
    overlap_chars: int = 150,
) -> list[Chunk]:
    """按标题树优先切块；超长滑窗续切；无标题整页一块。

    - heading_path 以 "A > B > C" 表示
    - doc_title 作为根标题（若 body 里没有 H1）
    """
    segments = _segment_by_markdown_ast(body)
    if not segments:
        whole = body.strip()
        if not whole:
            return []
        return [Chunk(heading_path=doc_title or "", body=whole, idx=0)]

    chunks: list[Chunk] = []
    for path, seg_text in segments:
        seg_text = seg_text.strip()
        if not seg_text:
            continue
        if len(seg_text) <= max_chars:
            chunks.append(Chunk(heading_path=path, body=seg_text))
        else:
            for sub in _split_by_length(seg_text, target_chars, max_chars, overlap_chars):
                chunks.append(Chunk(heading_path=path, body=sub))

    for i, c in enumerate(chunks):
        c.idx = i
    return chunks


def derive_section(
    fm: dict[str, Any],
    rel_path: Path,
    rules: list[str],
) -> str:
    """按 rules 顺序取 section；rules 元素支持 'menu_path[0]' / 'rel_path[0]'。"""
    for rule in rules:
        if rule == "menu_path[0]":
            mp = fm.get("menu_path")
            if isinstance(mp, list) and mp:
                return str(mp[0])
        elif rule == "rel_path[0]":
            parts = rel_path.parts
            if parts:
                return parts[0]
    return ""


def derive_doc_type(rel_path: Path, rules: list[dict[str, Any]]) -> str:
    rp = str(rel_path).replace("\\", "/")
    for rule in rules:
        if rule.get("match") == "path_contains":
            anys = rule.get("any", [])
            for kw in anys:
                if kw in rp:
                    return rule.get("type", "doc")
    return "doc"


_LINK_ONLY_LINE = re.compile(r"^\s*[-*]\s+\*?\*?\[.*\]\(.*\)\*?\*?\s*$")


def is_nav_page(rel_path: Path, fm: dict[str, Any], body: str, nav_rules: dict[str, Any]) -> bool:
    filenames = nav_rules.get("filenames", [])
    if rel_path.name in filenames:
        return True
    # 正文去掉标题后，全是链接行（或空行）→ 导航页
    lines = [l for l in body.splitlines() if l.strip() and not l.strip().startswith("#")]
    if not lines:
        return True
    if all(_LINK_ONLY_LINE.match(l) for l in lines):
        return True
    min_body_chars = int(nav_rules.get("min_body_chars", 0) or 0)
    menu_path = fm.get("menu_path")
    has_menu_path = isinstance(menu_path, list) and bool(menu_path)
    plain_body = "\n".join(lines).strip()
    if min_body_chars > 0 and len(plain_body) < min_body_chars and not has_menu_path:
        return True
    return False


def extract_symbols(rel_path: Path, fm: dict[str, Any]) -> str:
    """组装 symbols 列：路径片段 + 文件名主干 + menu_path。

    目的是让 pdd.mall.info.get / @ohos.security.cert / 错误码等精确符号能被 trigram 命中。
    """
    parts: list[str] = []
    for p in rel_path.with_suffix("").parts:
        parts.append(p)
    stem = rel_path.stem
    parts.append(stem)
    # 拆分常见分隔符，便于匹配 API 名片段
    for sep in ["-", "_", "/", ".", " ", "（", "）", "(", ")"]:
        stem = stem.replace(sep, " ")
    parts.extend(t for t in stem.split() if t)
    mp = fm.get("menu_path")
    if isinstance(mp, list):
        parts.extend(str(x) for x in mp)
    # 去重保持顺序
    seen: set[str] = set()
    ordered: list[str] = []
    for p in parts:
        if p and p not in seen:
            seen.add(p)
            ordered.append(p)
    return " ".join(ordered)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


@dataclass
class WarningSink:
    path: Path
    items: list[dict[str, Any]] = field(default_factory=list)

    def add(self, rel_path: str, kind: str, detail: str = "") -> None:
        self.items.append({"rel_path": rel_path, "kind": kind, "detail": detail})

    def flush(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as f:
            for item in self.items:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")


def read_text_safely(path: Path) -> tuple[str | None, str | None]:
    """读文件，UTF-8 失败时返回 (None, error)；不抛异常。"""
    try:
        return path.read_text(encoding="utf-8"), None
    except UnicodeDecodeError as e:
        return None, f"utf-8 decode error: {e}"
    except OSError as e:
        return None, f"io error: {e}"


def load_docsets(hub_root: Path) -> dict[str, Any]:
    cfg_path = hub_root / "docsets.json"
    with cfg_path.open("r", encoding="utf-8") as f:
        return json.load(f)
