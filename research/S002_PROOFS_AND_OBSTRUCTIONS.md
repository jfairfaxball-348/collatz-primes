# S002 — Exact exceptional lifts, first-descent cylinder, prime-return arithmetic and automaton limits

**15 October 2026.** All statements use shortened positive T and accelerated odd U(x)=(3x+1)/2^v2(3x+1). This is internally proved elementary mathematics and explicitly finite evidence, **NOT** an original claim or a universal proof of Collatz. Global CP-0007 remains OPEN.

## CP-0014: exact two-child exceptional transfer (PROVED_INTERNAL)

For k>=2 and odd 1<=r<2^k, define F_j(r)=(3^{a_j}r+b_j)/2^j for 1<=j<=k from r's T parity prefix. Let d_j=2^j-3^{a_j}, and define C_k(s) to mean some 1<=j<=k has d_j*s>b_j, using the parity prefix of the positive residue s. This exactly means **every** n=s+q*2^k, q>=0, has strict descent at the common time j. The proof is the affine formula and positivity of b_j: the inequality for all q is possible iff d_j>0 and holds at the smallest representative. In particular d_j*s>b_j itself implies d_j>0. The r=1 residue is BASE_1 (n=1 excluded).

The two odd residues above r at level k+1 are s_0=r and s_1=r+2^k. For every j<=k their parity words, a_j and b_j coincide with r, because adding 2^k changes the j-th state by 3^{a_j}*2^{k-j}, even for j<k. Therefore their **exact** early certification criterion is: there is some j<=k with d_j*s_e>b_j. Do not conflate failure at the parent representative with failure at a high child representative: d_j>0 could permit late threshold crossing even when r was not certified.

At j=k, T^k(s_1)=T^k(r)+3^{a_k}, so the two next-input parities are opposite. For each child compute epsilon = T^k(s_e) mod2. The next affine coefficients are (a',b')=(a_k,b_k) if epsilon=0, or (a_k+1,3*b_k+2^k) if epsilon=1. The exact novel (k+1)-step strict-class criterion is (2^{k+1}-3^{a'})*s_e>b'. Hence E_(k+1) consists exactly of the positive non-base odd children of E_k which fail ALL the early inequalities and the new inequality; this is a **computable exact transfer**, not a proved terminating well-founded recurrence.

Further, if no early j<=k descends for an individual child s_e and T^k(s_e) is odd, then T^{k+1}(s_e)=(3*T^k(s_e)+1)/2 > T^k(s_e)>=s_e. Thus a newly descending (k+1)-st step after no earlier descent must have even T^k(s_e). This implication applies to the chosen representative and separately to every member when the no-early-descent hypothesis is known for that member. It does NOT close the exceptional tree. Countermodel to fixed-depth closure: for any k, all sufficiently large composite 2^k*t-1 have no descent in the first k steps (CP-0012); the nested 2-adic -1 path does not represent a positive integer.

## CP-0015: exact first descent 59 for an infinite difficult family (PROVED_INTERNAL by finite parity-word identity + symbolic lifting)

For **every integer q>=0**, let N_q=27+2^59*q. Then the **first** j>=1 with T^j(N_q)<N_q is j=59. In particular, infinitely many odd composite integers (q a multiple of3; N_q>=27) have exactly this first-descending-time. No assertion is made for all integers 27+2^16*q.

Certificate: the first 59 T-input parity letters of 27 are

    OOEOOOOOEOEOOEOOOEOOOOEOEEOOOEOOEOOOOOOEEOOOOEEEOEOEOEEEOEE

which has length59, 37 O's; direct application of T to 27 yields T^59(27)=23. For each 1<=j<=58 its odd count a_j satisfies 3^{a_j}>=2^j (exact integer inequalities, all verified by the deterministic test in tests/test_s002_structure.py). Therefore, for all q>=0 and j<=58, T^j(N_q)=(3^{a_j}*N_q+b_j)/2^j >= N_q, in fact > because b_j>0 (the word begins O). The word persists across the whole residue modulo 2^59 by parity lifting. At j=59, 3^37=450283905890997363 < 2^59=576460752303423488 and the affine lift gives **exactly**

    T^59(N_q)=23+450283905890997363*q
                 <27+576460752303423488*q=N_q.

This proves an infinite family resolves to a strictly smaller input at a known time, not that the whole infinite 27 mod2^16 class descends. If that smaller input is itself known to converge, the family converges by ordinary induction; here no independent universal conclusion about arbitrary q is imported. The statement demonstrates a valid symbolic finite-to-infinite transfer but not the missing coverage of all E_k.

## CP-0016: two-U-step exact prime re-entry (PROVED_INTERNAL)

For every positive odd x, let a=v2(3x+1)>=1, y=U(x), b=v2(3y+1)>=1 and z=U(y). Since 2^a*y=3x+1 and 2^b*z=3y+1,

    2^(a+b)*z=9*x+3+2^a.

Because x is odd and 2^(a+b) is invertible modulo every divisor of x,

    **gcd(x,U(U(x))) = gcd(x, 2^a+3).**

Consequently each odd prime p|x reappears after precisely two U transitions iff p|(2^a+3), despite p not dividing U(x). Indeed for x=20t+15 (t>=0), 3x+1=2(30t+23) with the bracket odd, hence a=1, and gcd(x,U^2(x))=gcd(x,5)=5 for **all** t. The sequence 15 -> 23 -> 35 returns factor5. Hostile cases: x=121 gives a=2, 121 ->91 ->137 and gcd(121,137)=gcd(121,7)=1; x=27 gives a=1, 27->41->31, gcd(27,31)=gcd(27,5)=1. For composites 12t+3 the first U step increases (S001), so neither re-entry nor erasure proves numeric decrease. The exact identity is a useful multi-step factor constraint, but no well-founded factor rank has been established.

## CP-0017: permanent nonappearance of factor 3 after one U step (PROVED_INTERNAL)

For every odd x>0 and a=v2(3x+1), 2^a*U(x)=3x+1 congruent1 (mod3), so U(x) congruent 2^(-a)=(-1)^a (mod3), never 0. The same is true of **every** U^j(x) with j>=1. Thus for any odd x divisible by3, factor3 is eliminated at the first accelerated step and never reappears. Equivalently an odd y divisible by3 has no odd U predecessor, fully consistent with CP-0010. This is NOT a proof such sources lie outside the reverse basin of1; 3->5->1 is a counterexample to that inference.

The least hypothetical nonconvergent positive integer must still lie in six residue classes 7,15,27,31,39,43 modulo48. Values congruent 15,27,39 mod48 are divisible3 (no odd U predecessor); values 7,31,43 mod48 are 1 mod3 (all their odd U predecessors are larger). This class-level inverse obstruction, by itself, excludes NONE of these six classes as least counterexamples. It merely demonstrates why the 5 mod6 smaller-parent argument cannot be transferred. The full quantified positivity/descent argument remains absent.

## CP-0018: no fixed 2-adic residue predicts the next U output modulo3 (PROVED_INTERNAL)

For **every** k>=1 choose any even a>max(k,2), and any odd b>max(k,2). Put x_a=(2^a-1)/3 and x_b=(5*2^b-1)/3. They are positive odd >1 because 2^a*1 and 2^b*5 are 1 mod3 for even/odd exponents respectively, and the numerators are odd. Exact valuation gives U(x_a)=1 and U(x_b)=5, hence different residue classes modulo3. Nevertheless 3*x_a+1 and 3*x_b+1 are both divisible by 2^k, so as 3 is invertible modulo 2^k,

    x_a ≡ x_b ≡ -3^(-1)  (mod 2^k).

Thus for no fixed k can U(x) mod3 be a function of x mod2^k on ALL positive odd x. This kills a fixed-window **2-adic-only** automaton proposal, not automata with valuation counters or 3-adic state, and not Collatz convergence. Arbitrarily long valuation prefixes near the 2-adic root -1/3 are essential to the obstruction.

## Candidate rules and hostile status

- UNPROVED: E_k's lack of strict representative descent is equivalent to all first-k parity-prefix slopes 3^{a_j}>=2^j for every r>1. An exact *finite observation* for the depth16 certificate data must not be promoted to a theorem. S003 attacks it.
- UNPROVED: every positive start eventually leaves E_k. This is equivalent to CP-0009's global strict descent and would solve Collatz; no rank/coverage transfer has been obtained.
- REFUTED fixed k-only prediction of U(x) mod3 by CP-0018's two positive witnesses.
- INSUFFICIENT: interpreting a source y divisible3 as an unreachable/nonconvergent vertex; 3->5->1 directly refutes it.
- INSUFFICIENT: using prime-erasure as a monotone factor support potential; factor5 returns after two steps for all 20t+15.
- INSUFFICIENT: extrapolating the certified 27+2^59*q subfamily to the full 27+2^16*q residue.

## Source-to-lemma / novelty dependency audit (15 October 2026)

All CP-0014 through CP-0018 proofs above use elementary exact algebra and symbolic parity lifting only, no imported cycle lower bound. Primary literature checked: Lagarias overview arXiv:2111.02635 (historical survey); Tao *Forum Math Pi* 10 e12 (2022), logarithmic-density almost-bounded theorem, NOT pointwise convergence; Bařina *J. Supercomputing* 81:810 (2025), reported finite 2^71 verification, NOT this repo's independent certification; Angeltveit arXiv:2602.10466 (2026), finite verification complexity, NOT universal; Simons–de Weger *Acta Arith.* 117 (2005), m-cycle bounds; Hercher *J. Integer Sequences* 26 (2023), m counting local minima, and corrigendum dated June 14 2026 (linked on publisher page). Neither a cycle lower bound nor an empirical frontier implies absence of divergent orbits. Corrigendum existence and scope checked; no technical corrected claim imported. Source scan is not a novelty certificate; exact earlier appearances of these elementary identities have not been excluded. No Lean, Palomar, arXiv or original-priority claim.

## Evidence discipline / computation

Finite first-descent-59 certificate was checked by direct integer Python arithmetic in this session; tests/test_s002_structure.py encodes the same exact word and all 58 pre-descent integer inequalities for hosted CI. The S001 generator and independent checker are retained; tools/consume_residue_records.py additionally consumes the **actual** generated canonical JSONL and validates every row, ordering, coefficient, parity, first certification and per-depth SHA256. This avoids checker-only self-regeneration. Actual hosted execution and SHA256 must be cited from workflow observations, NOT assumed at authoring. S001's established k16 count 30653 STRICT + 1 BASE_1 + 2114 OPEN is unchanged until the hosted comparison says otherwise. No partition labels from retrospective exploratory data are advertised as frozen holdouts.
