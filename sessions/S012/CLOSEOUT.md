# S012 complete mathematical session closeout — 2026-10-15

## Verdict
**Mathematics complete; global composite Collatz / all-positive Collatz OPEN; Terras coefficient stopping time OPEN.** CP-0047 establishes an infinite near-resonant D<K true-first-crossing strict-descent family for **EVERY fixed a,c with 3^a>2^(a+c)**, not just S011's special pair. CP-0048 explicitly refutes completeness of the long-even-tail W_N family with n=27 (next four parities EOOO), and states the exact circular gap in a purported halting descent algorithm. CP-0049 gives composite forced-O no-descent prefix of length H>=6 with bitlength at most H+5. These do not solve universal renewal.

Proof and quantifiers: research/S012_PROOFS_AND_OBSTRUCTIONS.md. Exact executable tests: tests/test_s012_math.py. Validation: validation/S012_LOCAL_PROBES.md. Owner invocation: sessions/S012/INPUT.md. S012 branch/PR/main CI: check the specific actual run IDs and step results after push/merge; pre-entry main success run38733438917 job116416633742 is not a new-test certificate. Original local clone DNS BLOCKED; standalone local four tests PASS; original full hosted suite must be separately verified.

Attack A: attempted integer-dependent forward prefix completion and valuation/bitlength mod3-reverse renewal, both exposed precise noncircular missing property. A rank based only on state or strictly increasing n at fixed v2(n+1) fails on known exact constructions. An algorithm looping until n falls below its start is equivalent to the theorem, not a proof of termination. All 71 states and 5041 directed edges remain; all six potential least-counterexample classes are unresolved.

Attack B: for every fixed admissible a,c and every interval 0<ε<η<κ=(2^c-1)/3^a, infinitely many m have ε<δ_m<η, D<K and true-first-crossing strict descent for all lifts, including infinitely many composites. Exact carry h CRT reformulation recorded, without falsely claiming a complete parameter classification; boundary δ_m→0 still OPEN. No postfirst-crossing paradox confused with CST.

Sources: Terras 1976, Simons/de Weger 2005, Rozier/Terracol Oct2026, Niu May2026 compared in scoped audit; Steiner 1978 full primary NOT acquired; novelty UNESTABLISHED. No Lean, Palomar, arXiv, review, journal or independent proof certificate.

## FULL authoritative S013 NEXT SESSION PROMPT (FUTURE / UNEXECUTED)

# S013 — near-zero resonance, exact 2-adic carry classification and exceptional integer-dependent exhaustion (FUTURE / UNEXECUTED)

Repository: https://github.com/jfairfaxball-348/collatz-primes

**Authority:** The NEXT explicit owner instruction to run the authoritative prompt authorises exactly S013 immediately, not S014. This file is prepared during S012 and has NOT been executed.

## Mandatory entry
Read AGENTS.md, docs/SESSION_PROTOCOL.md, docs/EVIDENCE_POLICY.md, authoritative/STATE.json, START_HERE.md, this WHOLE prompt, S012 proof/tests/validation/input/closeout, S011–S008, research/CLAIMS.md, FAILURE_LEDGER.md, SOURCES.md and sessions/LEDGER.md. Inspect LIVE main SHA, actual git/commits tree and ordered parents, recent and open PRs, branch protections/rulesets and exact CI runs/jobs/steps. Preserve concurrent work. Do NOT assume CI success.

## Attack A — target universal positive-integer exit, not finite-state pseudo-completeness
S012 CP-0048 establishes the S011 W_N=p^N E^(4N) cylinders are NOT exhaustive even inside the 27 mod48 exception: 27 itself starts with p but its next four symbols are EOOO, not EEEE, and its next 13-step block cannot be p. The union does not cover 27. CP-0042 has 71 vertices and ALL 5,041 transitions, and every finite exceptional path has infinite composite realisations. CP-0041 has expanding same-residue, constant-valuation returns; CP-0049 forces H growing odd steps on composite inputs with bitlength H+O(1).

Try at least TWO concrete integer-dependent, computable certified-descent mechanisms, not density assumptions or finite-state arguments. For each give an explicit algorithm, inputs, integer-domain quantifiers, termination invariant or exact circular gap; try to falsify on 27, 43, 91, 155, 251, 393243+524288k, 2^H u-1 and all six 7/15/27/31/39/43 mod48 classes. Attempt a nontrivial well-founded potential involving actual bitlength, 3-adic information, inverse graph, or a signed affine remainder; confront growing same-valuation returns. Search exhaustively for a COMPLETE covering family of actual positive n, with a decision procedure and a noncircular termination proof; state exact unresolved lemma if it fails. Do not identify arbitrary long 2-adic paths with one divergent positive orbit.

## Attack B — sharpen first-crossing two-run theorem beyond compact windows
S012 CP-0047: for EACH fixed a,c>=1 with 3^a>2^(a+c), κ=(2^c-1)/3^a and ANY closed positive subinterval [ε,η] strictly contained in (0,κ), ALL sufficiently large m with δ_m=(2^ceil(m log2 3)-3^m)/3^m in [ε,η] yield genuine first crossings of O^a E^c O^(m-a) E^(ceil(m log2 3)-m-c), D<K, and strict descent for EVERY admissible q>=0. Irrational rotation supplies infinitely many m; this is NOT all m, all n, or Terras CST.

Investigate the shrinking near-zero window δ_m→0 where the existing exponential lower bound t0 becomes insufficient, and the complementary interval δ_m>=κ. Try exact necessary-and-sufficient modular carry classification for t0 (including h=[3^a t0+2^c-1]/2^(c+d)), prove any genuinely new uniform subfamily or explicitly exhibit adversarial parameters. Analyse equality/overshoot without invoking Simons cycles as an internal proof. Test full parity prefixes and exact minimal representatives, with FINITE bounds stated. Distinguish first coefficient crossing from later paradoxes.

## Sources and validation
Try credible library/archive pathways for Steiner 1978 *A Theorem on the Syracuse Problem*, Congressus Numerantium XX pp553–559; do NOT say the primary was read unless actually obtained. Compare Terras 1976, Simons/de Weger 2005, Rozier/Terracol October 2026, Niu May 2026; no unverified priority claim. Run actual original repository full Python unittests plus S000 byte-compare/hash, S001 depth10–16 recreation, independent checker, JSONL consumer and S003 corruption cases using GitHub-hosted checks if clone DNS remains blocked. Show actual run IDs/job IDs/step conclusions; separate standalone local tests from original suite. Keep all previous results, 71/5041 transducer and 6 exceptional classes intact.

Write S013 mathematical proofs AND failed conjectures with numbered claim IDs, exact new tests, validation record, source audit, INPUT, CLOSEOUT, updated state/START_HERE/claim and failure and session ledgers, and a COMPLETE S014 FUTURE/UNEXECUTED prompt in authoritative/NEXT_SESSION_PROMPT.md and verbatim in CLOSEOUT. Use branch/PR, merge only after verified CI and branch-safety inspection, verify actual merged main SHA/tree/parents/readback. Global Collatz/composite convergence, Terras CST, novelty, Lean, Palomar and publication remain OPEN/UNCLAIMED absent real verification.



### S012 hosted CI and postmerge attestation — 2026-10-15

**VERIFIED PR #18** https://github.com/jfairfaxball-348/collatz-primes/pull/18 was merged by ordinary merge (not force) to main SHA `1848d3021bba76da626ca0b91716fbbaa5fc4481`; actual Git commit tree `e5776f3ff499baf8d77cf68548830a16a3988a08`, ordered parents `b397596941173027c7a0d33fddf38009ab837a87` and `1cb322b4ed921154d8c45fb12b7df9e4a2e9d082`. Postmerge main ref and STATE, S012 CLOSEOUT, NEXT_SESSION_PROMPT (full S013) readback VERIFIED.

**Individual hosted GitHub Actions successes**, not local claims: S012 branch push run `38744583831`, job `116454759964`; PR run `38744619489`, job `116454901443`; merged-main run `38744739014`, job `116455297661`. For EACH of these three jobs, (1) Unit tests, (2) Finite parity and orbit sanity (exact S000 cmp), (3) Recreate finite residue stream and cross-check original manifest (S001 regeneration/independent checker/JSONL consumer) were individually **SUCCESS**. Main log: **Ran 55 tests / OK**, including four new S012 methods and prior S003 corruption cases. Actual merged-main log SHA256: S000 `45a4ee995384ec9154bf092e272562172797e78bf771611b1d31376627498084`; regenerated S001 manifest `d4686d95c47107af29d939accb8d161684f929eb348426f2d39ea8b1819b2b37`; canonical JSONL records `adec6e2b05d0671170ced97304a69f25a518ad0cd658be7feaa8238f0eafc1f9`. Validation is for the merger SHA, not a universal mathematical proof. Protection read returned 403; rulesets [] (no assertion of complete policy knowledge). The post-attestation commit has its own CI to be checked separately.

S013 is FUTURE/UNEXECUTED. Collatz, Terras CST, novelty, Lean, Palomar, publication remain OPEN/UNCLAIMED.
