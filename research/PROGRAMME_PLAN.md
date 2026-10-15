# Collatz Primes — proof-first research programme (15 October 2026)

**Status: PLAN ONLY, not S001 execution.** The target is OPEN. This document integrates the owner's 14 October 2026 research report with the live S000 scaffold. A report observation is not yet a repository-reproduced certificate.

## Governing theorem and proof obligation

We use the shortened map T(n)=n/2 when n is even, and T(n)=(3n+1)/2 when n is odd, for all positive integers.

**Headline H:** every composite positive integer reaches 1 under some iterate of T. By CP-0001 this is *equivalent* to convergence for every positive integer: for prime p, the composite 2p has T(2p)=p. Never present "composite only" as a logically weaker theorem.

A useful equivalent intermediate formulation is **global strict descent**:

> For every integer n>1, there exists j>=1 such that T^j(n)<n.

Global strict descent implies convergence by strong induction on n: apply the induction hypothesis to the smaller reached value. Conversely, full convergence implies strict descent to 1 for n>1. Any claim of a global descent theorem must prove its own termination/coverage conditions without assuming convergence.

For reverse dynamics, let U(x)=(3x+1)/2^v2(3x+1) for odd positive x. The inverse odd predecessors of odd y are exactly x=(2^a*y-1)/3 for integers a>=1 with 2^a*y congruent 1 modulo 3, x positive; then x is odd and U(x)=y. The required exponent parity is even if y=1 modulo 3, odd if y=2 modulo 3, and no such predecessor if y=0 modulo 3. This exact parametrisation is elementary, not a global basin certificate.

## Priority and attack hierarchy

**P0 / Proof architecture:** Work towards either global strict descent or a well-founded complete reverse-basin construction. A successful *finite-to-infinite bridge* requires a proved finite symbolic invariant, ranking, inductive cover, transfer theorem, or another mechanism applying to ALL remaining positive starts. Producing more residue coverage alone is not the bridge.

**P1 / Certified residues and exceptional-set dynamics (lead route).** For a fixed first j parity word, write

    2^j T^j(n) = 3^a n + b

for exact nonnegative integer b. If j<=k and r is an odd positive representative modulo 2^k, the first j parities agree for all n=r+q*2^k (q>=0). If 2^j>3^a and 3^a*r+b<2^j*r, all n in this entire residue class strictly descend by j. Store (k,r,j,a,b) and a proof of parity compatibility and inequality, then verify with a **separate exact checker**. Explain the distinction among (i) descent for an entire residue class, (ii) eventual descent beyond a threshold, (iii) empirical trajectories and (iv) missing classes.

Owner's report **reports**, but this repository has NOT independently replicated, these depth-16 statistics: 30654 of 32768 odd classes certified and 2114 unresolved; unresolved classes split 395 / 395 / 1324 across residues 7 / 11 / 15 modulo 16. Reproduce before promoting. Focus on recurrence, automata, transitions, conditional induction and structure of uncovered sets, rather than maximizing coverage percentage.

**P2 / Complete reverse-basin / compressed seed theorem (co-lead).** Formalise certified basin B generated from 1 by safe inverse edges y->2y and, for odd targets y, the above inverse odd predecessor formula. Being the union of all reverse paths to 1 is a *restatement* of Collatz, not progress. A new theorem must give a finite grammar/parametrisation + proved closure/completeness (e.g. all congruence classes or a well-founded rank), or produce a global return to a smaller certified state. Look for a direct interface between reverse classes and forward exceptional parity states. Hostile audit: show how every purported grammar covers arbitrarily large values without using the sought conclusion as an assumption.

**P3 / Prime and composite factor obstruction (target-specific route).** Factorisation is the motivating angle, but not inherently a progress measure. If n is odd and p is an odd prime dividing n, then 3n+1 is 1 modulo p and p does not divide U(n). Indeed gcd(n,U(n))=1. Record/ideally formalise this factor-erasure lemma and use it to kill simple persistent-factor potentials. Investigate genuinely new quantities involving *transitions*, valuations, prime-power congruence obstructions, consecutive-state identities and the inverse formula; require universal quantified proofs, not correlations.

**P4 / External mathematical bridges:** Compare any cycle obstruction with published definitions of number of minima (Hercher/Simons–de Weger) and identify the load-bearing missing orientation/sign theorem in the informal cycle repository. The Lean cycle programme's attempted Mignotte substitution does not meet the height hypothesis according to the owner report: do not borrow any unproved analytic cutoff. The divergence machine has no certified divergent orbit. Tao's logarithmic-density almost-all theorem leaves a pointwise exceptional set. These projects are sources of precise *conditional lemmas and failed mechanisms*, not shortcuts to a universal proof.

**P5 / Computational and formal infrastructure (support only):** Import PRIMES-style preregistered discovery/frozen holdout/adversarial cohorts; retain scripts, deterministic input and output hashes; use CEML strictly for finite-frontier engineering and algorithm benchmarking (Bařina/Angeltveit), not for an infinite theorem. Promote rigorously proved, useful elementary/structural lemmas to Lean with theorem-statement checks and axiom reports. Palomar requires actual submitted and returned verification.

## Research workstreams with dependencies and decision gates

| Workstream | First testable result | What would be a real breakthrough | Kill / redesign signal |
|---|---|---|---|
| W1 Factor erasure and transitions | Standalone proof of erasure, hostile examples for proposed potentials | A noncircular well-founded rank or composite-to-descent lemma for an infinite family not previously known | Needs persistence of a prime divisor, false multiplicativity, or assumes factors converge |
| W2 Affine certificates | Generator + independent checker; reproduce depth 10–16 class data | Prove the uncovered classes cannot support a least counterexample, using uniform finite-to-infinite closure | More numerical percentages without closure; invalid representative inequality |
| W3 Reverse basin completeness | Exact inverse-edge theorem and symbolic grammar prototype | A proved complete finite description of the reverse basin of 1, with non-tautological induction | Grammar merely enumerates known predecessors; unproved coverage |
| W4 Residue/prime joint bridge | A preregistered factor-residue identity with exact proof or refutation | Conditional theorem reducing all exceptional families to earlier certified families | Pattern only statistical or mixed prime/composite classes falsely treated as prime-free |
| W5 Cross-project theorem audit | Explicit dependency interfaces and source status for each imported lemma | New proved theorem closes a genuine missing universal case | Depends on unproved orientation/Mignotte interface or finite frontier |
| W6 Formal certification | Lean statement sketches for proof-complete W1/W2/W3 lemmas | Kernel-checked meaningful theorem with axiom audit; novelty separately reviewed | Source compiles but statement is weaker than advertised |

## Staged milestones (not automatic session authorisation)

- **M0 — S001:** mathematically credible attack on W1/W2/W3, prove elementary erasure/inverse identities; reconstruct residue statistics with independent checker; try and adversarially reject at least two global proof ideas. Preserve failure ledgers and hand over full S002 prompt.
- **M1 — Early sessions:** obtain *a new, nontrivial infinite family* theorem or rigorous obstruction; identify the precise remaining exceptional set and why the theorem is not universal. No compulsory session-count target substitutes for mathematical merit.
- **M2 — Structural bridge:** prove a symbolic transition/ranking/complete cover lemma not expressible as merely a longer finite table. If impossible, publish a precise negative theorem and pivot.
- **M3 — Formal trust:** Lean formalisation of completed load-bearing claims with no sorry/sorryAx; proof statement and accepted axioms independently audited.
- **M4 — External novelty/publication:** primary-source prior-art review and adversarial mathematical review before arXiv, journal, or breakthrough claims. Keep a working draft only when there is a genuinely substantive theorem.

Every 5 sessions review and reprioritise the evidence. Every 10 sessions perform a stronger novelty/assumption/dependency audit. Neither review automatically closes the programme, and no failure to prove Collatz is to be disguised as completion.

## Repository contract / deliverables

Keep this repository as the **programme coordinator** with one active numbered S### session prompt, not a parent repo that silently modifies siblings. Suggested paths:
- authoritative/START_HERE.md and STATE.json: actual status (do not mark S001 complete for a planning-only update).
- authoritative/NEXT_SESSION_PROMPT.md: full exact next executable S001 instruction, FUTURE / UNEXECUTED.
- research/PROGRAMME_PLAN.md: governing roadmap and gates.
- research/REPORT_INTEGRATION.md: source-vs-verified transfer ledger.
- research/CLAIMS.md, FAILURE_LEDGER.md, SOURCES.md: append only with evidence labels, not unvalidated report data as proven.
- sessions/S###/: input, mathematical output, validations, failure analysis, closeout.
- tools/, tests/, validation/: deterministic generators, independent proof-checkers and bounded certificates.
- lean/ only once proof-complete scoped lemmas justify a formalisation track.

**Cross-repository links:** PRIMES (holdout discipline); CEML (independently auditable finite computation); Collatz-Divergence-Machine (reverse graph / explicit divergence obstructions); Proof-that-non-trivial-cycles-cannot-exist-in-Collatz (orientation bridge, unproved); LEAN-non-trivial-collatz-cycles (formal cycle modules, analytic gap); leading-digit-hailstone (proof patterns on a DIFFERENT map). Never transfer a theorem across maps without an actual proof.

## Truth labels and stopping rules

Use THEOREM / PROVED_INTERNAL only for complete mathematical proofs, FORMAL_VERIFIED only for actual kernel proof + axiom audit, SOURCE_STATED for dated accurately quoted literature, FINITE_CERTIFICATE / FINITE_TEST for exact bounded results, EXPERIMENT for exploratory outputs, OPEN / CONJECTURE for missing universal quantifiers, and REFUTED for an explicit counterexample. Novelty is a separate attribute. A high-priority route can be killed when its required uniform inequality has an explicit infinite counterfamily or it smuggles Collatz into a premise; retain the evidence and choose another route, not a new name for the same claim.

**Ultimate acceptance:** a complete mathematically sound proof of H, including full quantified global coverage, a noncircular well-founded argument, and independent evaluation. As of 15 October 2026 this has **not** been achieved.

## Primary literature / report provenance

This roadmap is adapted from the owner's supplied 14 October 2026 report “Collatz Conjecture, Prime Numbers, and the Fairfax-Ball Repository Programme”. The report audits seven repositories but is a secondary **research input**; its newly computed depth-10–16 data and live external frontiers are not independently reproduced here.

Primary references: Lagarias (1985, 3x+1 survey, DOI 10.1080/00029890.1985.11971528); Tao (2022, Forum Math. Pi e12, DOI 10.1017/fmp.2022.8); Bařina (2025, Journal of Supercomputing 81:810, DOI 10.1007/s11227-025-07337-0); Angeltveit (2026 preprint, https://arxiv.org/abs/2602.10466); Simons–de Weger (2005, DOI 10.4064/aa117-1-3); Hercher (2023 + corrigendum, https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html). Verify exact applicable statements at point of use.
