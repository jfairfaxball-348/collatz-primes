# Owner research report — integration ledger (15 October 2026)

**Planning artefact, not an executed S001 experiment.** Input: owner-supplied report dated 14 October 2026, “Collatz Conjecture, Prime Numbers, and the Fairfax-Ball Repository Programme”. Interpret this as a deep-research synthesis, not an independently checked mathematical paper. This file marks which observations are already in the S000 repository, which are report-derived and what must be proved afresh.

| Report statement | Provenance / tier on intake | Next verification action |
|---|---|---|
| All composite-start convergence is equivalent to full Collatz | S000 CP-0001 PROVED_INTERNAL (elementary) | Preserve unchanged; optional Lean proof |
| Every odd prime dividing n disappears from accelerated U(n) | Elementary derivation from CP-0003; NOT yet separately claimed/formalised | Write quantified lemma, including integrality and valuation hypotheses; independent proof audit |
| Every odd class modulo 2^k contains primes and composites | S000 CP-0005; prime part invokes Dirichlet | Keep source dependence explicit |
| Affine descent class certificate 2^j T^j(n)=3^a n+b | S000 CP-0004 establishes shape, not S001 generator | Implement generator, exact independent verifier, boundary/threshold tests |
| Depth-16: 30654/32768 odd residue classes certified and 2114 remain; 395/395/1324 split across 7/11/15 mod16 | **REPORT_DERIVED_NOT_REPRODUCED_IN_REPO** | Recompute counts and per-class certificates; compare independent implementation; freeze deterministic input, checksums, exact convention for j<=k and representative |
| 27 modulo 2^16 an uncovered *composite* example | REPORT_DERIVED_NOT_REPRODUCED_IN_REPO | Independently recompute and clarify that a residue class includes both primes and composites |
| Inverse odd predecessor x=(2^a y-1)/3 | Standard algebraic identity / derived plan | Prove necessity and sufficiency with y odd, x>0 odd, exact a=v2(3x+1); handle y modulo 3 cases |
| Tao almost-all and Bařina finite bound | Literature stated, not this repo's certification | Read primary theorem hypotheses; timestamp dynamic frontiers |
| Angeltveit 2026 algorithm | External preprint source, not a repo benchmark | Check updated version, algorithm and cost before CEML engineering transfer |
| Hercher m>=92 / 2026 corrigendum | Owner report + peer-reviewed literature, not imported internal theorem | Audit exact m definition and corrigendum; prevent parameter mismatches |
| Ordinary Lean cycle programme unproved; alleged Mignotte height gap | Report of sibling repository status, not independently compiled here | Obtain present upstream checkpoint and verify exact analytic theorem interface before reuse |
| CDM: no certified divergence candidate; CEML: finite only | Report of sibling repository status | Re-check live authoritative sibling status if used in an S### theorem |

## Concrete hostile questions for S001

1. If a factor potential decreases on observed examples, can a counterexample be forced by the coprimality/factor-erasure identity?
2. Does a proposed residue certificate prove descent for **all** n=r+q*2^k including the smallest positive representative, or only n beyond a threshold?
3. If an algorithm lists infinitely many reverse predecessors of 1, does it prove *every* n appears? If not, where is the missing induction?
4. Does a proposed reduction treat primes as extra states or merely assume composite convergence is a weaker theorem?
5. Is a finite-sieve claim about numbers checked to 1 or about reaching a separately certified smaller state? What is the base and where is the induction?

No table or literary assertion in this integration file is a promotion to a universal Collatz theorem. The original report itself says the global target is unresolved.
