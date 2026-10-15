# Source register (S000)

Literature is read as background; none provides the desired universal theorem.

- SRC-0001 — Jeffrey C. Lagarias, "The 3x+1 problem: An Annotated Bibliography (1963–1999)," arXiv:math/0309224 (revised 2011). https://arxiv.org/abs/math/0309224 . Describes shortened-map convention and the longstanding open problem. Type: primary survey; scope historical.
- SRC-0002 — Jeffrey C. Lagarias, "The 3x+1 Problem: An Overview," arXiv:2111.02635. https://arxiv.org/abs/2111.02635 . High-level historical overview. Type: primary survey; no convergence theorem.
- SRC-0003 — Terence Tao, "Almost all orbits of the Collatz map attain almost bounded values," Forum of Mathematics, Pi (published online 20 May 2022). https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F . The theorem concerns almost all starting values in logarithmic density, not every integer.
- SRC-0004 — David Barina, "Improved verification limit for the convergence of the Collatz conjecture," Journal of Supercomputing 81, article 810 (published 2 May 2025). https://link.springer.com/article/10.1007/s11227-025-07337-0 . Reports computation to 2^71 as of publication; this project does not independently replay or certify that bound.
- SRC-0005 — Dirichlet's theorem on primes in arithmetic progressions (classical). The theorem is invoked for every odd residue mod 2^k in CP-0005; not claimed original.

**Source caution:** GitHub projects and secondary articles can change. Confirm literature and latest computational frontier at each relevant subsequent session; date all newly claimed records. No source in this list is evidence that the composite-convergence conjecture is settled.


## S001 dated live audits (15 October 2026)

- SRC-0006 — Vigleik Angeltveit, “An improved algorithm for checking the Collatz conjecture for all n<2^N,” arXiv:2602.10466, submitted 11 Feb 2026, https://arxiv.org/abs/2602.10466 . Primary abstract inspected; algorithm concerns finite verification, no global theorem.
- SRC-0007 — John Simons and Benne de Weger, “Theoretical and computational bounds for m-cycles of the 3n+1-problem,” *Acta Arithmetica* 117 (2005), 51–70, DOI 10.4064/aa117-1-3. Publisher/university abstract inspected, excludes m-cycles with 1<=m<=68 in its cycle definition. Not a full cycle/divergence theorem.
- SRC-0008 — Christian Hercher, “There are no Collatz m-Cycles with m ≤ 91,” *Journal of Integer Sequences* 26 (2023), https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html . Journal abstract inspected: lower bound m>=92 in its local-minima parameter. Journal page also links **June 2026 corrigendum**; its detailed impact not fully audited and should be read before importing lemmas. No full convergence implication.
- SRC-0009 — Lagarias arXiv:2111.02635 (2021) abstract and Tao publisher full abstract https://doi.org/10.1017/fmp.2022.8 (2022) rechecked: no all-positive theorem. Tao's result is log-density almost-all with lower orbit values below any function tending to infinity.
- SRC-0010 — Bařina publisher journal abstract DOI 10.1007/s11227-025-07337-0 rechecked: paper reports finite bound n<2^71; S001 did NOT rerun it. CEML later live frontier statements are separate, changing and not independently verified by S001.
- SRC-0011 — Live sibling GitHub README/authoritative status read (2026-10-15): https://github.com/jfairfaxball-348/PRIMES ; https://github.com/jfairfaxball-348/Proof-that-non-trivial-cycles-cannot-exist-in-Collatz ; https://github.com/jfairfaxball-348/Collatz-Divergence-Machine ; https://github.com/jfairfaxball-348/LEAN-non-trivial-collatz-cycles ; https://github.com/jfairfaxball-348/CEML ; https://github.com/jfairfaxball-348/leading-digit-hailstone . Exact scoped claims and caution in research/S001_PROOFS_AND_OBSTRUCTIONS.md; all sibling results are separate and cannot close Collatz here.

No S001 finding claimed novel. Dated source inspections were abstracts/statuses, not exhaustive full-paper theorem audits. Source-to-lemma table is in S001 research note.

## S002 follow-up source audit — 15 October 2026

- SRC-0002 Lagarias arXiv:2111.02635 confirmed historical overview, not a universal proof. https://arxiv.org/abs/2111.02635
- SRC-0003 Tao 2022 primary Cambridge theorem confirms almost all in *logarithmic density* attain almost-bounded orbit minima, not every start. https://doi.org/10.1017/fmp.2022.8
- SRC-0004 Bařina 2025 publisher article reports verification to 2^71; neither reproduced nor treated as a theorem over all positives. https://doi.org/10.1007/s11227-025-07337-0
- SRC-0006 Angeltveit 2026 arXiv:2602.10466 is a finite N verification algorithm and complexity improvement; not global convergence. https://arxiv.org/abs/2602.10466
- SRC-0007 Simons–de Weger Acta Arith.117 (2005) primary metadata confirms m-cycle topic, no use of technical m-bound in S002 proof. https://doi.org/10.4064/aa117-1-3
- SRC-0008 Hercher *There are no Collatz m-Cycles with m<=91*, JIS 26 (2023), publisher explicitly links corrigendum dated June 14 2026. Its m counts local minima. Corrigendum existence checked; technical corrected proposition NOT imported. https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html

**Dependency/novelty assessment:** CP-0014—CP-0018 use none of these papers as proof premises, only context. Exact earlier occurrences of the elementary identities were not exhaustively checked, so NO originality claim or publication gate passes. No sibling technical assumptions imported.

## S003 direct source check (15 October 2026)

- SRC-0012 — R. Terras, *A stopping time problem on the positive integers*, *Acta Arithmetica* 30 (1976). **Coefficient Stopping Time (CST)** original conjecture: j_s(n)=j_c(n) for all n>=2. Historical primary prior art, not proved by this repository; Lagarias 1985 overview and OEIS A126241 discuss it.
- SRC-0013 — Olivier Rozier and Claude Terracol, *Paradoxical behavior in Collatz sequences*, *Discrete Mathematics* 349 (2026), article 115167, DOI https://doi.org/10.1016/j.disc.2026.115167 ; https://arxiv.org/abs/2502.00948 . Read publisher abstract and arXiv introduction/definitions. Explicitly names Terras CST and the nonnegative affine remainder, and explains later paradoxical prefixes do not settle first crossing. **Direct novelty kill CP-0019**. No bound imported to prove Collatz.
- SRC-0014 — Christian Hercher, *Corrigendum to Article 23.3.5: There are no Collatz-m-Cycles with m<=91*, June 14 2026, https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf . Read both pages. Corrects erroneous inequality derivation in **Theorem 21** by convex-polytope maximisation; original m-cycle proof cannot be imported without correction. No external m bound used here.
- SRC-0002/0003/0004/0006/0007/0008 background refreshed: Lagarias overview, Tao 2022 logarithmic almost-all, Bařina 2025 finite 2^71 verification, Angeltveit 2026 finite verification algorithm, Simons–de Weger cycle limits, Hercher corrected cycle claims. None proves pointwise convergence. S003 CP-0020—CP-0022 rely on internal algebra only, no originality claimed.

## S004 primary source and priority audit — 2026-10-15

- SRC-0013: Rozier and Terracol, *Paradoxical behavior in Collatz sequences*, Discrete Mathematics 349 (2026) 115167, publisher full text https://www.sciencedirect.com/science/article/pii/S0012365X26001913 checked; coefficient stopping-time is explicitly Terras' OPEN conjecture and classical affine remainders/paradoxical prefixes are treated. CP-0023 no originality claim.
- SRC-0012: Terras, Acta Arithmetica 30 (1976), historical CST source reconfirmed through Rozier–Terracol's named Definition 1.2 / literature; original 1976 full text was not separately inspected this session.
- SRC-0014: Hercher corrigendum https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf, BOTH pages inspected. Corrects an incorrect inequalities derivation in Theorem 21 using a convex polytope maximization; no technical cycle theorem imported into S004.
- SRC-0004: Barina 2025 journal publisher text https://link.springer.com/article/10.1007/s11227-025-07337-0 reports finite 2^71 verification, not independently rerun. SRC-0003 Tao (2022) logarithmic almost-all, SRC-0006 Angeltveit arXiv:2602.10466 finite checking, not universal.

CP-0023—0025 self-contained arithmetic; exhaustive priority search NOT performed. Do not describe them as original or publication-ready.
