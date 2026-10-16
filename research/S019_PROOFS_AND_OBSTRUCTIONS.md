# S019 — periodic overcritical parity blocks: exact 2-adic divisibility, constant affine budget, and all-d first-crossing strict descent

Date: 2026-10-16. T(n)=(3n+1)/2 for odd input, n/2 for even. O/E are INPUT parity letters. For any word V with s O inputs and length L, 2^L T^L(n)=3^s n+B_V on the exact positive parity cylinder, with B_V computed by B_empty=0, B_{VE}=B_V, B_{VO}=3B_V+2^L. A finite word P is *overcritical* if every NONEMPTY prefix V satisfies 3^(#O(V))>2^|V|. A first coefficient crossing at j is the first index 3^(#O(prefix))<2^j, not automatically a numerical descent.

## Live entry evidence
Read actual live main ref e35857c7b6fd5054598998f009c39cd0edb4d3a6, actual underlying Git tree 0fdb82ac1ebe3ba56d0ff89d4a5ea5bcd9689040, ordered parents [ef5de1e4244179a2884c60261728997ed64ec0ed,093f6732c822c503d3bf211366f90a903bb883c5]. Open PRs [] and rulesets []; protection API returned HTTP403 FORBIDDEN => UNKNOWN, not free of protection. Most recent PRE-S019 merged-main run38813824079/job116693394879 individually observed COMPLETED SUCCESS in Unit tests, Finite parity and orbit sanity, Recreate finite residue stream and cross-check original manifest. This is NOT evidence for any new S019 code.

## CP-0068 — PROVED_INTERNAL exact elementary periodic-block arithmetic

Let P be ANY nonempty parity word, length ell>=1, with r=#O(P)>=1, and set A=3^r, Q=2^ell, B=B_P. For EVERY k>=1, and EVERY positive integer n whose first ell*k input parities are P repeated k times, the following are exact:
    Q^k*T^(ell*k)(n) = A^k*n + B*(A^k-Q^k)/(A-Q),                    (1)
    Q^k divides ((A-Q)*n+B).                                        (2)
In (1), the displayed quotient is an INTEGER because A-Q divides A^k-Q^k. No overcritical hypothesis is needed for (1)-(2), only A-Q!=0 (automatic since odd A and even Q). Indeed F=A-Q is ODD and invertible modulo Q^k; the P^k prefix class is precisely
    n == -B*F^(-1) (mod Q^k).                                      (3)

**Proof (no source theorem).** The single P affine map is x -> (A*x+B)/Q. Its formal k-fold iterate, multiplied by Q^k, is A^k*n+B sum_{i=0}^{k-1} A^(k-1-i)Q^i = A^k*n+B(A^k-Q^k)/(A-Q). Multiply by F to obtain
    F Q^k T^(ell*k)(n) = A^k (F*n+B) - B Q^k.
The left and last terms are divisible by Q^k, so Q^k | A^k(F*n+B). gcd(A,Q)=1 yields (2), and invertibility of F gives (3). This algebra is for actual P^k cylinder inputs, not a claim that arbitrary starting numbers follow P^k.

If A>Q (F>0), B>0 and n>=1 imply F*n+B positive. Thus
    F*n+B >= Q^k, and n >= (Q^k-B)/F.                               (4)
For EVERY fixed positive n, any P^k repetition is limited by Q^k<=F*n+B; in particular an integer cannot follow a FIXED overcritical P infinitely often consecutively. Equivalently the infinite periodic parity vector P^infinity corresponds 2-adically to rational -B/F (negative as an ordinary rational). This finite-repeat obstruction is entirely elementary, NOT universal Collatz descent: infinitely changing nonperiodic parity words are not constrained by ONE fixed P.

## CP-0069 — PROVED_INTERNAL scoped all-d first-coefficient-crossing strict descent; quantitative part imports SOURCE_STATED Matveev 2000

Fix ONCE AND FOR ALL any finite overcritical block P with ell=|P|, r=#O(P)>=1 and e=#E(P)>=1. Put A=3^r,Q=2^ell,B=B_P,F=A-Q>0. Then THERE EXISTS an explicit effectively computable integer K(P) such that for ALL integers k>=K(P) and ALL d>=1, define
    U=P^k, m=kr+d, j=bit_length(3^m), b=j-ell*k-d,
    W=P^k O^d E^b.
Then b>=1, W has FIRST coefficient crossing exactly at j, and EVERY positive n in its unique parity cylinder strictly descends T^j(n)<n. Infinitely many such n are composite. In particular the initial O-run of U can be BOUNDED independently of k, its number of even blocks grows without bound and r(U)/d is UNBOUNDED for d=1. This genuinely escapes S018's a-versus-e Matveev hypothesis and S016's bounded r/d, but is still a THIN fixed-block family, not all-U/all-positive convergence.

**Constant intercept budget, stronger than S018's growing 2^(ke):** For U=P^k, its exact affine intercept from (1) is B_U=B(A^k-Q^k)/F. Thus
    H_k=(B_U+Q^k)/A^k
       = B/F+(1-B/F)(Q/A)^k.                                      (5)
Because 0<Q/A<1, H_k lies between 1 and B/F, so H_k<=M=max(1,B/F). For the appended odd run then even tail (same general identity used in S018),
    B_W/3^m = H_k - Q^k 2^d/3^m < M.                                (6)
Writing D=2^j-3^m>0, delta=D/3^m, and using (4), every cylinder n satisfies
    delta*n >=D*(Q^k-B)/(3^m F).
Consequently the fully ELEMENTARY explicitly checkable certificate
    D*(Q^k-B) > 3^m*max(F,B)                                      (7)
implies delta*n>M>B_W/3^m, hence D*n>B_W and T^j(n)<n for ALL lifts, INCLUDING the least one. Failed (7) is just a failed sufficient bound, NOT an overshoot. A usable certificate can be computed without modular inverse or calculating n0.

**All k large, ALL d proof via SOURCE_STATED Matveev and independent prior S016:**
For all m>=1 the directly inspected Matveev (2000) §2 Corollary 2.3 implies, with C=10^10,
    ln delta > -C(1+ln(4m)), delta=2^bitlength(3^m)/3^m-1.       (8)
This uses L=j ln2-m ln3>0 and delta=e^L-1>L, NOT direct Matveev bound on delta. Let H=ln(2F)+C(1+ln(8r)); let K_B be the least positive integer with Q^K_B>=2B. Fix D0=[16(C+10)]^2 and the EFFECTIVE threshold
    K(P)=max{D0, K_B, ceil[(4(H+C+1)/(ell ln2))^2]}.             (9)
Every quantity is well-defined; finite exact integer search computes K_B.

For k>=K(P), Q^k>=2B and n>=(Q^k-B)/F>=Q^k/(2F). There are two cases:
(i) 1<=d<=kr gives m=kr+d<=2kr. For k>=1, ln k<=sqrt k (check elementary calculus). Thus ln(4m)<=ln(8r)+sqrt k. With X=sqrt k>=4(H+C+1)/(ell ln2) and X>=1, 
    k ell ln2 >= 4(H+C+1)X > H+C X.
Therefore
    ln(delta*n/M) >
       k ell ln2 - ln(2F M)- C[1+ln(8r)+sqrt k].
Here 2F M=2 max(F,B) MAY BE LARGER THAN 2F: for correct threshold (9), replace H with H'=ln(2 max(F,B))+C(1+ln(8r)), and K(P) with the formula using H' everywhere. With that CORRECTED H', the RHS >0, so delta*n>M and strict descent.
(ii) d>kr: write R=kr=#O(U), so R<=d and d>=kr>=K(P)>=D0. The ALREADY PROVED S016 CP-0061 (rho=1) directly proves first-crossing all-lift strict descent for all such U, regardless of number of E-blocks, using the same published Matveev source. No circular inference about arbitrary Collatz.

For clarity, the EFFECTIVE K(P) asserted in this theorem is obtained by formula (9) with H replaced throughout by H'=ln(2 max(F,B))+C(1+ln(8r)); the initial H form is NOT the operative value. Equivalently set
    H_P=ln(2 max(F,B))+C(1+ln(8r)),
    K(P)=max{D0,K_B,ceil[(4(H_P+C+1)/(ell ln2))^2]}.             (10)
Then the displayed inequalities hold exactly.

**First crossing and existence:** P overcritical at each of its own prefixes, and A/Q>1 per full block; hence EVERY prefix of U=P^k is overcritical. Appending O^d preserves that property. Since 3^m>2^(ell*k+d), b>=1. No shorter final E-prefix can cross, because for any prior j'<j we have 2^j'<=2^(j-1)<3^m. The full W has its unique positive 2^j parity residue; 2^j coprime to3 yields infinitely many composite (divisible by3, >3) representatives. S018 exact affine first-crossing sign test applies.

**Example:** P=OOOE has (A,Q,B,F)=(27,16,19,11), initial O-run 3. For ANY k, a P^k member has 16^k|(11n+19), hence n>=(16^k-19)/11. For k=2,d=1, the exact first-cross W=OOOEOOOEOEEE (j=12), n0=231, T^12(231)=124. k=3,d=1 yields n0=17127 and endpoint 15433. k growing, d=1: R/d=3k, e=k, so neither S016 bounded-R/d nor S018 growing-leading-a corollaries give this uniform conclusion. The Matveev K(P) is astronomically overconservative.

## Universal-certificate hostile pressure — OPEN, not a proof
CP-0068 bounds consecutive identical repetitions of a FIXED overcritical P, but it does NOT bound an infinite aperiodic sequence of changing blocks. Even a finite alphabet of possible P does not force a repeated P of unbounded consecutive length; alternating patterns are a countermodel to that combinatorial inference. A total all-n integer-dependent descent/exit rank would need an independent termination proof, absent here. Checkpoints 71 of512 z=11mod16 exceptional inputs through13 and all 5041 ordered finite-state pairs remain; every finite compatible exceptional path may have composite lifts but not one infinite divergent positive orbit. The finite tested 27,43,91,155,251, hard 7,15,27,31,39,43 mod48, expanding 393243+524288k and 64k+59->72k+67 renewal, and 2^H u-1 forced-O composites defeat fixed-horizon and naive monotone ranks. Composite-only goal is equivalent to full positive Collatz, so periodic cylinder selection cannot be misrepresented as exhaustion.

## Reproducibility and limitations
Fresh independent scratch /mnt/data/s019/independent_s019.py SHA256 8c0cc2ce7f342e5d9a00be9429136b8b4532fca347e1d88a506a9635031bc26d; output /mnt/data/s019/finite_output.json SHA256 d7993b56f0b47d6e7a8bb54ecbfa9229192913e3417d427f2aae348a5d835bf0. Python 3 exact ints: 143 overcritical P with 2<=ell<=10 and E present, k1..12, d in{1,2,3,5,9}, total 8580 exact first-cross cylinders. All n0 canonical trajectories and Q^k divisibility PASS; exact inequality (7) independently passes in 7854/8580 (remaining 726 still descend). Local tests/test_s019_math.py source SHA256 556e8e39fb94b45b51b508d831d70e18382bc9f79db8833ebaf5b391a4c55889: 6 tests PASS standalone; checked-in copy should independently be validated by actual hosted workflow. Rechecked 71/512 exceptional first-13 no-descent starts; arithmetic samples 393243+524288k k0,1,3,9 all expand 11 steps; n=64k+59 k0,1,4,10 grows after OOE. Finite bounds and tests CANNOT establish new universal theorems.

## Source and novelty
ORIGINAL Matveev (2000) 53-page English PDF https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng (printed p1219, PDF page3) DIRECTLY opened and visually inspected in S019: actual Cor.2.3 is bound on ln|L|, C1(2,1)<=2^32; conversion delta=e^L-1>L, C=10^10 as in CP-0056. The whole deep proof NOT rederived, and (8) remains SOURCE_STATED. Terras 1976 publisher https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/30/3/101028/a-stopping-time-problem-on-the-positive-integers and Rozier/Terracol October2026 https://www.sciencedirect.com/science/article/abs/pii/S0012365X26001913 explicitly retain coefficient-stopping-time conjecture OPEN. Bernstein–Lagarias (1996), *The 3x+1 Conjugacy Map*, Canadian J Math 48 1154–1169 https://geodesic.mathdoc.fr/articles/10.4153/CJM-1996-060-x/ is DIRECT relevant PRIOR ART for rational 2-adic periodic parity coding; no claim these elementary identities are original. Steiner 1978 original Congr. Numer. XX pp553–559 still unacquired: Lagarias annotated bibliography INDIRECT only. Simons/de Weger 2005 only finite cycle results, Tong Niu May2026 explicit no global proof. No exhaustive novelty determination; NOT READY for paper/Lean/Palomar claim. Global Collatz and Terras CST OPEN.
