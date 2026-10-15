# S004 — first-coefficient-crossing subfamilies, mixed-modulus barriers and valuation-jump traps

Date: 2026-10-15. Map T(n)=n/2 for even n and (3n+1)/2 for odd n; accelerated odd U(x)=(3x+1)/2^v2(3x+1). Global CP-0007 and Terras CST CP-0019 are OPEN. The statements here are internally proved elementary restrictions / obstructions and are NOT asserted original.

## CP-0023 — an infinite quantified first-crossing family (PROVED_INTERNAL, elementary)

Let a>=2 be an integer, alpha=log_2(3/2), and b=b(a)=floor(a*alpha)+1. Since alpha is irrational (otherwise 3^q=2^(p+q) for positive integers p,q), b is the unique minimal positive integer for which 2^(a+b)>3^a. Set j=a+b and D=2^j-3^a>0.

**Exact parity cylinder and first crossing:** The positive integers with shortened-T input parity word O^a E^b are exactly n=2^a*t-1 for positive integers t satisfying 3^a*t = 1 (mod 2^b). Proof: a consecutive odd iterations from n=2^a*t-1 yield T^i(n)=3^i*2^(a-i)*t-1 (0<=i<=a), and the b subsequent inputs are even iff 2^b divides 3^a*t-1. Conversely, a initial O's imply n congruent -1 mod2^a, and b subsequent E's force this divisibility. Since 3^a is odd, t occupies a nonempty residue class modulo2^b, hence there are infinitely many positive n, including composites. The coefficient 3^a/2^i stays >=1 through the first a steps and then decreases under E; its FIRST subunit value is exactly at j=a+b.

At this first crossing,
    T^j(n)=(3^a*t-1)/2^b
and therefore
    n - T^j(n) = (D*t-(2^b-1))/2^b.
Thus the exact first-crossing descent criterion is D*t > 2^b-1. This specializes (not replaces) the general classical affine cutoff CP-0020.

**Nontrivial uniform subfamily:** If 4*3^a <= 3*2^(a+b), then D>=2^(a+b)/4>=2^b for a>=2; for EVERY positive admissible t, D*t>=2^b>2^b-1. Therefore EVERY positive n with this full parity word strictly descends at its first coefficient crossing. It is not a mere assertion for all sufficiently large lifts: it includes the least positive representative.

**Infinitely many eligible a, bounded gaps:** Writing f_a={a*alpha}, the displayed condition is equivalent to f_a <= alpha, because 3^a/2^(a+b)=2^(f_a-1) and 2^(alpha-1)=3/4. We have alpha>1/2 since 3/2>sqrt(2). If f_a>alpha, then f_a>1-alpha and f_(a+1)=f_a+alpha-1 lies in (0,alpha). Hence for EVERY a>=2, either a or a+1 satisfies the sufficient condition. In particular infinitely many distinct first-crossing cylinders obey CST, with no assumption that CST holds universally.

Examples: a=2,b=2,t=1,n=3,j=4 (3->5->8->4->2); a=4,b=3,t=1,n=15,j=7; a=6,b=4,t=9,n=575,j=10. The sufficient condition does NOT cover every a: a=3,b=2 gives 3^3/2^5=27/32>3/4, yet its t=3 start n=23 descends at j=5. Do not infer failure outside the certified subfamily. a=1,b=1,t=1,n=1 fails strictness (base trivial 1->2->1); the stated theorem excludes a=1 and never pretends it covers 1.

## CP-0024 — no finite per-residue strict-descent horizon for ANY fixed modulus (PROVED_INTERNAL)

Let M>=1 be ANY fixed modulus, k=v2(M), and choose ANY residue r mod M for which r is congruent -1 mod2^k (when k=0 the condition is vacuous). Let h be any proposed finite nonnegative first-descent bound attached to residue r. Choose H>=max(2,k,h). By the generalized Chinese remainder theorem, the simultaneous congruences
    n=r (mod M),  n=2^H-1 (mod 2^(H+1))
are compatible (their common power-of-two gcd is 2^k). Choose a positive solution n0>1 and L=lcm(M,2^(H+1)). For every q>=1, n=n0*(1+q*L) is a positive COMPOSITE solution to the same congruences. In particular n=2^H*t-1 with t odd and positive and v2(n+1)=H.

For 1<=i<=H, the first i T inputs are O and
    T^i(n)=3^i*2^(H-i)*t-1 > n
since 3^i>2^i. Moreover T^H(n)=3^H*t-1 is even and
    T^(H+1)(n) - n = ((3^H-2^(H+1))*t+1)/2 > 0
because 3^H>2^(H+1) for H>=2. Thus these infinitely many positive composites lack strict descent even through H+1, in particular through h(r). This refutes finite class-dependent uniform first-descent bounds for *any* fixed M (including M with an odd part), strengthening S003 CP-0022. It does NOT refute a variable-depth or genuinely adaptive rank.

**Six hypothetical least-counterexample classes (CP-0010):** For n congruent to r modulo48, the exact valuations v2(n+1) are 3 for r=7,39; 2 for r=27,43; and can be arbitrarily high (>=4) for r=15,31. Both r=15 (n divisible by3) and r=31 (n congruent1 mod3) satisfy the CRT condition with M=48. Thus a finite mod48 horizon table necessarily fails in at least these two candidate classes, including infinitely many composites, but NO least-counterexample class has been eliminated and no actual divergent integer produced. The source obstacles y=0 mod3 (no odd U-parent) and y=1 mod3 (only larger U-parents) remain.

## CP-0025 — unbounded jump of v2(n+1) under ONE accelerated odd step (PROVED_INTERNAL)

For EVERY K>=3, CRT yields arbitrarily large positive odd y satisfying y=-1 (mod2^K) and y=7 (mod9). Define x=(4*y-1)/3. Since y=7 mod9, x is an integer divisible by3; choose y large so x>3, hence x is composite. As y is odd, 3*x+1=4*y has exact 2-valuation 2, hence U(x)=y. Also
    x+1 = 2*(2*y+1)/3,
whose quotient (2*y+1)/3 is odd, so v2(x+1)=1, while v2(U(x)+1)=v2(y+1)>=K.
An explicit witness is x=681 -> U(x)=511, with valuations 1 -> 9. Notice x>y: this family DOES decrease in numerical size. Its role is to disprove the proposed simple one-U-step rank v2(n+1), not to refute all combined size/valuation potentials or Collatz. It is compatible with prime-factor erasure: x is divisible by3, U(x) is not.

## Attack C: bounded odd-horizon factors and falsifications

S003 CP-0021 remains: for x0 positive odd, x_(i+1)=U(x_i), A_i=sum of valuations before step i, and F_m=sum_(i=0)^(m-1) 3^(m-1-i)*2^A_i, then 2^A_m*x_m=3^m*x0+F_m and gcd(x0,x_m)=gcd(x0,F_m). There is no proved adaptive sign or prime-support potential.

For each fixed m>=1, choose H>m and x=2^H*t-1 with t odd. The first m U steps have a_i=1 and
    U^m(x)=3^m*2^(H-m)*t-1 > x,
    F_m=3^m-2^m.
Taking t in a progression can make x composite without changing the m-step all-O prefix. Thus no global uniformly bounded number m of accelerated odd iterations guarantees numeric descent, nor does F_m alone. This statement is a scoped consequence of the long-O obstruction, NOT a rejection of start-dependent stopping time.

Hostile controls: 15->23->35 recovers 5 at m=2; 121->91 increases distinct-prime count; 27->41 grows; 12t+3->18t+5 grows for all t>=1; 7 at shortened j=8 is paradoxical AFTER first descent j=7; 27 first descends j=59 and its exact 27+2^59*q cylinder is unchanged; x=1+2^k*q with k>=2, q>=1 descends at shortened j=2, so high lifts need not be exceptional; y divisible3 still has no odd U-parent. None of these is a universal statement.

## Exact independent finite probes and reproduction boundary

A local separate Python 3 arithmetic probe (not original GitHub repository checkout) tested: a=2..129, exact integer b by multiplication comparison, every adjacent a pair, all eligible a with t0=(3^a)^(-1) mod2^b and t=t0+q*2^b for q=0,1,3, full parity/slope/descent checks; eligible count 75 of 128. CRT composite examples for H=4,5,8,12,20 in both mod48 classes 15 and31, checked through H+1; valuation jump for K=3..29; m-step affine-offset and gcd for m<=8 on [15,35,121,27,3,51,243,231,681,2^20*7-1]. All assertions passed. This is FINITE_TEST, not the source of any universal proof. In-repository tests/test_s004_boundaries.py repeats delimited exact checks; GitHub CI must separately be observed for the full original suite, S000 audit, frozen S001 k10..16 manifest, independent checker, canonical JSONL consumer, and S003 corruption tests. Local clone from github.com was unavailable (container DNS), so no local run of ORIGINAL repository tests is claimed.

## Primary sources / originality audit

Rozier–Terracol, Discrete Mathematics 349 (2026), 115167, DOI 10.1016/j.disc.2026.115167, arXiv:2502.00948: original text explicitly states Terras CST is open and develops standard affine remainder/paradoxical prefixes. This is a direct PRIOR-ART constraint, especially for CP-0023; no novelty claimed. Terras 1976 and Lagarias surveys: coefficient stopping-time formulation classical. Barina, J Supercomputing 81:810 (2025), source-reports finite verification to 2^71; Angeltveit arXiv:2602.10466 concerns finite algorithms; Tao (Forum Math Pi 2022) proves logarithmic almost-all almost bounded lower orbits. Hercher's June 2026 two-page corrigendum explicitly repairs an erroneous Theorem 21 inequality argument by convex-polytope maximization; we imported NO theorem about all cycles. These do not settle Collatz. CP-0023—0025 are elementary internally checked findings; priority/originality not established. No Lean, Palomar or universal theorem.

## Remaining open quantifiers

Find a noncircular rule closing EVERY positive exceptional residue tower or a proof of strict descent for every n>1; extend the restricted first-cross O^a E^b band without assuming Terras CST; construct a truly adaptive mixed-state well-founded rank that handles both y=0 and y=1 mod3; derive a genuine convergent potential from F_m rather than merely a gcd identity. All remain OPEN.
