# S011 — unbounded exceptional-to-descent cylinders and infinite genuine D<K first crossings

**15 October 2026.** LIVE entry main commit `5017318dc43f950fa63b4f704fa77c385c7aec87`, ACTUAL git commit tree `097d89ecce99c75cddb8789454a1184eede194a6`, parents `7dc3cce70243892c80209785bb9f1e87d0a67872` and `1ba2f7ef63b5f468bc899a231a582a8aba0120d2`. Previous PRs #14/#15 merged, no open PR in inspected first page; rulesets [], protection endpoint 403 **NOT OBSERVED**. Existing main hosted run 38728310174 job 116399522422 SUCCESS with all three substantive steps: unittest; byte-exact S000 audit; S001 manifest/independent checker/JSONL consumer. That predates this S011 commit. Original container clone DNS failed, no local full-suite claim. Global Collatz/composite convergence and Terras coefficient stopping time (CST) remain OPEN.

Notation shortened `T(n) = n/2` when even, `(3n+1)/2` when odd; parity input letters O/E. For an actual word of length j with A odd inputs, `2^j T^j(n)=3^A n+B`, where B>=0. Every finite parity word defines exactly one starting residue modulo `2^j`. Prefixes with `3^A>=2^j` cannot strictly descend below their positive start. FIRST coefficient crossing is the earliest j for which `3^A<2^j`.

## CP-0044 — PROVED_INTERNAL: general two-run 2-adic obstruction and sufficient strict minimum-lift criterion

Let `a,c,d,b>=1` be an ADMISSIBLE word `O^a E^c O^d E^b`; set `j=a+c+d+b`, `P=3^(a+d)`, `K=3^d(2^c-1)-2^(c+d)`, `M=2^(c+d+b)`, `D=2^j-P`. Assume genuine FIRST coefficient crossing at j (so D>0). The unique least positive admissible `t0 in [1,M-1]` satisfies `P*t0+K=0 mod M`; put `n_q=2^a(t0+Mq)-1`, q>=0. Then:

(i) `2^(c+d)` divides `3^a*t0+(2^c-1)`. In particular `3^a*t0+(2^c-1)>=2^(c+d)`, and
`t0 >= [2^(c+d)-(2^c-1)]/3^a` (as rational lower bound).

(ii) Exact integer drop at j is
`n_q-T^j(n_q)=[D*t0-(M+K)]/M+D*q`. Thus **necessary and sufficient** for least-lift strict descent is `D*t0>M+K`, equality gives a cycle (not assumed impossible here), and `D*t0<M+K` gives a true first-crossing overshoot (would refute CST and requires extraordinary independent verification).

(iii) A **pure parameter sufficient test, valid even for D<=K**, is
`D*[2^(c+d)-(2^c-1)] > 3^a*(M+K)`.
It implies `D*t0>M+K` and hence strict descent at first crossing for **ALL** q>=0. If the bracket is nonpositive, the test simply fails to apply; no negative-lower-bound conclusion is made.

Proof: Rewrite `P*t0+K = 3^d[3^a*t0+(2^c-1)]-2^(c+d)`. It is divisible by M, hence by `2^(c+d)`, so as 3^d odd the bracket is divisible by `2^(c+d)`; it is strictly positive. The fixed-word exact affine iterate identity gives (ii). Apply (i) to the strict inequality in (iii). No coefficient-crossing universal claim is hidden in this algebra; first-crossing is an explicit hypothesis.

## CP-0045 — PROVED_INTERNAL: arbitrarily deep exceptional positive-integer strict FIRST-crossing certificates

Let `p=OOEOOOOOEOEOO`, exactly the 13 parity INPUTS of start 27; `#O(p)=10`, `T^13(27)=206`. Fix **ANY integer N>=1** and let `W_N=p^N E^(4N)`; `J=17N`, `A=10N`, `3^A/2^J=(59049/131072)^N<1`. The bijective parity-prefix coding provides a unique `R_N in [0,2^J-1]` whose first J inputs have word W_N. Every positive n in the arithmetic progression `R_N+2^J q` has this entire word.

At EACH checkpoint `13i` for `0<=i<N`, the following 13 parity inputs equal p, hence `T^(13i)(n)≡27 mod8192`. By S008 CP-0036 the next 13 iterates remain greater than that block's starting integer and their local coefficients remain >1. Inductively for EVERY `1<=h<=13N`, `T^h(n)>n` and its GLOBAL prefix coefficient is >1. Thus no first coefficient crossing through step13N. Since final coefficient <1, its first crossing `h_N` exists in `13N<h_N<=17N`.

Put `G_N=2^J-3^(A_{h_N})2^(J-h_N)>0`, where `A_h` counts Os in the first h letters. The EXACT parity cylinder identity gives
`n-T^(h_N)(n)=R_N-T^(h_N)(R_N)+G_N*q`.
Consequently every integer `q> [T^(h_N)(R_N)-R_N]/G_N`, with n positive, has a **strict descent at its TRUE FIRST coefficient crossing**, after >13N non-descending steps. This is an explicit computable finite threshold, not an appeal to density or compactness. The rank `RANK(n)=n` strictly decreases on these verified certificates, so strong induction works on any n whose membership in one of the certified cylinders has actually been proven; **NO COVERAGE of all n** is claimed.

Since the first bit of p is odd and p forces n≡27 (mod8192), all starts are n≡11 (mod16). For any fixed N and all sufficiently large q, CRT modulo3 selects n≡27 (mod48), automatically composite (multiple of3); alternatively CRT modulo15 selects n≡43 (mod48) and n≡0 (mod5), again composite. `gcd(2^J,15)=1` guarantees solutions and arbitrarily many q. Thus FOR EVERY depth N there are infinitely many positive composites in BOTH hard classes 27 and43 mod48 which remain exceptional through 13N steps and then strictly descend at their first crossing. **Quantifiers are ∀N∃infinitely many n, not ∀n∃N.** This does not prove all E-state integers exit. The complete CP-0042 graph self-loops and arbitrary paths remain untouched. Independent small checks N1..4: (J,h_N,R_N,T^J(R_N))=(17,16,16411,7394),(34,32,12108996635,2457612461),(51,48,1185112435761179,108359606202731),(68,64,67716950119032070171,2789381225506424576). Values are finite examples, not the general proof.

**Two attempted integer-dependent renewal routes and their exact gaps.** Route A is the computable *stopping/parity certificate*: build W_N from a finite exceptional itinerary, refine the start residue to force a long even tail, and use rank n once the first crossing strictly drops. It succeeds for the prescribed infinite composite cylinders above with N unbounded, but there is NO proof that an arbitrary fixed n in E belongs to any such refined cylinder, because every appended tail imposes extra high bits. Route B is size plus `v2(n+1)` / mod3 reverse arithmetic: CP-0041 gives infinitely many positive (and infinitely many composite) `n=393243+524288k`, `T^11(n)=1259803+1679616k>n`, with BOTH starts and outputs ≡27 (mod256) and `v2(n+1)=v2(T^11(n)+1)=2`. Therefore every proposed renewal rank `F(n,v2(n+1))` strictly increasing with n at fixed valuation INCREASES on these prescribed 11-step returns (for instance `n^p/2^(λv)`, p>0, any λ). This REFUTES its universal-decrease claim on those returns, NOT every possible adaptive policy using later steps. Odd reverse U constraints: y≡0(mod3) has no odd predecessor; y≡1 requires even 2-exponent and predecessor >y for y>1; y≡2 admits some smaller predecessors. None yields universal branch completeness. The *missing exact lemma* is an algorithm, defined for EVERY positive n in the 71 exceptional classes, proved to terminate with an iterate <n or in a previously globally certified basin, and a rigorously decreasing well-founded rank on that algorithm's actual transition. No such lemma was established.

## CP-0046 — PROVED_INTERNAL: two simultaneous infinite FIRST-crossing D<K families, strict smallest lifts, all four other hard classes

For integer `m>=11`, define `j=ceil(m log_2(3))` (equivalently the bit length of `3^m`), `P=3^m`, `D=2^j-P`. Select those m satisfying the **strict open interval**
`1/100 < D/P < 1/50`.
There are infinitely many such m, unbounded, because `log_2(3)` is irrational and fractional parts of `m log_2(3)` are dense: the requested interval is equivalent to
`log_2(101/100) < j-m log_2(3) < log_2(51/50)`, a nonempty open subinterval of (0,1). No numerical heuristic is involved.

For EACH such m, simultaneously take either
**Family A:** `(a,c,d,b)=(3,1,m-3,j-m-1)`, or
**Family B:** `(a,c,d,b)=(4,2,m-4,j-m-2)`.
Both have `a+c+d+b=j`, the SAME `P,D`, and exactly the SAME
`K=3^(m-3)-2^(m-2)`. Their `M=2^(j-3)` and `2^(j-4)` respectively. For m>=11, b>=1 and `3^3>2^4`, `3^4>2^6`; the E^c segment cannot cross, subsequent O^d increases slope, and final b Es reach the **very first** crossing at j by definition. Each least `t0=(-K P^(-1)) modM` is positive.

The general divisibility in CP-0044 becomes, in **BOTH** families,
`2^(m-2) | (27t0+1)`. Hence `t0>=(2^(m-2)-1)/27>=511/27`, so integer `t0>=19`. Meanwhile
`0<D/P<1/50`,
`0<K/P=(1-2*(2/3)^(m-3))/27<1/27` and for m>=11 the last ratio exceeds 1/50; thus **D<K**.
Also `M/P=(P+D)/(2^a P) < (51/50)/8=51/400`. Combining,
`D*t0/P >19/100 >51/400+1/27 > (M+K)/P`.
Therefore `D*t0>M+K`; by the exact drop EVERY admissible positive lift q>=0 STRICTLY DESCENDS at its genuine FIRST coefficient crossing. NO published cycle-exclusion theorem is imported. The first-crossing length j grows unbounded over the infinite m.

In A, t0 odd implies starts `2^3(t0+Mq)-1≡7 mod16`; CRT produces infinite composite strict-first-crossing lifts in BOTH r=7 and39 mod48. In B the starts are ≡15 mod16 and similarly give composite strict lifts in BOTH r=15 and31 mod48 (use mod5 in residue classes not divisible by3). Coupled with CP-0045, all SIX possible least-nonconvergent mod48 classes contain infinite explicitly certified deep first-crossing-descent composite **SUBPROGRESSIONS**; absolutely NO full residue class, all-positive, or Terras CST theorem follows.

Finite example m=41: j65, D/P≈0.0115288518, K/P≈0.037037022; Family A (3,1,38,23), Family B (4,2,37,22), both D<K and strict at j65. Independent exact checks m=41,188,241,294 verify each parity input and strict minimum drop. Exact finite exploratory BOX a3..15, c1..8, d1..500 found 30,987 admissible first-crossing grammars, 88 with D<=K, and ZERO minimum-lift overshoots. This BOX is NOT an infinite proof or a universal CST claim.

## External literature / adversarial controls / status
- Terras (1976), *A stopping time problem on the positive integers*, Acta Arith. 30, historical CST. Rozier and Terracol, *Paradoxical behavior in Collatz sequences*, *Discrete Mathematics* 349(10), 115167 (October 2026), https://www.sciencedirect.com/science/article/pii/S0012365X26001913, primary current article directly confirms CST remains CONJECTURAL; it documents paradoxes occurring AFTER earlier descent, not a first-crossing counterexample.
- Tong Niu, *Parity vectors and paradoxical sequences in the accelerated Collatz map*, arXiv:2605.13886 (11 May 2026), treats parity-vector statistics and denies settling Collatz/CST. This strengthens PRIOR-ART caution; no novelty claim.
- Steiner (1978), *A Theorem on the Syracuse Problem*, *Congressus Numerantium* XX 553–559, original FULL TEXT still NOT acquired in this session. Lagarias annotated bibliography https://citeseerx.ist.psu.edu/document?doi=23fc93711a7dbf9b3441a5c957a8737538489405&repid=rep1&type=pdf and historical scholarly discussion https://math.stackexchange.com/questions/3092661/does-anyone-know-where-i-can-get-a-copy-of-r-p-steiner-a-theorem-on-the-syra give INDIRECT corroboration; no direct 1978 proof-reading claimed.
- Original local repo not cloned (container DNS). Isolated portable four-test script PASS, SHA256 in validation/S011_LOCAL_PROBES.md; original S000/S001/S003 audits pre-entry only at GitHub-hosted prior commit; new S011 test and original suite must be observed from S011 PR/main CI, NOT presumed. 7->5 at j7 then 8 at j8, 15->23->35, 27->23 j59, 91->61 j45, 121->91, 175->167, 681->511; r7/15/27/31/39/43 all considered. Infinite finite-prefix constructions are NOT divergent orbits.

**Scientific status:** CP-0044—0046 internal elementary/irrational-rotation results, originality UNESTABLISHED. All-composite convergence equivalent to all-positive Collatz remains OPEN; Terras CST remains OPEN. No Lean, Palomar, peer review, publication, or independent formal proof certificate.
