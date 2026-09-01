#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "$0")" && pwd)"
if [[ -n "${EVIDENCE_PRESS_TEX_BIN:-}" ]]; then
  export PATH="$EVIDENCE_PRESS_TEX_BIN:$PATH"
fi
for tool in xelatex latexmk bibtex qpdf pdftotext; do
  if ! command -v "$tool" >/dev/null; then
    echo "FAIL: required build tool not found: $tool" >&2
    exit 1
  fi
done

export SOURCE_DATE_EPOCH="1788220800"
export TZ=UTC
cd "$root_dir"
latexmk -xelatex -interaction=nonstopmode -halt-on-error paper.tex

if rg -n 'undefined references|Citation.*undefined|There were undefined citations|multiply defined|Overfull \\hbox' paper.log; then
  echo "FAIL: unresolved or overflowing LaTeX output" >&2
  exit 1
fi

qpdf --check paper.pdf >/dev/null
python3 update_pdf_text_digest.py --check
echo "PASS: paper.pdf built, structurally checked, and text-digest matched"
