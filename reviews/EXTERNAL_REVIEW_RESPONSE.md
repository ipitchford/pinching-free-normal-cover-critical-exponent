# Response to supplied full review

**Review date:** 1 September 2026  
**Response date:** 1 September 2026  
**Review artifact:** privately retained supplied attachment; raw third-party text excluded from the public package  
**Review SHA-256:** `b3e8035f0e61e93b1aab810b8972f071cfd3f54af1a0721f1e7247aca7b8136c`  
**Recommendation received:** minor revisions for Evidence Press candidate release  
**Decision confidence reported by reviewer:** 0.88

The review was adopted in full where it requested a mathematical,
bibliographic, semantic, or package-integrity repair. The stronger fixed-width
cutoff was adopted rather than merely regularising the earlier maximal-collar
endpoint. This response does not convert the supplied review into independent
specialist validation or peer review. The public package retains the exact hash
above so an authorised holder can identify the reviewed input without granting
or implying redistribution rights.

| ID | Review request | Action | Verification state |
|---|---|---|---|
| R1 | Define the exact quasiconformal deformation space and narrow the title | Retitled the paper to name reduced quasiconformal Teichmuller space; defined `T_qc^red(X0)` using marked surfaces and homotopy-to-conformal equivalence; stated that sphere extension represents the same marked Fuchsian point and does not quantify over arbitrary quasi-Fuchsian conjugates | Implemented in both manuscript sources; source-parity marker added |
| R2 | Add the closest literature and correct the problem chronology | Distinguished the 2012 workshop origin, 2014 accessible AIM document, and 2016 handbook chapter; added Astala--Zinsmeister, Bonfert-Taylor--Matsuzaki--Taylor, Bishop, and Huo--Zinsmeister with an explicit all-Fuchsian/quasi-Fuchsian novelty boundary | Implemented in manuscript, bibliography, novelty report, and source ledger |
| R3 | Prefer the fixed-width cutoff and stronger rate | Fixed transition width `R=1`; proved exact energy `2g ell sinh(1)`, plateau bound `4 pi(g-1)-2g ell sinh(1)`, `lambda_0 <= C_g ell`, and `1-delta <= 2C_g ell`, with `C_g=g sinh(1)/(pi(g-1))` | Implemented in both manuscripts, claim ledgers, checker, and 16-test publication suite |
| R4 | Reconcile the replay receipt with the exact released package | The old receipt is treated as superseded. A new clean-directory receipt will be generated only after the revised PDF and complete inventory are frozen; it will record extractor path/version, raw and normalised text hashes, PDF hash, manifest convention, file count, and clean replay result | Pending final freeze by design |
| m1 | Display the exact sequence | Added both `1 -> K -> pi_1(S_g) -> F_g -> 1` and `1 -> Gamma_m -> L_m -> F_g -> 1` | Implemented in both manuscript sources |
| m2 | Clarify the cut system and side pairing | Retained the connected-complement cut-system condition and the dual-arc monodromy explanation `q(a_i)=x_i` | Preserved; parity and PDF checks cover the construction |
| m3 | Make lift equivariance and descent explicit | Retained the holonomy-equivariance equation and added descent to the marked map `X0 -> X_m` | Implemented |
| m4 | State admissibility in `H^1_c` | Retained compact support, Lipschitz regularity, zero seam trace, `H^1_c` membership, and smooth approximation | Implemented |
| m5 | State the small-length domain | Added `w(ell)>1` for sufficiently small `ell`; every fixed-width formula is stated only in that regime | Implemented and executable domain check retained |
| m6 | Make constants and dependencies visible | Gave the explicit admissible constant `C_g=g sinh(1)/(pi(g-1))` and preserved the external-theorem dependency statement | Implemented |
| m7 | Do not overstate the scripts | Checker and manuscript continue to say finite execution corroborates explicit formulas only and does not prove the theorem or imported results | Preserved |
| m8 | Preserve non-English evidence limits | Traditional Chinese rendering remains included and explicitly labelled producer-generated and not independently translation-validated | Implemented |

## Claim change

This revision strengthens the quantitative theorem from
`1-delta=O_g(|log ell|^-2)` to `1-delta=O_g(ell)` and narrows the named target
from a generic quasiconformal deformation space to the Fuchsian points of the
reduced, surface-based space `T_qc^red(X0)`. The existence and infinitely-many-
values conclusion is unchanged.

## Remaining release action

R4 closes only when the final package has been rebuilt, visually inspected,
resealed, and replayed from a clean directory. The final verification record
is `EXTERNAL_REVIEW_VERIFICATION.md`.
