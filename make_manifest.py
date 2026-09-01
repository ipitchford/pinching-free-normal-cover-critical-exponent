#!/usr/bin/env python3
"""Create or verify the deterministic distributable-file SHA-256 manifest."""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parent
MANIFEST = ROOT / "MANIFEST.sha256"
EXCLUDED_NAMES = {
    "MANIFEST.sha256",
    "REPLAY_RECEIPT.json",
    "REPLAY_RECEIPT.md",
}
EXCLUDED_PARTS = {"__pycache__", ".git", ".pytest_cache"}
EXCLUDED_LATEX_SUFFIXES = {
    ".aux",
    ".bbl",
    ".bcf",
    ".blg",
    ".fdb_latexmk",
    ".fls",
    ".log",
    ".out",
    ".run.xml",
    ".synctex.gz",
    ".toc",
    ".xdv",
}


def is_generated_latex_file(path: pathlib.Path) -> bool:
    return path.name.startswith("paper.") and any(
        path.name.endswith(suffix) for suffix in EXCLUDED_LATEX_SUFFIXES
    )


def eligible_files() -> list[pathlib.Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.name not in EXCLUDED_NAMES
        and not is_generated_latex_file(path)
        and not any(part in EXCLUDED_PARTS for part in path.relative_to(ROOT).parts)
    )


def digest(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rendered_manifest() -> str:
    return "".join(
        f"{digest(path)}  {path.relative_to(ROOT).as_posix()}\n"
        for path in eligible_files()
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    expected = rendered_manifest()
    if args.write:
        MANIFEST.write_text(expected, encoding="utf-8")
        print(f"WROTE: MANIFEST.sha256 ({len(eligible_files())} files)")
        return 0
    if not MANIFEST.is_file():
        print("FAIL: MANIFEST.sha256 is missing", file=sys.stderr)
        return 1
    actual = MANIFEST.read_text(encoding="utf-8")
    if actual != expected:
        print("FAIL: manifest does not match the complete inventory", file=sys.stderr)
        return 1
    print(f"PASS: complete manifest ({len(eligible_files())} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
