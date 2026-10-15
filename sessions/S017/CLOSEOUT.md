# S017 closeout — 2026-10-15

Owner's "run next session" executed S017 ONLY. Baseline main e183c3a2133b6154700c0cb989318865a1387b80, tree 18cc76572a4e9aee1e73d94a900d7adbda3cf991, ordered parents d985e26f.../975ec8bc...; open PRs [] and rulesets []; branch protection unavailable 403. Pre-entry main run 38768747419/job116538721403 completed SUCCESS all three substantive steps, which MUST NOT be attributed to new S017.

**CP-0064 PROVED_INTERNAL, imported primary SOURCE_STATED Matveev:** New explicit *ratio-free two-run* first-coefficient-crossing theorem: for ALL r,c,d>=1 with 3^r>2^(r+c) and m=r+d >= [16(10^10+10)]^2, the exact positive cylinder O^r E^c O^d E^b, b=bit_length(3^m)-r-c-d>=1, strictly descends at its TRUE first coefficient crossing for EVERY positive lift and has infinitely many composite lifts. No r/d bound; handles r/d arbitrarily large and c varying. Split r<=d via S016 sharp intercept and r>d via actual integer n=2^r u-1 (u odd), with exact endpoint condition delta(2^r u-1)>1+(2/3)^r(2^c-1). Full proof research/S017_PROOFS_AND_OBSTRUCTIONS.md. Extends but does not imply global reachability or Terras CST.

**CP-0065 PROVED_INTERNAL elementary:** exact parity canonical residue n0=-B_W/(3^m) mod2^j and exact finite cutoff qmin for strict first-crossing descent; this is a sound per-cylinder decision, NOT universal total admission. Explicit composites 2^H u-1 force arbitrarily long no-descent O^H prefixes, so every bounded-depth finite certificate collection fails universal coverage. No global well-founded rank or exhaustive reverse-basin rule was discovered. Existing hostile expanding and exceptional families remain.

**FINITE_TEST:** standalone exact script SHA256 3ce5dceb6baae591c07f9a986cc871daafc3bc80db8439b9cfac3f78dc899522 tested 4,425 parameter triples and 17,700 canonical/shifted lifts, all passed, plus intercept extrema and 200 one-run expanding hostile instances. Checked-in new tests mirror computations and require actual hosted run to validate; local script is NOT original repository clone. The enormous Matveev bound is proved symbolically, not tested numerically to that scale.

**Sources:** Original Matveev 2000 English p1219 Cor.2.3 DIRECTLY reinspected; its 53-page proof not independently reproduced. Steiner 1978 seven-page original still NOT located; INDIRECT. Terras 1976 and Rozier/Terracol October2026 explicitly leave CST conjectural; Simons/de Weger 2005 finite cycle scope; Tong Niu May2026 expressly no Collatz/CST resolution. Novelty not established; no human referee or formal Lean/Palomar, publication or preprint.

**OPEN**: all-composite/all-positive Collatz convergence, Terras CST, arbitrary multi-E-block overcritical U when r/d unrestricted, every-positive-number entrance into ANY certified strict-descent cylinder, integer-dependent well-founded rank; all six mod48 hard classes, 71/5041 transducer and forced towers. Do not promote thin asymptotic cylinders to full residues. Detailed proof, input, validation, and registers linked below. New GitHub PR/CI/merge evidence must be appended ONLY after actual observation.

## COMPLETE VERBATIM S018 NEXT-SESSION PROMPT — FUTURE / UNEXECUTED

# S018 — arbitrary overcritical prefixes: a ratio-free first-crossing theorem or exact modular obstruction (FUTURE / UNEXECUTED)

Repository: https://github.com/jfairfaxball-348/collatz-primes

AUTHORITY: The next fresh owner "run next session" instruction authorises EXACTLY S018 immediately. Preparing this prompt in S017 does NOT execute S018 or later sessions.

## Read first and provenance
Read AGENTS.md, docs/SESSION_PROTOCOL.md and EVIDENCE_POLICY.md; authoritative/START_HERE.md, STATE.json and this COMPLETE S018 prompt; all S017 and S016 INPUT/CLOSEOUT/proofs/tests/validation, research CLAIMS/FAILURE/SOURCES and sessions/LEDGER. Inspect live main ref, real git tree and ordered parents, open PRs, rulesets/protection (unavailable != pass), and latest hosted job/individual substantive steps. Preserve other contributors and compare actual commit SHA before updates.

## Single direct theorem target — arbitrary U, no r/d restriction
S017 CP-0064 proves ratio-free first-coefficient-crossing strict descent for O^r E^c O^d E^b as soon as m=r+d exceeds an explicit astronomical bound, with r,c,d varying and 3^r>2^(r+c). S016 CP-0061 covers ANY overcritical U provided r/d<ln2/ln(3/2). The missing intersection is arbitrary multi-E-block overcritical U with r/d unbounded.

ATTACK ONE DIRECT THEOREM: for every overcritical finite parity prefix U with arbitrary number of E blocks, r=#O(U), and d>=1, does U O^d E^b (b=bit_length(3^(r+d))-|U|-d) strictly descend at its FIRST coefficient crossing uniformly for sufficiently large r+d, with no r/d restriction? Derive a defensible all-lifts proof OR produce exact counterparameters (U,d,canonical n0, j, T^j(n0)) falsifying it; distinguish a failed sufficient bound from an actual overshoot. Try a leading-O-run integer parameter and a CRT-derived lower bound on the minimal odd-run carry h, incorporating ALL E blocks. If no uniform all-U proof survives, prove a scoped theorem with explicit structural hypotheses, or a rigorous obstruction.

## Universal-certificate attack (still essential)
Try a computable integer-dependent, genuinely exhaustive admission/exit method, not only sound sparse cylinders. Check every quantifier required to show for all positive n>=2 there is finite j with T^j(n)<n. Independently challenge using 71 exceptional states/5041 edges, 27/43/91/155/251, 393243+524288k expansion, 64k+59->72k+67 same-v2 growth, towers 2^H u-1 and all six 7/15/27/31/39/43 mod48 classes. Refute proposed all-n rank if possible; no finite tests imply convergence. Keep prime/composite route logically equivalent to full Collatz.

## Reproducibility and source discipline
Re-check Matveev (2000) original English §2 Corollary2.3 for log|L| and log(delta), without claiming independent proof of its 53 pages; Steiner (1978) original seven pages remain INDIRECT unless actually obtained. Cross-check Terras 1976, Simons/de Weger 2005, Rozier/Terracol October 2026, Tong Niu May 2026 and any directly relevant stronger prior art. Novelty not established. Create exact independent finite scripts with SHA256 and hostile samples. After GitHub commit independently observe hosted unittest discovery, original S000 exact byte/SHA parity audit, S001 depths10–16 manifest/checker/JSONL consumer, S003 corruption cases, and each substantive job step.

## Stop and writeback
Update numbered claims, failures, sources, STATE, START_HERE, sessions/LEDGER, S018 INPUT/CLOSEOUT, mathematical proof and validation; put COMPLETE S019 FUTURE/UNEXECUTED prompt in authoritative/NEXT_SESSION_PROMPT.md and verbatim in S018 closeout. Prefer dedicated branch, clean PR, observed PR CI success, unchanged main safety inspection, ordinary nonforce merge, real git main tree/ordered parents/readback, independently observed merged-main CI. Never assert global Collatz/composite convergence, Terras CST, originality, Lean, Palomar or publication without evidence.


S018 has NOT been executed during S017.
