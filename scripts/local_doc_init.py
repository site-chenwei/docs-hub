"""初始化 docs-hub 本地构建环境。"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _bootstrap import INIT_STATE_FILE, REQUIREMENTS_FILE, requirements_hash  # noqa: E402


def deps_site_packages(hub_root: Path) -> Path:
    return hub_root / ".deps" / "site-packages"


def install_requirements(site_packages: Path, req_path: Path) -> str:
    uv = shutil.which("uv")
    if uv:
        subprocess.run(
            [uv, "pip", "install", "--python", sys.executable, "--upgrade", "--target", str(site_packages), "-r", str(req_path)],
            check=True,
        )
        return "uv"

    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--upgrade", "--target", str(site_packages), "-r", str(req_path)],
        check=True,
    )
    return "pip"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hub-root", default=".")
    args = ap.parse_args()

    hub_root = Path(args.hub_root).resolve()
    req_path = hub_root / REQUIREMENTS_FILE
    if not req_path.exists():
        raise SystemExit(f"[error] 缺少依赖清单: {req_path}")

    site_packages = deps_site_packages(hub_root)
    site_packages.mkdir(parents=True, exist_ok=True)

    print(f"[init] 安装依赖到本地目录: {site_packages}")
    installer = install_requirements(site_packages, req_path)

    state = {
        "initialized_at": datetime.now(timezone.utc).isoformat(),
        "hub_root": str(hub_root),
        "installer": installer,
        "installer_python": sys.executable,
        "site_packages": str(site_packages),
        "requirements_file": REQUIREMENTS_FILE,
        "requirements_hash": requirements_hash(hub_root),
        "python_version": ".".join(str(part) for part in sys.version_info[:3]),
    }
    state_path = hub_root / INIT_STATE_FILE
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[init] 完成: {state_path}")
    print(f"[init] 后续可直接运行: python3 {hub_root}/scripts/search_docs.py --hub-root {hub_root} <keywords>")


if __name__ == "__main__":
    main()
