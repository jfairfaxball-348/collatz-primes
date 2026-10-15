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

## S002 updated proof routes (15 October 2026)

- W2 exceptional tower CP-0014 now gives exact high/low child inequalities; missing universal positive-integer tower-exit rank. S003 tests whether first strict descent coincides with first slope 3^{a_j}<2^j (only finite observation so far), and seeks a quantified counterexample/proof.
- W2 CP-0015 proves exact first descent step59 for every 27+2^59*q, including infinitely many composites, but makes no claim over entire coarser 27 mod2^16 family.
- W1 CP-0016 establishes genuine two-U-step prime re-entry; monotone prime-support rank refuted by family x=20t+15. Explore m-step offsets/valuation tradeoffs, not factor disappearance alone.
- W3 CP-0017 establishes 3 never appears after first U, but this source obstruction says nothing about convergence. CP-0018 forbids a fixed 2^k residue alone predicting output mod3; mixed automata remain OPEN.
- Hosted S002 CI now consumes actual canonical S001 JSONL in addition to independent regeneration; cite actual job outputs before PASS claim. Universal theorem OPEN.

## S003 proof-route redirect (2026-10-15)

- W2 CST: the explored identity first descent = first parity slope crossing is NOT an original conjecture; it is Terras' existing OPEN CST conjecture (CP-0019). CP-0020 proves only the classical exact intercept cutoff per parity cylinder. The stronger arbitrary negative-slope-implies-descent is false at n=7, j8. Work on a new delimited tractable family and counterexample audit, not renaming CST.
- W2 tower: OPEN iff slopes all >=1 is finite-only k10..16; equivalence for all representatives would solve CST. CP-0022 rules out ANY finite per-residue first-descent horizon assigned to a fixed 2^k modulus; seek a genuinely adaptive or mixed-modulus rank.
- W1 prime factors: CP-0021 explicit valuation-sensitive U^m offset and gcd for every m. It lacks monotone size/factor rank and survives hostile factor-return cases; S004 must search noncircular rank or kill defined candidates.
- W3 U-inverse grammar remains sound, exact source classes y divisible3 and larger-only parents y=1 mod3 obstruct naive induction. Six least hypothetical counterexample classes mod48 unchanged. Full Collatz OPEN.

## S004 route decision — 2026-10-15

First-crossing route: CP-0023 gives a proof for O^a E^b cylinders, including all least positive representatives under a 3/4 coefficient margin, and proves the eligible a have gaps at most one. S005 must attack the complementary a via the inverse residue t0, not simply extend numerical counts. Arbitrary-modulus finite horizon route killed by CP-0024 (including r15,31 mod48), so any plausible algorithm needs unbounded state, growing parity window, or start-dependent rank; the y≡0,1 mod3 inverse obstacles persist. Valuation-only route killed by CP-0025's unbounded one-U jump and bounded-m all-O growth. Explore combined potentials with explicit decreasing transitions; do not assume prime erasure helps. Collatz and CST OPEN, originality unknown.

## S005 route verdict — 2026-10-15

First crossing CP-0026: every O^a E^b first-crossing representative is weakly non-increasing; all positive lifts beyond the least t0 strictly descend. The ONLY remaining possibility at q=0 is D*t0=2^b-1, implying a nontrivial periodic orbit; do NOT claim no such cycle. CP-0027 extends S004's all-t sufficient band from f<=alpha to f<=4/5 for a>=3, proving infinitely many formerly uncovered exponents. Near-resonant f>4/5 remains open. Future S006 one-block-cycle prior-art and exact inequality gate.

Mixed-state CP-0028: exact finite-word forward cylinders give an infinite STRICT composite progression in all six least-counterexample mod48 residues, plus an actual variable H O-exit grammar for r15/31 arbitrary H and r7/39 at H3; NO full residue eliminated. r27/43 incompatible with the simple H2 b2 O-run condition, so improve their sparse coverage in S006. U-inverse y=0,1 mod3 obstacles persist.

Factor-rank CP-0029: even arbitrary fixed real state-dependent additive valuation/omega corrections to numeric n fail stepwise U monotonicity on infinite x=96q+15 composites. Seek genuinely nonlinear/block adaptive ranks; m-step F_m has no automatic sign. Universal and CST conjectures remain OPEN; novelty not established.

## S006 route verdict — 2026-10-15

**Steiner classical theorem import:** CP-0030 closes the S005 O^a E^b equality obstruction for a>=2 using EXISTING published one-circuit theory, NOT a new no-cycle proof. Every positive member of such a parity cylinder strictly decreases at the first coefficient crossing; this says nothing about first-crossing parity words with multiple odd blocks. Advance to true multi-block words in S007.

**Six-class grammar:** CP-0031 three disjoint full parity-word cylinders (11 mod32 step5, 59 mod128 step7, 123 mod256 step8) cover exactly 11/16 of BOTH r27 and r43 mod48, much greater than sparse lifts. Remaining 5/16 and other four whole classes remain unresolved, so neither full class is excluded. Target the remaining mixed 27 mod32 subtrees, not merely global density.

**Rank no-go:** CP-0032 rules out ALL separable multiplicative n^p f(v2(n+1)) strictly monotone at each U step even for composite starts. Input high-h O-runs vs output high-h jumps force incompatible growth. Nonseparable r/h, multi-step and terminal-state ranks remain possible. No Collatz/CST theorem.
