# S000 — foundations, exact reductions and limits

Map T: for n>0, T(n)=n/2 if n even and T(n)=(3n+1)/2 if n odd. Reaching 1 is equivalent under T and the standard 3n+1-with-separate-halving convention.

## CP-0001: composite-target equivalence (PROVED_INTERNAL, elementary)

Let C be "every composite positive integer reaches 1" and A be "every positive integer reaches 1". A => C. For C => A, n=1 is done, composite n are covered by C, and for prime p the composite 2p is covered by C. Since T(2p)=p, the suffix of the orbit from p must reach 1. Thus A iff C. This is a logical reduction, not progress proving A or C.

## CP-0002: immediate descent (PROVED_INTERNAL, elementary)

If n>1 is even, T(n)=n/2<n.

If n>1 satisfies n=1 (mod 4), n is odd, and T(n)=(3n+1)/2 is even; T^2(n)=(3n+1)/4<n because 3n+1<4n.

If n=3 (mod 16), check its first parity word O,O,E,E (for n=3 the orbit starts 3,5,8,4,2). The affine parity-branch formula gives T^4(n)=(9n+5)/16<n for every positive n in that class (since 9n+5<16n). This is a universal subfamily descent statement, not full convergence unless a previously proved smaller-start induction is available.

Consequently the **least** counterexample to convergence, if one exists, must be odd and in classes 7,11,15 modulo 16. Necessity only; this does not mean all members of these classes diverge or fail to descend later.

## CP-0003: prime-factor reset on odd steps (PROVED_INTERNAL, elementary)

For odd n, gcd(n,3n+1)=gcd(n,1)=1, and T(n)=(3n+1)/2 is an integer. Hence gcd(n,T(n))=1. The same is true for the accelerated odd-to-odd Syracuse step dividing out all powers of 2. A consecutive odd step shares no prime factor with the odd starting number. This does not imply termination or statistical independence.

For odd primes p=1 (mod 4), T(p)=(3p+1)/2 is even and greater than 2, hence composite. For odd primes p=3 (mod 4), T(p) is odd and can be prime (e.g. p=3 gives 5). The orbit of the composite 2p enters p directly: this is an exact relation but not a proof of convergence.

## CP-0004: parity-residue affine representation (PROVED_INTERNAL, elementary)

For every k>=1 and residue r modulo 2^k, the parities of the first k iterates are determined by r. On that branch, T^k(n)=(3^a n+b)/2^k for integers a>=0, b>=0 depending on the parity word. Under an even step (A,B,D)->(A,B,2D); under an odd step (A,B,D)->(3A,3B+D,2D), starting at (1,0,1). The first k parity bits are invariant on changing n by a multiple of 2^k: at each earlier step the change is a multiple of a positive power of 2, proving inductively that the parity decisions agree.

If 3^a < 2^k, then every sufficiently large n in that residue class satisfies T^k(n)<n. More explicitly for n=r+q*2^k with 0<=r<2^k, the equality T^k(n)=T^k(r)+3^a*q holds whenever representative r>0, and descent follows for q>(T^k(r)-r)/(2^k-3^a). This is **eventual descent for selected classes**, not descent for all classes nor a proof of Collatz.

## CP-0005: mod-2^k cannot segregate primes and composites (PROVED_INTERNAL + external Dirichlet)

For any odd r modulo 2^k, gcd(r,2^k)=1, so Dirichlet's theorem on primes in arithmetic progressions yields infinitely many primes in the residue class. There are also infinitely many composites in it: choose t>=1 large enough that m=r+t*2^k>1 and let N=m*(1+2^k)>1. Then N is composite, N congruent r mod 2^k, and distinct choices of t give distinct N.

A finite parity-residue partition by itself cannot isolate all composites into prime-free classes. This is a barrier to a simplistic prime/composite residue sieve, NOT a barrier to descent proofs which work for both primes and composites.

## Limitations and hostile examples

Collatz is not multiplicative: T(3*3)=T(9)=14, while T(3)*T(3)=25. One cannot transfer a proof about factors directly to the product by assuming multiplicative trajectories.

Every proof of a proposed "composites hit smaller certified composites" rule must account for primes and nonmonotone steps. Knowing convergence for [1,B] only proves higher starts which reach that actual interval. No finite table proves the infinite case.
