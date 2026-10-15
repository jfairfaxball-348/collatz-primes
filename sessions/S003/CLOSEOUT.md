# S003 closeout — CST prior-art kill, affine cutoff and m-step prime re-entry

**Date:** 2026-10-15. **Mathematical outcome:** Full Collatz remains **OPEN / UNPROVED**. A critical source audit identified CP-0019 as **Terras' existing open coefficient stopping-time conjecture** (not original, not proved), including the distinction between first coefficient crossing and later paradoxical prefixes. No counterexample to CST was found.

**Exact elementary deliverables:** CP-0020 explicit intercept sum, extremal bounds and exact finite bad-lift interval at first coefficient crossing; CP-0021 exact valuation-sensitive m-step U affine offset and gcd re-entry; CP-0022 a fully delimited no-go for any fixed 2^k class table assigning a finite uniform first-descent horizon. Proofs and hostile cases are in research/S003_PROOFS_AND_OBSTRUCTIONS.md.

**Critical negative example:** n=7 reaches 5 at j=7 (its first coefficient crossing and first descent) yet at j=8 has 243/256<1 and T^8(7)=8>7. Thus "EVERY negative-slope step descends" is false even though CST may still be true.

**Finite-only work:** Discovery n=2..100000 and untouched holdout n=100001..1000000 each under step cap1000 had no CST mismatch and no cap; depth k10..16 OPEN representative counts 64,128,226,367,734,1295,2114 with no coefficient crossing; 27's first descent at j59 and m-step formula independently checked locally. These are NOT a proof. Exact original repository CI is responsible for full generator/manifest/independent checker/consumer/corruptions. Local container could not clone GitHub (DNS); GitHub connector handled remote writes and hosted workflow. Validation statuses / actual job evidence must be checked outside this authored text; do NOT infer PASS from code alone.

**Source audit:** Primary Rozier–Terracol (*Discrete Mathematics* 349:115167, 2026, doi:10.1016/j.disc.2026.115167; arXiv:2502.00948); Terras and Lagarias. Inspected **both pages of Hercher June 2026 corrigendum**: it fixes an erroneous derivation in Theorem 21 using a replacement convex-polytope argument, not a solution to Collatz. No technical external cycle bound imported. No original novelty, Lean, Palomar, arXiv or external proof validation is claimed.

**Github provenance at entry:** main cd06922419225d68853c38e8144066a37d7e16ec tree 02225d29f1314d5950040a37149637b25b4d527d, S002 PR #4 authored b714223d... parent cc35a3...; ordinary merge cd069224... (parents cc35a3... and b714223d..., matching tree). S002 PR run 38702830309 / job 116314910717 SUCCESS, main run 38702945301 / job 116315288005 SUCCESS. S003 PR/main outcome must be separately observed before claimed.

## Full next session prompt — S004 FUTURE / UNEXECUTED (verbatim)

# S004 — CST boundary, exceptional-tree compression and mixed-modulus rank (FUTURE / UNEXECUTED)

Repository: https://github.com/jfairfaxball-348/collatz-primes

**Authority:** The owner's next explicit instruction to run this linked or pasted prompt immediately authorises exactly S004. No second confirmation. This handover is not execution. Do not execute S005 automatically.

## Governing mathematical target

Prove every positive composite integer reaches 1 under shortened Collatz T(n)=n/2 for even n and (3n+1)/2 for odd n; by CP-0001 this equals the full Collatz conjecture. **OPEN.** Keep prime/composite claims, finite certificates, mathematical proofs and published source statements separate. No universal inference from bounded checks, almost-all, cycles alone or 2-adic compactness.

## Read first and provenance gate

Freshly pin remote main SHA and tree; reconcile S003's authored one-parent commit, PR, ordinary two-parent merge and matching tree, open PRs/branches/rulesets, and actual PR/merged-main hosted checks with job steps. A branch protection 403 means UNKNOWN. Read AGENTS, README, authoritative START_HERE/STATE/NEXT prompt, docs SESSION_PROTOCOL/EVIDENCE_POLICY, sessions/S003 INPUT/CLOSEOUT, research S003, CLAIMS, FAILURE_LEDGER, SOURCES, RESEARCH_ROUTES, S001/S002 proofs, the producer/checker/consumer, S003 corruption tests and CI. Ensure no active competing owner session. Owner invocation authorises this S004 only.

## Attack A — do not rebrand Terras' open CST conjecture

The S003 identification of j_s(n)=j_c(n) as **Terras' Coefficient Stopping Time conjecture** is binding. Read Terras (1976), Lagarias, and Rozier–Terracol (*Discrete Mathematics* 349, 2026, article 115167; arXiv:2502.00948). Respect its still-open status. Distinguish first coefficient crossing from later paradoxical prefixes: n=7 at j=8 has coefficient 243/256 yet T^8(7)=8>7, but first descent and first coefficient crossing both occur at j=7.

Use CP-0019/S003's exact bad-lift cutoff q bound for a parity cylinder and the extremal offset formula to seek a NEW delimited theorem with full quantified proof: e.g. a nontrivial family of first-crossing words where all positive representatives >1 satisfy descent, or an unconditional quantified bound on possible exceptional representatives. Do not merely restate the classical finite-exception theorem. Falsify every candidate on long O prefixes, 1+2^k q, n=7's paradoxical later window, 27's 59-step cylinder and sampled larger starts. Avoid claiming CST proven by sample agreement.

## Attack B — positive exceptional paths and finite-state rank

Go beyond CP-0022's fixed-modulus, fixed-finite-horizon impossibility: the all-O prefixes near 2-adic -1 refute EVERY finite depth bound assigned solely by n mod2^k, but do not preclude mixed-modulus state, valuation counters, arbitrarily growing windows or start-dependent ranks.

Formulate one concrete rank/grammar capable of handling the six hypothetical least-counterexample residues mod48 (7,15,27,31,39,43), with y=0,1 mod3 source/large-parent obstacles. Prove an actual descent/coverage lemma or construct an explicit structural counterfamily. Check CP-0014 child early certification at high lifts; do not assume exceptional set is a regular finite-state tree. Universal tower exit remains exactly Collatz; never close by assuming it.

## Attack C — valuation offsets and prime factors

Extend and exploit CP-0021: 2^{A_m} U^m(x)=3^m x+F_m where F_m=sum_{i=0}^{m-1}3^{m-1-i}2^{A_i} and gcd(x,U^m(x))=gcd(x,F_m). Search for a nontrivial *well-founded* size/factor/valuation potential after adaptive m, with a falsifiable inequality and proof. Test x=15+20t (prime5 return at m=2), x=121 (factor-count growth), x=27, every x=12t+3, long growth prefixes 2^k t-1, and U-predecessor-free y divisible3. An offset identity alone is not progress on convergence.

## Reproduction, source, closeout

Run full original unit tests, S000 audit, k10..16 producer, exact frozen S001 manifest comparison, independent checker, direct canonical JSONL stream consumer, corruption suite (missing/reordered/parity/status/hash), exact 27-cylinder and m-step offset tests. Preserve observed job IDs, statuses, commands and SHA256 from real runs; report unavailable local execution. Inspect up-to-date primary bounds and Hercher's June 2026 corrigendum (Theorem 21 correction), and check each claim's novelty status; do not claim original results, Lean, Palomar or full theorem without corresponding evidence.

Complete **only S004** with quantified proofs and hostile counterexamples, research note, claims/failure/sources/routes, sessions/S004/INPUT and CLOSEOUT, session ledger, authoritative status. Prepare a COMPLETE S005 FUTURE/UNEXECUTED handover verbatim in both next prompt and closeout. Prefer one isolated single-parent authored commit, real PR, observed successful checks, ordinary merge, and live SHA/tree/parents/readback verification. If any action fails, report the exact block rather than asserting success.

---
**S003 ends here. S004 remains FUTURE / UNEXECUTED.**
