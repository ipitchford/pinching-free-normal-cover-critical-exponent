#!/usr/bin/env python3
"""Corroborate the explicit collar calculations in the AIM 4.3 proof.

This program does not verify the cited normal-subgroup or spectral theorems,
nor does finite sampling prove the universal asymptotic statement.  It checks
the algebraic identities, domain assumptions, factors, signs, and sample
inequalities used by the written proof.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from typing import Iterable


@dataclass(frozen=True)
class ModelAssumptions:
    genus: int
    deck_free_rank: int
    half_collar_count: int
    full_collar_count: int
    seam_trace: float = 0.0
    transition_width: float = 1.0

    @classmethod
    def canonical(cls, genus: int) -> "ModelAssumptions":
        return cls(
            genus=genus,
            deck_free_rank=genus,
            half_collar_count=2 * genus,
            full_collar_count=genus,
            seam_trace=0.0,
            transition_width=1.0,
        )

    def validate(self) -> None:
        if self.genus < 2:
            raise ValueError("the construction requires genus at least two")
        if self.deck_free_rank != self.genus or self.deck_free_rank < 2:
            raise ValueError("the deck group must be the nonabelian free group F_g")
        if self.half_collar_count != 2 * self.genus:
            raise ValueError("the cut cell must contain exactly 2g half-collars")
        if self.full_collar_count != self.genus:
            raise ValueError("the closed base must contain exactly g full collars")
        if self.seam_trace != 0.0:
            raise ValueError("extension by zero requires zero trace at every seam")
        if not math.isfinite(self.transition_width) or self.transition_width <= 0.0:
            raise ValueError("transition width must be finite and positive")


def validate_length(ell: float) -> None:
    if not math.isfinite(ell) or ell <= 0.0:
        raise ValueError("ell must be a finite positive length")


def collar_half_width(ell: float) -> float:
    validate_length(ell)
    return math.asinh(1.0 / math.sinh(ell / 2.0))


def transition_strip_area(model: ModelAssumptions, ell: float) -> float:
    model.validate()
    validate_length(ell)
    return ell * math.sinh(model.transition_width)


def plateau_area(model: ModelAssumptions, ell: float) -> float:
    return 4.0 * math.pi * (model.genus - 1) - (
        model.half_collar_count * transition_strip_area(model, ell)
    )


def half_collar_energy(model: ModelAssumptions, ell: float) -> float:
    model.validate()
    validate_length(ell)
    return ell * math.sinh(model.transition_width) / (model.transition_width**2)


def test_energy(model: ModelAssumptions, ell: float) -> float:
    model.validate()
    if collar_half_width(ell) <= model.transition_width:
        raise ValueError("the collar must be wider than the fixed transition")
    return model.half_collar_count * half_collar_energy(model, ell)


def rayleigh_core_upper_bound(model: ModelAssumptions, ell: float) -> float:
    denominator = plateau_area(model, ell)
    if denominator <= 0.0:
        raise ValueError("the selected cell leaves no positive plateau area")
    return test_energy(model, ell) / denominator


def close(a: float, b: float, *, rel: float = 2e-13, abs_: float = 1e-14) -> bool:
    return math.isclose(a, b, rel_tol=rel, abs_tol=abs_)


def sample_record(genus: int, ell: float) -> dict[str, float | int]:
    model = ModelAssumptions.canonical(genus)
    model.validate()
    w = collar_half_width(ell)
    energy = test_energy(model, ell)
    area = plateau_area(model, ell)
    rayleigh = rayleigh_core_upper_bound(model, ell)

    collar_identity_left = math.sinh(w)
    collar_identity_right = 1.0 / math.sinh(ell / 2.0)
    energy_integral_form = model.half_collar_count * (
        ell * math.sinh(model.transition_width) / (model.transition_width**2)
    )
    if not close(collar_identity_left, collar_identity_right):
        raise AssertionError("collar-width identity failed")
    if not close(energy, energy_integral_form):
        raise AssertionError("fixed-width energy identity failed")
    if not w > model.transition_width:
        raise AssertionError("sample collar does not contain the transition")
    if not area > 0.0:
        raise AssertionError("core-area denominator must be positive")
    explicit_constant = genus * math.sinh(1.0) / (math.pi * (genus - 1))
    if area >= 2.0 * math.pi * (genus - 1) and rayleigh > explicit_constant * ell:
        raise AssertionError("explicit linear Rayleigh bound failed")

    return {
        "genus": genus,
        "ell": ell,
        "half_width": w,
        "plateau_area": area,
        "energy": energy,
        "rayleigh_core_upper_bound": rayleigh,
        "rayleigh_over_ell": rayleigh / ell,
        "explicit_linear_constant": explicit_constant,
        "width_minus_log4_over_ell": w - math.log(4.0 / ell),
    }


def run_samples(
    genera: Iterable[int] = range(2, 9),
    lengths: Iterable[float] = (1e-1, 1e-2, 1e-3, 1e-4, 1e-6, 1e-8),
) -> dict[str, object]:
    genera = tuple(genera)
    lengths = tuple(lengths)
    records = [sample_record(g, ell) for g in genera for ell in lengths]

    for genus in genera:
        genus_records = [row for row in records if row["genus"] == genus]
        rayleigh_values = [float(row["rayleigh_core_upper_bound"]) for row in genus_records]
        if any(
            later >= earlier
            for earlier, later in zip(rayleigh_values, rayleigh_values[1:])
        ):
            raise AssertionError("sampled Rayleigh bounds must fall as ell decreases")

    return {
        "status": "PASS",
        "evidence_class": "finite corroboration of explicit formulas only",
        "model": asdict(ModelAssumptions.canonical(2)),
        "sample_count": len(records),
        "records": records,
        "not_verified": [
            "Dougall-Sharp theorem",
            "Elstrodt-Patterson-Sullivan formula",
            "topology of the covering construction",
            "quasiconformal deformation-space semantics",
            "historical novelty or priority",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()
    result = run_samples()
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("PASS: 42 collar-model samples")
        print("Evidence class: finite corroboration of explicit formulas only")
        last = result["records"][-1]
        print(
            "Final sample: "
            f"g={last['genus']}, ell={last['ell']:.0e}, "
            f"R<={last['rayleigh_core_upper_bound']:.12g}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
