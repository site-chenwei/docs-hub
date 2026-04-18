"""docs-hub 构建环境初始化与本地 site-packages 注入。"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any


INIT_STATE_FILE = ".local-doc-init.json"
REQUIREMENTS_FILE = "requirements-build.txt"


def resolve_hub_root(argv: list[str], cwd: Path | None = None) -> Path:
    cwd = cwd or Path.cwd()
    for idx, arg in enumerate(argv):
        if arg == "--hub-root" and idx + 1 < len(argv):
            return (cwd / argv[idx + 1]).resolve()
        if arg.startswith("--hub-root="):
            return (cwd / arg.split("=", 1)[1]).resolve()
    return cwd.resolve()


def init_state_path(hub_root: Path) -> Path:
    return hub_root / INIT_STATE_FILE


def requirements_path(hub_root: Path) -> Path:
    return hub_root / REQUIREMENTS_FILE


def requirements_hash(hub_root: Path) -> str:
    req = requirements_path(hub_root)
    if not req.exists():
        raise FileNotFoundError(req)
    data = req.read_bytes()
    return hashlib.sha256(data).hexdigest()


def load_init_state(hub_root: Path) -> dict[str, Any] | None:
    path = init_state_path(hub_root)
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def activate_local_site_packages(hub_root: Path) -> dict[str, Any] | None:
    state = load_init_state(hub_root)
    if not state:
        return None
    site_packages = str(state.get("site_packages") or "")
    if site_packages and site_packages not in sys.path:
        sys.path.insert(0, site_packages)
    return state


def ensure_initialized(hub_root: Path, command_label: str) -> dict[str, Any]:
    state = load_init_state(hub_root)
    init_script = Path(__file__).with_name("local_doc_init.py")
    init_cmd = f"python3 {init_script} --hub-root {hub_root}"
    if not state:
        raise SystemExit(
            f"[error] docs-hub 尚未初始化，无法{command_label}。\n"
            f"  请先手动运行: {init_cmd}"
        )

    site_packages = Path(str(state.get("site_packages") or ""))
    if not site_packages.exists():
        raise SystemExit(
            f"[error] docs-hub 初始化状态已失效，缺少 site-packages: {site_packages}\n"
            f"  请重新运行: {init_cmd}"
        )

    try:
        expected_hash = requirements_hash(hub_root)
    except FileNotFoundError as exc:
        raise SystemExit(
            f"[error] docs-hub 缺少依赖清单: {exc}\n"
            f"  请确认仓库完整后重新运行: {init_cmd}"
        ) from exc
    if state.get("requirements_hash") != expected_hash:
        raise SystemExit(
            f"[error] docs-hub 依赖清单已变更，当前初始化状态过期。\n"
            f"  请重新运行: {init_cmd}"
        )

    activate_local_site_packages(hub_root)
    return state
