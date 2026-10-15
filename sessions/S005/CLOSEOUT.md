# S005 CLOSEOUT — first-crossing nonovershoot, complementary band, six-class grammar, rank kill

Date 2026-10-15. S005 mathematical investigation COMPLETE (the GitHub PR and hosted checking must be observed separately; no future execution implied). Central full Collatz/composite convergence CP-0007 and Terras CST CP-0019 OPEN. Nothing formalised in Lean or verified by Palomar. No novelty or publication priority established.

PROVED_INTERNAL CP-0026: every positive O^a E^b first-crossing cylinder with a>=2 has T^(a+b)(n)<=n, with exact difference (D*t+1)/2^b-1. All lifted t=t0+q2^b, q>=1, strictly descend. Any equality at q=0 implies a genuine periodic orbit; no false no-cycle theorem is assumed.

PROVED_INTERNAL CP-0027: all a>=3 with {a log_2(3/2)}<=4/5 satisfy D>2^b and strict first-crossing descent for ALL t, including infinitely many complementary a with alpha<f<=4/5 beyond S004's alpha-band. Integer-exact finite check a=2..256 found 55 such new complementary exponents; numerical check is separate from the irrational-rotation proof.

PROVED_INTERNAL CP-0028: one exact first-descent word and infinite strict-lift arithmetic progression for EACH r=7,15,27,31,39,43 mod48, with composites in every progression; unbounded state (H,t,3^H*t mod2^b) adds an O-run adaptive exit family for r15/31 (arbitrary H) and r7/39 (H=3). It does NOT cover all six entire residue classes and does NOT universally close r27/43. Source y mod3 reverse obstacles remain.

PROVED_INTERNAL CP-0029: the composites x=96q+15 -> U(x)=144q+23 refute every one-U-step strictly decreasing rank n + state(r,h) additive constants + state(r,h) fixed coefficients times omega(n), by linear size increase vs logarithmic factor penalties. This is a no-go for that explicit rank, not all adaptive/nonlinear/multi-step ranks.

Hostile 7 at later j8, 27 j59 and exact cylinder, 15->23->35 factor5 return, 121->91 omega increase, 12t+3 growth, arbitrary O-runs, y divisible3 without odd U-predecessor and 1+2^k*q descent checked independently (FINITE_TEST), not universality. Local container git DNS failed, so original repo tests/manifest cannot be reported as locally executed; real hosted PR/main workflow steps must be checked. Source priority status and limitations in research/S005_PROOFS_AND_OBSTRUCTIONS.md; exact independent probe output in validation/S005_LOCAL_PROBES.md.

S005 updates claims, failures, sources, routes, session ledger, state, tests and the full handover in one authored change. No post-commit merge/check evidence can be pre-written as already observed. Reconcile remote and GitHub Actions at closeout; any missing run is UNKNOWN, not PASS.

## COMPLETE S006 NEXT SESSION PROMPT (VERBATIM — FUTURE / UNEXECUTED)

# S006 — one-block equality elimination and full adaptive mixed-state coverage (FUTURE / UNEXECUTED)

Repository: https://github.com/jfairfaxball-348/collatz-primes

**Authority:** The owner's next message to run the linked/pasted authoritative next-session prompt directly authorises exactly S006. S006 is NOT executed by creation of this prompt; do not automatically execute S007. Work in this same repository under AGENTS.md and docs/SESSION_PROTOCOL.md.

## Target and evidence gate

Prove every positive composite reaches 1 under shortened Collatz T(n)=n/2 if even and (3n+1)/2 if odd, equivalent to full Collatz (OPEN). Terras' coefficient stopping time conjecture is likewise OPEN. Do not promote finite verifications, density results, 2-adic limiting branches, or one-cycle folklore into universal proofs. All S005 statements are internally elementary; originality UNESTABLISHED.

## Entry and repository governance

Pin FRESH live main SHA/tree; reconcile S005 authored single-parent commit, real PR, ordinary merge, parent/tree matching and separately observed PR and merged-main Actions run/job/step evidence. Inspect open PRs/branches/rulesets/protection (403 means UNKNOWN), AGENTS, README, authoritative START_HERE/STATE/NEXT, docs protocol/evidence, all proof records through S005, claims/failure/source/route ledgers, S005 INPUT/CLOSEOUT, original code/CI and new S005 tests. Abort for conflicting active work. Do not silently rely on S005's unverified postcommit predictions.

## Attack A — exact one-block equality problem

S005 CP-0026 proved on O^a E^b with a>=2 and b=floor(a log_2(3/2))+1: for D=2^(a+b)-3^a>0, t0=(3^a)^(-1) mod2^b, t=t0+q2^b, the exact drop is (D*t+1)/2^b-1>=0. For q>=1 descent is STRICT, for q=0 equality iff D*t0=2^b-1; no first-cross overshoot possible. Equality would be an actual periodic cycle (one monotone O-run and one E-run), NOT a proven impossibility. S005 CP-0027 proved all a with fractional part {a log_2(3/2)} <=4/5 and a>=3 have D>2^b, including infinitely many a outside S004's f<=alpha band. Investigate equality for ALL a>=2 by genuinely new rigorous arguments; search exact one-cycle prior art (Steiner and subsequent corrections), demonstrate precise applicable hypotheses before importing any no-cycle claim. Alternatively certify an explicit infinite new complementary domain and a noncircular exceptional reduction. Use exact modular inverses and exponential Diophantine bounds, not float approximations or assumptions of CST. Do not claim to have solved Collatz by eliminating one-block equality.

## Attack B — six-class grammar beyond sparse cylinders

S005 CP-0028 constructs strict finite-word lift progressions n=r+3*2^j*q for EACH r=7,15,27,31,39,43 mod48, and an adaptive O-run exit rule for a=h=v2(n+1); for r=27/43 the latter simple b(h) rule is incompatible with t mod4, so only thin progressions are established. Prove a quantified substantially larger symbolic region for BOTH r=27 and r=43, or a genuine rank/grammar covering all six full residue classes. Separate reverse sources y=0 mod3 (no odd U parents) and y=1 mod3 (only larger), offsets >=0, and the unbounded high-h branches r15/31. Any no-go must give an infinite structural family countering a precisely stated proposal. Do not equate coverage of some infinite subset with universal convergence.

## Attack C — genuinely nonadditive adaptive rank

S005 CP-0029 refutes one-U step monotonicity of every fixed R(n)=n+A_(n mod48,h)+B_(n mod48,h)*omega(n), h=v2(n+1), even with arbitrary finite real state penalties: x=96q+15 -> U(x)=144q+23 has (r,h)=(15,4)->(23,3) and growth 48q+8 dominating O(log q) factor penalties. Seek a *new explicit* nonlinear/block-based well-founded rank with genuine strict progress on a proved infinite domain, or refute it via quantified families. Adversaries: 15+20t with factor5 re-entry, 121->91 with omega increase, 27 and its exact step59 cylinder, 12t+3 growth, n=2^H*t-1 O-run growth, y divisible3 with no U inverse, and 7's later j8 paradoxical prefix.

## Reproduction, literature and closure

Run original Python unittest, S000 audit, k10..16 producer with bytewise comparison to frozen S001_manifest.json, independent checker, canonical JSONL consumer and S003 corruption checks; report exact observed commands, SHA256, hosted job IDs and steps. Local GitHub cloning unavailable in prior environment; if still unavailable, explicitly separate independent local arithmetic from HOSTED repository tests. Recheck Terras 1976 original/metadata, Rozier–Terracol 2026 Discrete Mathematics 349:115167 / arXiv:2502.00948, Tao 2022 logarithmic almost-all, Bařina 2025 finite 2^71, Angeltveit arXiv:2602.10466 finite algorithms, Hercher 2026 Theorem 21 corrigendum. Evaluate one-cycle priority independently; no novelty claim without a real audit.

Complete S006 alone: rigorous research note, adversarial tests, claim and failure registers, sources/routes, sessions/S006 INPUT and CLOSEOUT, authoritative state, session ledger, and COMPLETE S007 FUTURE/UNEXECUTED next prompt both in authoritative/NEXT_SESSION_PROMPT.md and verbatim in S006 closeout. Prefer isolated one-parent commit -> real PR -> observe hosted checks -> ordinary merge -> independent live merged-main SHA/tree/parents/CI/readback. Report blocked actions precisely; never invent mathematical, GitHub, Lean, Palomar, or independent verification.

---
S005 stops here. S006 is FUTURE / UNEXECUTED.
