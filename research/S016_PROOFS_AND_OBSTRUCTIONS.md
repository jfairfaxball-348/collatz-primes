# S016 — sharp affine intercept, larger uniform slope regime and global-certificate hostile audit

Date: 2026-10-15. Shortened Collatz T(n)=(3n+1)/2 for odd n and n/2 for even n. U is a finite INPUT parity word of length ell with r letters O and affine intercept B_U defined by 2^ell T^ell(n)=3^r n+B_U on its exact parity cylinder. Every prefix overcritical means 3^(#O(V))>2^|V| for EVERY nonempty initial V. A first *coefficient* crossing is NOT itself the first actual descent. Universal positive/composite Collatz and Terras coefficient-stopping time (CST) are OPEN. Originality UNESTABLISHED.

## Entry and independent baseline
GitHub main at entry 84a50048934ab5742ab76517e223267ddd44bc37; actual tree e1823bff883c4cfc77bc4f8d20ebd79aedf5cfc1; ordered parents 8dc1592d6429d717a89f07edcb0476acb6afe718 and 8dc7d81a22c19a4fb4fd3b1dc88a52e5f3d38b76. Open PRs [] ; rulesets []; main protection endpoint 403 (UNOBSERVED). Latest preceding main GitHub Actions run 38757992468 job 116501433066 completed SUCCESS; independently observed each Unit tests, Finite parity and orbit sanity, Recreate finite residue stream and cross-check original manifest SUCCESS. This PRECEDES S016 and proves nothing about NEW S016 code. S015 Matveev source and algebra independently rechecked against actual primary PDF §2 p1219; see sources section below.

## CP-0060 — PROVED_INTERNAL elementary: exact SHARP fixed-(ell,r) affine-intercept extrema
For ALL ell>=1 and 1<=r<=ell, and ALL U of length ell with exactly r O letters,
  3^r-2^r <= B_U <= 2^(ell-r)(3^r-2^r).
The bounds are best possible, simultaneously across the indicated class: equality at LEFT for U=O^r E^(ell-r), and RIGHT for U=E^(ell-r) O^r. For ell=r both endpoints coincide. This strictly sharpens CP-0058, which did not exploit distinct O positions.

**Proof.** With O at zero-based positions 0<=i_1<...<i_r<=ell-1, the recurrence B_empty=0; append E: B unchanged; append O at position i: B becomes 3B+2^i gives
  B_U=sum_{j=1}^r 2^(i_j)3^(r-j).
Order forces j-1 <= i_j <= ell-r+j-1. All coefficients positive, hence
  sum_{j=1}^r 2^(j-1)3^(r-j) <= B_U <= 2^(ell-r)sum_{j=1}^r 2^(j-1)3^(r-j).
The sum is 3^r-2^r (geometric sum). Setting all positions simultaneously to their lower, respectively upper, bounds produces the specified words. QED.

Crucially with Z=B_U/2^ell, we therefore have the EXACT universal bound
  0<=Z<=(3/2)^r-1, so A=1+Z <= (3/2)^r,
independently of ell, of parity-block count, and of any overcritical hypothesis. The previous S015 Z<3^r lost an exponential factor 2^r.

## CP-0061 — PROVED_INTERNAL using SOURCE_STATED Matveev 2000: uniform r/d<ln2/ln(3/2) all-lifts TRUE first-crossing strict descent

Fix ANY real rho with 0<rho<rho_star=ln(2)/ln(3/2) (approximately 1.7095). Define epsilon=ln(2)-rho*ln(3/2)>0 and C=10^10. Let
  D_rho=ceil(4(C+10)/epsilon)^2
(an integer, much greater than 256). For EVERY integer d>=D_rho and EVERY nonempty parity word U, INCLUDING U VARYING ARBITRARILY with d, with ell=|U|, r=#O(U)>=1, every nonempty prefix overcritical, and r<=rho*d, define
  m=r+d; j=bit_length(3^m); b=j-ell-d; W=U O^d E^b.
Then b>=1, W's UNIQUE positive parity cylinder has its TRUE FIRST coefficient crossing at step j, EVERY positive n in this cylinder satisfies T^j(n)<n, and infinitely many such n are composite. This is a sufficient cylinder theorem, NOT a global coverage statement.

**Detailed proof.** From all-prefix overcritical, 3^r>2^ell and every initial coefficient >1. O^d maintains overcriticality, and because ell+d < log_2(3^m), b=j-ell-d>=1. At every earlier prefix of final E^b, number of O letters is m and its length <=j-1, with 2^(j-1)<3^m; j is the first crossing since 3^m<2^j.

For an actual word-realising n, write T^ell(n)=2^d h-1 with integer h>=1 (necessary and sufficient for the d subsequent O inputs, up to suffix congruences). The affine prefix gives
  n=2^ell(2^d h-1-Z)/3^r >= 2^ell(2^d-1-Z)/3^r.
The complete intercept is B_W=3^d(B_U+2^ell)-2^(ell+d), so writing delta=2^j/3^m-1 in (0,1), the exact endpoint inequality T^j(n)<n follows from
  delta*(2^d-1-Z)>1+Z. (*)
Indeed multiply the endpoint condition (2^j-3^m)n>B_W by 3^(-m), substitute the lower bound for n, and simplify. With A=1+Z<=(3/2)^r from CP-0060, (*) follows if delta*(2^d-A)>A, which is implied by delta*2^d>2A, since delta<1.

**PRIMARY-SOURCE imported input:** Matveev (2000), Corollary 2.3 §2, applied to nonzero linear form L=j ln2-m ln3>0 with (alpha1,alpha2)=(2,3), K=Q degree 1, n=2, A1=ln2,A2=ln3, B<=2m, gives
  ln|L|> -2^32(ln2)(ln3)(1+ln(2m)) > -C(1+ln(4m)).
Since delta=e^L-1>L, ln(delta)>-C(1+ln(4m)). The *entire 53-page Matveev proof* was not rederived here.

Now m<= (1+rho)d<3d, so for d>=256, ln(4m)<ln(12d)<=sqrt(d)=X. The latter inequality follows at d=256 (ln3072<16) and by derivative 1/(2sqrt d)>1/d for d>4. Thus
  ln(delta*2^d/A) >= ln(delta)+d ln2-r ln(3/2)
                    > epsilon*d-C(1+X).
By d>=D_rho, X>=4(C+10)/epsilon, so epsilon*X^2 >= 4(C+10)X > C(1+X)+ln2. Therefore delta*2^d/A>2, establishing (*) and strict descent for EVERY lift, including least lift. The complete parity cylinder exists uniquely modulo 2^j (the parity-vector bijection; odd invertibility of 3^m mod 2^j) and is the positive class n0+q2^j, q>=0. Coprimality with 3 permits infinitely many n divisible by 3 and >3; they are composite. QED.

**Substantive strengthening:** rho=1 gives epsilon=ln(4/3)>1/4 and simpler effective D_1=[16(C+10)]^2, improving S015's r<=d/2, D_0=[64(C+10)]^2. For U_k=(OOOE)^k and d=2k (r=3k=(3/2)d), this proves an unbounded alternating-block family for all k with 2k>=D_(3/2). The older U_k,d=6k special case is subsumed. Five isolated S016 exact tests include k=1..31 with d=2k,3k,6k and least/q=1,2,7 lifts; those finite cases are not the proof of the infinite result.

**Coverage remains NONEXHAUSTIVE and quantitatively thin near the origin.** Because d>=D_rho implies delta*2^d>2A and delta<1, 2^d>2A. Since ell>=r,
 n >=2^ell(2^d-A)/3^r >2^(d-1)*(2/3)^r >=(1/2)*exp(epsilon*d).
Hence NONE of the finitely many positive integers n<exp(epsilon*D_rho)/2 is covered by this large-d regime. In particular no entire positive residue class (mod 48 or ANY modulus) is covered; 7/15/27/31/39/43 are excluded. This is a lower-bound/noncoverage theorem, NOT a claim about the natural density of the whole union or failure of smaller-d certificates.

**Sharp boundary of THIS sufficient-inequality argument:** choose U=O^(2d), r=2d, ell=2d, every prefix overcritical. Here A=(3/2)^(2d)=(9/4)^d>2^d=(8/4)^d for all d>=1; as delta<1, delta*2^d>2A is IMPOSSIBLE. The failure is the method's exponential budget, NOT an actual first-crossing endpoint counterexample. In finite exact checks these particular cylinders still strictly descend. One must NOT claim a refutation of rho>=rho_star actual descent.

## CP-0062 — PROVED_INTERNAL elementary: same-valuation expanding SINGLE completed odd-run renewal
For EVERY integer k>=0 put n_k=64k+59 (odd). The exact initial parity word is OOE and
  n_k -> 96k+89 -> 144k+134 -> 72k+67 = n'_k,
with n'_k-n_k=8k+8>0 and
  v2(n_k+1)=v2(64k+60)=2=v2(72k+68)=v2(n'_k+1).
For k≡1 (mod3), n_k is a multiple of 3 greater than 3, hence infinitely many COMPOSITE such starts. All equations follow by direct T substitution; the two displayed n+1 are 4 times odd integers (16k+15 and 18k+17). Thus ANY proposed potential Phi(n,v2(n+1)) strictly increasing in n at fixed valuation 2 CANNOT strictly decrease on EVERY completed odd-run renewal. This independently strengthens the previously observed 11-step same-v2 obstruction CP-0041. It does NOT preclude a multi-renewal potential, history-dependent rank, or eventual descent. The n=59 witness expands to67 in this OOE renewal.

## CP-0063 — PROVED_INTERNAL elementary but only a limitation: reverse-basin mod3 rigidity
The complete positive one-step reverse predecessors of y>=1 are 2y always, plus x=(2y-1)/3 when y≡2 mod3; the latter is positive odd and T(x)=y. If y≡0 mod3, all reverse descendants from y are exactly {2^k y:k>=0}, because each is 0 mod3 and has NO odd reverse predecessor. Thus a reverse-branching algorithm started at a multiple of3 cannot branch or greedily choose a smaller precursor, and y=3 exhibits this infinite doubling ray. This does NOT prevent 3 from lying in the reverse basin of 1: 1->2->4->8->5->3 is a valid reverse route. A proof that reverse traversal from1 contains EVERY n is exactly the full Collatz claim; no independent completeness lemma is available.

## Target-A two candidate certificates and hostile conclusions
(1) FORWARD: for odd n=2^h u-1, h=v2(n+1)>=1 and u odd, T^h(n)=3^h u-1 even. Put t=v2(3^h u-1)>=1, compressed next odd n'=(3^h u-1)/2^t. This is an exact computable **single** checkpoint, but if one claims a strictly decreasing size+v2 rank at EVERY such checkpoint, CP-0062's 64k+59 family refutes it. A scheme permitted to wait arbitrary later checkpoints is not refuted; proving universal finite exit would prove Collatz and remains OPEN.
(2) INVERSE: exact predecessor rule just proved, enumerate the rooted reverse basin at1 in finite breadth-first stages; membership is a finite forward-to1 certificate. But the claim every positive integer appears has NO proof, and greedy smaller-predecessor rule is false at y≡0,1 mod3. Adding factorisation does not make Collatz multiplicative. Hence the second candidate is INCOMPLETE, not a theorem of global reachability.

All 71 exceptional residues among 512 starts z≡11 mod16 modulo8192 and 5041 possible ordered exceptional 13-block transitions, arbitrary finite compatible paths, expanding 393243+524288k 11-step returns and forced 2^H u-1 O towers remain legitimate controls, not a single infinite positive divergent orbit. Exact finite independent tests rechecked those states, with witnesses first descent 7:7->5, 15:7->10, 27:59->23, 31:56->23, 39:8->38, 43:5->37, 91:45->61, 155:40->122, 251:27->244. They do NOT close all six r mod48 exceptional classes.

## Sources, validation and limits
- Matveev (2000), Izvestiya: Mathematics 64:6 1217–1269, ORIGINAL English 53-page PDF: https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng . For this session ORIGINAL §2 printed p1219 Cor.2.3 and (2.6) re-read against the PDF page image; constants 2^32, D=1, Omega=ln2 ln3 and delta=e^L-1 conversion CHECKED. Entire 53-page proof NOT independently reproduced. Imported bound remains SOURCE_STATED.
- R. P. Steiner (1978), Congressus Numerantium XX pp553–559 primary seven pages not acquired after targeted lookup. Lagarias bibliography gives INDIRECT attribution; no direct original content claim.
- Terras 1976 Acta Arith. 30 pp241–252 and Simons/de Weger 2005 Acta Arith. 117 pp51–70 verified publisher metadata; Rozier/Terracol 2026 Discrete Math. 349 article115167 primary abstract explicitly leaves Terras CST conjectural, Niu May2026 arXiv:2605.13886 explicitly disclaims total Collatz. Priority of CP-0060–0063 remains UNCHECKED.
- Isolated Python 3 local S016 math script FIVE PASS, SHA256 b6d3efaf3dde18d66cfa88a16371e2e73137214bc4a7d72a7ad8cea934b5cc43; isolated and checked-in test implementations address the same statements, but byte-identical script correspondence requires comparing committed bytes. New hosted full suite and S000/S001/S003 checks must be independently observed on the ACTUAL S016 PR head; do not infer from pre-entry run 38757992468.
- NO Collatz/composite universal theorem, Terras CST proof, external novelty validation, formal Lean, Palomar, preprint or publication.
