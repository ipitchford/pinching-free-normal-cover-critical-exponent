# Pinching a free normal cover: variable critical exponent in reduced quasiconformal Teichmuller space

**Anonymous candidate contribution — 1 September 2026**

**Status.** Anonymous, AI-assisted, unrefereed all-Fuchsian strengthening
candidate. The package
contains a complete written proof and producer-side formula checks, but no
claim of historical priority, external specialist validation, independent
reconstruction, formal proof verification, or peer review. Candidate
publication and DOI assignment do not alter those assurance limits.

## Abstract

For every closed oriented surface `S_g` of genus `g >= 2`, fix the kernel `K`
of the epimorphism `pi_1(S_g) -> F_g` that kills a disjoint cut system. For
every marked closed hyperbolic metric `m`, the Fuchsian image `Gamma_m` of `K`
is infinitely generated and of the first kind. Marked quasiconformal maps of
the compact base lift to quasiconformal conjugacies of these groups, so the
family lies in one reduced, surface-based quasiconformal Teichmuller space.
Nonamenability of `F_g`
forces the critical exponent below one for every marked compact-base metric.
Simultaneously pinching
the cut curves to common length `ell` gives a compactly supported collar test
function with Rayleigh quotient `O_g(ell)`. The
Elstrodt--Patterson--Sullivan formula yields

```text
1/2 < delta(Gamma_ell) < 1,
1 - delta(Gamma_ell) = O_g(ell),
delta(Gamma_ell) -> 1.
```

Thus the critical exponent assumes infinitely many values among the
all-Fuchsian points of one reduced quasiconformal Teichmuller space. Under the
reduced surface-based reading of the AIM question this is a direct solution
candidate; under the broader group-deformation reading it is an all-Fuchsian
strengthening of an affirmative precedent of Astala and Zinsmeister.

## 中文摘要（繁體）

對每個虧格 `g >= 2` 的閉可定向曲面，固定一個通往非阿貝爾自由群之滿同態
的核；此滿同態消去一組互不相交的割曲線。相應的正常覆蓋在所有有標記的
閉雙曲度量下皆給出第一類且無限生成的 Fuchsian 群，並且位於同一約化擬共形
Teichmuller 空間。商自由群的非可均性迫使每一有限階段的臨界指數小於一；同時壓縮
割曲線則產生趨近零的 Rayleigh 商。譜公式遂推出臨界指數從下方趨近一，故
在同一變形空間中取得無限多個不同值。

**Translation note.** The Traditional Chinese abstract is a producer-generated
rendering and was not independently assessed by a Chinese language reviewer;
the English abstract controls if the two differ.

## Problem context and deformation-space convention

Kapovich's Problem 4.3 arose at the 2012 AIM workshop, appears in the
accessible AIM problem document dated 2014, and was published by Weixu Su in
handbook form in 2016. It asks whether the critical exponent can vary in the
reduced quasiconformal Teichmuller space of an infinitely generated,
first-kind Fuchsian surface.

Its exact statement is: “Construct an infinitely generated Fuchsian group
`Gamma_0` of the first kind such that the critical exponents of some elements
in `T_qc(Gamma_0)` are different.”

The critical exponent measures exponential orbit growth: roughly, how rapidly
the number of group translates within distance `R` grows with `R`. A full
boundary-circle limit set does not force exponent one for an infinitely
generated group. Pinching the cut curves creates long collars, allowing a
function concentrated on one lifted cell to have very low spectral energy;
the spectral formula then drives the exponent toward one.

Under a broad group-deformation reading, Astala and Zinsmeister's 1995
quasi-Fuchsian family appears already to give an affirmative existential
example. No first-solution or priority claim is made here. The present result
is an all-Fuchsian strengthening and alternative; it is a direct solution
candidate under the reduced surface-based, all-Fuchsian reading.

Fix a base metric `m0` and set `X0=X_m0`. Here
`T_qc^red(X0)` means the reduced, surface-based marked quasiconformal
Teichmuller space: a point is an equivalence class of a marked conformal
surface `(Y,f)`, where `f:X0 -> Y` is quasiconformal, and two markings are
equivalent when their transition map is homotopic to a conformal map. The
reduced convention preserves boundary components setwise rather than
pointwise; the present surfaces have no boundary, so that distinction is
moot. The theorem concerns the Fuchsian uniformising groups of the marked
surfaces below, not arbitrary quasi-Fuchsian sphere conjugates.

For comparison with the AIM notation, `T_qc(Gamma_0)` denotes the reduced group
quasiconformal deformation space: a quasiconformal sphere map conjugating
`Gamma_0` to a Kleinian group determines a point, modulo marked Mobius
conjugacy. Mobius conjugacy preserves critical exponent. The lifted disk maps
below extend by reflection to sphere maps conjugating `Gamma_0` to `Gamma_m`.
Thus every marked compact-base metric produces a point in the all-Fuchsian
locus of the AIM group space. This does not claim a global identification of
all group deformations with the surface-based space.

## 1. Construction

Choose a geometric symplectic basis
`(a_1,b_1,...,a_g,b_g)` such that the `b_i` are disjoint and their complement
is connected. Define

```text
q : pi_1(S_g) -> F_g = <x_1,...,x_g>,
q(a_i)=x_i, q(b_i)=1,
K=ker(q).
```

The surface relator maps to the identity, and the images of the `a_i`
generate, so `q` is onto. Thus

```text
1 -> K -> pi_1(S_g) -> F_g -> 1
```

is exact. For a marked hyperbolic metric `m`, let `rho_m` be
the Fuchsian holonomy, `L_m=rho_m(pi_1(S_g))`,
`Gamma_m=rho_m(K)`, and `X_m=H^2/Gamma_m`. Then `X_m -> H^2/L_m` is the
regular `F_g`-cover, with exact sequence

```text
1 -> Gamma_m -> L_m -> F_g -> 1.
```

The subgroup `Gamma_m` is nontrivial and normal in the cocompact lattice
`L_m`. Its limit set is a nonempty closed `L_m`-invariant subset of the
boundary circle. Minimality of the ambient limit set gives
`Lambda(Gamma_m)=S^1`, so `Gamma_m` is nonelementary and of the first kind.

If `Gamma_m` were finitely generated, then—having no parabolics—it would be
convex cocompact. Its full limit set would make all of `H^2/Gamma_m` compact.
A compact cover of the compact base has finite degree, contradicting the
infinite deck group `F_g`. Thus `Gamma_m` is infinitely generated.

For any two marked base metrics, an orientation- and marking-preserving
quasiconformal map of the closed surfaces lifts equivariantly to the disk. The lift conjugates the
full holonomies and therefore their restrictions to the fixed subgroup `K`;
it descends to a marked quasiconformal map `X0 -> X_m`. Hence `X_m`
represents a point of `T_qc^red(X0)`, uniformised by `Gamma_m`. Boundary
quasisymmetry and reflection give a sphere representative `W_m` satisfying
`W_m Gamma_m0 W_m^-1 = Gamma_m`, hence a point of `T_qc(Gamma_m0)` in the
original AIM notation. The markings identify the same abstract kernel `K`.
Equivalent surface representatives have Mobius-conjugate uniformising groups,
so their critical exponents agree. This does not enlarge the theorem to arbitrary
quasi-Fuchsian conjugates. No injectivity of the compact-base family into the
infinite-type Teichmuller space is claimed.

## 2. Every compact-base exponent is below one

The cocompact group `L_m` has critical exponent one. Dougall and Sharp's
normal-subgroup theorem says that a normal subgroup of a convex-cocompact
group has the same exponent as the ambient group exactly when the quotient is
amenable. Here `H^2` is complete, simply connected, and has curvature `-1`;
`L_m` is nonelementary and cocompact, hence convex cocompact; `Gamma_m` is
normal; and `L_m/Gamma_m` is the nonamenable group `F_g`, since `g >= 2`.
Therefore

```text
delta(Gamma_m) < 1
```

for every marked metric `m`.

## 3. Pinching and the Rayleigh quotient

Extend the cut system to a pants decomposition and use Fenchel--Nielsen
coordinates to choose metrics `m_ell` with every `b_i` of length `ell -> 0`.
Cutting along the `b_i` gives a compact sphere with `2g` boundary components.
Copies indexed by `F_g` form the regular cover. More explicitly, `a_i` is
dual to `b_i`; after cutting, it is an arc joining the two boundary copies of
`b_i`, crosses no other cut curve, and has monodromy `q(a_i)=x_i`. Therefore
crossing that side changes a cell label from `h` to `hx_i` (up to the chosen
orientation).

The standard collar half-width and metric are

```text
w(ell) = arcsinh(1/sinh(ell/2))
       -> infinity as ell -> 0,
ds^2 = dr^2 + ell^2 cosh^2(r) dtheta^2.
```

For sufficiently small `ell`, `w(ell)>1`. On each of the `2g` selected-cell
half-collars define

```text
u(r) = r   for 0 <= r <= 1,
u(r) = 1   for 1 <= r < w(ell).
```

Set `u=1` on the remainder of the selected cell and `u=0` outside it. It is
compactly supported and Lipschitz, with matching zero traces across the seams;
it lies in `H^1_c` and is admissible for the Rayleigh principle by smooth
approximation.

One half-collar has energy

```text
integral |grad u|^2 dA
= integral_0^1 ell cosh(r) dr
= ell sinh(1).
```

Thus the total energy is

```text
E_ell = 2g ell sinh(1).
```

The base surface has area `4 pi(g-1)`. Each width-one transition strip has
area `ell sinh(1)`, so the plateau on which `u=1` has area at least

```text
D_ell = 4 pi(g-1) - 2g ell sinh(1).
```

Whenever `2g ell sinh(1) <= 2 pi(g-1)`, we have
`D_ell >= 2 pi(g-1)`. Since `u=1` on this
plateau, the Rayleigh principle gives the explicit estimate

```text
C_g = g sinh(1)/(pi(g-1)),
lambda_0(X_ell) <= C_g ell -> 0.
```

## 4. Spectral conversion and the all-Fuchsian conclusion

For a nonelementary Fuchsian group, in the nonnegative-Laplacian convention,

```text
lambda_0 = 1/4                         if delta <= 1/2,
lambda_0 = delta(1-delta)              if delta >= 1/2.
```

Sullivan's Theorem 2.17 applies because `Gamma_ell` is torsion-free, discrete,
and nonelementary, `X_ell` is a complete curvature-`-1` surface, and the
nonnegative Laplacian is used. For small `ell`, the constructed upper bound is below `1/4`, so
`delta(Gamma_ell)>1/2`. The strict ambient comparison gives
`delta(Gamma_ell)<1`, and hence

```text
1-delta(Gamma_ell)
= lambda_0(X_ell)/delta(Gamma_ell)
< 2 lambda_0(X_ell)
<= 2C_g ell.
```

Therefore `delta(Gamma_ell) -> 1` from below. No value belonging to a marked
compact-base metric is one, so
the values along a sequence `ell_n -> 0` cannot form a finite set. The
critical exponent takes infinitely many distinct values among the Fuchsian
points of `T_qc^red(X0)`. This is the all-Fuchsian strengthening described
above and, under the reduced surface-based reading, answers AIM Problem 4.3.

The proof does not claim monotonicity or an exact formula for the exponent.
The symbol `ell=0` is a boundary degeneration, not a metric or point in the
asserted family.

## Relation to previous work

Astala and Zinsmeister (1995) used a normal cover of a compact genus-three
surface with abelian deck group `Z^3` and holomorphic quasi-Fuchsian
deformations to exhibit variation of the Poincare exponent, including values
above one. Under a broad group-deformation reading, that appears already to
answer the existential AIM question. The present result is therefore an
all-Fuchsian strengthening and alternative construction, and a direct solution
candidate only under the reduced surface-based, all-Fuchsian reading. It is not
the same family: here the deck group is the nonamenable free group `F_g`, every
compact-base exponent is below one, and
pinching makes the exponents approach one from below. Bishop's
`delta`-stability results and Huo--Zinsmeister's later Ruelle-property work
concern the relation between exponent, limit-set dimension, and
quasi-Fuchsian deformation. Bonfert-Taylor, Matsuzaki, and Taylor study
regular covers and the sharp lower threshold `1/2` for their exponents.

These results delimit the contribution. The claim here is the fixed-kernel,
all-Fuchsian pinching construction in reduced surface-based quasiconformal
Teichmuller space, not a general deformation or stability theorem. No exact
collision was located in the bounded search, but that is not a priority claim.

## Declarations

- **Data and materials:** no empirical data; all manuscript and replay files
  are in the research package. Public repository:
  `https://github.com/ipitchford/pinching-free-normal-cover-critical-exponent`;
  version DOI: `https://doi.org/10.5281/zenodo.22229561`. The PDF is visually checked but untagged;
  `paper.md` is the accessible-text fallback, with linearized plain-text rather
  than fully semantic mathematics. Public repository and archival identifiers,
  these identifiers do not increase the mathematical assurance level.
- **Ethics:** no human participants, personal data, animals, clinical
  material, or field interventions were used.
- **Author contributions (CRediT):** Anonymous candidate contribution —
  Conceptualization, Formal analysis, Methodology, Software, Validation,
  Writing—original draft, Writing—review and editing.
- **Funding:** none declared.
- **Competing interests:** none declared.
- **AI use:** OpenAI Codex assisted with source search, proof development,
  stress testing, drafting, typesetting, checks, and package assembly. This is
  producer-side work, not independent mathematical validation.

## Principal references

- W. Su, *Problems on Thurston Metric* (AIM problem document dated 2014;
  originating workshop 2012), Problem 4.3; and *Problems on the Thurston
  metric*, in *Handbook of Teichmuller Theory V* (2016), 55–72,
  DOI `10.4171/160-1/3`.
- K. Astala and M. Zinsmeister, *Abelian coverings, Poincare exponent of
  convergence and holomorphic deformations*, Ann. Acad. Sci. Fenn. 20 (1995),
  81–86.
- P. Bonfert-Taylor, K. Matsuzaki, and E. C. Taylor, *Large and small covers
  of a hyperbolic manifold*, J. Geom. Anal. 22 (2012), 455–470.
- S. Huo and M. Zinsmeister, *On Ruelle's property*, Ergodic Theory Dynam.
  Systems 42 (2022), 1474–1486.
- R. Dougall and R. Sharp, *Amenability, critical exponents of subgroups and
  growth of closed geodesics*, Math. Ann. 365 (2016), 1359–1377.
- D. Sullivan, *Related aspects of positivity in Riemannian geometry*, J.
  Differential Geom. 25 (1987), 327–351.
- L. Keen, *Collars on Riemann surfaces* (1974).
- P. Buser, *Geometry and Spectra of Compact Riemann Surfaces* (1992).
