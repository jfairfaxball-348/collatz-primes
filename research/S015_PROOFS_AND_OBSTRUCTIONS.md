# S015 — PRIMARY Matveev, quantified growing-prefix descent, hostile universality audit

2026-10-15. T(n)=(3n+1)/2 if n odd, n/2 if even. O/E denote INPUT parities. Every finite parity word W of length j with r odds has exact 2^j T^j(n)=3^r n+B_W for n in its unique parity cylinder. First *coefficient* crossing is the first i with 3^(#O in W[:i])<2^i; this does not imply integer descent by itself. All novelty unestablished, all-positive/composite Collatz and Terras CST OPEN.

Entry: LIVE main ae692ae686102e3e07b5c3b5a60e97148eff7458; true git tree ecee406746b89d9d4bef03e846028fd9a7e39554; ordered parents 14a381126f13867ff41d9614783184dc3f473c48, c6b0cb90deff9cb8bc2ff6dff1b38b8687b0b009. Open PRs [] at entry; rulesets []; main protection GET 403 UNOBSERVED. Pre-entry main push run 38752996133 job 116483964285 COMPLETED SUCCESS; individually Unit tests, Finite parity and orbit sanity, Recreate finite residue stream and cross-check original manifest SUCCESS. This was preceding S014-attestation checkout, NOT S015. Local git clone/ls-remote DNS github.com fails. S015 isolated local tests 5/5 PASS; S015 hosted outcomes must be independently observed after writing branch.

## CP-0056 — PROVED_INTERNAL **using SOURCE_STATED Matveev 2000 PRIMARY Corollary 2.3**

For ALL integers m>=1, put P=3^m, j=bit_length(P), delta=2^j/P-1. Since 2^(j-1)<3^m<2^j, delta>0. The following deliberately conservative bound is valid:
    log(delta) > -C (1+log(4m)),  C=10^10.
Proof from **directly inspected ORIGINAL Matveev** (2000) Corollary 2.3, English 53-page PDF https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng , printed p1219 PDF page 3. Matveev's theorem bounds LOG of a nonzero linear form L= b1 log alpha1 + b2 log alpha2, not directly the product-minus-one expression. Use (alpha1,alpha2)=(2,3), field Q of degree D=1 (real kappa=1), b=(j,-m), A=(log2,log3), Ω=A1 A2. Nonzero L=j log2-m log3>0 by prime factorisation and definition of j. Its logarithms log2,log3 are linearly independent over Z; A_i>=max(Dh(alpha_i),|log alpha_i|,0.16). In the paper's (1.3), B=max(1,j log2/log3,m) <=2m as j<=2m. Corollary 2.3 states log|L|> -C1(2,1) D² Ω log(eD) log(eB), where the explicit (2.6) min gives C1(2,1)<=2^(6*2+20)=2^32. Hence log L> -2^32 log2 log3 (1+log(2m)) > -10^10(1+log(4m)). Since delta=e^L-1>L>0, the same claimed bound holds for delta. The PRIMARY PDF was actually accessed; the entire 53-page analytic proof was NOT independently rederived. Previous 2021 secondary restatement also agrees in its distinct product-minus-one form. This is an imported theorem, NOT an original proof of Matveev. It improves the previous convenient 10^12 bound, and directly validates the key type/constant distinction.

## CP-0057 — PROVED_INTERNAL conditional on Matveev SOURCE_STATED: UNIFORM GROWING-PREFIX THEOREM

Let C=10^10 and D0=[64(C+10)]². For EVERY d>=D0 and EVERY finite nonempty word U (which MAY depend arbitrarily on d) with ell=|U|, r=#O(U)>=1, satisfying:
  (i) ALL nonempty prefixes V of U obey 3^(#O(V))>2^|V|;
  (ii) 2r<=d,
set m=r+d, j=bit_length(3^m), b=j-ell-d, and W=U O^d E^b.
THEN b>=1, the unique full parity cylinder of W has its GENUINE FIRST coefficient crossing precisely at j, and EVERY positive integer n in the cylinder has T^j(n)<n. Infinitely many such starts are COMPOSITE. This is uniform in all U and all d satisfying the displayed bounds, with no fixed-U constant smuggled into 'sufficiently large'.

**Complete proof.** CP-0058 below proves 0<=B=B_U<=2^(ell-2)(3^r-1), with 2^(ell-2) read as an exact rational for ell=1. Put Z=B/2^ell, so 0<=Z<3^r, 1+Z<2*3^r. For every actual word-realising n, the intermediate T^ell(n)=2^d h-1 with integer h>=1 (because the subsequent d input steps are O). Thus
    3^r n+B=2^ell (2^d h-1),
    n >= 2^ell(2^d-1-Z)/3^r.
The exact full affine intercept is
    B_W=3^d(B+2^ell)-2^(ell+d);
hence integer strict descent is equivalent to
    delta*n > (B+2^ell)/3^r - 2^(ell+d)/3^m.
It therefore suffices that delta*(2^d-1-Z)>1+Z.

Now 2r<=d implies m<=3d/2 and
d log2-r log3 >= d(log2-(log3)/2)>d/8
(the latter by log(4/3)>1/4). For d>=256, log(4m)<=log(8d)<=sqrt(d). Write X=sqrt(d)>=64(C+10). Then
    d/8=X²/8 >= 8(C+10)X > C(1+X)+log 8.
By CP-0056,
    log(delta*2^d/(3^r)) > d log2-r log3-C(1+log(4m)) > log8,
so delta*2^d >8*3^r. Also delta<1 implies 2^d>8*3^r. Thus 1+Z<2*3^r<2^d/4, so
    delta(2^d-1-Z) > (3/4)delta*2^d >6*3^r>1+Z,
proving strict drop for EVERY positive member, including the least lift and arbitrarily large lifts.

The entire U prefix has coefficient>1 by (i). Adding O^d increases slope and the coefficient just before final E is 3^m/2^(ell+d)>1. Hence j>ell+d so b>=1. The decreasing E^b tail cannot cross earlier because 2^(j-1)<3^m; at j, 2^j>3^m. All words have a unique residue class mod2^j: the invertible odd 3^m coefficient and exact inverse congruence give n0=(-B_W*(3^m)^(-1)) mod2^j in 1,...,2^j-1 (B_W odd). Its representatives n0+2^j q, q>=0, realise the word by the parity-vector bijection (induct backwards modulo powers of2). Coprimality gcd(2^j,3)=1 permits infinitely many q with n divisible by3 and n>3. QED.

**Genuinely growing example:** U_k=(OOOE)^k has ell=4k, r=3k, each prefix overcritical since each full OOOE block multiplies slope by 27/16>1 and intermediate O letters increase. Take d=6k, so 2r=d. For ALL k with 6k>=D0, CP-0057 proves full-cylinder descent; number of separate E-blocks increases without bound. Exact **finite** k=1..24, d=6k full parity and q=0,1,3 checks PASS; this finite k-range is NOT the reason for the infinite result.

General variant: for any fixed real rho in (0, log2/log3), use r<=rho*d and d sufficiently large depending ONLY on rho, since d(log2-rho log3) dominates C log(4(1+rho)d); all preceding estimates hold. No uniform statement is made at rho>=log2/log3.

## CP-0058 — PROVED_INTERNAL exact universal intercept budget

For every finite parity word U of length ell>=1 with r>=1 O inputs, write B_U by recursion B_empty=0, B_{prefix+E}=B_prefix, B_{prefix+O}=3 B_prefix+2^i for an appended O at zero-based index i. The r odd positions contribute terms 2^i 3^k where k counts later odd positions. Since i<=ell-1, 
    0<=B_U <=2^(ell-1) sum_{k=0}^{r-1}3^k =2^(ell-2)(3^r-1).
Equivalently the exact integer bound 4 B_U <=2^ell(3^r-1), and it is valid WITHOUT overcritical assumption. Enumerated ALL 2^ell binary words for ell=1..12 (8190 total) in the S015 exact test, with no failures. The algebra, not enumeration, proves the claim.

## CP-0059 — PROVED_INTERNAL scoped coverage obstruction and OPEN global schemes

The CP-0057 **large-d family itself cannot cover any complete positive residue class**, irrespective of varying U. Indeed when d>=D0 and r<=d/2, 2^d>8*3^r, Z<3^r, so every cylinder start satisfies
    n >= 2^ell(2^d-1-Z)/3^r > 2^(d-1)/3^r >= (2/sqrt(3))^d/2.
This bound grows with d and is far larger than 43 for d>=D0. Thus positive starts 7,15,27,31,39,43 lie outside EVERY cylinder covered by CP-0057. This is a theorem about THIS huge-threshold subfamily, NOT a no-go theorem against other smaller-d certificates or eventual termination of those six integers.

Hostile controls: U=OE has first coefficient crossing already at step2; CP-0057 cannot drop the all-prefix overcritical condition. For the 27 prefix p=OOEOOOOOEOEOO (13 letters) one has T^13(27)=206 even, so 27 is in NONE of the p O^d E^b cylinders for d>=1, although p has all coefficients >1. Exact exceptional-state enumeration restricted to z≡11 mod16 yields 71 first-13 noncrossing residues mod8192. Each of 71 has affine 13-block P odd, so map q↦T^13(z)+P*q mod8192 is a permutation; every ordered pair of 71 states occurs, 71²=5041 directed potential finite edges. Arbitrarily long fixed itineraries have composite lifts by parity congruences. This does NOT yield a single positive infinite exceptional orbit.

A. **Forward number-dependent renewal:** compute maximal odd run exactly h=v2(n+1), use the known exact 3^h u-1 formula, skip its even run, test an actual later x<n. Each local run is finite. But count of renewals may be unbounded and proving the algorithm eventually drops for every n>=2 is exactly the universal descent/Collatz claim; no independent ALL-n halting lemma is available. Hostiles: 27 needs 59 steps, 91 needs45, 155 needs40, 251 needs27; arbitrary 71-state paths; 393243+524288k expands at its exact 11-step same-v2 return; forced-O towers last H steps above start. No size+v2 monotone rank.

B. **Inverse-basin/3-adic/factor route:** reverse predecessors of y are 2y always and, only if y≡2 mod3, the positive odd (2y-1)/3. Bounded reverse BFS from1 is decidable and membership gives a verifiable forward orbit to1. It does NOT prove all positive n are enumerated. Indeed y≡0 or1 mod3 admits no odd reverse predecessor, and 2y>y; the blanket proposed 'every inverse step can be chosen smaller' is false (e.g. y=3). A globally bounded inverse basin completeness theorem would be equivalent to resolving Collatz; no such theorem was established. Prime/composite factorisation supplies no multiplicativity of T.

All 71/5041 edges were checked EXACTLY, alongside finite witnesses 7/15/27/31/39/43/91/155/251, expanding k=0,1,3,9 and H=6,12,24,48,96 forced-O composites. FINITE_TEST only. No divergent integer orbit was inferred, and no universal integer-dependent certificate was proved.

## Primary and secondary sources / validation boundary
- **PRIMARY ACQUIRED AND SPECIFIC ORIGINAL THEOREM READ:** E. M. Matveev (2000), "An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II", *Izvestiya: Mathematics* 64:6, 1217–1269, §2 Theorems 2.1–2.2/Corollary 2.3, original 53-page full-English PDF at https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng . Full source is accessible, but all 53 pages' proof has NOT been independently verified. Note MATVEEV proves inequality for log|L| with L a linear form; we convert to delta=e^L-1> L. Matveev theorem remains SOURCE_STATED, not reproduced.
- Previously used published 2021 secondary product-minus-one restatement Theorem 3 https://link.springer.com/article/10.1007/s40993-021-00252-2 independently agrees on polynomial separation, but is not needed for CP-0056.
- R. P. Steiner (1978), "A Theorem on the Syracuse Problem", *Congressus Numerantium* XX, pp553–559: original seven pages STILL NOT FOUND/READ; indirect Lagarias/Steiner access discussion only.
- Terras (1976) publisher https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/30/3/101028/a-stopping-time-problem-on-the-positive-integers , Simons–de Weger (2005) https://doi.org/10.4064/aa117-1-3 finite m-cycles, Rozier–Terracol (October 2026) https://doi.org/10.1016/j.disc.2026.115167, Tong Niu (May 2026) https://arxiv.org/abs/2605.13886 . None supplies total Collatz or Terras CST proof. No exhaustive novelty review performed.

S015 tests: isolated Python 3 /mnt/data/s015_work/test_s015_math.py, `python ... -v`, 5 tests PASS (0.067s), source hash SHA256 e722aaee44b5e25ff0fec3cbcffcade8e718b447df9490b531c87a3798ed84b2. FIRST iteration of exceptional test erroneously counted 367 among all 8192 residues; corrected domain to z≡11 mod16 and EXACTLY 71; the discarded 367 was a TEST DOMAIN ERROR, not a theorem. Original repository full suite needs actual hosted GitHub observation on S015 branch. No Lean/Palomar or external referee, priority, preprint or journal claim.
