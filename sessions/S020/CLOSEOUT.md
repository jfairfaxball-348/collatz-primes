# S020 CLOSEOUT — 2026-10-16

## Mathematical accomplishment

**CP-0070 PROVED_INTERNAL, elementary:** exact normalized affine carry H(V)=(B_V+2^|V|)/3^#O(V) is UNCHANGED by appending O and increases by S(V)=2^|V|/3^#O(V) by appending E. For EVERY arbitrary concatenation of k>=1 blocks selected independently from {OOOE, OOOOE}, H(U)<19/11, even for sequences with bounded runs and aperiodic symbolic limit.

**CP-0071 PROVED_INTERNAL, elementary:** for EVERY m>=1, at least one of delta(m),delta(m+1)>1/3 where delta(m)=2^bit_length(3^m)/3^m-1. Elementary proof: if the first ratio q<=4/3, the next bitlength jumps EXACTLY two and the next ratio becomes (4/3)q>4/3. NO Matveev.

**CP-0072 PROVED_INTERNAL, elementary and genuinely arbitrary block transitions:** ANY overcritical U beginning O^a with 3*(B_U+Q_U)<(2^a-1)*A_U has some d in {1,2} such that ALL positive inputs in W=U O^d E^(bit_length(3^(r+d))-|U|-d) strictly descend at their actual FIRST coefficient crossing. The alphabet {OOOE,OOOOE} obeys this uniformly for ALL finite k and arbitrary choices. Infinitely many certified inputs composite. No fixed repeating period, enormous threshold, source analytic theorem, or finite maximum k is required.

**IMPORTANT NONCOVERAGE:** This is a conditional theorem on CHOSEN extensions of U. It does NOT show an actual arbitrary integer has the prescribed extension, so all-positive/composite Collatz, Terras CST and an all-n terminating admission algorithm remain OPEN. No independent priority assessment clears publication.

## Evidence and code

Standalone scratch local Python 3 6 tests PASS (3.913s); 2046 variable-block words k1..10, d1=1225/d2=821, canonical least lifts and two further positive lifts exact; 150 irregular blocks; 20,000 exact two-choice exponent pairs; 71/512 historical exceptional check; selected expanding/forced-O hostile cases. Source SHA256 b66a6fc40ac2bfeafddbc05cb03bba08f4ae7a614c307d97323884ed02cd5d09, output SHA256 94eced05644b55bcd6ccc8c6d4ede7a206a90bc85851342004e183f70b21d130; scratch paths are not GitHub files. Checked-in S020 original tests require hosted post-push confirmation separately. Historical S000/S001 golden manifest SHA and S003 corruption remain to be checked in new workflow.

Source S020 primary Matveev2000 printed1219 Cor2.3 directly re-inspected, full 53-page proof not rederived and NOT invoked. Bernstein–Lagarias1996 parity conjugacy and Terras1976 are material prior art; Steiner1978 original unavailable, later Simons/de Weger finite-cycles and Rozier/Terracol 2026 CST-open checked by official metadata. Priority/novelty UNCHECKED. NO_LEAN_VERIFIED (no lean/lake locally); proof-ready Nat Lean specification only, no compiling Lean; no Palomar/preprint/journal or all-n claim.

## GitHub provenance

At entry live main 3342189c197b4e11f2e0c9a951076d3e7abb0977, true Git tree 7379373e0bd930d9e37d96a5d9dc51221da44e6d, ordered parents [9adefb03af2493e59582a77b5a82bc13a859bf4c,f52996e03a7fc15c669200e39cc300cfcea6390d]. No open PRs, rulesets [], protection403 UNKNOWN; BEFORE S020 main run38881357952/job116908595237 had all substantive steps SUCCESS. This initial research closeout does NOT anticipate branch/PR/main outcome for S020. Later provenance may be appended on a separately verified follow-up write, distinguishing the original research commit's hosted checks from later attestation checks.

## FULL NEXT-SESSION PROMPT — S021 FUTURE / UNEXECUTED (verbatim)

# S021 — formalise the elementary two-choice aperiodic-cylinder theorem and hard novelty gate (FUTURE / UNEXECUTED)

Repository https://github.com/jfairfaxball-348/collatz-primes

AUTHORITY: This COMPLETE S021 instruction was prepared at S020 close; S021 is FUTURE / UNEXECUTED. Only the NEXT fresh owner "run next session" executes exactly S021, never preparation itself.

## Required entry, no stale assumptions

Inspect live main SHA, ACTUAL Git tree, ordered parents, open PRs, branch protection/rulesets (403 means UNKNOWN), last FULL hosted main workflow and each substantive step. Read AGENTS.md, docs/SESSION_PROTOCOL.md, docs/EVIDENCE_POLICY.md, authoritative STATE/START_HERE/NEXT_SESSION_PROMPT, latest S020 INPUT/CLOSEOUT/research proof/Lean specification/validation/test, S019 proof, updated CLAIMS/FAILURE_LEDGER/SOURCES/LEDGER. Preserve other contributors' commits and refuse a stale-parent write.

## Mandatory mathematical and formal deliverable — no another data-only session

CP-0070 exact carry H=(B+Q)/A, CP-0071 for every m>=1 one of delta(m),delta(m+1)>1/3, and CP-0072: arbitrary transitions among P_i in {OOOE, OOOOE}, U=P_1...P_k, choose d in {1,2}; all positive W=U O^d E^b cylinders STRICTLY drop at actual FIRST coefficient crossing. The core proof is completely elementary (NO Matveev). Formalise the most valuable self-contained step in ACTUAL Lean 4 using a pinned installed toolchain, real checked-in .lean code without sorry/axioms, and an observed GitHub CI job. Prioritise CP-0071 Nat pow/bitlength lemma plus the conjugated affine identity and inductive carry inequality CP-0070. If full CP-0072 not finished, compile a useful nontrivial narrower theorem and leave rest clearly NO_LEAN_VERIFIED. The proof-ready specification research/S020_LEAN_SPEC.md is NOT verified source.

## Critical prior-art check / publication triage

Search primary Bernstein–Lagarias 1996 2-adic parity conjugacy (full 16-page article if accessible), Terras 1976 original 12 pages and stopping-time literature; specifically test whether the two-choice bounded-carry variable-block strict-cylinder theorem was already stated and whether it genuinely adds to S015–S019. Distinguish generic affine identities (classical), elementary corollaries, a credible novel theorem and unreviewed conjecture. No publication claim without source-complete originality and independent mathematical inspection. Steiner 1978 primary remains UNACQUIRED unless actually read; Matveev original §2 Cor2.3 is ln|Lambda|, 53-page proof not redone, but CP-0070–72 are analytic-free. Record novelty UNCHECKED if uncertain.

## Aggressive theorem strengthening or falsification (choose one real gap, not just tests)

Try replacing two overcritical blocks by a wider explicitly quantified finite alphabet satisfying H< (2^a-1)/3. Explore the SHARP threshold of the two-consecutive exponent gap or a bounded-gap d<=D certificate for ALL variable overcritical alphabets. In every purported generalisation calculate canonical least lifts exactly and seek a genuine overshoot D*n0<=B_W; never confuse failed sufficient bound with counterexample. Conversely investigate whether a nonselective all-d and all-extension theorem is false. Try to demonstrate precise remaining obstruction to an all-integer admission theorem, not a fabricated totality proof. Re-test residual 71/5041, 27/43/91/155/251, 393243+524288k, 64k+59->72k+67, 2^H u-1 towers, and six 7/15/27/31/39/43 mod48 classes. An arbitrary compatible finite exception path is NOT an infinite divergent orbit.

## Reproducibility and GitHub closure

Write research proof/obstruction, ACTUAL Lean module+CI or honest NO_LEAN_VERIFIED, independent exact tests with finite bounds and SHA256, update numbered claims/failures/sources/STATE/START_HERE/LEDGER, S021 INPUT and CLOSEOUT, and install full S022 FUTURE/UNEXECUTED prompt both in NEXT_SESSION_PROMPT and S021 CLOSEOUT. Prefer new dedicated branch/PR, check original branch and PR workflow individually, ordinary nonforce merge with HEAD/base verification, read live main true Git tree+ordered parents and independent new merged-main original CI, including S000 byte/SHA, S001 depths10–16 checker/JSONL and S003 corruption checks. If blocked, report it precisely, never claim merge or verification. Never assert universal Collatz/composite convergence, Terras CST, proven originality, Lean/Palomar or paper unless actual action/evidence matches.