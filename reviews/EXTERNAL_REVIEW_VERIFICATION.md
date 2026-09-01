# Supplied-review verification

**Date:** 1 September 2026  
**State:** in progress pending final freeze

## Already verified

- The supplied review copy is byte-identical to the user attachment and has
  SHA-256 `b3e8035f0e61e93b1aab810b8972f071cfd3f54af1a0721f1e7247aca7b8136c`.
- The revised standard-library checker passes 42 fixed-width samples.
- All 14 positive and mutation tests pass.
- Theorem-critical LaTeX, Markdown, and claim-scope markers agree.
- The old logarithmic rate remains only inside the preserved review artifact.

## Final-freeze checks still required

- Build the revised PDF with no undefined citations, references, or overfull
  boxes.
- Inspect every rendered PDF page.
- Run the PDF text and raw-TeX leakage gates.
- Freeze the complete manifest and replay it from a fresh directory.
- Replace the superseded replay receipt with one bound to the final PDF,
  extractor version, normalised text hash, and complete-inventory convention.
- Run the differentiated editorial-review gate against one exact frozen ZIP.

No release-ready conclusion is recorded until all checks above pass.
