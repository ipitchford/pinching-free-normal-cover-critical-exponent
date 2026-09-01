# Source and theorem-dependency ledger

Search and access date: **1 September 2026**.

## Decisive sources

| Source | Exact use | Inspection record |
|---|---|---|
| W. Su, *Problems on Thurston Metric*, Problem 4.3, attributed to M. Kapovich | Exact originating problem statement; 2012 workshop origin and document dated 21 April 2014 | Primary PDF inspected; SHA-256 `3657833c65d9b103451da6595624a726609ded826405c989b7e632478ae9691e`; 159,761 bytes; [source](https://aimath.org/pastworkshops/lipschitzteichproblems.pdf) |
| W. Su, *Problems on the Thurston Metric* (2016) | Published problem formulation and reduced quasiconformal Teichmuller-space context | EMS publisher record inspected; pp. 55--72; DOI `10.4171/160-1/3`; [record](https://ems.press/content/book-chapter-files/23469) |
| R. Dougall and R. Sharp, *Amenability, Critical Exponents of Subgroups and Growth of Closed Geodesics*, Theorem 1.1 | For a normal subgroup of a convex-cocompact group, equality of critical exponents is equivalent to amenability of the quotient | arXiv v3 primary PDF inspected; SHA-256 `04b53f8bbf3a2ca8ab7ed92d5cc3eb2f3221178a48179a7b255cde70d76817c4`; 241,425 bytes; [article](https://doi.org/10.1007/s00208-015-1338-1), [arXiv](https://arxiv.org/abs/1411.6817) |
| D. Sullivan, *Related Aspects of Positivity in Riemannian Geometry*, Theorem 2.17 | The bottom-of-spectrum/critical-exponent formula, translated to the nonnegative-Laplacian convention | Author-hosted primary PDF inspected; SHA-256 `102340ea0f063307534a7745782aa4f1e7cacfb24beff206c6cfb0cc7da5fa61`; 1,942,113 bytes; [source](https://www.math.stonybrook.edu/~dennis/publications/PDF/DS-pub-0082.pdf) |
| L. Keen, *Collars on Riemann Surfaces* | Standard collar lemma | Publisher record and theorem restatements inspected; [chapter](https://doi.org/10.1515/9781400881642-021) |
| P. Buser, *Geometry and Spectra of Compact Riemann Surfaces* | Standard collar coordinates and finite-type hyperbolic background | Bibliographic reference; DOI `10.1007/978-0-8176-4992-0` |
| A. F. Beardon, *The Geometry of Discrete Groups* | Standard fact that a finitely generated Fuchsian group without parabolics is convex cocompact | Bibliographic reference; DOI `10.1007/978-1-4612-1146-4` |
| D. Alessandrini, L. Liu, A. Papadopoulos, and W. Su, *On Various Teichmuller Spaces of a Surface of Infinite Topological Type* | Terminology and context for quasiconformal Teichmuller space | Primary author copy/arXiv record inspected; DOI `10.1090/S0002-9939-2011-10918-3` |

## Adjacent sources, not proof dependencies

| Source | Why adjacent | Why it is not the present theorem |
|---|---|---|
| C. J. Bishop, *delta-Stable Fuchsian Groups* (2003) | Infinitely generated first-kind groups and critical exponents under quasiconformal/quasi-Fuchsian deformation | Its principal deformation result concerns quasi-Fuchsian groups in `PSL(2,C)` and `delta`-stability, not distinct Fuchsian exponents in one `T_qc`; primary PDF SHA-256 `38ffad587d1d2087f30338a786f625e37db96e7dffbb3d34985b7295bec1ef6d` |
| K. Astala and M. Zinsmeister, *Abelian Coverings, Poincare Exponent of Convergence and Holomorphic Deformations* (1995) | Closest located prior exponent variation for an infinitely generated normal-cover group and apparent affirmative precedent under the broad group-deformation reading of AIM Problem 4.3 | Uses abelian deck group `Z^3` and holomorphic quasi-Fuchsian deformation, including exponents above one; not the present all-Fuchsian free-cover pinching family; primary PDF SHA-256 `4f0b0893bb44de2d97a23f40dda92458852ddacab1cfef680a2647f44db5c98e` |
| P. Bonfert-Taylor, K. Matsuzaki, and E. C. Taylor, *Large and Small Covers of a Hyperbolic Manifold* (2012) | Regular-cover exponent bounds and sharp lower threshold `1/2` | Does not state variation along a fixed-kernel all-Fuchsian pinching family; DOI `10.1007/s12220-010-9204-6`; author-hosted primary preprint inspected |
| S. Huo and M. Zinsmeister, *On Ruelle's Property* (2022) | Later Ruelle-property and quasi-Fuchsian deformation context | Does not give the present all-Fuchsian reduced-space construction; primary PDF SHA-256 `accdff76f9c544e6b606aea90eca90aa265cd1431fed251741442ac7b09baef4`; DOI `10.1017/etds.2020.149` |
| R. Lehnert, *On the Critical Exponent of Infinitely Generated Veech Groups* (2017) | Gives infinitely generated first-kind Fuchsian groups with exponent strictly between `1/2` and `1` | Does not establish variation of the exponent within a fixed quasiconformal deformation space |

## Convention audit

- Curvature is `-1`.
- The Laplacian is nonnegative and `lambda_0` is defined by the Rayleigh
  quotient.
- The critical exponent is the Poincare-series abscissa.
- Sullivan's original displayed formula is read in the corresponding
  nonnegative convention as `delta(1-delta)` above the `1/2` threshold and
  `1/4` below it.
- The ambient cocompact Fuchsian lattice has critical exponent `1`.
- `T_qc^red(X0)` is the reduced marked-surface quasiconformal Teichmuller
  space. Reflected sphere extensions give points in the all-Fuchsian locus of
  the AIM group space `T_qc(Gamma_0)`; marked Mobius conjugacy preserves the
  critical exponent. No global identification, parametrization, injectivity,
  or arbitrary quasi-Fuchsian claim is made.

## Citation-to-claim map

| Manuscript claim | Source or derivation |
|---|---|
| Exact AIM question and chronology | AIM problem list, Problem 4.3; Su handbook chapter |
| Strict exponent inequality | Dougall--Sharp, Theorem 1.1, plus `F_g` nonamenable |
| Collar width and metric | Keen; Buser |
| Spectral conversion | Sullivan, Theorem 2.17 |
| Infinite generation | Direct contradiction using the standard convex-cocompactness fact cited to Beardon |
| Quasiconformal family and AIM group-space bridge | Direct equivariant-lift, reflection, and marked-Mobius proof; Alessandrini et al. for surface-space terminology |
| Fixed-width energy, plateau area, and linear rate | Direct calculations in this package |
