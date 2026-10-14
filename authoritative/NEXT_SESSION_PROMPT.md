# S001 — Prime/composite factor bridge and descent certification (FUTURE / UNEXECUTED)

Repository: https://github.com/jfairfaxball-348/collatz-primes

This prompt is a queued future session. When the owner supplies this text or URL with an instruction to run it, that instruction alone authorises **immediate execution of exactly S001**. Do not demand separate owner confirmation, and do not execute S002 within S001.

## Governing problem

Prove for ALL composite positive integers n that some shortened Collatz iterate reaches 1; equivalently solve the complete Collatz conjecture by CP-0001. If the problem is not solved in S001, obtain a genuinely useful rigorous nontrivial lemma or a precisely labelled obstruction, and preserve the unsolved status. Do not represent finite exhaustive checks or density estimates as the theorem.

## Read first / live verification

Independently fetch LIVE main and pin actual head and current tree, PR and merge history, outstanding branches/PRs, statuses and hosted workflows accessible. Check if S000 scaffold merged; reconcile actual remote files and CI rather than trusting predicted GitHub refs. Read AGENTS.md, authoritative/STATE.json, authoritative/START_HERE.md, docs/SESSION_PROTOCOL.md, docs/EVIDENCE_POLICY.md, research/S000_FOUNDATIONS.md, research/RESEARCH_ROUTES.md, research/SOURCES.md, research/CLAIMS.md, research/FAILURE_LEDGER.md, sessions/S000/CLOSEOUT.md and validation/S000_audit.json. Claim CI PASS only for actual completed checks; missing checks = NOT OBSERVED. Note CP-0001 equivalence and the mod16 necessary least-counterexample classes before commencing.

## Central proof-first research task

Investigate whether the **composite factorization** n=ab, both a,b>1, can yield a rigorous, genuinely noncircular finite-descent theorem:

(i) Identify candidates for a well-founded potential involving odd prime factors, valuations v2(3n+1), factor chains, or the accelerated odd map. Show exact hypotheses and prove algebraic sublemmas.

(ii) Distinguish a prime-to-composite transition, a composite-to-composite transition, and mere gcd(n,T(n))=1. Test false multiplicativity claims on explicit hostile examples. Do not assume convergence of proper factors implies convergence of a product.

(iii) In parallel, derive affine parity certificates for 2-adic residue classes to depths 10–16, proving when a full infinite class has strict descent and cataloguing **uncovered** classes. Preserve explicit thresholds and explain which quantifiers remain missing; do not confuse coverage of most classes with all.

(iv) Seek a meaningful bridge joining arithmetic factorization with parity-residue classes, ideally a finite symbolic or reverse-graph induction with a provable global covering property. Attempt at least two approaches and record falsification of seductive conjectures. A finite table alone does not establish a universal property.

(v) Compare literature primary sources (Lagarias, Tao, Barina, and focused prime-related Collatz literature newly verified) for prior art. Date every new fact and separate source claims from original arguments. Attempt to identify an actual novel question or lemma rather than advertising elementary observations as original.

## Computation / proof gate

Use exact Python or other reproducible integer arithmetic; version every changed script. Run unit tests and independent small counterchecks, including boundary residues and prime/composite classifications. The 10000-start S000 audit is a finite baseline, NOT an externally certified frontier. Investigate whether every claimed universal reduction actually preserves ALL composite starts and avoids circular dependence. If a substantial general lemma survives, draft Lean 4 formalisation scope only after its mathematical proof is complete; never claim Lean or Palomar passed without actual tool evidence.

## Closeout / publication requirements

One unique S001 session: archive input/assumptions, produce sustained substantive mathematics, precise numbered claims and hostile failure log, reproducible finite evidence, validation and review, session S001 closeout, updated authoritative START_HERE/STATE/CLAIMS/SOURCES/FAILURE_LEDGER/LEDGER, and the FULL S002 prompt at authoritative/NEXT_SESSION_PROMPT.md, clearly FUTURE/UNEXECUTED. Do not claim S002 executed.

Prefer a dedicated branch with one coherent single-parent commit, PR and ordinary nonforce merge if allowed; independently fetch actual main SHA/tree after merging. If GitHub permissions or verification blocks, report exact issue rather than claiming success. In the user-facing closeout provide links to the merged work and the complete next-session prompt, along with rigorous proof-versus-experiment boundaries.

**Priority:** Make a serious attempt at the composite-to-descent bridge, not a cosmetic session cycle. The full theorem is the ultimate target; honestly state any gap that remains.
