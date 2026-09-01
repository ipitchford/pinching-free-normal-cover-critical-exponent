# AIM-TOPOLOGY-0203: revised all-Fuchsian release candidate

This directory contains a complete anonymous, AI-assisted, unrefereed
all-Fuchsian strengthening candidate related to M. Kapovich's AIM Problem 4.3:
construct an infinitely
generated Fuchsian group of the first kind whose critical exponent is not
constant among the Fuchsian points of its reduced quasiconformal Teichmuller
space.

The construction fixes the kernel of a surface-group epimorphism onto a free
group.  The corresponding regular covers remain in one reduced,
surface-based quasiconformal Teichmuller space as the closed base metric
varies.  Nonamenability of the
deck group forces every marked compact-base exponent to be strictly below one,
while
simultaneously pinching a cut system produces compactly supported collar test
functions whose Rayleigh quotients are `O_g(ell)`.  The
Elstrodt--Patterson--Sullivan formula then forces the exponents to tend to one.

## Read first

- `paper.pdf`: typeset reader manuscript (generated during the build gate).
- `paper.tex`: canonical LaTeX manuscript.
- `paper.md`: accessible-text fallback; mathematics is linearized plain text,
  not fully semantic math.
- `PROOF_OBLIGATIONS.md`: claim-by-claim proof ledger.
- `CLAIM_SCOPE.md`: exact claim and assurance boundary.
- `NOVELTY_REPORT.md`: bounded literature search, including nearby results.
- `SOURCES.md`: source and theorem-dependency ledger.
- `ASSURANCE.md`: what has and has not been checked.

## Replay

The mathematical sanity check uses only Python's standard library:

```sh
python3 verify_estimates.py
python3 -m unittest -v tests/test_mutations.py
```

After the PDF is built, the complete read-only package gate is:

```sh
bash run_all.sh
```

Finite numerical replay corroborates the explicit collar identities and
inequalities.  The theorem itself rests on the written proof and the cited
external results; the program is not a proof assistant.

## Status

Revised after a supplied workflow review and internal model-mediated editorial
review; anonymous, AI-assisted, unrefereed release candidate. The supplied
review is not authenticated specialist review, independent reconstruction, or
peer review.
Publication records and public identifiers are documented in `STATUS.md` and
the release metadata when assigned. They do not imply external specialist
validation, independent reconstruction, formal verification, or peer review.
