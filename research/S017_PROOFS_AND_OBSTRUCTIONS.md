# S017 — ratio-free long two-run first coefficient crossing, exact arithmetic admission, and the universal exit gap

Date: 2026-10-15. T(n)=(3n+1)/2 (odd) and n/2 (even). O/E encode input parities. For a word W of length j with m odd letters, 2^j T^j(n)=3^m n+B_W on its exact positive parity cylinder; a *first coefficient crossing* means 3^m<2^j, while every earlier prefix has coefficient >1. This is NOT a proof that every positive integer has such a crossing.

## Entry and provenance
Live main at entry e183c3a2133b6154700c0cb989318865a1387b80, actual Git tree 18cc76572a4e9aee1e73d94a900d7adbda3cf991 and ordered parents d985e26f40befdd5f28332fffcffd395e9a5c620, 975ec8bcb2d1f25482b2f815d8fc5580c669c3b6. Open PRs [] and rulesets []; main protection API 403 (UNKNOWN). Latest pre-S017 hosted main run 38768747419/job116538721403 completed SUCCESS with EACH original Unit tests, Finite parity and orbit sanity, and Recreate finite residue stream and cross-check original manifest step SUCCESS; the run precedes S017. No local clone (github.com DNS unavailable). No new-hosted-code outcome inferred.

## CP-0064 — PROVED_INTERNAL conditional on SOURCE_STATED Matveev 2000: RATIO-FREE two-run theorem (r,c,d all vary)

Set C=10^10 and M0=[16(C+10)]^2, an explicit integer. For EVERY triple of integers r>=1,c>=1,d>=1 satisfying the strict *overcriticality* 3^r>2^(r+c), if m=r+d>=M0, put
    j=bit_length(3^m),   b=j-(r+c+d),   W=O^r E^c O^d E^b.
Then b>=1, the positive cylinder W exists uniquely modulo 2^j, its first coefficient crossing occurs EXACTLY at step j, and EVERY positive input n in that cylinder satisfies T^j(n)<n. The cylinder has infinitely many composite members. No bound on r/d or on c (other than overcriticality) is required. In particular r/d can tend to infinity. This is a *restricted parity-cylinder theorem*, not global Collatz or Terras CST and not a priority claim.

**First-crossing calculation.** All O prefixes are overcritical. All r initial O's followed by c E's are overcritical by 3^r>2^(r+c); therefore so is EVERY earlier prefix. Adding d O's preserves overcriticality, with final odd coefficient 3^m/2^(r+c+d)>1. Since 2^(j-1)<3^m<2^j, j>r+c+d, b>=1, and all intermediate E prefixes are likewise >1 in coefficient. Thus j is exactly the first coefficient crossing.

**Exact prefix.** Set U=O^r E^c, ell=r+c. Its affine intercept is B_U=3^r-2^r (CP-0060 exact extremum), so A=1+B_U/2^ell=[3^r+2^r(2^c-1)]/2^(r+c)<(3/2)^r. The latter uses the strict positive c and overcriticality. For any word-admissible n the d following odd inputs require T^ell(n)=2^d h-1 with integer h>=1. Because B_W=3^d(B_U+2^ell)-2^(ell+d), with delta=2^j/3^m-1 in (0,1), the exact criterion for endpoint descent is
    delta(2^d h-A)>A.                                               (1)
The congruence conditions that make W a real word can only INCREASE the minimal h beyond 1.

**External quantitative input.** The ORIGINAL English 53-page Matveev (2000), §2 Corollary 2.3 p.1219 gives ln|L|> -C1(2,1) A1 A2 ln(eB) for nonzero L=j ln2-m ln3>0, with C1(2,1)<=2^32, A1=ln2, A2=ln3, B<=2m. Since delta=e^L-1>L, we obtain
    ln delta > -10^10[1+ln(4m)].                                    (2)
This imports published deep mathematics and does not independently reprove it. For m>=256, ln(4m)<=sqrt(m); check at 256 and differentiate. Since m>=M0 and x=sqrt(m)>=16(C+10), simple algebra gives
    m/8 - C(1+sqrt(m)) > 2.                                          (3)
Also ln(4/3)>1/4 and ln2>1/4.

**Case I, r<=d.** Then d>=m/2 and r<=d, so A<=(3/2)^r. From (2) and (3),
    ln(delta 2^d/A) > d ln2-r ln(3/2)-C(1+ln(4m))
                        >= (m/2)ln(4/3)-C(1+sqrt(m))
                        > m/8-C(1+sqrt(m))>2>ln2.
Thus delta 2^d>2A. Since delta<1, this implies delta(2^d-A)>A, and hence (1) for every h>=1.

**Case II, r>d.** The first r odd inputs force n=2^r u-1 for an odd INTEGER u>=1; this is the crucial extra integer-dependent information absent from the generic S016 bound. The E^c block and next O^d imply
    2^(c+d)h = 3^r u + 2^c-1.
Substitution into (1), multiplying by 2^(r+c)/3^r, gives the EQUIVALENT exact descent inequality
    delta(2^r u-1)>1+(2/3)^r(2^c-1).                                (4)
Overcriticality 2^c<(3/2)^r forces the RHS of (4) strictly below 2. Since r>m/2 and 2^r-1>=2^(r-1), (2) and (3) yield
    ln[delta(2^r-1)] > (m/2)ln2-ln2-C(1+sqrt(m))
                           > m/8-ln2-C(1+sqrt(m))>2-ln2>ln2.
Therefore delta(2^r-1)>2, proving (4) for EVERY u>=1, hence strict descent for every positive cylinder lift. This completes the two-case proof.

**Existence and composites.** For each finite word W, odd invertibility of 3^m modulo 2^j gives one canonical residue n0=(-B_W*(3^m)^(-1)) mod2^j, in 1..2^j-1 for these O-starting words; parity-vector invertibility proves the word is realised by n0+q2^j, q>=0. Since 2^j is a unit modulo 3, one q residue modulo3 makes n divisible by3; infinitely many q give n>3 composite. Thus actual positive/composite families, not just formal words.

**NONCOVERAGE.** In Case I, from delta 2^d>2A and delta<1, n=2^ell(2^d h-A)/3^r>2^(r+c+d-1)/3^r >=(4/3)^d >=(4/3)^(m/2). In Case II, n=2^r u-1>=2^r-1 > (4/3)^(m/2)/2 (at our huge m). Consequently EVERY member of the M0-or-larger union exceeds (4/3)^(M0/2)/2. No complete positive mod48 class, no 27/43/91/155/251 or any small hard start is certified by THIS theorem. No universal exit rank follows.

**Falsification pressure.** The S016 sufficient dominance delta 2^d>2(3/2)^r fails for U=O^(2d) identically since (3/2)^(2d)>2^d, but this does NOT imply actual overshoot. CP-0064 handles prefixes with c>=1 and r/d arbitrarily large by using n=2^r u-1. It says NOTHING about unrestricted multi-E-block prefixes, lower m<M0, nor that an arbitrary input ever belongs to one of these certified cylinders.

## CP-0065 — PROVED_INTERNAL elementary: exact canonical all-lifts admission and bounded-horizon obstruction

For ANY finite parity word W of length j with m odds, affine B_W as above and D=2^j-3^m>0, let
    n0=(-B_W*(3^m)^(-1) mod 2^j), chosen in {1,...,2^j}.
Every positive word-realising n is n0+q2^j (q>=0); strict endpoint drop is EXACTLY
    D(n0+q2^j)>B_W.
Therefore the smallest admissible q for drop is max(0, floor((B_W-D*n0)/(D*2^j))+1), and the ENTIRE positive cylinder drops if and only if D*n0>B_W. This yields finite, integer-exact, computable admissibility for any proposed W; it is NOT an ALL-n coverage algorithm.

For each finite H>=1 there are infinitely many composites with an O^H prefix and no strict drop in the first H iterations: n=2^H u-1, with u odd chosen congruent to (2^H)^(-1) modulo3 (e.g. u=7 if H even and 5 if H odd), and u increased by multiples6. Indeed T^k(n)=3^k 2^(H-k)u-1>n for 1<=k<=H. All these numbers are divisible by3 and >3. Thus no finite maximum-word-length collection of first-crossing drop cylinders can cover all positive integers. A genuinely adaptive UNBOUNDED exit rule remains open; these controls do not produce a divergent orbit.

## Hostile checks and exact finite evidence — FINITE_TEST ONLY
A standalone Python3 exact-integer script (local container, not the repository checkout) with SHA256 3ce5dceb6baae591c07f9a986cc871daafc3bc80db8439b9cfac3f78dc899522 enumerated ALL r=3..25, all c>=1 with 3^r>2^(r+c), all d=1..25: 4,425 parameter triples and 17,700 q=0,1,2,7 positive lifts. Independently computed B_W and canonical residue via inverse mod2^j; simulated every bit of W and exact T^j(n)<n. ALL PASS within the stated FINITE range. Example r17,c4,d1 => j29,b7,n0=112590847,T^29(n0)=81248584. Extreme r24,c9,d1 => j40,b6,n0=503064821759,T^40(n0)=387664016024. r4,c1,d7 => j18,b6,n0=173295,T^18(n0)=117107. Enumerated exact equality extremum words and all bit-placement words through ell9; verified 64k+59 OOE expansion through k199. The committed test module independently reproduces these exact checks; equality of the local scratch source and committed module is NOT claimed.

The known 71 exceptional residues among 512 inputs z=11 mod16 (mod8192), 5041 ordered finite transitions, 393243+524288k expansion, 64k+59 ->72k+67 same-v2, 27/43/91/155/251, and ALL six 7/15/27/31/39/43 mod48 classes remain hostile controls and NOT closed. First-crossing entrance and global eventual descent remain unproved. No finite path compactness or simulation-cap inference.

## Source status and limitations
- Matveev (2000), ORIGINAL English PDF https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng ; §2 Corollary2.3 (2.6) DIRECTLY re-inspected this session (printed p1219); full 53-page proof NOT reproduced.
- Steiner (1978), Congressus Numerantium XX pp553–559 original SEVEN PAGES NOT ACQUIRED; Lagarias bibliography INDIRECT only; no source-status upgrade.
- Terras (1976), https://doi.org/10.4064/aa-30-3-241-252 ; Rozier–Terracol (Oct2026) https://www.sciencedirect.com/science/article/pii/S0012365X26001913 explicitly still calls CST conjectural; Tong Niu (May2026) https://arxiv.org/abs/2605.13886 expressly disclaims Collatz/CST; Simons–de Weger (2005) https://doi.org/10.4064/aa117-1-3 concerns bounded m-cycle questions. These do not establish priority or total convergence.
- CP-0064 original priority UNCHECKED; analytic correctness is internal algebra CONDITIONAL on SOURCE_STATED Matveev. CP-0065 elementary, no novelty claim. NO universal Collatz/composite theorem, Terras CST, Lean, Palomar, peer review or publication.
