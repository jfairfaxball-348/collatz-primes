# S007 CLOSEOUT — 2026-10-15

**S007 RESEARCH COMPLETE** (GitHub branch/PR checks independently observe after authoring). Universal CP-0007 composite/all-positive Collatz and CP-0019 Terras Coefficient Stopping Time remain **OPEN/UNPROVED**. No novelty, Lean, Palomar, publication or divergent-orbit claim.

**CP-0033, PROVED_INTERNAL elementary:** 30 precise FULL infinite parity cylinders, listed with j, odd count, exact word and output in research/S007_PROOFS_AND_OBSTRUCTIONS.md. They add **89/512** of EACH 27 and43 mod48 class, disjoint from CP-0031's **352/512**, hence total exactly **441/512=86.1328125%**, unhandled **71/512=13.8671875%**. Infinite composites in every cylinder by CRT. Coverage does not imply all starts converge.

**CP-0034, PROVED_INTERNAL elementary:** For a>=3, b minimal with 2^(a+b+2)>3^(a+1), in the true two-O-run word O^a E O E^b, all positive t congruent 3^{-(a+1)} mod2^(b+2) strictly drop at coefficient first crossing provided 4*2^(a+b+2)>=5*3^(a+1). At least one of each pair a,a+1 qualifies; this yields infinitely many parameterised full first-crossing cylinders. Direct proof uses positive intercept inequality; does NOT import Steiner/Simons cycle exclusion. Does not cover arbitrary multi-block words.

**CP-0035, PROVED_INTERNAL obstruction:** For every H>=8, a compatible parity cylinder 27 mod256 with word OOEOOOOO O^(H-8) contains infinitely many composites in EACH 27 and43 mod48 class whose first H T iterates stay STRICTLY above start. Thus a **uniform** finite descent-time bound is impossible even in this residual subtree. Nested 2-adic cylinders ≠ a single divergent positive integer. Does not exclude adaptive unbounded-time ranks.

**Source:** Original Steiner 1978 primary article NOT retrieved; the exact one-circuit theorem remains SOURCE_STATED via Lagarias, consistent with Simons/de Weger original 2007 author PDF, which also cites existing no-nontrivial-2-cycle work. Terras and Rozier–Terracol confirm CST is OPEN. Novelty UNCHECKED.

**Independent FINITE_TEST:** exact Python probes PASS, script SHA256 ae653f33a162f3c256d3c2e03a1e1873a351ced451490e6907023ce736fb6cb0 and canonical result JSON SHA256 4bda38601fdc6874c36b125696ea5c37a594ec40d4b7a4d63bcc0a2b3e56e8c8; details validation/S007_LOCAL_PROBES.md. Original repo clone DNS unavailable and actual ORIGINAL unittest/manifest/consumer were NOT run locally; S007 CI must be observed separately on PR and merged main. S006 PR/main hosted CI WERE independently checked: 38715995495 / job 116358694217 and 38716089354 / job 116359009506, all step-level checks successful. We do NOT conflate either with S007 runs.

**Gap:** 71/512 still unhandled inside each hard class; other four least-counterexample residue classes and all unbounded positive exceptional towers are OPEN. A global well-founded rank, strict descent for EVERY n>1, and a proof of reverse-basin completeness remain unavailable. No composite convergence proof.

## COMPLETE S008 NEXT SESSION PROMPT (VERBATIM — FUTURE / UNEXECUTED)

# S008 — residual 71/512 renewal-rank test and two-block boundary (FUTURE / UNEXECUTED)

Repository: https://github.com/jfairfaxball-348/collatz-primes

**Execution authority:** The owner's next request to run the current authoritative prompt immediately authorises EXACTLY S008 in this repository. Do not require another confirmation and do not auto-execute S009. Read AGENTS.md and docs/SESSION_PROTOCOL.md.

## Governing mathematical target
Prove that every composite positive integer eventually reaches 1 under shortened Collatz T(n)=n/2 for even n and (3n+1)/2 for odd n. This is equivalent to full Collatz and is OPEN. Terras' Coefficient Stopping Time conjecture is OPEN. Do not infer the universal statement from percentage coverage, source-reported cycle theorems, or large tests; originality is NOT established.

## Mandatory live entry
Pin current live main SHA, exact commit-tree SHA and parents; inspect authored commits, recent merged/open PRs, stale branches and rulesets/protection; inspect separate PR/main hosted workflow runs, jobs and steps and reconcile the S007 pending evidence. Read authoritative START_HERE/STATE/NEXT, research S001–S007 proofs, CLAIMS/FAILURE_LEDGER/SOURCES/RESEARCH_ROUTES, S007 INPUT/CLOSEOUT, validation/S007_LOCAL_PROBES.md, tests/test_s007_math.py and existing CI. Preserve concurrent edits.

## Attack A: the hard 71/512, beyond coverage percentages
S007 CP-0033 certifies 441/512 of EACH r=27,43 mod48 class by 33 disjoint full parity cylinders: S006's three and S007's 30 added at depths 8,10,12,13. The residual 71/512 is not proved to descend in bounded time. Enumerate its exact symbolic residue-tree representation at depth13; seek a **noncircular regenerative/renewal inequality or well-founded state/energy ranking** on the full infinite residual subtree rather than more percentages alone. Explore 27 mod256, 91 mod96, y=0,1 mod3 inverse obstacles, composite witnesses, and the other four hypothetical least-counterexample mod48 classes. Require explicit precise quantifiers, positivity, branch exhaustiveness and a falsifier.

## Attack B: confront arbitrarily slow finite descent and CST
CP-0035 proves for every H>=8 there exist infinitely many composites in BOTH r27 and r43 mod48, also congruent 27 mod256, that remain ABOVE their own start for every 1<=j<=H: forced parity prefix OOEOOOOO followed by O^(H-8). Thus no fixed-step bound or bounded-memory step count closes even that subtree. Test adaptive start-dependent blocks / global rank that do not require a uniform horizon. Explicitly distinguish finite paths from a single infinite natural-number trajectory and do not mistake the nested 2-adic path for divergence.

## Attack C: genuinely enlarged multi-block theorem
CP-0034 proves strict first-coefficient-crossing descent for infinitely many exponents a>=3 on the full O^a E O E^b cylinder (b minimal with 2^(a+b+2)>3^(a+1)), provided 4*2^(a+b+2)>=5*3^(a+1); at least one of each adjacent pair a,a+1 meets this. Determine what happens in the complementary near-resonant exponents with exact t0, intercept and strict-drop threshold, and test more general O^a E^c O^d E^b. Do not assert general multi-block CST; source-compare to Steiner 1-cycles, Simons/de Weger 2-cycle work and Rozier–Terracol paradoxical prefixes.

## Computation, sources and close
Run repo unittest and S000 audit byte/hash check, frozen S001 depth10–16 manifest exact comparison, independent checker, canonical JSONL consumer and S003 corruptions; separately check CI PR and merged-main results. Run independent exact integer adversarial tests for boundary congruences, all new cylinders, the least reps, 7 prefix, 27/91, 121->91, 15->23->35, 681->511 and the mod3 source failures. Acquire Steiner 1978 primary article if accessible, else keep SOURCE_STATED indirect; review 2026 literature and no-cycle citations carefully. Produce complete S008 proofs/obstructions, evidence, claims/failures/sources/routes, sessions/S008 INPUT+CLOSEOUT, state and complete S009 FUTURE/UNEXECUTED prompt copied verbatim into closeout. Prefer safe branch/PR, independently observed PR CI, ordinary merge and verified main SHA/tree/readback. No Lean, Palomar, publication or universal proof claims without corresponding evidence.


---
S007 stops here. S008 is FUTURE / UNEXECUTED.
