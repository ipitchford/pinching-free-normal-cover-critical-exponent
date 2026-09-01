#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "$0")" && pwd)"
cd "$root_dir"

python3 verify_estimates.py
python3 -m unittest -v tests/test_mutations.py
python3 -O verify_estimates.py
python3 -O -m unittest -v tests/test_mutations.py
qpdf --check paper.pdf >/dev/null
python3 update_pdf_text_digest.py --check
python3 verify_package.py

if [[ -f paper.log ]] && rg -n 'undefined references|Citation.*undefined|There were undefined citations|multiply defined|Overfull \\hbox' paper.log; then
  echo "FAIL: unresolved or overflowing LaTeX output" >&2
  exit 1
fi

echo "PASS: complete read-only replay"
