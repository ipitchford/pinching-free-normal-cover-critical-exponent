# Claim scope

## Main claim

For every integer `g >= 2`, let `S_g` be a closed oriented surface with a
geometric symplectic basis `(a_i,b_i)` such that the `b_i` form a disjoint cut
system.  Let

```text
q : pi_1(S_g) -> F_g,
q(a_i) = x_i,
q(b_i) = 1,
K = ker(q).
```

For each marked closed hyperbolic metric `m`, let `rho_m` be its Fuchsian
holonomy and `Gamma_m = rho_m(K)`.  The associated regular cover has deck
group `F_g`.  Then:

1. `Gamma_m` is infinitely generated and of the first kind.
2. The marked covers `X_m` give Fuchsian points in one reduced,
   surface-based space `T_qc^red(X0)` and, by reflected sphere extensions, in
   the all-Fuchsian locus of the AIM group-deformation space `T_qc(Gamma_0)`.
3. The critical exponent is not constant on this family.
4. More precisely, along a path on which all `b_i` have common length
   `ell -> 0`, one has, for all sufficiently small `ell`,

   ```text
   1/2 < delta(Gamma_ell) < 1,
   1 - delta(Gamma_ell) = O_g(ell),
   delta(Gamma_ell) -> 1.
   ```

Under the broad group-deformation reading, Astala--Zinsmeister (1995) appears
already to supply an affirmative existential example. This theorem is an
all-Fuchsian strengthening and alternative construction; it supplies the
example requested by AIM Problem 4.3 under the reduced surface-based,
all-Fuchsian reading.

## Explicit exclusions

- No monotonicity or exact formula for `delta(Gamma_ell)` is claimed.
- No classification of all first-kind infinitely generated Fuchsian groups is
  claimed.
- The family induced from `Teich(S_g)` is not claimed to embed injectively in
  the infinite-type quasiconformal Teichmuller space.
- A reflected sphere extension represents the same marked Fuchsian point; no
  claim is made about arbitrary quasi-Fuchsian deformations in `PSL(2,C)`.
- No historical-priority, external-validation, formal-verification, or
  peer-review claim is made.
- `ell=0` is a boundary degeneration, not a metric or point in the asserted
  family.
