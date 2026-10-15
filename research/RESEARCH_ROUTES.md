# Research routes — see governing research/PROGRAMME_PLAN.md

**Status: S001 FUTURE / UNEXECUTED.** The full target is all composite positive integers converge to 1 under shortened T, equivalent to all-positive Collatz by CP-0001.

1. **Global strict descent:** Prove for every n>1 that some iterate T^j(n)<n using a noncircular well-founded argument; equivalent in strength to Collatz.
2. **Exceptional affine residues:** Produce independently verified certificates for all covered congruence classes. Characterise and *close* uncovered classes by an unbounded symbolic transition or rank; do not treat coverage percentages as proofs.
3. **Reverse basin and compressed complete grammar:** The safe predecessor edges y->2y and x=(2^a*y-1)/3 (for odd y, appropriate exponent and positive x) are exact. A complete finite grammar requires a non-tautological coverage proof.
4. **Prime-factor transitions and erasure:** The accelerated odd successor loses every current odd prime factor. Seek a new transition invariant, not naive factor persistence or multiplicativity; test on hard composite residues.
5. **Cross-project analytic/formal bridges:** Borrow only proved precise statements from the cycle/Lean/divergence projects; respect unproved orientation and Mignotte-height gaps. Use PRIMES holdouts; CEML finite verification never stands in for universal proof.

First session requirements and evidence/kill gates are in authoritative/NEXT_SESSION_PROMPT.md and research/PROGRAMME_PLAN.md. Every attempted route needs an exact quantified theorem, constructive adversarial falsification, an explicit coverage/induction obligation and a dated source/novelty status.


## S001 proof-route update (2026-10-15)

- **Factor erasure (W1):** CP-0008 proved as elementary. Universal U-size descent refuted for infinitely many odd composite 12t+3, distinct-prime-factor count increase at 121->91. Target a genuinely multi-step transition invariant in S002.
- **Affine residue (W2):** producer/independent code checker verify k=10..16, split strict 30653 + base-only 1 + uncovered 2114 at k16. CP-0012 proves exceptional ancestry projection but no tower closure; infinite -1-prefix positive composites defeat every fixed step bound. S002 must attack per-child transition and start-dependent rank, not just larger percentages.
- **Inverse basin (W3):** CP-0010 exact inverse theorem; least counterexample cannot lie in 5 mod6, leaving six necessary residues mod48; no smaller inverse for odd y≡0 or 1 mod3. Grammar sound but universality circular if assumed; S002 target this gap.
- **Cross-project (W4–W6):** primary abstracts, corrigendum existence and six sibling READMEs/statuses checked; no sibling proof promoted and no Lean/Palomar performed. Novelty unestablished. See research/S001_PROOFS_AND_OBSTRUCTIONS.md.
