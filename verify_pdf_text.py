#!/usr/bin/env python3
"""Check that the reader PDF exposes the theorem and assurance boundary."""

from __future__ import annotations

import pathlib
import re
import shutil
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parent
PDF = ROOT / "paper.pdf"

REQUIRED = (
    "AIM Problem 4.3",
    "reduced, surface-based convention",
    "The fixed free normal cover",
    "Strict comparison with the ambient lattice",
    "Pinching the cut system",
    "All-Fuchsian strengthening candidate for AIM Problem 4.3",
    "Relation to previous work",
    "fixed-width test function",
    "infinitely many distinct values",
    "Dougall and Sharp",
    "Elstrodt–Patterson–Sullivan",
    "AI-use disclosure",
    "no claim of historical priority",
    "Astala and Zinsmeister",
    "accessible-text fallback",
)

FORBIDDEN_PATTERNS = (
    r"\\(?:begin|end|section|cite|label|ref)\b",
    r"\?\?",
    r"undefined citation",
    r"undefined reference",
)


def extract_text() -> str:
    if not PDF.is_file():
        raise FileNotFoundError("paper.pdf is missing")
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        raise RuntimeError("pdftotext is required")
    proc = subprocess.run(
        [pdftotext, "-layout", str(PDF), "-"],
        check=True,
        text=True,
        capture_output=True,
    )
    return proc.stdout


def main() -> int:
    text = extract_text()
    normalized = " ".join(text.split())
    missing = [marker for marker in REQUIRED if marker not in normalized]
    forbidden = [
        pattern for pattern in FORBIDDEN_PATTERNS if re.search(pattern, normalized, re.I)
    ]
    if missing or forbidden:
        if missing:
            print("FAIL missing PDF markers:", ", ".join(missing), file=sys.stderr)
        if forbidden:
            print("FAIL forbidden PDF patterns:", ", ".join(forbidden), file=sys.stderr)
        return 1
    if len(text) < 12000:
        print("FAIL: extracted PDF text is unexpectedly short", file=sys.stderr)
        return 1
    print(f"PASS: PDF text gate ({len(text)} extracted characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
