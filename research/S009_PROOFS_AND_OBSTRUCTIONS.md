# S009 — universal fixed-middle-run arithmetic subfamilies and exceptional-state expanding return

Date: 2026-10-15. Entry `main` commit `b75d7a8097ab60dc0f22196bacc575214c81d29b`; **actual Git commit tree** `7b93b208e549bee6b05d6d046f1b99263ca0ea7d`; parents `5cd92afdd23532b604faf6055be68aea3c3d094a`, `350dd68bfbea09c739777604dbb6f3b5225e1f5b`. S008 PR #11 merged and its independent PR/main CI runs both SUCCESS with individual steps observed. Main branch reports unprotected, public rulesets []; original checkout network DNS unavailable.

**Boundary:** CP-0007 (full positive/composite Collatz) and CP-0019 (Terras coefficient stopping time) remain **OPEN**. These are scoped infinite-cylinder statements with elementary proofs, NOT a global result. Priority/novelty unchecked. No Lean or Palomar.

## Exact notation and preceding facts

Shortened Collatz `T(n)=n/2` for even n, `T(n)=(3n+1)/2` for odd n. An O/E word records the parity of the INPUT at each T-step. A first coefficient crossing is the first j with `3^(# O in first j inputs) < 2^j`. By S008 CP-0038 for admissible `O^a E^c O^d E^b`, letting `n=2^a t-1` and
`P=3^(a+d), K=3^d(2^c-1)-2^(c+d), M=2^(c+d+b), D=2^a M-P`,
there is exactly one positive t residue modulo M determined by `P*t ≡ -K (mod M)`; the least positive representative `t0` lies in `[1,M-1]`. Its nonnegative lifts `t=t0+M q` realise that word, with
`T^j(n)=(P*t+K)/M`, `n-T^j(n)=(D*t-(M+K))/M`, `j=a+c+d+b`.
Thus `D*t ≡ K (mod M)`. For (c,d)≠(1,1), S008 establishes `K>=1`.

### CP-0039 — PROVED_INTERNAL infinite first-crossing strict families for *every* fixed nontrivial pair c,d

**Theorem (elementary weak; source-dependent strict at smallest lift).** Fix ANY positive integers `c,d` with `(c,d)!=(1,1)`, and put `K=3^d(2^c-1)-2^(c+d)>=1`. Select an integer `s>=3` with `2^s-1>K`. There exists an explicit finite threshold `A(c,d,s)` such that **for every a>=A with `a+d≡0 (mod 2^(s-1))`**, set `b>=1` *minimal* with `2^(a+c+d+b)>3^(a+d)`, and `M,P,D,t0` as above. Then (i) this word has its first coefficient crossing exactly at j=a+c+d+b; (ii) every positive lift `n=2^a(t0+M q)-1` satisfies `T^j(n)<=n`; (iii) q>=1 satisfies the STRICT inequality `T^j(n)<n` without cycle theory; (iv) equality for q=0 would give a nontrivial positive two-circuit, excluded by the published SOURCE_STATED Simons–de Weger no-2-cycle result. This applies to **infinitely many a** for EACH fixed c,d, and each qualifying a has infinitely many composite strict-descent lifts (take suitable q mod3). It does NOT cover all a, all parity words or all integers.

**Proof.** Choose A so large that `3^a>2^(a+c)`, `a+c+d+1>=s`, and `3^(a+d)>2^(a+c+d)`. Such an A exists since (3/2)^a grows without bound. All prefixes of the first O^a run have slope >1. The following E^c run ends with coefficient `3^a/2^(a+c)>1` and prior prefixes have larger coefficient. The following O^d run multiplies the coefficient by (3/2)^d, so all intermediate slopes remain >1. By minimality b>=1 of the final E run, every prefix before the last E has coefficient >=1 while at the last E it is <1. Thus j is exactly the first coefficient crossing.

For `a+d` divisible by Euler's exponent `phi(2^s)=2^(s-1)`, Euler's theorem gives `3^(a+d)≡1 (mod 2^s)`. As `a+c+d+b>=s`, `2^(a+c+d+b)≡0 (mod 2^s)`, hence the *positive* integer `D=2^(a+c+d+b)-3^(a+d)≡-1 (mod 2^s)` obeys `D>=2^s-1>K`. Because t>=1, `D*t>K`. Because also `D*t≡K (mod M)`, the positive multiple `D*t-K` of M must be >=M. Consequently `D*t>=M+K` and the exact drop formula proves (ii). Writing `t=t0+Mq`, every q>=1 adds Dq>0 to the drop and proves (iii). For equality q=0, the positive n>1 returns to itself after an O^a E^c O^d E^b cycle with exactly two alternating O/E runs; this is excluded only by already-published no-nontrivial-2-cycle theory, NOT proved from the current elementary congruence. The arithmetic progression a≡-d mod2^(s-1) contains infinitely many qualifying a. Finally `n=2^a t0-1+2^a Mq`; since 2^a M is invertible mod3, one q residue mod3 makes n divisible by3, and for arbitrarily large q this makes n composite. QED for scoped assertions.

**Explicit witness with c>1 AND d>1:** (a,c,d,b)=(6,2,2,3), `P=6561`, `K=11`, `M=128`, `D=1631`, `t0=85`, `n=5439`, first-crossing word `OOOOOOEEOOEEE`, endpoint `4357<5439`. (The same example falls in the progression: s=4, a+d=8 divisible by phi(16)=8.) This numerically illustrates but does not prove the general result.

### CP-0040 — PROVED_INTERNAL all-a positive-K unit-offset case, two distinct grammars

**Theorem.** For ALL `a>=4`, both (c,d)=(2,1) and (c,d)=(1,2), with final b chosen minimally as above, have genuine first coefficient crossing at j and `T^j(n)<=n` for **every** positive t in their admissible residue class; all q>=1 strictly descend. Source-stated nontrivial-2-cycle exclusion implies strict for q=0 as well.

**Proof.** Both pairs have `K=1`; for a>=4, `3^a>2^(a+c)`, so the first-crossing proof from CP-0039 applies without any arithmetic progression. Since `a+d>=5` and total j>=8, `2^j≡0 (mod8)` and `3^(a+d)≡1 or3 (mod8)`, whence `D≡7 or5 (mod8)`. Since D>0, necessarily D>=5>K=1. Apply the integral congruence argument `D*t≡1 (modM)` and distinguish q=0/q>=1 exactly as in CP-0039. QED.

Independent smallest representatives: (a,c,d)=(4,2,1) gives b=1, t0=5, 79->76 at j8, word OOOOEEOE; (4,1,2) gives b=3, t0=23, 367->262 at j11, word OOOOEOOEEE. CP-0040 is a stronger quantified coverage result than S008's K>=1 caveat, not a proof of all c,d,a. Exact elementary identities may be known; originality UNCHECKED.

## Attack A — why a residue-return induction needs a genuine rank

### CP-0041 — PROVED_INTERNAL expanding 27 mod256 return, infinite composite examples

**Theorem.** For every integer k>=0, with `n_k=393243+524288k`, the first 11 iterates follow 27's 11-bit parity word and satisfy
`T^11(n_k)=1259803+1679616k > n_k`,
and BOTH n_k and T^11(n_k) are `27 (mod256)`. For k divisible by3, n_k is composite (divisible by3). So a permitted "regeneration" solely because the residue state r=27 mod256 reappears **does not** give a smaller integer, even on infinitely many odd composite inputs.

**Proof.** Exact iteration gives `T^11(27)=91` with eight O inputs; parity-cylinder affine identity gives `T^11(27+2048q)=91+6561q` for every q>=0. Set `q=192+256k`; algebra yields the displayed n_k and output. Both are 27 mod256 because 393243≡1259803≡27 mod256 and increments are divisible by256. Their difference is `866560+1155328k>0`. Since `393243≡0 (mod3)` and `524288≡2 (mod3)`, every k divisible3 yields a multiple of3 greater than3. QED.

**Logical caution:** this is ONE expanding state return, not an infinite repeated return on a single integer: the complete 11-bit parity state need not be preserved by the output. It proves neither divergence nor existence of a Collatz cycle. It refutes a specific attempt to declare a residue recurrence itself a well-founded descent.

### Precise conditional regenerative induction and its unsolved branch-completeness

Let `C` be any sound decidable strict-descent cylinder collection and `E=N_{>=2}\C` its unhandled positive starts. A proposed regeneration policy gives a positive integer block length h(n)>0 at every n in E, with state (n, parity/residue prefix). To deduce Collatz by strong induction on n it is NOT enough that some intermediate state is in C, or that a coefficient becomes <1: for every n in E the policy must provide a FINITE verified chain whose resulting endpoint m satisfies `1<=m<n`, or hit a globally certified convergent base. Such universal termination is exactly the missing well-founded branch-completeness lemma. Assuming it for the 71-tree without proof is circular. CP-0035 excludes any uniform bound h(n)<=H; CP-0036 excludes one-step descent through j13; CP-0041 kills residue-only recurring-state decreases. No general adaptive rank R(n,state) with a proved strictly decreasing well-founded order was obtained.

Hostile tests: 27->91 at j11 (91>27), and 27->206 at j13. The long first descents j59 for 27 and j45 for 91 show delay, NOT failure of convergence. Odd U inverse: for odd y divisible by3 no odd predecessor, for y≡1 mod3 all valid k even and predecessor (2^k y-1)/3>y when y>1, and for y≡2 mod3 k odd can give smaller predecessor; not a forward proof. Six possible least-nonconvergent residue classes mod48 remain 7,15,27,31,39,43; composite test seeds 55,15,27,175,39,91 descend at j5,7,59,8,8,45 respectively, finite examples only. Earlier factor counterexamples 121->91, 15->23->35, 681->511 remain.

## Falsification, sources, independent testing and limits

The proposed false lemma "D*t automatically >=M+K for ALL c,d,a" is **not** proved: CP-0039 explicitly imposes a congruence class and sufficient size D>K. First-crossing overshoot would contradict Terras CST, so no unchecked counterexample is claimed. Likewise no assertion is made that the 71 exception set eventually empties. Independent isolated standard-library tests in `tests/test_s009_math.py` and `validation/S009_LOCAL_PROBES.md` cover fixed c,d<=5, a<160 as eligible, exact symbolic lifting, positive K, q=0/1/3, expanding self-return and historic adversaries. This is finite testing distinct from the complete quantified proofs above.

Source: Rozier–Terracol (2026) publisher article explicitly calls CST conjectural, DOI 10.1016/j.disc.2026.115167. Simons–de Weger (2005), *Acta Arith.* 117:51–70, publisher `https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/117/1/82263/theoretical-and-computational-bounds-for-m-cycles-of-the-3n-1-problem`, explicitly states no nontrivial m-cycles m<=68; full original article PDF is available at `https://www.impan.pl/shop/en/publication/transaction/download/product/82263`, but its proof was NOT independently rederived here. Steiner 1978 original remained unacquired; SRC-0015 remains indirect scholarly corroboration. Nothing here establishes novelty or universal Collatz/CST.
