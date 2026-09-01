#!/usr/bin/env python3
"""Fail-closed package-level checks for the local solution candidate."""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parent
REQUIRED_FILES = (
    "README.md",
    "paper.tex",
    "paper.md",
    "paper.pdf",
    "PDF_TEXT.sha256",
    "references.bib",
    "CLAIM_SCOPE.md",
    "PROOF_OBLIGATIONS.md",
    "ASSURANCE.md",
    "SOURCES.md",
    "NOVELTY_REPORT.md",
    "METHOD_ALIGNMENT.md",
    "PAPER_CONFIGURATION.md",
    "STATUS.md",
    "PROVENANCE.md",
    "AI_INDEX.md",
    "CLAIMS.json",
    "CITATION_AUDIT.md",
    "PUBLIC_DOMAIN.md",
    "RELEASE_NOTES.md",
    "target.yaml",
    "CITATION.cff",
    ".zenodo.json",
    "LICENSE",
    "LICENSE-CODE",
    "LICENSES.md",
    "RESEARCH_METRICS.json",
    "RESEARCH_METRICS.md",
    "REPLAY_RECEIPT.json",
    "REPLAY_RECEIPT.md",
    "reviews/PRODUCER_SELF_REVIEW.md",
    "reviews/EXTERNAL_REVIEW_RESPONSE.md",
    "reviews/EXTERNAL_REVIEW_VERIFICATION.md",
    "reviews/REVISION_RESPONSE.md",
    "reviews/REVISION_VERIFICATION.md",
    "reviews/internal/EDITOR_IN_CHIEF.md",
    "reviews/internal/METHODOLOGY_SPECIALIST.md",
    "reviews/internal/DOMAIN_SPECIALIST.md",
    "reviews/internal/APPLICATIONS_SPECIALIST.md",
    "reviews/internal/DEVILS_ADVOCATE.md",
    "reviews/internal/EDITORIAL_SYNTHESIS.md",
    "reviews/internal/EDITORIAL_RESPONSE_MATRIX.md",
    "reviews/internal/DOMAIN_CONFIRMATION.md",
    "verify_estimates.py",
    "update_pdf_text_digest.py",
    "assets/fonts/NotoSerifCJKtc-Regular.otf",
    "assets/fonts/OFL.txt",
    "tests/test_mutations.py",
    ".github/workflows/verify.yml",
    "MANIFEST.sha256",
)


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def main() -> int:
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing:
        print("FAIL missing required files: " + ", ".join(missing), file=sys.stderr)
        return 1

    metrics = ROOT / "RESEARCH_METRICS.json"
    if metrics.exists():
        payload = json.loads(metrics.read_text(encoding="utf-8"))
        if payload.get("measurementScope") != "research-only":
            print("FAIL: metrics scope must remain research-only", file=sys.stderr)
            return 1

    claims = json.loads((ROOT / "CLAIMS.json").read_text(encoding="utf-8"))
    if claims.get("status") != "unrefereed-solution-candidate":
        print("FAIL: machine claim status lost candidate boundary", file=sys.stderr)
        return 1
    if claims.get("creator") != "Anonymous":
        print("FAIL: scholarly creator must remain Anonymous", file=sys.stderr)
        return 1

    if (ROOT / "reviews/EXTERNAL_REVIEW_2026-09-01.md").exists():
        print("FAIL: raw supplied third-party review must not be public", file=sys.stderr)
        return 1

    run(sys.executable, "verify_source_parity.py")
    run(sys.executable, "verify_pdf_text.py")
    run(sys.executable, "update_pdf_text_digest.py", "--check")
    run(sys.executable, "make_manifest.py")
    print("PASS: package gate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
