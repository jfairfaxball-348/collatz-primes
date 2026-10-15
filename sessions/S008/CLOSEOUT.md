# S008 CLOSEOUT — 2026-10-15

**Research session S008 completed (mathematics and handover; S008 hosted validation and GitHub merge evidence must be checked separately after authoring).** Universal CP-0007 and Terras CST CP-0019 **OPEN / UNPROVED**. Originality UNCHECKED, no Lean, Palomar, preprint or paper.

- **CP-0036 PROVED_INTERNAL:** Exhaustive symbolic 512-slot classification within n≡11 mod16: exactly 441 full cylinders have strict first-crossing descent at j<=13; exactly 71 residue classes r mod8192, partition 26+15+15+15 over x=27,91,155,251 (mod256), have T^j(n)>n for EVERY positive lift and EVERY 1<=j<=13. No depth13 all-class rank; arbitrarily long forced-O subtrees persist by CP-0035.
- **CP-0037 PROVED_INTERNAL + SOURCE_STATED strict corollary:** for ALL a>=3 O^a E O E^b at minimal coefficient crossing, D*t≡-1 modM and D*t>0 forces T^j(n)<=n even for near-resonant exponents. All nonminimum lifts strict; equality at minimum equivalent to nontrivial 2-cycle, ruled out only by existing Simons / Simons–de Weger SOURCE_STATED no-2-cycle literature. S007's 5/4 band no longer needed for weak theorem. Finite a4 example 175->167 at step8.
- **CP-0038 PROVED_INTERNAL affine identity:** general O^a E^c O^d E^b has exact correction K=3^d(2^c-1)-2^(c+d) and strict criterion D*t>M+K at a crossing. K=-1 uniquely at c=d=1; all other c,d yield K>=1, so simple integrality proof cannot extend. Global multi-run CST remains OPEN.
- **ATTACK A gap:** No noncircular renewal inequality or well-founded descent ranking covers infinite 71-residue subtree or other four least-counterexample classes; 2-adic forced-O path does not prove divergence, and 27->206 at j13 falsifies naïve endpoint rank.
- **SOURCE:** 2026 journal Rozier–Terracol explicitly retains CST as open; 2-cycle exclusion cited only as existing source theorem, no new cycle theorem. Original Steiner 1978 article still inaccessible; SOURCE_STATED via Lagarias. No novelty claim.
- **FINITELY VALIDATED:** Local independent Python 4/4 isolated exact tests, finite scopes in validation/S008_LOCAL_PROBES.md. Original clone blocked by GitHub DNS. S007 PR/main plus erratum PR/main hosted runs successfully checked, including all job steps. S008 own PR/main CI needs actual postauthoring verification, not anticipated.
- **ENTRY:** main 5cd92afdd23532b604faf6055be68aea3c3d094a; git tree f490f9e2615710fae17794e889c0f6427b903b72; parents b698d4537d48e46d85ca576ad38596cf4bc8a920 and dcc0e80373b99726f544c7908fafa7283c763c98. S008 detail research/S008_PROOFS_AND_OBSTRUCTIONS.md and tests/test_s008_math.py.

## COMPLETE S009 NEXT SESSION PROMPT (VERBATIM — FUTURE / UNEXECUTED)

# S009 — regenerative exceptional-tree induction and general two-run CST boundary (FUTURE / UNEXECUTED)

Repository: https://github.com/jfairfaxball-348/collatz-primes

**Authority:** The owner's next request to run the current authoritative prompt authorises EXACTLY S009. Do not require separate confirmation; do not run S010 without a new owner instruction. Read AGENTS.md, docs/SESSION_PROTOCOL.md and all authoritative files first.

## Governing goal and evidence
Prove every composite positive integer reaches 1 under shortened Collatz T; equivalent to full Collatz, OPEN. Terras coefficient stopping time conjecture OPEN. No density argument, finite check, local circle exclusion or external unverified theorem settles either. Novelty and publication status NOT established.

## Entry and validation
Pin live main commit, actual git commit TREE and PARENTS; inspect open/recent PRs, stale branches, rulesets/protection and successful/failed hosted runs with actual jobs/steps, especially S008 PR/main and prior S007 evidence. Read S008 proofs, INPUT/CLOSEOUT, tests and validation; CLAIMS, FAILURE_LEDGER, SOURCES, RESEARCH_ROUTES, S001–S007, original S000/S001 suite and CI; preserve concurrent updates. If original checkout unavailable, report that honestly and use GitHub CI as separately observed evidence.

## Attack A — NONCIRCULAR regenerative mechanism
S008 CP-0036 proves an exact finite-versus-infinite dichotomy on 11 mod16: 441/512 residue cylinders STRICTLY descend by depth13; all other 71/512 have coefficient >=1 at EVERY prefix through depth13 and EVERY positive lift remains above start through step13. Symbolic 71-node sets partition 26+15+15+15 mod256; 27 mod256 contains an arbitrarily long forced-O 2-adic path with composite CRT witnesses. Propose a **precise** induction that handles ALL positive descendants from the full exceptional tree, not percentage increments: an adaptive stopping block or rank R(n,state) in a well-founded order with a proved uniform branch-completeness lemma. Carefully test whether any proposed return/renewal state follows a smaller *integer* rather than merely a smaller coefficient or residue. Search for hostile residual cycles and tower nontermination; distinguish a nested 2-adic parity path from a positive divergent orbit. Test 27 mod256, 91 mod96, odd-U inverse y=0,1 mod3, all six least-counterexample r=7,15,27,31,39,43 mod48 and composite witnesses. Pre-register explicit counterexamples to proposed ranks and automatic strategy stop conditions.

## Attack B — multi-run coefficient first crossing beyond c=d=1
S008 CP-0037: for ALL a>=3, with b minimal such that 2^(a+b+2)>3^(a+1), every n=2^a t-1 on O^a E O E^b has weak descent at first crossing by residue congruence D t ≡-1 mod M. All but the least positive t0 lift descend STRICTLY by elementary arithmetic, and strictness at t0 uses existing SOURCE_STATED no-nontrivial-two-cycle theory of Simons (2007)/Simons–de Weger (2005). No new cycle proof. S008 CP-0038: general O^a E^c O^d E^b has K=3^d(2^c-1)-2^(c+d), and K=-1 only when c=d=1; K>=1 otherwise, so the automatic congruence no-overshoot argument fails. Attempt a genuinely proven infinite class with c>1 or d>1, explicit t0, positivity, first-crossing, and noncircular minimum-representative inequality. A first-crossing overshoot would refute open Terras CST, so scrutinise proof rather than advertising finite probes. Compare original journal source Rozier–Terracol 2026, Terras, Steiner 1978 and 2-cycle work; seek Steiner original primary article and disclose availability.

## Computational and closeout obligations
Execute complete repo unittest, S000 exact audit bytes/hash, frozen S001 depth10–16 manifest independent checker, JSONL consumer and S003 corruptions, through local original checkout if available and hosted PR/main CI; observe each run, job and step. Independently check exact lifts, coefficient crossing, near-resonant a=4 n175->167, general multi-run intercept, 7 paradoxical after descent, 27/91 long first descents, 121->91, 15->23->35, 681->511 and mod3 predecessor obstructions. Record exact finite bounds and environment. Produce complete S009 research proof/falsifiers, claims, failures, sources, routes, session INPUT/CLOSEOUT, authoritative STATE/START and complete S010 FUTURE/UNEXECUTED full next prompt in BOTH next prompt and closeout. Prefer safe branch, PR and independently observed hosted CI followed by ordinary merge and remote main/tree/readback. No Lean, Palomar, arXiv, journal, original-priority or global-proof claim absent proof.

---
S008 stops here. S009 is FUTURE/UNEXECUTED.
