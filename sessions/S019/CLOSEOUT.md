# S019 CLOSEOUT — 2026-10-16

## Result
CP-0068 **PROVED_INTERNAL elementary**: for any finite P, A=3^r, Q=2^ell, B=B_P, all positive n following P^k satisfy Q^k | (A-Q)n+B; if A>Q then n>=(Q^k-B)/(A-Q). Hence every fixed positive n can follow a FIXED overcritical P only a finite computably bounded number of consecutive repetitions; changing/aperiodic words remain unrestricted.

CP-0069 **PROVED_INTERNAL conditional on SOURCE_STATED Matveev 2000**: for any fixed overcritical block P with at least one E, every P^k O^d E^b first-coefficient crossing cylinder strictly descends, uniformly all d>=1, for every k above explicit computable K(P). Stronger exact elementary sufficient check (2^j-3^m)(Q^k-B)>3^m max(A-Q,B), and exact constant normalised intercept H_k=B/F+(1-B/F)(Q/A)^k. Initial odd run may remain bounded (P=OOOE), #E-blocks unbounded, r(U)/d unbounded, so this is OUTSIDE S018's leading-run and S016's r/d scope. Full proof research/S019_PROOFS_AND_OBSTRUCTIONS.md. No unconditional universal all-U theorem, actual first-cross overshoot or all-n renewal halting proof.

Exact finite independent 143 overcritical P patterns length2..10, k1..12,d1,2,3,5,9: 8580 first crossings with real modular n0 all drop, 7854 certified by simpler exact inequality, remaining 726 merely sufficient-bound failures. Existing 71/512 exceptional length13, 5041 possible transitions, hostile 27/43/91/155/251, forced-O composites, expanding returns remain globally unclosed. Novelty NOT established: earlier Bernstein–Lagarias 1996 2-adic parity coding directly relevant; Matveev SOURCE_STATED original printed p1219 directly inspected, proof not rederived, Steiner 1978 primary unread. All composite/full positive Collatz and Terras CST OPEN, no Lean, Palomar or publication claim.

## GitHub provenance
S019 began from live e35857c7b6fd5054598998f009c39cd0edb4d3a6 and true tree 0fdb82ac1ebe3ba56d0ff89d4a5ea5bcd9689040; PRE-S019 hosted main run38813824079/job116693394879 all 3 substantive steps SUCCESS. S019 new hosted workflow/PR/main status must be independently observed after research commit, NOT inferred from earlier runs. Branch research/s019-periodic-parity-divisibility; no push/merge outcome asserted in this initial proof closeout.

## FULL NEXT-SESSION PROMPT — S020 FUTURE/UNEXECUTED, VERBATIM

# S020 — variable-period aperiodic renewal or certified small theorem formalisation (FUTURE / UNEXECUTED)

Repository: https://github.com/jfairfaxball-348/collatz-primes

AUTHORITY: Prepared at S019 close. This COMPLETE S020 instruction is FUTURE / UNEXECUTED, and the NEXT fresh owner "run next session" executes exactly S020; S020 is NOT automatically executed by preparation.

## Required entry
Read AGENTS.md, docs/SESSION_PROTOCOL.md, docs/EVIDENCE_POLICY.md; authoritative START_HERE, STATE, NEXT_SESSION_PROMPT; S019 exact INPUT/CLOSEOUT/mathematics/tests/validation; S018, S017, current CLAIMS, FAILURE_LEDGER, SOURCES, session LEDGER. Recheck LIVE default main commit SHA, true git tree and ordered parents, open PRs, branch policy/rulesets (403/unknown is not PASS), last hosted workflows and each substantive step. Keep other contributors' commits safe and compare main SHA before writes.

## ONE aggressive mathematical target: from fixed period to changing blocks
S019 CP-0068/0069 proves for every fixed overcritical block P with E letters and all sufficiently large k, and EVERY d>=1, EVERY positive cylinder P^k O^d E^b strictly descends at its FIRST coefficient crossing (SOURCE_STATED Matveev); exact Q^k|(A-Q)n+B lower bound holds with no analytic input. The missing cases are multi-E prefixes with no long repetition of a FIXED P, bounded initial odd run, r/d unbounded, and patterns of changing blocks P_1 P_2 ... . Develop a rigorous POSITIVE theorem for variable P_i with explicitly quantified conditions not implied by a fixed P: e.g. a finite alphabet of overcritical blocks of bounded lengths with arbitrary transitions, a common denominator/carry invariant, a noncommutative affine product with provable exponentially growing canonical minimum, or a new explicit 2-adic separation bound. Falsify each candidate on exact canonical least lifts before promoting it. If a fully unrestricted theorem fails, provide exact U,d,n0,j,T^j(n0) genuine first-crossing overshoot (not simply insufficient bounds), or prove a narrower honest theorem.

## Publication/formalisation gating — do not spend another session only collecting data
Assess CP-0068/0069 for precise mathematical novelty against Bernstein–Lagarias 1996 2-adic parity conjugacy, Terras 1976 and related rational periodic parity codes. If original priority genuinely uncertain, label UNCHECKED and DO NOT claim paper-ready. Identify the strongest short SELF-CONTAINED elementary lemma suitable for immediate Lean 4 proof (periodic affine identity and divisibility), and if toolchain is available implement an actual compiling Lean file plus logged CI; otherwise produce a proof-ready Lean specification with exact types, natural-number divisibility and sign domains and an explicit NO_LEAN_VERIFIED label. Do not substitute a pseudo-Lean text for a compile.

## Exhaustive global-certificate pressure
Try integer-dependent all-n admission/exit TOTALITY, distinguish finite sound certificates from proved termination. Test 71 exceptional states/5041 edges, 27/43/91/155/251, 393243+524288k expansion, 64k+59 ->72k+67 same-v2, 2^H u-1 forced-O towers, all 7/15/27/31/39/43 mod48. No finite path compactness or composite multiplicativity, no unproved universal rank.

## Sources, tests and writeback
Recheck Matveev 2000 ORIGINAL English printed p1219 §2 Cor.2.3 log|L| (L=jln2-mln3, delta=e^L-1), note no rederivation of full proof; Steiner 1978 PRIMARY unavailable unless actually acquired, Terras 1976, Simons/de Weger 2005, Rozier/Terracol 2026, Niu 2026, Bernstein–Lagarias 1996. Exact independently reproducible scripts with SHA256 and hostile examples; observe hosted S000 byte/SHA, S001 depths10–16 manifest/checker/JSONL, S003 corruption and new S020 unit tests. Update numbered claims/failures/sources, STATE, START_HERE, ledger, S020 INPUT/CLOSEOUT, proof and validation, and install COMPLETE S021 FUTURE/UNEXECUTED prompt verbatim in NEXT_SESSION_PROMPT and S020 CLOSEOUT. Prefer new branch, checked PR, observed branch/PR CI, nonforce safe merge, main ref/tree/ordered parents/readback and independent merged-main original CI. NEVER claim universal Collatz/composite convergence, Terras CST, novelty, Lean/Palomar, preprint or journal without actual matching proof/action.



## S019 INDEPENDENT original research PR #32 and merged-main hosted attestation — 2026-10-16

Dedicated research branch research/s019-periodic-parity-divisibility final original research HEAD e215700a5a5d333eac91a56e123afa233babcc5e had true git tree 72c1e8b26445b2e91b055db90bb0a2f6b2ca2422 and single ordered parent 6a791d61deeb544e63a26cc29a69480b116b611e (the preceding proof clarity amendment; initial research commit 6a791d61deeb544e63a26cc29a69480b116b611e had original base parent e35857c7b6fd5054598998f009c39cd0edb4d3a6). PR #32 https://github.com/jfairfaxball-348/collatz-primes/pull/32 was checked as mergeable=true, clean, head unchanged e215..., and PR base matching independently read unchanged main e358... . Github nonforce merge_method=merge with expected_head_sha returned merged=true, resulting SHA 9adefb03af2493e59582a77b5a82bc13a859bf4c. Independently read live main SAME SHA, underlying true git tree 72c1e8b26445b2e91b055db90bb0a2f6b2ca2422, ordered parents [e35857c7b6fd5054598998f009c39cd0edb4d3a6,e215700a5a5d333eac91a56e123afa233babcc5e]. Remote main STATE S019 COMPLETE/S020 FUTURE_UNEXECUTED, full S020 prompt, S019 CLOSEOUT and proof all read back.

Independently observed TRUE ORIGINAL S019 GitHub Actions hosted CI, all 3 substantive steps (Unit tests; Finite parity and orbit sanity; Recreate finite residue stream and cross-check original manifest) EACH COMPLETED SUCCESS in each run:
- S019 final BRANCH push run38880983331 job116907374205;
- PR #32 run38881024455 job116907507642;
- NEW merged-MAIN push run38881098610 job116907747783.

Original branch and main raw logs each report **Ran 92 tests / OK**, all SIX new test_s019_math methods individually ok, earlier S003 corruption tests still in unittest discovery. Original S000 regenerate byte-for-byte cmp success and SHA256 45a4ee995384ec9154bf092e272562172797e78bf771611b1d31376627498084. Original S001 independent complete 7 depth checker success, JSONL STREAM CONSUMER PASS, manifest SHA256 d4686d95c47107af29d939accb8d161684f929eb348426f2d39ea8b1819b2b37, records SHA256 adec6e2b05d0671170ced97304a69f25a518ad0cd658be7feaa8238f0eafc1f9. These were OBSERVED, not imputed from older sessions.

The NEW attestation-only documentation commit itself triggers new GitHub checks, not covered by these original S019 successes; independently inspect those separately before merging attestation. Full Collatz/composite, Terras CST, general aperiodic all-U, novelty, Lean, Palomar, publication remain OPEN / UNCLAIMED. S020 still FUTURE/UNEXECUTED.
