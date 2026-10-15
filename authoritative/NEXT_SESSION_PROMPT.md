# S001 — Report-driven proof attack: factor erasure, exceptional residues and complete reverse basins (FUTURE / UNEXECUTED)

Repository: https://github.com/jfairfaxball-348/collatz-primes
Date of planning revision: 2026-10-15.
Research source: owner-supplied 14 October 2026 deep report “Collatz Conjecture, Prime Numbers, and the Fairfax-Ball Repository Programme”.
Roadmap: research/PROGRAMME_PLAN.md
Source-transfer checklist: research/REPORT_INTEGRATION.md

## Execution authority / scope

**S001 HAS NOT BEEN EXECUTED BY THIS PLANNING REVISION.** When the owner pastes this prompt or links it and instructs “run next session”, that owner instruction immediately authorises exactly S001. No second confirmation is required. Do not execute S002 as part of S001. Do not treat the attachment or the planning commit as a past S001 result.

## Mission (full proof target, no substitution)

Find original, sound, genuinely noncircular mathematical structure towards

    for every composite positive integer n, exists j>=0 with T^j(n)=1,

where T(n)=n/2 for even n and (3n+1)/2 for odd n.

CP-0001 proves this is equivalent to full Collatz, since T(2p)=p for each prime p. The theorem remains OPEN. Prioritise a hard attempt at **global strict descent** (for all n>1 some T^j(n)<n) or a **complete, well-founded reverse basin**. A finite search, a 94%-coverage table, density one, or the nonexistence of a restricted cycle is not a proof of the target.

## Mandatory live entry and source precedence

1. Pin LIVE main commit SHA and tree, branch and PR state, recent merges, hosted workflows and accessible branch rules before changes. S000's last observed main on 2026-10-15 planning entry was efec7756f47364f1da0b7d2e6ff1c54f51804c94 with tree bab2765a35e6ebb1d92212d6f477a0d5ebafc138, CI finite-sanity-checks run 38641993543 SUCCESS. **These are historical baseline refs, NOT guesses about future entry.** Re-fetch fresh.
2. Read AGENTS.md; README; authoritative/START_HERE.md, STATE.json and THIS PROMPT; docs/SESSION_PROTOCOL.md and EVIDENCE_POLICY.md; research/S000_FOUNDATIONS.md, RESEARCH_ROUTES.md, PROGRAMME_PLAN.md, REPORT_INTEGRATION.md, SOURCES.md, CLAIMS.md and FAILURE_LEDGER.md; sessions/S000/CLOSEOUT.md; validation/S000_audit.json; scripts and tests.
3. Read the report integration ledger before importing statements from the owner's attachment. Never promote unreplicated depth-16 counts or sibling status to a new verified repo result; never treat an external paper as proving Collatz.
4. Archive S001 input and exact live entry conditions in sessions/S001/INPUT.md. Note which source material was actually retrievable. Do not manufacture attachment hashes if raw bytes are unavailable.

## Mathematics task A — exact obstruction and candidates (proof first)

A1. Prove rigorously for every odd n>0 and every odd prime p dividing n, p does not divide U(n), where U(n)=(3n+1)/2^v2(3n+1). Include the elementary gcd(n,U(n))=1 identity, exact integrality, exceptional n=1, and distinguish the T and U maps. Classify this as elementary, not novel. Give explicit hostile examples invalidating false factor-multiplicative/descent inferences.

A2. Derive the equivalence: all orbits converge iff every n>1 has some finite iterate <n. Give a noncircular well-founded induction proof of the forward implication from global descent. Identify exactly what part of a proposed composite-factor descent proof would still need to handle primes.

A3. Seriously test at least TWO separate candidates for a universal theorem: one involving prime factors/valuations/transitions and one involving an inverse-graph or exceptional-residue rank. Write complete quantified statements and try to prove them; construct adversarial counterfamilies if they fail. A negative theorem with proof is preferable to an unexplained failure or more trajectory counts.

## Mathematics task B — residue certificate reconstruction and exceptional-set dynamics

B1. Build an exact integer affine-certificate producer, with records (k,r,j,a,b,parity_word) and deterministic output; for 10<=k<=16 follow the same convention as the report (positive odd representatives, first j<=k steps) before comparing counts.

B2. Write a SECOND independent checker, not calling the producer's predicate, which verifies:
  - all parities for the specified residue are fixed for the first j iterates;
  - the identity 2^j*T^j(n)=3^a*n+b on that branch;
  - 2^j>3^a AND 3^a*r+b < 2^j*r for the smallest positive representative, where claiming full-class descent;
  - the inequality for all n=r+q*2^k by an explicit symbolic coefficient argument.

B3. Reproduce or correct the report's depth-16 30654/32768 certified / 2114 uncovered and 395/395/1324 residue split, including a deterministic manifest and hash; audit uncovered composite examples such as 27. If conventions differ, state exactly how and do not silently tune the computation.

B4. **New theory attempt:** characterise how uncovered classes lift from depth k to k+1; try one finite automaton/invariant/ranking that would show every uncovered start eventually enters a certified smaller class. Supply either a rigorous nontrivial infinite-family theorem or a precise counterexample/obstruction. Do not claim global coverage from a finite table, bounded depth or growth percentages.

## Mathematics task C — reverse-basin compressed-structure attack

C1. State and prove the exact inverse edges: y->2y always, and for odd y the odd predecessors under U are x=(2^a*y-1)/3 for a>=1, positive x, with exponent congruence 2^a*y=1 (mod 3). State the parity of a for y=1 or 2 mod3 and absence of this U inverse when y=0 mod3.

C2. Define a compact proposed grammar/finite rule system G for certified seed descendants and prove soundness for every generated number. Then attempt completeness or a genuinely stronger lemma (e.g. every exceptional residue has a rank-decreasing transition into G). **The equality "union of reverse paths from 1 = convergent starts" is tautological**, not a completeness proof. Expose the first unproved quantifier explicitly.

C3. Try to connect inverse factor constraints to the uncovered parity classes; test whether compositeness-forcing conditions can create an unbounded, noncircular induction. Include a hostile counterexample search for each proposed bridge. Distinguish finite search from a quantified proof.

## Cross-repository and prior-art audit

Read/verify as relevant the latest authoritative statements in:
- https://github.com/jfairfaxball-348/PRIMES (discovery/holdout/adversarial discipline);
- https://github.com/jfairfaxball-348/Proof-that-non-trivial-cycles-cannot-exist-in-Collatz (orientation/sign gap);
- https://github.com/jfairfaxball-348/Collatz-Divergence-Machine (reverse trees, no proved divergence);
- https://github.com/jfairfaxball-348/LEAN-non-trivial-collatz-cycles (formal results only, missing Mignotte-hypothesis bridge);
- https://github.com/jfairfaxball-348/CEML (bounded frontier/verification engineering);
- https://github.com/jfairfaxball-348/leading-digit-hailstone (different map, proof methodology only).

Use primary sources Lagarias, Tao (2022), Bařina (2025), Hercher (+corrigendum), Simons–de Weger, and Angeltveit (2026 preprint). Date new external facts. Produce a source-to-lemma dependency table and a separate novelty assessment; no priority claim for factor-erasure or basic affine algebra.

## Reproducibility, classification, and adversarial gates

Use exact arithmetic and precise positive domain bounds. Run Python tests, original S000 audit, new generator/checker tests and explicit edge-case tests (n=1, y multiple of 3, short parity words, r=1, depth-lift boundaries, known hard composites). If local execution is unavailable use the permitted GitHub runner, marking missing validation as NOT OBSERVED. Archive reproducible commands, hashes, range/depth definitions, output samples, independently checked examples and any code changes. PRIMES-style holdout partitions must be frozen *before* exploration; do not claim holdout replication after viewing it.

For every proposed universal argument, name the exact lemma that closes (or fails to close) all remaining positive integers. Check for circularity, prime/composite leakage, confusion between eventual smaller value and reaching 1, use of unproved sibling results, and confusion between U and T.

Do not claim Lean/Palomar passed without real proof/check output. Formalise only correctly stated proof-complete claims; inspect Lean axioms if a formal result is promoted. No world-frontier or divergence announcement from finite experiments.

## Required S001 closeout and handover (exactly one session)

Deliver:
1. sessions/S001/INPUT.md, substantial mathematical proof/obstruction note, reproducible validation manifest + scripts/tests, hostile failure ledger, and sessions/S001/CLOSEOUT.md.
2. Explicit outcomes for A/B/C, each labelled THEOREM / PROVED_INTERNAL / SOURCE_STATED / FINITE_CERTIFICATE / EXPERIMENT / REFUTED / OPEN, and a list of all missing global quantifiers.
3. Updated authoritative/STATE.json and START_HERE.md; research/CLAIMS.md, FAILURE_LEDGER.md, SOURCES.md, RESEARCH_ROUTES.md or PROGRAMME_PLAN.md as needed; sessions/LEDGER.md.
4. The COMPLETE S002 prompt in authoritative/NEXT_SESSION_PROMPT.md, marked FUTURE / UNEXECUTED, and include its complete text (or verbatim linked same-commit copy) in S001 closeout. Do not run S002.
5. Prefer one coherent authored single-parent commit on a dedicated S001 branch, ordinary PR, verified CI before non-force merge where possible, and independently checked final main SHA/tree. If any stage is blocked, report the precise block; never invent successful checks.
6. A user-facing closeout with actual GitHub file/PR/merge URLs, critical mathematical findings, explicit non-results, and **the full S002 prompt**.

**Priority rule:** A mathematically decisive new route or rigorously refuted tempting route matters more than increasing finite coverage or manufacturing a positive session narrative. Keep the central Collatz problem OPEN unless a genuinely complete proof survives hostile review.
