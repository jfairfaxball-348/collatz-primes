# S001 — Factor erasure, depth obstructions and reverse-basins

**15 October 2026.** Work on the shortened positive Collatz map `T(n)=n/2` if even, `(3n+1)/2` if odd. Let `U(x)=(3x+1)/2^{v_2(3x+1)}` on odd positive `x` (an **odd-to-odd** jump). Claim labels below are mathematical evidence tiers, not novelty assertions. **The all-composite/all-positive Collatz assertion remains OPEN.**

## A1. CP-0008 — factor erasure (PROVED_INTERNAL, elementary)

For any positive odd `n`, `3n+1` is positive and even, so `e=v_2(3n+1)>=1` is finite; `U(n)` is a positive odd integer and `T(n)=2^{e-1}U(n)`. We have

    gcd(n,3n+1)=gcd(n,1)=1,
    gcd(n,U(n))=1.

If odd prime `p|n`, then `2^e U(n)=3n+1 ≡ 1 (mod p)`; since `2^e` is invertible modulo `p`, `U(n) ≡ 2^{-e} (mod p)` and **p does not divide U(n)**. Because `n` is odd, the same holds for the single shortened step `T(n)`. For `n=1`, `e=2`, `T(1)=2`, `U(1)=1`; gcd identity holds vacuously, and 1 is not a candidate for strict descent. This result is not presented as new.

**Counterexamples / failure of unlicensed inferences:** `T(9)=14 ≠ T(3)^2=25`; `U(27)=41>27` (composite); `U(121)=91=7·13`, increasing the count of **distinct** odd prime factors from one to two. In fact for every integer `t>=1`, the odd composite `n=12t+3` satisfies `v_2(3n+1)=1`, `U(n)=18t+5>n`. Hence coprimality does NOT supply a decreasing size, number-of-prime-factors, or multiplicative potential.

## A2. CP-0009 — global strict-descent equivalence (PROVED_INTERNAL, elementary)

Let `D` mean `∀n>1 ∃j>=1, T^j(n)<n`, and `C` mean `∀n>=1 ∃j>=0,T^j(n)=1`. If `C`, choose an iterate equal to 1 for every n>1, proving `D`. Conversely, assume `D`. Strong induction on n: base n=1 already equals 1; for n>1 select `m=T^j(n)<n` using `D`. Its positivity follows from T preserving positives. By the induction hypothesis, m reaches 1 in finitely many steps, so n does. Thus `C iff D`. This induction is valid ONLY if every n>1 has a descent witness without assuming convergence. The formulation `∀ composite n ∃j:T^j(n)<n` plus an induction hypothesis **does not** settle primes; proving composite convergence first would cover primes via `2p->p` (CP-0001), but that composite convergence is itself the open theorem. These obligations must not be switched.

## A3. Two adversarially tested proposed universal routes

**Candidate F (REFUTED):** `∀ odd composite n>1, U(n)<n` (proposed numeric descent from odd-prime-factor erasure). Explicit infinite counterfamily `n=12t+3, t>=1`, as above. **Stronger tested variant also false:** `ω(U(n))<=ω(n)` (distinct odd prime factors), refuted by 121 -> 91. Consequently erasing *old* factors says nothing about the size or factor richness of *new* odd factors. Required missing lemma: a new transition-based well-founded quantity that decreases after a finite number of steps for **every** remaining prime/composite start.

**Candidate R (REFUTED):** `∀ odd y>1, ∃odd x<y, ∃a>=1, U(x)=y` (smaller inverse-parent rank). The inverse lemma below shows every y≡0 (mod3) has no U-predecessor at all; every y≡1 (mod3) has smallest allowed exponent a=2, yielding x=(4y-1)/3>y for y>1; only y≡2 (mod3) gives a smaller x. Hence a universal inverse monotonicity argument cannot close. Required missing lemma: a rank-decreasing predecessor or a forward descent argument for all y≡0,1 (mod3) without importing convergence.

## C1. CP-0010 — all inverse edges and precise small-parent subfamily (PROVED_INTERNAL; elementary)

For shortened **T**, every positive y has even predecessor `2y`, and an additional odd predecessor `x=(2y-1)/3` precisely when `y≡2 (mod3)` and `x>0` (then x odd). For accelerated **U**, fix odd `y>=1`; an odd positive x satisfies `U(x)=y` iff there is integer `a>=1` with `2^a y ≡1 (mod3)` and `x=(2^a y-1)/3>0`. Necessity: `3x+1=2^a y`, with exponent exactly `v_2(3x+1)` since y odd. Sufficiency: RHS gives positive odd x (odd integer divisible by odd 3), `3x+1=2^a y` and `v_2=a`, hence U(x)=y. If y≡0 (mod3), no exponent works. If y≡1 (mod3), **a even**; if y≡2 (mod3), **a odd**, by powers of 2 modulo 3.

For odd `y>1` with y≡2 mod3 (equivalently y≡5 mod6), choose a=1. Then `x=(2y-1)/3` is a positive odd integer `x<y` and `U(x)=y`. Therefore a *least* nonconvergent positive n, if one exists, **cannot** be 5 mod6: its smaller x would be nonconvergent too, because a trajectory from x contains y. Combining with CP-0002 gives the **necessary** classes `7,15,27,31,39,43 (mod48)` for a least counterexample; none is asserted to contain one. This may be familiar reverse-tree arithmetic; originality NOT ESTABLISHED. No claim that every `5 mod6` number converges unconditionally follows from this lemma.

For y≡1 mod3 and y>1, smallest valid exponent a=2 produces x=(4y-1)/3>y, and larger valid exponents only increase x. At y=1, a=2 yields x=1, the U self-loop; all larger even a give larger x. For y≡0 mod3, none exists. These two cases exhibit exactly why the smaller-predecessor method stalls.

## B. CP-0011 — certified affine branch criterion (PROVED_INTERNAL elementary) and finite reconstruction (FINITE_CERTIFICATE)

For an odd positive representative `1<=r<2^k`, `k>=2`, let the first j<=k input parities of T be a word of `O/E` with `a` odd positions. The exact affine composition is

    2^j T^j(n) = 3^a n + b,

where initial `(M,b,D)=(1,0,1)` and under an odd input `(M,b,D) -> (3M,3b+D,2D)`; under an even input `(M,b,D)->(M,b,2D)`. The fixed prefix for n=r+q 2^k is proved inductively: at step i<k, the two current states differ by `3^(number of O among first i)*q*2^(k-i)`, which is even. Hence the next parity agrees and the identity persists. For all q>=0, strict descent at time j holds exactly when

    (2^j - 3^a)*(r+q*2^k) > b.

The certificate **sufficient** condition `2^j>3^a` and `(2^j-3^a)*r>b` implies strict descent for **every** q>=0; it is symbolic rather than sampling. Conversely, this sufficient condition is necessary for `T^j(n)<n` to hold for **every** n in this class, since a nonpositive slope difference cannot remain greater than fixed b>=0 as q->∞. Here `b>=0`. Therefore it is an exact full-class-descent test for each j<=k.

**Base-case caveat:** residue r=1 is NOT uniformly strictly descending because n=1 cycles `1->2->1`. For k>=2 and n=1+q2^k, q>=1, the first two inputs are `O,E` and `T^2(n)=(3n+1)/4<n`. The report's total `30654` at k=16 is precisely `30653` genuine all-positive-representative strict classes **plus** this one `BASE_1` class, certified only after excluding n=1. Treating 30654 as literally all-class strict descent would be mathematically inaccurate.

Independent local producer `tools/residue_certificates.py` emits records `(k,r,j,a,b,parity_word,status)`, with `status=OPEN` when no full-class certificate exists among j<=k and with `BASE_1` separately. `tools/check_residue_certificates.py` imports **nothing from producer**, reconstructs trajectory and affine coefficients, asserts the parity, identity, slope, representative and symbolic full-class inequalities, and checks per-depth JSONL SHA256. Neither running them nor checking individual records proves convergence for OPEN families.

| k | genuine strict | BASE_1 | uncovered | total odd |
|---:|---:|---:|---:|---:|
|10|447|1|64|512|
|11|895|1|128|1024|
|12|1821|1|226|2048|
|13|3728|1|367|4096|
|14|7457|1|734|8192|
|15|15088|1|1295|16384|
|16|30653|1|2114|32768|

At k=16, uncovered classes have residue mod16 counts `7:395`, `11:395`, `15:1324`. `27` (composite) is uncovered at depth16 and first descends at j=59 (27 -> 23); no infinite failure is implied. The independently verified manifest is `validation/S001_manifest.json`. Its canonical SHA256 is `d4686d95c47107af29d939accb8d161684f929eb348426f2d39ea8b1819b2b37`. The full class-by-class records can be regenerated using the exact commands in the closeout; `records_sha256` in the manifest commits to all class records, not only samples. Input representative domain is strictly **positive odd** 1<=r<2^k; certificate steps j<=k; no representative 0 is permitted. External owner report's raw bytes were not available to hash.

## B4. CP-0012 — exceptional lifting and a hostile infinite family (PROVED_INTERNAL, elementary)

Define `E_k` to be odd positive r<2^k having no full-class strict certificate in j<=k and r≠1. If `s` is an uncovered class at depth k+1, its positive residue `r=s mod 2^k` must be uncovered at depth k: any strict full-class descent witness j<=k for r works at all n≡r (mod2^k), including every lift; if parent r=1, all lifts n>1 descend in 2 steps, while s=1 itself is BASE_1. Thus the projection of E_(k+1) is contained in E_k (with appropriate base exception excluded). **Only a necessary inclusion**, never sufficient: uncovered parents may acquire a certificate on one or both children either from a larger representative or from the new (k+1)-st step.

For **every** fixed k>=1, and every positive t such that n=2^k t-1>1, the first k T-input parities are all odd and

    T^j(n) = 3^j * 2^(k-j) * t - 1   (0<=j<=k).

Induction: the state at j<k is odd and substituting `(3x+1)/2` gives the next expression. Since `3^j>2^j` for all j>=1, **every** first j=1..k output exceeds n. No universal finite iteration bound k for strict descent exists. The family includes infinitely many composite n: choose t>=1 with `2^k t ≡1 mod3`, so n multiple of3, and t arbitrarily large so n>3. In particular r=2^k-1 is OPEN through depth k (k>=2). The consistent 2-adic exceptional prefixes `-1 mod2^k` select the **2-adic integer -1**, not any fixed positive integer. It would be logically invalid to infer a positive divergent trajectory from the nested residue prefixes alone.

This theorem defeats a finite bounded-depth closure and a naive depth-uniform rank. It does **not** defeat the possibility of a start-dependent, unbounded but finite descent time, which is exactly what the Collatz conjecture demands. Novelty **NOT ESTABLISHED**: parity-prefix calculations are classical.

## C2-C3. CP-0013 — reverse grammar: sound, complete only relative to convergence (PROVED_INTERNAL identity / OPEN universality)

Odd grammar `G_odd`: start with `1`; from an already generated odd y, whenever `a>=1`, `2^a*y≡1(mod3)` and `x=(2^a*y-1)/3>0`, add x. Full grammar G additionally adds `2^b*x` for every generated odd x and every integer b>=0. Every generated x converges: one odd reverse-U step is a finite, legitimate forward T path to its parent; each even double has a finite halving path to x. Conversely a positive convergent n, after stripping powers of 2, has a finite U path to 1 and thus lies in G, read in reverse. Therefore `G = {positive convergent starts}`. **This is a tautological characterization, not a proof that G=N+**. Missing first global quantifier: `∀ odd y>0, y∈G`, or equivalently a new invariant which puts *every* y in the generated grammar without assuming y converges.

The 5 mod6 small-predecessor identity shows a useful closure implication *for a least counterexample*: that counterexample cannot be 5 mod6. But it does not establish an unconditional generated-membership implication `x∈G => y∈G` for y=U(x) without already knowing x is generated. Thus the bridge from inverse factors to forward exceptional parity prefixes remains **OPEN**. Counterexample to the tempting `y≡5(mod6)` covers all composite exceptions: y=27 is 0 mod3 and remains uncovered at depth16, so neither the reverse a=1 branch nor bounded parity certificate applies. Family n≡-1 mod2^k (arbitrarily large composite n) defeats any fixed-depth bridge; no claim of actual nonconvergence.

## Source-to-lemma dependency and novelty audit (checked 15 October 2026)

| External/sibling source | Inspected evidence | Legitimate use | NOT licensed |
|---|---|---|---|
| Lagarias, *The 3x+1 Problem: An Overview*, arXiv:2111.02635 (2021 posting of older survey) | arXiv abstract | Context/map/history | Universal convergence |
| Tao, *Forum Math Pi* 10 e12 (20 May 2022) | Cambridge primary abstract/theorem formulation | Logarithmic-density almost-all **almost bounded** orbit result | Every integer converges / no exceptional starts |
| Bařina, *J. Supercomputing* 81:810 (2025) | Publisher abstract | Source-reported verification below 2^71 | S001 independent confirmation or unbounded theorem |
| Angeltveit, arXiv:2602.10466 (11 Feb 2026) | arXiv abstract | Improved *finite verification* algorithm | A proof for all n |
| Simons–de Weger, *Acta Arith.* 117 (2005) | University publisher metadata/abstract | Historical m-cycle bound | Exclusion of unbounded orbits/all m-cycles |
| Hercher, *J. Integer Sequences* 26 (2023) | Author journal abstract and listed June 2026 corrigendum | Source-stated exclusion m<=91 / m>=92; corrigendum exists | Unqualified reuse of all pre-corrigendum details; no all-cycle theorem |
| PRIMES repo README/NEXT_SESSION | 15 Oct live repo read | Preregistration and blind/holdout discipline | Prime theorem imported into Collatz |
| Proof-that-non-trivial-cycles-cannot-exist-in-Collatz START_HERE | RL350 queued, RL349 correction/orientation gap | Treat gap as OPEN | Completed cycle proof |
| Collatz-Divergence-Machine README | Closed T24; no qualifying theorem | Negative-results discipline | Divergent explicit integer |
| LEAN-non-trivial-collatz-cycles README | Local verified cycle transport; stated final target unproved | Background possible proof ingredients | Global Collatz proof / missing Mignotte bridge |
| CEML README | Research-only frontier engineering | Finite verification methods | Owner-independent world-frontier proof |
| leading-digit-hailstone README | Distinct map `3n+2L(n)+1` on odds | Methodological inspiration | Any standard-Collatz implication |

**Novelty assessment:** CP-0008, CP-0009, CP-0010, parity affine identities, reverse grammar soundness, E_k projection, and the all-odd -1 parity-prefix obstruction appear elementary/closely adjacent to classical tools. No global, unexpected or publishable new theorem is established and **no exhaustive prior-art search of every sublemma** has been done. Label originality UNCHECKED. The report's precise finite depth16 numbers are independently reproduced as finite observations, not independently discovered original mathematics.

## Remaining global quantifiers and honest state

1. `∀n>1 ∃ finite j T^j(n)<n` — **OPEN**, no rank/closure proof.
2. `∀ odd y≡0,1 (mod3)`: some noncircular descent or smaller generated predecessor of a suitable rank — **OPEN**.
3. `∀k ∀r∈E_k`: a uniform symbolic mechanism removing every positive starting integer from the exceptional tower after some start-dependent finite depth — **OPEN**.
4. `∀ odd y>0: y∈G_odd` (equivalently reverse-basin completeness) — **OPEN**.
5. No Lean/Palomar or independent human proof audit was performed for S001. Local independent *code-path* checker is not an external audit.
