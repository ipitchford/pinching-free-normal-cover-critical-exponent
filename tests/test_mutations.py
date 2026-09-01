#!/usr/bin/env python3

import math
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from verify_estimates import (  # noqa: E402
    ModelAssumptions,
    collar_half_width,
    plateau_area,
    rayleigh_core_upper_bound,
    run_samples,
    test_energy,
    transition_strip_area,
)


class FormulaTests(unittest.TestCase):
    def test_canonical_sample_suite(self) -> None:
        result = run_samples()
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["sample_count"], 42)

    def test_collar_identity(self) -> None:
        for ell in (0.1, 0.01, 1e-4, 1e-8):
            w = collar_half_width(ell)
            self.assertTrue(
                math.isclose(
                    math.sinh(w),
                    1.0 / math.sinh(ell / 2.0),
                    rel_tol=2e-13,
                )
            )

    def test_unit_transition_strip_area(self) -> None:
        model = ModelAssumptions.canonical(2)
        self.assertAlmostEqual(
            transition_strip_area(model, 0.01), 0.01 * math.sinh(1.0)
        )

    def test_plateau_area_tends_to_base_area(self) -> None:
        model = ModelAssumptions.canonical(2)
        self.assertAlmostEqual(plateau_area(model, 1e-12), 4.0 * math.pi, places=10)

    def test_energy_has_two_halves_per_cut_curve(self) -> None:
        model = ModelAssumptions.canonical(3)
        ell = 0.01
        expected = 6.0 * ell * math.sinh(1.0)
        self.assertTrue(math.isclose(test_energy(model, ell), expected))

    def test_rayleigh_bound_decays_on_samples(self) -> None:
        model = ModelAssumptions.canonical(2)
        coarse = rayleigh_core_upper_bound(model, 1e-2)
        fine = rayleigh_core_upper_bound(model, 1e-8)
        self.assertLess(fine, coarse)


class MutationRejectionTests(unittest.TestCase):
    def assertRejected(self, model: ModelAssumptions) -> None:  # noqa: N802
        with self.assertRaises(ValueError):
            model.validate()

    def test_genus_one_is_rejected(self) -> None:
        self.assertRejected(ModelAssumptions.canonical(1))

    def test_amenable_deck_rank_is_rejected(self) -> None:
        self.assertRejected(ModelAssumptions(2, 1, 4, 2, 0.0))

    def test_missing_half_collars_are_rejected(self) -> None:
        self.assertRejected(ModelAssumptions(2, 2, 2, 2, 0.0))

    def test_extra_full_collar_is_rejected(self) -> None:
        self.assertRejected(ModelAssumptions(2, 2, 4, 3, 0.0))

    def test_nonzero_seam_trace_is_rejected(self) -> None:
        self.assertRejected(ModelAssumptions(2, 2, 4, 2, 1.0))

    def test_nonpositive_length_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            collar_half_width(0.0)

    def test_nonfinite_length_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            rayleigh_core_upper_bound(ModelAssumptions.canonical(2), math.nan)

    def test_plateau_formula_uses_all_half_collars(self) -> None:
        model = ModelAssumptions.canonical(2)
        ell = 0.01
        expected = 4.0 * math.pi - 4.0 * ell * math.sinh(1.0)
        self.assertTrue(math.isclose(plateau_area(model, ell), expected))

    def test_transition_wider_than_collar_is_rejected(self) -> None:
        model = ModelAssumptions(2, 2, 4, 2, 0.0, 10.0)
        with self.assertRaises(ValueError):
            rayleigh_core_upper_bound(model, 0.1)

    def test_nonpositive_plateau_is_rejected(self) -> None:
        model = ModelAssumptions.canonical(2)
        with self.assertRaises(ValueError):
            rayleigh_core_upper_bound(model, 10.0)


if __name__ == "__main__":
    unittest.main()
