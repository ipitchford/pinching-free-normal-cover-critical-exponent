#!/usr/bin/env python3
"""Bind the complete normalized reader text to a checked digest."""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import shutil
import subprocess
import sys
import unicodedata


ROOT = pathlib.Path(__file__).resolve().parent
PDF = ROOT / "paper.pdf"
DIGEST = ROOT / "PDF_TEXT.sha256"


def normalized_pdf_text() -> bytes:
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        raise RuntimeError("pdftotext is required")
    proc = subprocess.run(
        [pdftotext, "-layout", str(PDF), "-"],
        check=True,
        capture_output=True,
    )
    text = unicodedata.normalize("NFKC", proc.stdout.decode("utf-8"))
    portable = "".join(text.split()).replace("-", "") + "\n"
    return portable.encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check", action="store_true", help="compare with PDF_TEXT.sha256"
    )
    args = parser.parse_args()
    digest = hashlib.sha256(normalized_pdf_text()).hexdigest()
    line = f"{digest}  paper.pdf.normalized.txt\n"
    if args.check:
        if not DIGEST.is_file() or DIGEST.read_text(encoding="ascii") != line:
            print("FAIL: complete normalized PDF text digest mismatch", file=sys.stderr)
            return 1
        print(f"PASS: complete normalized PDF text digest {digest}")
        return 0
    DIGEST.write_text(line, encoding="ascii")
    print(f"WROTE: {DIGEST.name} {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
