# S013 — uniform large-m two-run first crossings via Matveev; exact carry CRT; odd-run termination

Date: 2026-10-15. Research scope: shortened Collatz T(x)=(3x+1)/2 on odd x and x/2 on even x. O/E designate INPUT parities, and j_c is the first j with 3^(number of odd inputs)<2^j. No global convergence or Terras coefficient stopping time proved; novelty UNCHECKED.

Entry LIVE main commit cee8936245d497bdd51cc817c8283c8bd41b2839, ACTUAL git commit TREE 0e3a7afa11b9a951fb1feb286a78268b9c4bc00e, ordered parents 1848d3021bba76da626ca0b91716fbbaa5fc4481 and da0cd4ecb220d634c541c0fbd5d444cdf1722e4e. Open pull requests []; rulesets []; main protection GET 403 NOT OBSERVED. S012 attested full hosted suite at PR #18 and merged main. Last S012-attestation main CI run 38745181460: success at workflow level; NOT this S013 source. The S013 original suite must be observed separately.

## CP-0050 — PROVED_INTERNAL using externally established Matveev inequality: ALL sufficiently large m, every positive lift

For ANY FIXED positive integers a,c such that 3^a>2^(a+c), there exists an integer m_0(a,c) such that FOR EVERY integer m>=m_0, let
j=ceil(m log_2 3), d=m-a, b=j-m-c, P=3^m, M=2^(j-a),
D=2^j-P, K=3^d(2^c-1)-2^(c+d).
Then d,b>=1, the word W=O^a E^c O^d E^b is admissible, j is its TRUE FIRST coefficient crossing, its unique minimal cylinder representative is
t0=(-K P^(-1)) mod M in {1,...,M-1}, with n_q=2^a(t0+M q)-1 for all q>=0, and EVERY n_q strictly decreases at step j. Infinitely many n_q are composite for EACH m. This includes all sufficiently large m with arbitrarily small positive delta=(2^j-3^m)/3^m, AND all sufficiently large m with delta>=kappa=(2^c-1)/3^a. No claim of all parity words or all positive starting integers.

Proof. Irrationality of log_2 3 follows from unique prime factorisation, so m log_2 3 is never integer and j=bit_length(P); 0<delta=(2^j/P)-1<1. Since j/m approaches log_2 3>1, eventually d,b>=1; furthermore 3^m>2^(m+c). The initial a Os have growing coefficient >1; the c Es leave coefficient 3^a/2^(a+c)>1; the d Os increase it; before the final E tail coefficient is >1; every earlier point of the last tail has 2^i<=2^(j-1)<3^m. At time j the coefficient is below 1, proving FIRST crossing.

The parity-cylinder composition gives exact endpoint (P t+K)/M, unique positive odd t0 mod M because P is odd and K is odd, and drop n_q-T^j(n_q)=[D t0-(M+K)]/M +Dq. The c Es and d Os imply the exact carry divisibility
2^(c+d) divides 3^a t0+(2^c-1); hence t0 >= [2^(m-a+c)-(2^c-1)]/3^a.
(The right side is positive for all sufficiently large m.) Notice that K/P=kappa-2^(c-a)*(2/3)^m <=kappa, and M/P=(1+delta)/2^a<2/2^a. Therefore strict drop follows if
delta*t0 > (2/2^a)+kappa.
The logarithm bound now decisively handles the shrinking-delta regime.

EXTERNAL theorem explicitly used: Matveev's lower bound on nonzero products of powers of algebraic numbers minus 1, as quoted in Theorem 3 of Bugeaud et al. / the Research in Number Theory paper "Integers representable as differences of linear recurrence sequences", https://link.springer.com/article/10.1007/s40993-021-00252-2 . For t=2, field degree 1, gamma_1=2, gamma_2=3, exponents b_1=j, b_2=-m, B=2m (j<=2m), heights A_1=log2, A_2=log3, its displayed theorem yields
log(delta)> -C*(1+log(4m)),
C = 3*30^6*3^(11/2)*(log 2)*(log 3) >0,
since delta=2^j*3^(-m)-1 is nonzero. Thus delta>exp(-C)*(4m)^(-C). The preceding exact t0 bound grows exponentially in m for FIXED a,c, so delta*t0 >= exp(-C)*(4m)^(-C)*[2^(m-a+c)-(2^c-1)]/3^a tends to +infinity. It eventually exceeds (2/2^a)+kappa. This is a genuine quantified existence proof of m_0(a,c), in principle effective but with an absurdly enormous bound; it is NOT an explicit practical numerical threshold. The exact endpoint inequality proves strictness for q=0, hence all q>=0. Since 2^a M is a power of 2 and invertible mod3, choose q in a congruence class modulo3 such that n_q=0 mod3; for sufficiently large q this gives infinitely many positive composites. QED.

CONTEXT: Matveev is an imported published deep theorem, NOT an original proof of a logarithmic irrationality bound. This new deduction concerns a specified 2-run parity grammar and might have prior art. S012 CP-0047 had required delta within positive compact windows and D<K; CP-0050 eliminates BOTH restrictions asymptotically, but does not cover any arbitrary initial parity word or establish CST.

## CP-0051 — PROVED_INTERNAL exact two-modulus carry classification

For any admissible a,c,d,b>=1 in this two-run grammar (not requiring fixed parameters or large m), with P=3^(a+d), j=a+c+d+b, M=2^(c+d+b), K=3^d(2^c-1)-2^(c+d), D=2^j-P>0, first crossing verified independently from all earlier prefixes, define:
u = 3^(-d) mod 2^b in {1,...,2^b-1};
v = (2^c-1)*2^(-(c+d)) mod 3^a in {0,...,3^a-1};
h = u + 2^b * ( (v-u)*(2^b)^(-1) mod 3^a ),
with the final parenthesis chosen as an integer in [0,3^a-1].
This defines the UNIQUE h in [1,3^a*2^b-1] satisfying h=u mod2^b and h=v mod3^a. Then t0=[2^(c+d)h-(2^c-1)]/3^a is a positive integer <M and exactly the canonical minimal lift (-K*P^(-1)) modM. The full word is realised by all n_q=2^a(t0+M q)-1. EXACT necessary and sufficient first-crossing outcomes for q=0 are:
strict descent iff D*[2^(c+d)h-(2^c-1)] >3^a*(M+K);
equality iff the two sides equal; overshoot iff left < right.
For general q>=0 the criterion is D*t0 +M*D*q > M+K. These are integer comparisons, so no floating-point resonance test is needed.

Proof. After O^a E^c, the input to O^d must be 2^d h-1, giving 3^a*t0+2^c-1=2^(c+d)h. After O^d it is 3^d h-1, and b Es mean h=3^(-d) mod2^b. The same identity modulo3^a gives h=v mod3^a. Since gcd(2^b,3^a)=1, the CRT formula is unique modulo3^a2^b, and the odd u representative forces 0<h<3^a2^b. It follows that 0<t0<M (the 2^c-1 correction is smaller than 2^(c+d)), and the parity word is exactly realised. The standard endpoint identity proves the three mutually exclusive sign cases. The displayed formula is an explicit CRT *algorithm*, not a symbolic inequality with an unspecified carry. It is not a universal classification of arbitrary Collatz words.

## CP-0052 — PROVED_INTERNAL exact finite odd-run progress; no-go for a global run-count argument

For ANY positive odd integer n, write n+1=2^h u with u odd and h=v2(n+1)>=1. For every i=0,...,h,
T^i(n)=3^i 2^(h-i)u-1.
For i<h the current input is odd and v2(T^i(n)+1)=h-i, hence v2(x+1) decreases by exactly 1 on every O step; T^h(n)=3^h u-1 is EVEN, so its maximal consecutive O run ends in exactly h steps. This is a fully terminating integer-dependent algorithm to skip each O run. However, the endpoint grows because 3^h>2^h; subsequent E/O runs can restore v2(x+1) and may grow again. The accelerated algorithm "repeat finite O run, then all consecutive E steps, until reaching lower than original n" is a valid partial descent prover but total termination on all n>=2 would prove Collatz. CP-0041 gives an exact growing 11-step return with both endpoints v2(n+1)=2, so a rank based on size increasing and this valuation fails on every such return.

## Attack A — explicit integer-dependent descent certificates, precise failure to close all positives

A1 (forward signed-affine certificate): input any integer n>=2; compute (x_j,A_j,B_j) exactly with 2^j*x_j=3^A_j*n+B_j, initial x_0=n,A_0=B_0=0; each step uses actual input parity. At each j test (2^j-3^A_j)*n>B_j, equivalently x_j<n. On success output j, all parities and strict well-founded successor x_j<n; on any finite budget B(n) otherwise output UNKNOWN, never DIVERGENT. The unbounded algorithm is a semidecision; proving it terminates for ALL integers is exactly the global Collatz statement by induction. An n-only budget shorter than about log2 n fails on CP-0049 forced-O composites. On 27,43,91,155,251, 393243+524288k and all six smallest r7/15/27/31/39/43 classes, finite positive certificates exist (specific checks below); no finite sample yields a universal time bound. The complete 71-state, 5041-edge exceptional transducer forbids a proof by well-founded *state-only* budgeting.

A2 (integer-dependent odd-run and inverse-basin certificate): start from odd n, h=v2(n+1), skip exactly h Os by CP-0052, then divide out the full even run (using v2 of the even endpoint) to obtain the next odd number; repeat until a value smaller than the INITIAL start is seen. Every micro-run terminates by a verified valuation potential h or v2(x), so any finite certificate is algorithmically checkable. Equivalently enumerate the reverse predecessor graph of 1, generated by y->2y and, when y=2 mod3, y->(2y-1)/3 (positive odd), with breadth-first search: membership yields a finite verified path. But the number of runs or breadth-first search depth has NO known uniform integer-dependent finite bound. A decreasing lexicographic (size,v2(n+1)) rank is refuted on the CP-0041 return, and the reverse-graph membership predicate is not proved total. These algorithms never assert an infinite Collatz orbit from infinitely realisable finite 2-adic paths.

Exact finite hostile instances for A1: n=7 ->5 at j7; 15->10 j7; 27->23 j59; 31->23 j56; 39->38 j8; 43->37 j5; 91->61 j45; 155->122 j40; 251->244 j27; 393243->269366 j37; 917531->588548 j26. The larger 2^48*13-1 first drops at j130 (independent finite check, no uniform inference). For every n=393243+524288k the EXACT 11-step return expands to 1259803+1679616k while preserving v2(n+1)=2; it need not be prime/composite for each k, but infinitely many k give composite starts.

Unresolved lemma U-S013: prove that EVERY positive integer n>=2 not already covered by an explicit strict-descent cylinder admits a finite certifiable integer-decreasing successor, with a terminating algorithm and well-founded bound that is not itself equivalent to assuming the Collatz conjecture. All six least-counterexample residue classes 7/15/27/31/39/43 mod48 remain OPEN; no complete covering family or unconditional global rank was found.

## Finite validation and sources

Local Python 3 isolated script: 4/4 methods PASS, test source in tests/test_s013_math.py. Exhaustive declared grid a=2..10,c=1..7,m=a+1..150 when admissible: 3854 exact cases, 43 D<K and 3811 D>=K, ZERO failures of CRT, positive minimal lift and strict-first-crossing arithmetic. Selected parity prefixes fully checked for (2,1,m) m=3,17,971,1636 and (3,1,41),(4,2,41),(6,3,253),(7,3,306), including q=0,1. Separate exact odd-run inputs, expanding return k=0,1,3,9, and six least-counterexample mod48 classes tested. These are FINITE_TEST only. The asymptotic theorem comes from the written proof plus imported Matveev theorem, not finite execution. The original repository full suite and S000/S001/S003 hosted checks must be independently observed after the S013 commit.

Dated literature: Matveev theorem as reproduced in Research in Number Theory https://link.springer.com/article/10.1007/s40993-021-00252-2 (explicit inequality inspected; Matveev original publication not inspected). Terras 1976 https://doi.org/10.4064/aa-30-3-241-252; Rozier/Terracol October 2026 https://doi.org/10.1016/j.disc.2026.115167 still discusses OPEN CST; Niu May 2026 https://arxiv.org/abs/2605.13886 disclaims Collatz/CST; Simons/de Weger 2005 https://doi.org/10.4064/aa117-1-3 finite m-cycles, not a global proof. Steiner 1978 "A Theorem on the Syracuse Problem", Congressus Numerantium XX pp553–559: primary FULL TEXT NOT ACQUIRED/READ; bibliography/location https://math.stackexchange.com/questions/3092661/does-anyone-know-where-i-can-get-a-copy-of-r-p-steiner-a-theorem-on-the-syra/5063547 only secondary. No originality, formal proof, Palomar, arXiv or publication claim.

Global Collatz/composite convergence OPEN; Terras CST OPEN; no universal exhaustion, no positive divergent orbit constructed, no new verified cycle exclusion.
