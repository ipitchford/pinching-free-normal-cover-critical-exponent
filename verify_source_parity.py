#!/usr/bin/env python3
"""Check theorem-critical facts across the LaTeX and Markdown surfaces."""

from __future__ import annotations

import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parent

SURFACES = {
    "paper.tex": (
        r"q(a_i)=x_i",
        r"q(b_i)=1",
        r"T_{\mathrm{qc}}^{\mathrm{red}}",
        r"\delta(\Gamma_m)<\delta(L_m)=1",
        r"2g\ell\sinh1",
        r"4\pi(g-1)-2g\ell\sinh1",
        r"\le2C_g\ell",
        r"$\delta(\Gamma_\ell)\to1$",
        r"T_{\rm qc}(\Gamma_{m_0})",
        "AstalaZinsmeister1995",
    ),
    "paper.md": (
        "q(a_i)=x_i, q(b_i)=1",
        "T_qc^red(X0)",
        "delta(Gamma_m) < 1",
        "E_ell = 2g ell sinh(1)",
        "D_ell = 4 pi(g-1) - 2g ell sinh(1)",
        "<= 2C_g ell",
        "delta(Gamma_ell) -> 1",
        "does not claim monotonicity",
        "T_qc(Gamma_m0)",
        "all-Fuchsian strengthening",
    ),
    "CLAIM_SCOPE.md": (
        "deck group",
        "T_qc^red",
        "1/2 < delta(Gamma_ell) < 1",
        "No monotonicity",
        "No historical-priority",
    ),
}


def main() -> int:
    failures: list[str] = []
    for relative, markers in SURFACES.items():
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"missing {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        failures.extend(
            f"{relative}: missing {marker!r}"
            for marker in markers
            if marker not in normalized
        )
    if failures:
        print("FAIL: source parity", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print("PASS: theorem-critical source markers agree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
