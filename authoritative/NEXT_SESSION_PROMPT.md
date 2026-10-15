# S005 — resolve uncovered O-run first crossings and adaptive mixed-state ranks (FUTURE / UNEXECUTED)

Repository: https://github.com/jfairfaxball-348/collatz-primes

**Execution authority:** The owner's next request to run the current linked or pasted prompt immediately authorises S005, and ONLY S005. This is a future handover, not evidence of execution. Do not run S006 without a later owner instruction.

## Non-negotiable target and status

Prove every positive composite integer reaches 1 under shortened Collatz T(n)=n/2 (even), T(n)=(3n+1)/2 (odd); by CP-0001 this is equivalent to full Collatz and remains OPEN. Neither Terras' Coefficient Stopping Time conjecture (also OPEN) nor eventual exceptional-tower exit may be assumed. Avoid numerical universality, 2-adic compactness, finite-modulus proofs or unjustified novelty claims.

## Entry and safety gate

Pin fresh live main commit and tree. Reconcile S004 one-parent authored commit, PR and ordinary two-parent merge with matching tree; inspect open PRs, branches, repository rulesets/protection, PR and merged-main Actions runs and individual steps. A 403 branch-protection read is UNKNOWN. Read AGENTS.md, README, authoritative/START_HERE.md, STATE.json and this entire prompt, docs/SESSION_PROTOCOL.md and EVIDENCE_POLICY.md, research/CLAIMS.md, FAILURE_LEDGER.md, SOURCES.md, RESEARCH_ROUTES.md, research/S001 through S004 proofs, sessions/S004/INPUT.md and CLOSEOUT.md, validation/S001_manifest.json, validation/S004_LOCAL_PROBES.md, all tests, producer, independent checker and canonical JSONL consumer. Abort for conflicting active owner work.

## Attack A — exact first-crossing complement

S004 CP-0023 proved a genuinely quantified but elementary restriction: with alpha=log_2(3/2), b(a)=floor(a alpha)+1, and first-crossing parity word O^a E^b, the prefix consists exactly of n=2^a t-1 with 3^a t congruent 1 mod2^b. Its first coefficient crossing is j=a+b, and it descends there iff (2^(a+b)-3^a)t>2^b-1. If 4*3^a <= 3*2^(a+b), this holds for EVERY positive member for a>=2; at least one of any adjacent pair of a>=2 meets that sufficient condition. Novelty NOT ESTABLISHED.

Attack the complementary a, not merely reprove this sufficient condition. Decide whether EVERY positive member with parity O^a E^b (a>=2) descends at the first crossing, or construct an explicit exact exception. Reduce the question to the least modular inverse t0 = (3^a)^(-1) mod2^b in [1,2^b] and inequality D*t0>2^b-1. Beware deep Diophantine approximation or implicit CST assumptions. Provide a rigorous infinite subfamily with no numeric dependence if full result is unavailable, or a clear counterexample to an overstrong statement. Test n=7 at the LATER j=8 paradoxical window, n=27 and its j=59 cylinder, O prefixes, and 1+2^k*q.

## Attack B — positive adaptive-rank mechanism

S004 CP-0024 excludes EVERY fixed modulus M (even 48) if its residue states have finite class-dependent uniform first-descent horizons. For M=48 the hypothetical least-counterexample classes 15 and 31 can have arbitrary valuation h=v2(n+1) and strict growth through h+1; classes 7/39 have h=3, 27/43 have h=2. A negative theorem on fixed horizons is NOT a theorem forbidding growing-depth counters.

Construct one explicit adaptive state/rank or inverse/forward grammar that actually handles all six residues (7,15,27,31,39,43 mod48), with explicit source difficulties y=0,1 mod3 and nonnegative affine offsets. Prove a noncircular descent/coverage lemma for a delimited class, or produce an infinite structural counterfamily to the proposed mechanism. State its domain, transition, quantifiers, obstruction, and whether it genuinely improves known coverage. Do not infer universal positive exit from the 2-adic branch -1.

## Attack C — valuation/factor rank, not factor erasure alone

S004 CP-0025: for any K>=3 choose y congruent -1 mod2^K and 7 mod9, set x=(4y-1)/3. Then x is composite and v2(x+1)=1 but U(x)=y has v2(y+1)>=K; example 681->511. Hence v2(n+1) is not a decreasing U-rank. The m-step affine formula CP-0021 remains exact, but the offset F_m does not produce a sign or prime-count monotonicity.

Propose and falsify at least one specific adaptive combined rank (numeric size, valuations, factor returns, residue states), or prove a delimited actual descent theorem. Mandatory obstacles: x=15+20t (factor5 returns), x=121, x=27, x=12t+3, long 2^k t-1 prefixes, and U-predecessor-free multiples of 3. Check all formulas with an independent arithmetic implementation.

## Reproduction / sources / closure

Run all original unit tests, S000 audit, k10..16 manifest recreation and bytewise comparison to frozen S001 manifest, independent certificate checker, canonical JSONL consumer and corruption tests; preserve actual commands, SHA256 and hosted job IDs/status/steps. If local checkout unavailable, say so explicitly and let hosted CI provide observed repository execution. Verify current primary literature including Terras 1976; Rozier–Terracol, Discrete Mathematics 349 (2026) 115167, arXiv:2502.00948; Tao almost-all; Barina finite 2^71; Angeltveit finite verification; and Hercher June 2026 corrigendum explicitly correcting Theorem 21. Treat elementary work as non-novel unless a genuine priority audit shows otherwise.

Complete exactly S005 with mathematical proofs, hostile cases, claims/failure/source/routes, sessions/S005 INPUT and CLOSEOUT, ledger, authoritative state and a COMPLETE S006 FUTURE/UNEXECUTED prompt (both next prompt and verbatim closeout). Prefer one isolated one-parent commit, real PR, observed PR checks, ordinary merge, independent live commit-tree-parent and merged-main check/readback verification. Any blocked operation must be reported exactly; no invented proof, verification, novelty, Lean or Palomar.
