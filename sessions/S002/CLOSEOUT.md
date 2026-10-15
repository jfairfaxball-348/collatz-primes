# S002 closeout — exceptional transfer and factor re-entry (15 October 2026)

**Outcome:** CP-0014—CP-0018 proved internally as elementary, exact quantified statements (research/S002_PROOFS_AND_OBSTRUCTIONS.md). Full composite/full Collatz conjecture CP-0007 **OPEN**; no global strict-descent rank or reverse-basin completeness found; no independent mathematical peer review or originality claim.

## Mathematical deliverables

1. CP-0014: exact child-by-child necessary-and-sufficient strict full-class certificate test, including high-child representative thresholds, opposite next parity and the special base1 exception. Nested exceptional tower persists; no proof positive paths leave it.
2. CP-0015: all integers 27+2^59*q, q>=0, have **exact first descent step 59** by full 59-symbol parity word and symbolic affine lift. Formula T^59=23+3^37*q; 3^37 <2^59; all first 58 prefix slopes >=1. Infinite composite subfamily q divisible3; does NOT cover all 27 mod2^16.
3. CP-0016: exact two odd U-step factor re-entry gcd(x,U²(x))=gcd(x,2^a+3), a=v2(3x+1). For all x=20t+15 this gcd is 5, with 15->23->35. A factor disappears after one step yet returns after two, so no monotone factor-support rank.
4. CP-0017: U(x)≡(-1)^v2(3x+1) (mod3), always ±1. Multiples3 have no odd U-predecessor, but can and do converge (3->5->1).
5. CP-0018: for every k, distinct odd starts x,y>1 are congruent mod2^k yet U(x)=1 and U(y)=5, so fixed 2^k state does not determine U(x) mod3; this is NOT a no-go for all mixed automata.

Necessary least counterexample residues stay 7,15,27,31,39,43 mod48; no new universal exclusion. Original novelty UNCHECKED. See separate source-to-lemma table and hostile failures in research proof file.

## Computational status and evidence boundaries

- At S002 entry, S001 branch PR run https://github.com/jfairfaxball-348/collatz-primes/actions/runs/38699290266, and merged-main run https://github.com/jfairfaxball-348/collatz-primes/actions/runs/38699378379 were **observed SUCCESS**, latter job 116303570398 with unit/S000 checks SUCCESS.
- Direct Python 3 exact arithmetic spot check at authoring: 27's first descent 59, T^59(27)=23, odd count37, integer constants for the family confirmed. This is a finite symbolic proof ingredient, not a finite frontier or universal theorem.
- This commit adds tests/test_s002_structure.py and a **consumer** of the real generated JSONL with canonical-row/order/shape/parity/first-certification/count/checksum checks, independent of the producer. CI now runs original unittest, S000 audit, generator with manifest + records, byte-compare to frozen S001 manifest, regenerating checker, consuming checker and SHA256 output. No existing S001 manifest/count is reclassified.
- Exact PR/merged-main CI and hashes: not asserted here at authoring; verify the actual hosted runs and cite URLs in final owner closeout. Local git clone was unavailable due container DNS; no assertion of local execution of the exact original command.
- No Lean, Palomar, arXiv submission, new finite Collatz frontier, external novelty clearance, or universal theorem is claimed.

## Hostile failure register

No uniform depth bound (CP-0012), no inferred positive divergent 2-adic branch; no reverse-parent rank at y divisible3 or y=1 mod3; fixed-window prediction of U mod3 false (CP-0018); prime-support rank false (CP-0016); 27+2^59*q cylinder does not cover 27+2^16*q. Remaining universal obligation: every n>1 admits finite first descent, or a complete independent reverse-basin cover.

## Next session prompt — exact full copy, FUTURE / UNEXECUTED

# S003 — Stopping-time slope threshold and exceptional-path termination (FUTURE / UNEXECUTED)

Repository: https://github.com/jfairfaxball-348/collatz-primes

**Authority:** An owner request to run this linked or pasted prompt executes exactly S003 immediately without further confirmation. This file is only a handover; S003 has NOT executed. Do NOT automatically execute S004.

## Governing target and non-negotiable truth

Prove every composite positive integer reaches 1 under the shortened map T(n)=n/2 (even), (3n+1)/2 (odd). By CP-0001 this is the full Collatz conjecture. OPEN. Neither the verified finite depth-16 residue certificates, CP-0015's infinite cylinder around 27, nor CP-0016's prime-return identity implies global convergence. Avoid any implication from 2-adic compactness to positive-integer divergence or from relative finite depth to universal first descent.

## Entry and governance

Pin LIVE main SHA and tree, check S002's actual one-parent authored commit, PR, ordinary two-parent merge parents/tree, separately check PR and merged-main hosted runs/jobs, all open PRs/branches and accessible rulesets. Branch-protection 403 means UNKNOWN, not absent. Read AGENTS.md, README.md, authoritative/{START_HERE.md,STATE.json,NEXT_SESSION_PROMPT.md}, docs/{SESSION_PROTOCOL.md,EVIDENCE_POLICY.md}, all S002 proof/input/closeout files, research/{S000_FOUNDATIONS.md,S001_PROOFS_AND_OBSTRUCTIONS.md,S002_PROOFS_AND_OBSTRUCTIONS.md,CLAIMS.md,FAILURE_LEDGER.md,SOURCES.md,RESEARCH_ROUTES.md}, sessions/LEDGER.md, certificate generator/checker/consumer/tests, and CI. Execute tests, generator, independent checker, consumer and S000 audit; save real logs and SHA256 and explicitly label any unavailable runtime. No concurrent-work collision.

## Attack A — first-descent vs parity-slope threshold

For n>1, let j_s(n) be the least j>=1 such that T^j(n)<n, if it exists. Let a_j(n) count odd inputs among the first j and define j_c(n) as the least j with 3^{a_j}<2^j, if one exists. The S002 finite exploratory observation is j_s=j_c on the explored starts, NOT a theorem. Derive the exact affine intercept condition and either (i) prove the universally quantified equivalence without presupposing termination, or (ii) provide the smallest explicit counterexample with full parity word, coefficients and trace. Do not infer equivalence from samples. Even if the equivalence is proved, it is NOT Collatz unless finiteness of j_c for every n>1 is proved separately.

For a branch with j_c=j, derive an honest bound on the intercept b_j relative to its least positive representative. Attack candidate bounds symbolically using arbitrary long O-prefixes, the n=1 exception and parity cycles. Test for counterfamilies beyond shallow depth; preregister the exploration split before inspecting any new data.

## Attack B — exceptional child transition and finite-state impossibility

Use CP-0014's exact two-child criterion to seek a genuine well-founded rank on positive exceptional representatives, not merely E_(k+1) subset of inverse image E_k. Investigate whether OPEN at k is equivalent to 3^{a_j}>=2^j for all j<=k for every representative r>1; this was only finitely observed at depth16, not established. Prove it or produce a hostile residue/counterexample. Examine how new early certification at high lifts could invalidate naive tree recurrences.

Find a noncircular theorem showing that every fixed positive n eventually leaves the exceptional tower; alternatively prove a precise obstacle for a clearly delimited class of automata/ranks. The universal tower exit is equivalent to global strict descent and remains OPEN. CP-0018 precludes predicting U(x) modulo3 from a fixed modulus 2^k alone, NOT all mixed 2-adic/3-adic automata.

## Attack C — prime re-entry arithmetic and reverse-basin rank

Extend CP-0016 gcd(x,U^2(x))=gcd(x,2^a+3) to m accelerated odd steps with exact valuation-sensitive affine offsets. Decide whether any proposed multiplicative/factor-count potential decreases after bounded or start-dependent many U steps. Kill candidates on x=15+20t, x=121, x=27, the composite growth family 12t+3, and all y divisible by3 (which have no U predecessor).

Test a genuinely non-tautological reverse-basin grammar for categories y=0,1 mod3 and the six least-counterexample residues mod48. Distinguish a finite rule system from its *unproved universal coverage*. A source class modulo3 does not imply divergent starts.

## Validation, literature and end state

Re-run original k10..16 producer and S001 manifest comparison, independently regenerate and consume the canonical JSONL with direct record integrity checks; design deliberate corruptions (missing row, reordering, wrong parity, wrong status, wrong hash) and require rejection. Replay exact first-descent-59 cylinder and CP-0016 identities with independent code. Inspect primary Lagarias, Tao (2022), Bařina (2025), Angeltveit (2026), Simons–de Weger and Hercher INCLUDING corrigendum before importing external bounds. Differentiate PROVED_INTERNAL, FINITE_CERTIFICATE, SOURCE_STATED, EXPERIMENT, REFUTED, OPEN; no originality or Lean/Palomar assertion without evidence.

Finish exactly S003 in one isolated branch and coherent commit if possible, real PR, successful observed hosted checks, ordinary merge, independently verified live main SHA/tree/parents/file readback. Update claims, failure ledger, sources, routes, sessions/S003/INPUT.md, proof record and CLOSEOUT.md, ledger, authoritative status. Write COMPLETE S004 FUTURE/UNEXECUTED next prompt in authoritative/NEXT_SESSION_PROMPT.md AND verbatim inside closeout. If blocked, identify exact incomplete GitHub actions and never fabricate results. Return all links and full S004 handover.

---
**S002 ends here. S003 NOT executed.**
