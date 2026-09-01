# Proof-obligation ledger

| ID | Obligation | Discharge | Evidence class |
|---|---|---|---|
| P1 | The map `q : pi_1(S_g) -> F_g` is a surjection. | The surface relator maps to the identity and the images of the `a_i` generate `F_g`. | Direct proof |
| P2 | `K` is nontrivial, normal, and infinite index. | It is a kernel, contains every `b_i`, and has quotient `F_g`. | Direct proof |
| P3 | `Gamma_m` is of the first kind. | A nontrivial normal subgroup of a cocompact Fuchsian group has the same limit set. | Standard lemma, proved in the manuscript |
| P4 | `Gamma_m` is infinitely generated. | Finite generation plus absence of parabolics would imply convex cocompactness; full limit set would then make the cover compact and hence finite-sheeted, contradicting quotient `F_g`. | Standard Fuchsian-group fact plus direct contradiction |
| P5 | All marked covers occur in one `T_qc^red(X0)` and in the all-Fuchsian locus of the AIM group-deformation space `T_qc(Gamma_0)`. | An orientation- and marking-preserving quasiconformal map between compact bases lifts equivariantly, conjugates the fixed subgroup `K`, and descends to `X0 -> X_m`; reflection gives a sphere map conjugating `Gamma_0` to `Gamma_m`. Reduced surface equivalence lifts to marked Mobius conjugacy, which preserves critical exponent. | Direct lift, reflection, and descent argument |
| P6 | Every marked compact-base exponent is below one. | Dougall--Sharp Theorem 1.1: `H^2` is a pinched Hadamard manifold; `L_m` is nonelementary and cocompact, hence convex cocompact; `Gamma_m` is normal; and `L_m/Gamma_m = F_g` is nonamenable for `g >= 2`. Therefore equality of exponents is impossible. | Cited theorem with hypothesis map |
| P7 | A simultaneous pinching path exists. | Extend the cut system to a pants decomposition and prescribe the `b_i` lengths by Fenchel--Nielsen coordinates. | Standard theorem |
| P8 | The lifted cut surface is a compact cell. | Cutting along the `b_i` gives a sphere with `2g` boundary components; copies indexed by `F_g` reconstruct the regular cover. | Direct covering construction |
| P9 | The test function is admissible. | It is compactly supported and Lipschitz, has zero trace on the cell seams, and is approximable in `H^1` by compactly supported smooth functions. | Direct Sobolev argument |
| P10 | Fixed-width collar energy equals `2g ell sinh(1)`. | On each of `2g` half-collars integrate `|du/dr|^2=1` against `ell cosh(r) dr dtheta` over `0<r<1`. | Direct calculation; executable corroboration |
| P11 | The plateau denominator stays positive. | Gauss--Bonnet gives area `4 pi(g-1)`; deleting the `2g` unit transition strips leaves `D_ell=4 pi(g-1)-2g ell sinh(1)`, at least `2 pi(g-1)` for small `ell`. | Direct calculation; executable corroboration |
| P12 | `lambda_0 <= C_g ell`. | Apply the Rayleigh principle to P10 and P11, with `C_g=g sinh(1)/(pi(g-1))`. | Direct proof |
| P13 | The exponents tend to one. | Sullivan Theorem 2.17, p. 333: `Gamma_ell` is torsion-free, discrete, and nonelementary; `H^2/Gamma_ell` is complete of curvature `-1`; and the nonnegative-Laplacian convention is used. The formula rules out `delta <= 1/2` once `lambda_0 < 1/4`; then `lambda_0=delta(1-delta)` and `1-delta <= 2 lambda_0`. | Cited theorem with hypothesis map plus direct algebra |
| P14 | The exponent is nonconstant. | All values are below one while a sequence tends to one; in fact the sequence has infinitely many distinct values. | Direct consequence |

No executable check is promoted above its evidence class.  In particular,
P3--P9 and P13 are semantic mathematical obligations, not conclusions of the
finite replay program.

The exact AIM Problem 4.3 statement is reproduced in the manuscript. Under the
broad group-deformation reading, Astala--Zinsmeister (1995) appears already to
supply an affirmative existential precedent. P5 establishes the narrower new
contribution: a fixed-kernel family that stays in the all-Fuchsian locus.
