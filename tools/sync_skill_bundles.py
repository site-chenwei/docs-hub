from __future__ import annotations

import argparse
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PRIMARY_SKILL_ROOT = REPO_ROOT / "skills" / "docs-hub"
TARGET_SKILL_ROOTS = [
    REPO_ROOT / ".claude" / "skills" / "docs-hub",
    REPO_ROOT / ".codex" / "skills" / "docs-hub",
    REPO_ROOT / ".gemini" / "skills" / "docs-hub",
]
MANAGED_ENTRIES = [
    "SKILL.md",
    "agents",
    "references",
    "requirements-build.txt",
    "scripts",
]


def ignore_transient(_dir: str, names: list[str]) -> set[str]:
    ignored: set[str] = set()
    for name in names:
        if name == "__pycache__" or name.endswith(".pyc"):
            ignored.add(name)
    return ignored


def sync_entry(src: Path, dst: Path) -> None:
    if dst.exists():
        if dst.is_dir():
            shutil.rmtree(dst)
        else:
            dst.unlink()

    if src.is_dir():
        shutil.copytree(src, dst, ignore=ignore_transient)
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def collect_managed_files(root: Path) -> dict[str, bytes]:
    result: dict[str, bytes] = {}
    for entry in MANAGED_ENTRIES:
        src = root / entry
        if src.is_dir():
            for path in sorted(
                p for p in src.rglob("*") if p.is_file() and "__pycache__" not in p.parts and not p.name.endswith(".pyc")
            ):
                result[path.relative_to(root).as_posix()] = path.read_bytes()
        elif src.exists():
            result[src.relative_to(root).as_posix()] = src.read_bytes()
    return result


def check_target(primary_files: dict[str, bytes], target_root: Path) -> list[str]:
    target_files = collect_managed_files(target_root)
    errors: list[str] = []

    missing = sorted(set(primary_files) - set(target_files))
    extra = sorted(set(target_files) - set(primary_files))
    changed = sorted(path for path in primary_files if path in target_files and primary_files[path] != target_files[path])

    if missing:
        errors.append(f"missing: {', '.join(missing)}")
    if extra:
        errors.append(f"extra: {', '.join(extra)}")
    if changed:
        errors.append(f"changed: {', '.join(changed)}")
    return errors


def run_check() -> int:
    primary_files = collect_managed_files(PRIMARY_SKILL_ROOT)
    stale = False
    for target_root in TARGET_SKILL_ROOTS:
        errors = check_target(primary_files, target_root)
        if not errors:
            print(f"[check] ok {target_root.relative_to(REPO_ROOT)}")
            continue
        stale = True
        print(f"[check] stale {target_root.relative_to(REPO_ROOT)}")
        for line in errors:
            print(f"  - {line}")
    return 1 if stale else 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只校验镜像是否与主 skill 一致，不写入文件")
    args = ap.parse_args()

    if not PRIMARY_SKILL_ROOT.exists():
        raise SystemExit(f"missing primary skill root: {PRIMARY_SKILL_ROOT}")

    if args.check:
        raise SystemExit(run_check())

    for target_root in TARGET_SKILL_ROOTS:
        target_root.mkdir(parents=True, exist_ok=True)
        for entry in MANAGED_ENTRIES:
            sync_entry(PRIMARY_SKILL_ROOT / entry, target_root / entry)
        print(f"[sync] updated {target_root.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
