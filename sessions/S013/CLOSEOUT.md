# S013 research closeout — 2026-10-15

## Mathematics, classification and limitations

S013 carried out the authorised S013 research and recorded CP-0050, CP-0051 and CP-0052 with full quantifiers/proofs in research/S013_PROOFS_AND_OBSTRUCTIONS.md.

- CP-0050 PROVED_INTERNAL relying on established externally sourced Matveev linear-forms logarithmic lower bound: for EACH FIXED admissible (a,c), ALL sufficiently large m have genuine first coefficient crossing and STRICT descent for EVERY positive parity-cylinder lift of O^a E^c O^(m-a) E^(ceil(m log2 3)-m-c). Unlike S012 no bounded-away-from-zero delta and no D<K assumption needed. This is only a proper family of parity words; no numeric reasonable threshold or global theorem.
- CP-0051 PROVED_INTERNAL: explicit dual-modulus CRT least carry h and exact integer necessary/sufficient strict/equality/overshoot sign test for two-run first crossings (conditional on independently checked earlier coefficients).
- CP-0052 PROVED_INTERNAL: maximal consecutive O run for an odd integer has EXACT length v2(n+1), which is a finite integer-dependent rank but NOT a descent certificate; a later E step restores potential and CP-0041 grows across same-valuation returns.

TWO separately specified integer-dependent descent algorithms attempted: exact signed-affine forward-search certificate (A1) and v2-run/block-accelerated or reverse-graph membership certificate (A2). Individual micro-steps are terminating and fully verifiable. Global completion of A1 or A2 requires the unproved all-positive eventual descent/coverage lemma U-S013; 71 states and 5041 transitions, CP-0041 growing return, forced odd tower and six 7/15/27/31/39/43 mod48 classes remain as adversarial constraints. No complete covering family with a noncircular termination proof was found. No 2-adic infinite finite-prefix path was mistaken for one divergent positive integer.

LOCAL finite-only validation: four isolated Python 3 unittest methods PASS, exact 3,854 admissible triples, 43 D<K / 3,811 D>=K, nine full prefix samples, odd-run and original 71-exception boundary controls. Original hosted full repository CI status for this NEW commit must be obtained separately and reported in an attestation after observation; previous S012 workflow success is not S013 success.

Literature: Matveev theorem was inspected in published secondary explicit quotation https://link.springer.com/article/10.1007/s40993-021-00252-2; original primary not separately inspected. Terras 1976, Simons/de Weger 2005, Rozier/Terracol October 2026, Niu May 2026 compared; Steiner 1978 original primary still NOT ACQUIRED/READ. Priority of this structured grammar result NOT ESTABLISHED.

**Global positive/composite Collatz OPEN. Terras coefficient stopping time OPEN.** No Lean, Palomar, formal proof, external mathematical certification, arXiv submission, journal publication or novelty established.

## FULL AUTHORITATIVE S014 NEXT SESSION PROMPT — FUTURE / UNEXECUTED

# S014 — uniform-grammar generalisation, quantitative Baker thresholds and noncircular exceptional exit (FUTURE / UNEXECUTED)

Repository: https://github.com/jfairfaxball-348/collatz-primes

AUTHORITY: The next explicit instruction from the owner to run the next session authorises exactly S014 immediately; this is a complete prepared prompt, NOT execution authority for S015.

## Mandatory entry
Read AGENTS.md, docs/SESSION_PROTOCOL.md, docs/EVIDENCE_POLICY.md, authoritative/START_HERE.md, authoritative/STATE.json and this entire prompt; S013 INPUT/CLOSEOUT/proof/tests/validation, S012 and S011 mathematical notes, research/CLAIMS.md, FAILURE_LEDGER.md, SOURCES.md and sessions/LEDGER.md. Independently examine LIVE main ref, exact commit tree and ordered parents, open/recent PRs, branch policies and actual hosted CI runs/jobs/individual steps. Do not invent CI status, originality, proof verification or a local clone. Preserve concurrent work.

## Attack A — still seek an ACTUAL universally terminating positive-integer descent certificate
S013 CP-0052 proves each maximal odd run has EXACT length v2(n+1), but the number of odd/even blocks may be unbounded and each O-run grows. CP-0041 expanding 11-step return preserves v2(n+1)=2; CP-0042 gives 71 exceptional states and all 5041 successors (arbitrarily long finite exceptional itineraries, NOT one infinite positive orbit). Try TWO rigorously different n-dependent descent/renewal algorithms: e.g. block-accelerated odd/even dynamics with a signed affine or 3-adic invariant; inverse-basin proof search with a meaningful decidable sufficient covering criterion. Exhibit exact termination potential under clearly stated hypotheses and try to falsify universal hypotheses on 27,43,91,155,251,393243+524288k, 2^H u-1, all six 7/15/27/31/39/43 mod48. Explicitly identify the unproved ALL-n lemma if unable to close it. Do NOT infer termination from density, all 5041 edges, 2-adic compatibility, or brute-force coverage at finite depth.

## Attack B — quantitative uniform Matveev theorem, beyond fixed a,c
S013 CP-0050 (using published Matveev's theorem) proves: for EACH fixed a,c>=1 with 3^a>2^(a+c), ALL sufficiently large m give genuine first coefficient crossings for O^a E^c O^(m-a) E^(ceil(m log2 3)-m-c), with strictly decreasing EVERY least and later lift, INCLUDING shrinking delta->0 and complementary delta>=kappa. Verify the exact Matveev-inequality transcription against a PRIMARY credible theorem (present reliance is on a published secondary explicit statement). Derive a reproducible explicit though enormous m0(a,c), check for any arithmetic error, and consider a,c growing with m while maintaining first crossing and t0 lower bound. Attack arbitrary parity words/carry patterns beyond two-run grammar: general CRT, later O-runs, equality and genuine first-crossing overshoot; do NOT conflate later paradoxical behavior with Terras CST. Attempt concrete counterparameters to any proposed generalisation, and classify exact integer congruence restrictions. CP-0051 gives a computable CRT h with exact sign comparison; seek a nontrivial new infinite family or a precise obstruction rather than restating an equivalent test.

## Required validation, literature and writeback
Rerun ORIGINAL GitHub-hosted full Python unit suite and workflow with exact byte cmp/hash of S000, S001 depth10–16 regeneration, independent certificate checker, JSONL consumer and S003 corruptions. Keep all earlier tests and 71/5041 graph. Add exact finite new probes with bounds; verify 27/43/91/155/251 controls; record branch/PR/main run IDs/job IDs/step conclusions, and distinguish local standalone tests. Continue Steiner 1978 original seven-page source search via libraries and cite it as INDIRECT until acquired; examine Terras 1976, Simons/de Weger 2005, Rozier/Terracol Oct2026, Niu May2026. Full novelty review still not completed.

Write S014 numbered claims, proofs, failed conjectures and proper counterexamples, tests, validation, source audit, INPUT/CLOSEOUT, updated STATE/START_HERE/CLAIMS/FAILURE/SOURCES/session ledger, and a COMPLETE S015 FUTURE/UNEXECUTED prompt BOTH in authoritative/NEXT_SESSION_PROMPT.md AND verbatim in CLOSEOUT. Branch/PR, merge only after actual CI success and safety inspection, then verify merged main HEAD/tree/ordered parents and file readback. Global Collatz/composite convergence and Terras CST, novelty, Lean, Palomar, arXiv, peer review and publication remain OPEN/UNCLAIMED without actual separate proofs/verification.


S014 is a future prepared session, NOT executed here. Verify actual S013 branch/PR/main CI and final Git tree separately before describing as hosted PASS.


### S013 hosted full-suite CI and merged-main verification — 2026-10-15

Original FULL GitHub-hosted repository Python suite and workflow, NOT standalone local evidence:
- branch push run 38748744680, job 116469213101; 59 unit tests PASS; substantive steps Unit tests, Finite parity and orbit sanity, Recreate finite residue stream and cross-check original manifest each SUCCESS.
- pull request #20 run 38748780774, job 116469340254; 59 unit tests PASS; same three substantive steps each SUCCESS. PR mergeability inspected CLEAN; premerge main unchanged. Rulesets [] and branch protection 403 (policy NOT fully observable).
- ordinary nonforce PR #20 merge to main SHA 76b0bcc89e485d67dd7799250593c277ec5068dd, ACTUAL git tree 526680f937ebc2003444650f33251cbd871f2a31, ordered parents cee8936245d497bdd51cc817c8283c8bd41b2839 and 15573dbd8ba30c13215e614e4da800ba0ccbd7c1. Main ref readback matched and STATE, full S014 prompt, S013 closeout and test source read back.
- merged main run 38748940596, job 116469898271; 59 Python tests OK including four S013 and legacy S003 corruption scenarios; individual Unit tests, S000 exact byte cmp/hash, S001 regenerated manifest byte cmp + independent checker + canonical JSONL consumer each SUCCESS. Seven certificate depths confirmed by independent checker. SHA256 from ACTUAL merged-main logs: S000 audit 45a4ee995384ec9154bf092e272562172797e78bf771611b1d31376627498084 ; S001 regenerated manifest d4686d95c47107af29d939accb8d161684f929eb348426f2d39ea8b1819b2b37 ; JSONL adec6e2b05d0671170ced97304a69f25a518ad0cd658be7feaa8238f0eafc1f9 .

These attest specific finite Python and file-regeneration checks only; CP-0050's universal-in-m proof is on paper relative to the published Matveev theorem. Collatz/CST OPEN, originality, independent proof refereeing, Lean, Palomar, arXiv and publication NOT established. The subsequent attestation commit creates its own CI run and cannot be described as checked until observed.

