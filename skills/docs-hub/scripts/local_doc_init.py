"""初始化 docs-hub skill 自身依赖。"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from _bootstrap import INIT_STATE_FILE, REQUIREMENTS_FILE, requirements_hash, resolve_init_hub_root, skill_root  # noqa: E402


def deps_site_packages(root: Path) -> Path:
    return root / ".deps" / "site-packages"


def install_requirements(site_packages: Path, req_path: Path) -> str:
    uv = shutil.which("uv")
    if uv:
        subprocess.run(
            [uv, "pip", "install", "--python", sys.executable, "--upgrade", "--target", str(site_packages), "-r", str(req_path)],
            check=True,
        )
        return "uv"

    pip = shutil.which("pip3") or shutil.which("pip")
    if pip:
        subprocess.run([pip, "install", "--upgrade", "--target", str(site_packages), "-r", str(req_path)], check=True)
        return "pip"

    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--upgrade", "--target", str(site_packages), "-r", str(req_path)],
        check=True,
    )
    return "python -m pip"


def load_docsets_config(hub_root: Path) -> dict[str, Any]:
    cfg_path = hub_root / "docsets.json"
    if not cfg_path.exists():
        raise SystemExit(f"[error] DocsHub 缺少 docsets.json: {cfg_path}")
    with cfg_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def detect_missing_index_docsets(hub_root: Path) -> list[str]:
    cfg = load_docsets_config(hub_root)
    missing: list[str] = []
    for docset in cfg.get("docsets", []):
        docset_id = str(docset.get("id") or "").strip()
        if not docset_id:
            continue
        db_path = hub_root / "index" / f"{docset_id}.sqlite"
        if not db_path.exists():
            missing.append(docset_id)
    return missing


def build_missing_indexes(root: Path, hub_root: Path, missing_docsets: list[str]) -> None:
    if not missing_docsets:
        print("[init] 索引已存在，无需补建")
        return

    build_script = root / "scripts" / "build_docset_index.py"
    print(f"[init] 检测到缺失索引的 docset: {', '.join(missing_docsets)}")
    for docset_id in missing_docsets:
        print(f"[init] 自动构建索引: {docset_id}")
        result = subprocess.run(
            [sys.executable, str(build_script), "--hub-root", str(hub_root), "--docset", docset_id],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.stdout:
            print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
        if result.stderr:
            print(result.stderr, end="" if result.stderr.endswith("\n") else "\n", file=sys.stderr)
        if result.returncode != 0:
            raise SystemExit(f"[error] 自动构建索引失败: {docset_id}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill-root", default=None, help="skill 根目录；默认按当前脚本位置推断")
    ap.add_argument("--hub-root", default=None, help="DocsHub 根目录；未传时尝试从 env/当前工作区自动发现")
    args = ap.parse_args()

    root = Path(args.skill_root).resolve() if args.skill_root else skill_root()
    hub_root = resolve_init_hub_root(args.hub_root)
    req_path = root / REQUIREMENTS_FILE
    if not req_path.exists():
        raise SystemExit(f"[error] 缺少依赖清单: {req_path}")

    site_packages = deps_site_packages(root)
    site_packages.mkdir(parents=True, exist_ok=True)

    print(f"[init] 安装 skill 依赖到本地目录: {site_packages}")
    installer = install_requirements(site_packages, req_path)

    state = {
        "initialized_at": datetime.now(timezone.utc).isoformat(),
        "skill_root": str(root),
        "installer": installer,
        "installer_python": sys.executable,
        "site_packages": str(site_packages),
        "hub_root": str(hub_root),
        "requirements_file": REQUIREMENTS_FILE,
        "requirements_hash": requirements_hash(root),
        "python_version": ".".join(str(part) for part in sys.version_info[:3]),
    }
    state_path = root / INIT_STATE_FILE
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    build_missing_indexes(root, hub_root, detect_missing_index_docsets(hub_root))
    print(f"[init] 完成: {state_path}")
    print(f"[init] 已记录 DocsHub 根目录: {hub_root}")
    print(f"[init] 后续可直接运行: python3 {root / 'scripts' / 'search_docs.py'} <keywords>")


if __name__ == "__main__":
    main()
