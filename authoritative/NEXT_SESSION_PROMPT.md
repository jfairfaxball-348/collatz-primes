# S002 — Exceptional-tower transfer, reverse-parent gap and prime-transition barrier (FUTURE / UNEXECUTED)

Repository: https://github.com/jfairfaxball-348/collatz-primes

**Execution authority:** This is the COMPLETE handover for S002, not evidence of S002 execution. A fresh owner instruction to “run next session”, a pasted prompt or a link to this file authorises **exactly S002 immediately** without a second confirmation; it does not authorise S003. Do not execute S003 in S002.

## Governing mathematical objective

Prove the original target that every composite positive integer eventually reaches 1 under `T(n)=n/2` for even n, `(3n+1)/2` for odd n. CP-0001 shows this is full Collatz, **OPEN**. Focus on noncircular global strict descent or a genuinely complete reverse basin; do not substitute bounded computations, logarithmic-density results, a partial cycle bound, 94% residue certificates or a 2-adic infinite branch for proof.

## Mandatory live read / governance

Pin fresh **live** main SHA + tree, verify S001 authored single-parent commit, PR, actual ordinary merge parents/tree, hosted PR and main checks separately, open PRs/branches and available rulesets. Inspect branch protection; report access errors as UNKNOWN. No concurrent-work collision. Read `AGENTS.md`, `README.md`, `authoritative/START_HERE.md`, `authoritative/STATE.json`, this full prompt, `docs/SESSION_PROTOCOL.md`, `docs/EVIDENCE_POLICY.md`, `research/S000_FOUNDATIONS.md`, `research/S001_PROOFS_AND_OBSTRUCTIONS.md`, `research/REPORT_INTEGRATION.md`, `research/PROGRAMME_PLAN.md`, `research/CLAIMS.md`, `research/FAILURE_LEDGER.md`, `research/SOURCES.md`, `sessions/S001/CLOSEOUT.md`, `validation/S001_manifest.json`, and producer/checker/tests. Archive entry in `sessions/S002/INPUT.md`.

Re-run `python -m unittest discover -s tests -v`, `python tools/residue_certificates.py --output /tmp/S002_manifest.json --records /tmp/S002_records.jsonl`, `python tools/check_residue_certificates.py /tmp/S002_manifest.json`, byte-compare to `validation/S001_manifest.json`, and run S000 audit. Record exact environment and SHA256; do not claim actions succeeded without output. Preserve exact convention: positive odd representative r in [1,2^k), first j<=k shortened steps; 30653 strict + 1 base-only + 2114 uncovered at k16. Inspect whether the S001 checker independence can be strengthened further by certificate consumption in addition to independent regeneration.

## Proof attack A — exceptional-class transfer, not more coverage percentages

A1. Model the exceptional `E_k` tower and prove an **exact per-child lift criterion** in terms of `(k,r,j,a,b,parity_word)`; account for inherited descent at a larger representative and novel descent at time k+1. Prove or refute a candidate *rank or finite-state transfer law* that implies every fixed positive n eventually exits the tower. Distinguish 2-adic compactness from N+; nested classes around -1 are an infinite 2-adic branch without a positive start. Do not assert all exceptional branches are -1 unless proved.

A2. Try a mathematically substantive universal theorem rather than an enlarged search: derive an explicit symbolic bound on the first descent time of a nontrivial infinite family of uncovered representatives (`27+2^k q`, `2^k q-1`, or another preregistered hostile class). The bound must quantify over **all q** and specify whether it is relative to initial n and whether a new parity word depends on q. Prefer a genuine infinite-family proof or a counterfamily to a proposed uniform bound. Check small n=27 first descending at T-step 59 is **finite only**.

A3. Propose a transfer from uncovered class to a previously certified smaller class with an independently justified well-founded rank. Try a falsifying residue or 2-adic family before accepting it. Explicitly identify the unresolved quantified case if no proof exists.

## Proof attack B — odd reverse graph and first-counterexample sieve

B1. Starting from S001 CP-0010, exploit rigorously that a least nonconvergent positive number cannot be 5 mod6, and S000 gives its mod16 restrictions. Check 6 remaining necessary classes `7,15,27,31,39,43 mod48`, and attempt a NEW modular/dynamical exclusion that does not merely assume a smaller predecessor or convergence. Prove it on an infinite family with complete quantifiers, or give exact adversarial counterfamilies.

B2. Attempt a non-tautological compressed reverse-basin grammar: define membership with finite rules + a provable coverage or rank property. Show soundness separately from completeness. `G={convergent starts}` is an exact tautology, not a complete result. Inspect reverse steps at y divisible by3 and y≡1 mod3, where the smaller-U-predecessor route fails.

B3. Investigate whether the no-small-predecessor mod3 categories and `E_k` parity tower have an exact finite automaton or mixed 2-adic/3-adic invariant. For every candidate invariant list the hypothesis needed to cover **all** remaining positive odd y, and falsify it on 27 or explicit -1-prefix composites when relevant. A new theorem must avoid an unproved global reachability assumption.

## Proof attack C — factor transition with hostile composite cases

C1. Beyond the elementary `gcd(n,U(n))=1`, identify a nontrivial prime-valuation/transition invariant across two or more U-steps, and test against `121->91`, `27->41`, and all odd composites `12t+3` (t>=1) with one-step increase. Do not infer a numeric or factor-count rank from mere erasure.

C2. If exploring primes vs composites, remember that `T(2p)=p` makes the composite target equivalent to the full conjecture, and odd modulo powers of two contain both primes and composites. State a precise quantified theorem and attempt proof or an infinite counterfamily.

## Prior art, formal trust and result classification

Cross-check primary Lagarias, Tao (2022), Bařina (2025), Angeltveit (2026), Simons–de Weger, and Hercher INCLUDING the corrigendum before using technical cycle bounds. Check current sibling repository statements only as needed. No unproven orientation bridge, Mignotte-height assumption, finite frontier, or modified leading-digit map may be imported as proved universal Collatz. Make a separate source-to-lemma dependency/novelty assessment. Formalise only proof-complete propositions if useful and actually verified; report exact Lean axiom lines if promoting.

Freeze any PRIMES-style discovery and holdout partitions **before** examining data; no posthoc validation labels. Reproduce finite tests and put hostile failures in the ledger. Keep THEOREM/PROVED_INTERNAL, FINITE_CERTIFICATE, SOURCE_STATED, EXPERIMENT, REFUTED and OPEN distinct.

## Required S002 closeout and handover

Deliver `sessions/S002/INPUT.md`, deep proof and obstruction record, exact computational manifest/test updates if changed, failure log, `sessions/S002/CLOSEOUT.md`, revised `research/{CLAIMS,FAILURE_LEDGER,SOURCES,RESEARCH_ROUTES}.md` as necessary, `sessions/LEDGER.md`, `authoritative/{STATE.json,START_HERE.md,NEXT_SESSION_PROMPT.md}`. Include **COMPLETE S003 prompt** in next-session file and verbatim inside closeout, marked FUTURE / UNEXECUTED. One S002 session only.

Prefer one isolated branch, one coherent single-parent authored commit, real ordinary PR, observe hosted checks before ordinary non-force merge if permitted, verify new main SHA/tree/parents and file readback. If any step is blocked, state precisely what exists and what was not observed, never fabricate checks. Return GitHub PR, commit, merge and key file links plus the full S003 prompt. The central theorem remains OPEN unless a complete genuinely universal noncircular proof withstands hostile analysis.
