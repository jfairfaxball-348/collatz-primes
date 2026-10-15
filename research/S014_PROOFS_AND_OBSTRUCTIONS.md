# S014 — arbitrary-prefix first-crossing descent and effective Matveev thresholds

**15 October 2026.** Shortened Collatz T(n)=(3n+1)/2 on odd n and n/2 on even n. A parity word W of length j with r odd input letters gives T^j(n)=(3^r n+B_W)/2^j, B_W>=0, on its unique residue cylinder modulo 2^j. "First coefficient crossing" means the least i>=1 with 3^(#O in first i inputs)<2^i, NOT a stopping time assertion. Results below use an imported, PUBLISHED SECONDARY statement of Matveev's inequality; original Matveev 2000 full text was NOT acquired. No global convergence or Terras CST proof; novelty NOT established.

## CP-0053 — PROVED_INTERNAL relative to Matveev SOURCE_STATED; fully explicit and variable (a,c)

Put C0=10^12. For ANY positive a,c with 3^a>2^(a+c), define the integer threshold
  m0(a,c)=[4(C0+a+c+10)]^2.
For EVERY m>=m0(a,c), set j=bit_length(3^m), d=m-a, b=j-m-c. Then d,b>=1, the word O^a E^c O^d E^b has its TRUE first coefficient crossing at j, and EVERY positive member of its exact parity cylinder strictly drops below its start at j; infinitely many are composite. Unlike CP-0050, the bound is explicit and the quantifier also allows a,c to vary with m subject to this inequality.

**Proof.** Theorem 3 in the 2021 *Research in Number Theory* article (published restatement of Matveev) states for nonzero Lambda=product gamma_i^b_i -1:
 log|Lambda| > -3*30^(t+4)*(t+1)^5.5*D^2*(1+log D)*(1+log(tB))*product A_i.
For gamma=(2,3), b=(j,-m), t=2, D=1, B=2m, A=(ln2,ln3), the exact constant C=3*30^6*3^5.5*(ln2)*(ln3)<C0. 2^j/3^m-1=delta>0, and j<=2m, so
 log delta > -C0*(1+ln(4m)).
The statement is the one in that PUBLISHED SECONDARY paper, not independently verified against Matveev's primary original.

S013's exact carry identity gives t0>=[2^(m-a+c)-(2^c-1)]/3^a >=2^(m-a+c-1)/3^a (d=m-a>=1). Thus
 log(delta*t0) > (m-a+c-1)ln2-a ln3-C0*(1+ln(4m))
 >= m/2-(5a/2)-C0*(1+sqrt(m))
for m>=256, since ln2>1/2, ln3<2, c>=1 and ln(4m)<=sqrt m for m>=256. Write S=sqrt m>=4(C0+a+c+10). Then m/2=S²/2 >=2(C0+a+c+10)S > (5a/2)+C0*(1+S)+ln2; hence delta*t0>2. [This uses elementary monotonicity of ln(4m)/sqrt m for m>=256.] For this grammar M/P=(1+delta)/2^a<2^(1-a)<=1 and K/P=(2^c-1)/3^a-2^(c-a)*(2/3)^m <2^(-a)<=1/2. Consequently delta*t0>2> M/P+K/P, so (2^j-P)*t0>M+K. S013's exact drop formula gives strict drop for minimal t0 and all larger lifts. Also d>=1 and b=j-m-c>m/2-c>=1 because log_2 3>3/2, m>>2(c+1); 3^a>2^(a+c) prevents any earlier crossing and the final E run crosses at exactly j. Odd coprimality of the cylinder modulus 2^j with 3 supplies infinitely many composite lifts. QED. The bound is intentionally astronomical (m0(2,1)≈1.6*10^25), not a feasible testing range.

Uniform-rate corollary (PROVED_INTERNAL relative to the same imported bound): fix 0<rho<ln2/(ln2+ln3). For all sufficiently large m, uniformly for every admissible a,c with 1<=a<=rho*m and 3^a>2^(a+c), the above two-run word descends. Indeed c<a(log_2(3)-1)<a, hence b>=1 for large m; the exact log estimate is at least [ln2-rho(ln2+ln3)]m -O(log m), which tends to +infinity uniformly. The size of "sufficiently large" depends on rho; the explicit m0(a,c) above is a different, concrete sufficient condition.

## CP-0054 — PROVED_INTERNAL relative to Matveev: ANY fixed overcritical parity prefix

Fix ANY nonempty finite parity word U, length ell, r>=1 odd letters, with EVERY nonempty prefix V satisfying 3^(#O(V))>2^|V|. Let B=B_U from the exact affine recursion. For EVERY sufficiently large integer d, set m=r+d, j=bit_length(3^m), b=j-ell-d. Then b>=1 and **EVERY positive starting integer in the cylinder of W_d=U O^d E^b strictly decreases at its GENUINE first coefficient crossing j**. This holds for arbitrarily many alternating O/E blocks in U (not merely two-run grammar); there are infinitely many composite starting integers in EACH such cylinder.

**Complete proof.** For the actual W_d cylinder T^ell(n)=(3^r n+B)/2^ell. At the beginning of its forced O^d segment, necessarily T^ell(n)=2^d h-1, h>=1, hence for EVERY positive cylinder start
 n >= [2^ell(2^d-1)-B]/3^r.
After that O^d and the b final Es,
 2^j T^j(n)=3^(r+d)*n + 3^d*(B+2^ell)-2^(ell+d).
Thus strict drop is exactly
 delta*n > (B+2^ell)/3^r -2^(ell+d)/3^m,
where delta=2^j/3^m-1>0. For d sufficiently large, 2^ell(2^d-1)-B >= 2^(ell+d-1). By the published Matveev inequality applied with exponents (j,-m), delta>exp[-C0(1+ln(4m))]. Therefore for EVERY such n,
 delta*n >= exp[-C0(1+ln(4m))]*2^(ell+d-1)/3^r.
Its ratio to (B+2^ell)/3^r tends to infinity, since d ln2 outruns C0 ln(4(r+d)) and B,ell,r are FIXED. Choose d beyond that effective threshold so the ratio exceeds 1: then the exact endpoint strictly drops (even after discarding the helpful negative intercept). The first crossing is exactly j: by hypothesis none within U, O^d strictly increases every slope, and all prefinal-E checkpoints have 3^m>2^(j-1)>=2^i while 3^m<2^j. b>=1 eventually because (log_2 3-1)d grows. Existence of the full parity cylinder is unconditional: finite parity words label a unique residue class modulo 2^j via the invertible odd leading coefficient 3^m; all positive lifts realise precisely W_d. Since modulus 2^j is coprime to3, infinitely many lifts have n≡0 mod3 and n>3, hence composite. QED.

**Reproducible gross effective d threshold (not optimal).** Define H=B+2^ell, L=ceil(log_2 H) (integer H.bit_length() is a safe upper bound), and S=C0+ell+r+H.bit_length()+10. Take d0=[8S]^2. For d>=d0: d>=r, m=r+d<=2d, ln(4m)<=sqrt m<=2sqrt d; 2^ell(2^d-1)-B>=2^(ell+d-1); (ell+d-1)ln2>d/2; and d/2>C0*(1+2sqrt d)+ln H. Therefore the preceding strict inequality holds uniformly for ALL d>=d0. It is vast, explicit, computable and does NOT cover U depending arbitrarily on d.

**New concrete genuinely multi-run example.** U=OOOEOOEOOE (ell=10,r=7,B=2899) has THREE E blocks, each nonempty prefix slope >1. At d=12, m=19, b=9, j=31: least positive n=1633475239 -> T^31(n)=884069749, strict drop 749405490; d=19 gives (j,b,n,T^j(n))=(42,13,2267417467559,1310461579885). These are FINITE_TEST examples, not a proof that 12 is sufficient for ALL U/d. Four prefixes U=OOOE, OOOOEOO, OOOEOOEOOE, OOOOEOOOEOOEOOE tested for d=6..100: 380 exact cylinders with full prefix parity, j-first-crossing, least positive and next lifts strict descent, each PASS. CP-0054 supplies the infinite theorem conditional on the imported published inequality.

## CP-0055 — PROVED_INTERNAL boundary and unresolved renewal

The hypothesis that EVERY prefix of U remains above coefficient1 cannot simply be removed. U=OE already crosses at step 2 (3/4<1). For W=OE O^40 E^b with b chosen from bit_length(3^41), the first crossing is step2, NOT the asserted long final j. This is an exact COUNTERPARAMETER to the overgeneralisation "for EVERY fixed U the first crossing of U O^d E^b occurs only after O^d".

Two independent all-integer schemes were attacked, with no proved totality: (A) run-compressed forward exact affine descent, skip O-run of length v2(n+1), skip the following E-run v2(3^h (n+1)/2^h-1), and test x<n; every micro-run terminates but the count of mixed runs is unbounded without the unknown universal descent lemma; the 393243+524288k ->1259803+1679616k expanding same-v2 11-step return refutes using size plus that valuation as a monotone rank on each prescribed return. (B) bounded reverse-basin enumeration starting from 1 using edges y->2y and y->(2y-1)/3 when y≡2 mod3 and resulting predecessor positive odd, with finite depth/size cutoff; membership gives an actual forward path to1, but no finite bound covering every n has been proved. In particular y=3 has NO odd immediate reverse predecessor (mod3 obstruction) and its even predecessor6 is larger, refuting a one-step strictly decreasing reverse-predecessor blanket lemma. Both are decidable sufficient certificates for particular n under finite resource bounds, NOT a universally terminating proof.

Exact hostile finite first drops preserved: 7->5 at7; 15->10 at7; 27->23 at59; 31->23 at56; 39->38 at8; 43->37 at5; 91->61 at45; 155->122 at40; 251->244 at27; 393243->269366 at37; 917531->588548 at26. Same-v2 expansion for k=0,1,3,9, and composite 2^H u-1 forced-O towers for H=6,12,24,48 verified independently. 71 exceptional states/5041 finite possible edges remain, and all six r=7/15/27/31/39/43 mod48 least-counterexample classes globally unresolved. The exact missing lemma U-S014 is a **noncircular terminating and exhaustive positive-integer certificate** proving every n>=2 attains a lower iterate, including those missing all explicitly described parity-cylinder unions. Infinitely many certified composite progressions for every fixed U/d do NOT imply this.

## Primary sources and proof classification
- Matveev E. M., *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, Izvestiya: Mathematics 64 (2000), DOI 10.1070/IM2000V064N06ABEH000314: bibliographic metadata checked (Matveev original full paper NOT directly read). The precise C inequality above is from an accessible **PUBLISHED SECONDARY RESTATEMENT**, Theorem 3 in *Integers representable as differences of linear recurrence sequences*, Research in Number Theory (2021), https://link.springer.com/article/10.1007/s40993-021-00252-2 . It states the exponent and logarithm of |product-1| and tB exactly as transcribed. No unverified primary inspection claim.
- Steiner R. P. (1978), *A Theorem on the Syracuse Problem*, Congressus Numerantium XX, pp553–559; original seven-page text still NOT obtained. Lagarias' annotated bibliography https://citeseerx.ist.psu.edu/document?doi=23fc93711a7dbf9b3441a5c957a8737538489405&repid=rep1&type=pdf is INDIRECT.
- Terras R. (1976), *A stopping time problem on the positive integers*, Acta Arithmetica 30, 241–252, DOI 10.4064/aa-30-3-241-252; Rozier–Terracol (October 2026), *Paradoxical behavior in Collatz sequences*, Discrete Mathematics 349(10) 115167, https://www.sciencedirect.com/science/article/pii/S0012365X26001913 explicitly distinguishes later paradoxes and names Terras CST as open; Simons–de Weger (2005) bounded-m-cycle results not global; Niu (May 2026) https://arxiv.org/abs/2605.13886 explicitly makes NO claim toward Collatz/CST. Full novelty/priority survey not completed.

No primary Matveev original theorem proof read, independent referee, Lean/Palomar, arXiv or journal. Global composite/positive Collatz and Terras CST REMAIN OPEN.
