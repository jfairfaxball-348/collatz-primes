# S020 — a two-choice first-crossing theorem for arbitrary changing overcritical blocks

Date 2026-10-16. Shortened Collatz T(n)=(3n+1)/2 for odd input, n/2 for even. O/E describe INPUT parity. All statements below are conditional parity-CYLINDER theorems; the result is NOT an all-integer convergence theorem.

## Entry evidence

Live DEFAULT main commit 3342189c197b4e11f2e0c9a951076d3e7abb0977; actual underlying Git tree 7379373e0bd930d9e37d96a5d9dc51221da44e6d; ordered parents [9adefb03af2493e59582a77b5a82bc13a859bf4c, f52996e03a7fc15c669200e39cc300cfcea6390d]. Open PRs []; rulesets []; branch protection API 403 FORBIDDEN, so status UNKNOWN, not unrestricted PASS. Last PRE-S020 main push run 38881357952/job116908595237 completed SUCCESS, and the three substantive steps Unit tests, Finite parity and orbit sanity, Recreate finite residue stream and cross-check original manifest independently each SUCCESS. Those steps DO NOT attest to new S020 code.

## Definitions

For a finite word V, let L=|V|, r=#O(V), A_V=3^r, Q_V=2^L and B_empty=0, B_(VE)=B_V, B_(VO)=3 B_V+2^L. Every actual positive cylinder input n satisfies Q_V*T^L(n)=A_V*n+B_V. Define
   S(V)=Q_V/A_V,     H(V)=(B_V+Q_V)/A_V,
as exact positive rational numbers. An overcritical word U has 3^#O(V)>2^|V| at EVERY nonempty prefix V. For positive m let j(m)=bit_length(3^m), D(m)=2^j(m)-3^m>0, delta(m)=D(m)/3^m.

## CP-0070 PROVED_INTERNAL (elementary, novelty UNCHECKED): exact carry recurrence

For EVERY finite O/E word V:
   H(empty)=1,
   H(VO)=H(V),
   H(VE)=H(V)+S(V),
   S(VO)=(2/3)S(V),
   S(VE)=2 S(V).
This is an EXACT identity, not an asymptotic estimate, and holds with no overcritical assumption.

Proof: For O, A'=3A, Q'=2Q, B'=3B+Q, so (B'+Q')/A'=(B+Q)/A. For E, A'=A, Q'=2Q, B'=B, so H'=H+Q/A. The S identities follow from A and Q.

For ANY k>=1, and ANY arbitrary choices P_i in {OOOE, OOOOE}, U=P_1...P_k satisfies:
   H(U) <= 1+(8/27) sum_{i=0}^{k-1}(16/27)^i
        =19/11-(8/11)(16/27)^k <19/11.               (1)
Indeed each block ends with one E; at the E immediately before completion the increment in H is S(boundary)*(8/27) for OOOE or S(boundary)*(16/81) for OOOOE. Each completed block multiplies S by 16/27 or 32/81, both at most 16/27. Sum the geometric series; the order of different blocks is unrestricted. All prefixes of either block are overcritical; hence all prefixes of the concatenation are overcritical. Every positive actual word input begins with OOO and is n=8u-1>=7 (integer u>=1).

The alphabet contains two different blocks and permits e.g. Fibonacci/Thue–Morse-style aperiodic infinite choices. (1) holds for EACH finite prefix of such a formal word, without a single repeated fixed period.

## CP-0071 PROVED_INTERNAL (elementary, novelty UNCHECKED): universal two-consecutive-exponent gap

For EVERY integer m>=1, at least one of delta(m), delta(m+1) is STRICTLY GREATER than 1/3. The chosen exponent is computable from the exact integers 3^m,2^j(m); no logarithms, transcendence or analytic result is used.

Proof: Put q=2^j(m)/3^m, so 1<q<2. If q>4/3 we are done at m. Otherwise q<=4/3 and hence 3^m>=3*2^j(m)/4. Then
   2^(j(m)+1) < (9/4)*2^j(m) <=3^(m+1)
              < 3*2^j(m) <2^(j(m)+2).
Consequently j(m+1)=j(m)+2 and
   2^j(m+1) / 3^(m+1) = (4/3)*q >4/3.
So delta(m+1)>1/3. The strictness comes from q>1, since 3^m is NEVER a power of 2 for m>=1.

## CP-0072 PROVED_INTERNAL (elementary, novelty UNCHECKED): unrestricted block transitions; first-crossing STRICT descent

First a general sufficient theorem. Let U be ANY nonempty overcritical word beginning O^a for an integer a>=1. Suppose its exact rational carry satisfies
   3*(B_U+2^|U|) < (2^a-1)*3^#O(U).                 (2)
Equivalently H(U)<(2^a-1)/3. THEN there exists d in {1,2} such that, writing
   r=#O(U), m=r+d, j=bit_length(3^m), b=j-|U|-d,
   W=U O^d E^b,
we have b>=1; W has its FIRST coefficient crossing at EXACTLY position j; and EVERY positive n in the cylinder W satisfies T^j(n)<n. The cylinder contains infinitely many composite n.

Proof. Choose d=1 or2 using CP-0071 applied to m0=r+1: delta(r+d)>1/3. Overcriticality of every prefix of U and adding O letters gives 3^(r+d)>2^(|U|+d); hence j>|U|+d and b>=1. Every prefix before the tail is overcritical; at any earlier E-tail length t<j, 2^t<=2^(j-1)<3^m. Thus j is genuinely the FIRST coefficient crossing, not a later arbitrary iterate.

Appending O^d to U and then E^b yields the exact identity
   B_W=3^d*(B_U+2^|U|)-2^(|U|+d),
   B_W/3^m=H(U)-2^(|U|+d)/3^m <H(U).               (3)
Actual input parity O^a forces n=2^a*u-1 >=2^a-1 (u positive integer). By (2),(3), and delta(m)>1/3:
   delta(m)*n > (2^a-1)/3 >H(U)>B_W/3^m.
Multiply by 3^m: D(m)*n>B_W. Since 2^j T^j(n)=3^m n+B_W, this is EXACTLY T^j(n)<n. Every finite parity word starting O has a unique positive residue n0 mod2^j because 3^m is odd and the stepwise parity-cylinder bijection holds; n0>=1, all n0+q2^j (q>=0) realise it. Since gcd(2^j,3)=1, infinitely many lifts divisible by3 and >3 are composite. End of proof.

Concrete variable-block corollary: for ALL k>=1 and ALL choices P_i in {OOOE, OOOOE}, U=P_1...P_k, we have a>=3 and H(U)<19/11<7/3<=(2^a-1)/3. Therefore CP-0072 applies with d CHOSEN from just {1,2}, UNIFORMLY independent of k and the entire block sequence. No long repeated fixed P, no assumption of eventual periodicity, and no Matveev estimate is necessary.

This does NOT say BOTH d choices work, that every extension of U satisfies a selected W, or that any particular fixed positive n lies in one of the W cylinders. It therefore does NOT prove an infinite integer orbit, universal coefficient stopping time (CST), all-positive/composite convergence, or a total all-n admission/exit verifier.

## Hostile falsification and certificate-totality boundary

The large-k fixed-period divisibility of S019 CP-0068 says nothing about U with irregular bounded runs: CP-0070–0072 are a genuinely different sufficient mechanism. It is FALSE that a finite alphabet forces arbitrarily long identical consecutive block runs, and NOT proved that every integer enters the successful d=1 or2 subcylinder. Conditional existence of real positive/composite lifts DOES NOT imply a chosen preexisting n chooses the certified continuation. Every certified W begins OOO, excluding n=2 already; all-positive admission cannot follow.

S020 standalone exact Python tests explored 2,046 binary block sequences of lengths k=1..10 (1,225 use d=1, 821 use d=2), their exact canonical n0 and lifts n0+2^j,n0+3*2^j, 150-block irregular example, all m0=1..20000 gap pairs, overcritical prefixes, true first-crossing and positive integer T^j(n0)<n0. All PASS. These finite results CHECK the symbolic proof, not replace it. Existing known hard controls: 71 of 512 early exceptional 11 mod16 starts through13, 5041 compatible finite exception-edge pairs, 27/43/91/155/251, six 7/15/27/31/39/43 mod48, 393243+524288k, 64k+59->72k+67 same-v2 expansion, and 2^H u-1 forced-O composite towers remain NOT GLOBALLY CERTIFIED. Compatible finite paths are not divergent positive integer orbits. No genuine first-crossing overshoot was found in this restricted language; none is inferred from failed sufficient conditions elsewhere.

## Prior art, formal status and limitations

- Bernstein & Lagarias 1996 original article metadata/abstract inspected: https://doi.org/10.4153/CJM-1996-060-x and https://geodesic.mathdoc.fr/articles/10.4153/CJM-1996-060-x/ . Their 2-adic parity conjugacy and finite parity-code permutations are directly relevant to S019 CP-0068. The affine word recurrence already appears in classical stopping-time literature (Terras 1976 https://doi.org/10.4064/aa-30-3-241-252); CP-0068/0070 should NOT be marketed as a novel affine discovery. Unrestricted priority for the particular two-choice bounded-carry cylinder corollary is UNCHECKED; publication is NOT CLEARED.
- Matveev 2000 ORIGINAL English 53-page primary re-opened and visually inspected at printed p1219 PDF page2 §2 Corollary2.3 https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng . It states a LOWER BOUND on log|Lambda|, Lambda=j log2-m log3; delta=e^Lambda-1>Lambda when Lambda>0. Full Matveev proof NOT rederived. The new CP-0070–0072 proof DOES NOT USE Matveev.
- Steiner 1978 seven-page ORIGINAL not acquired, attribution INDIRECT via Lagarias; Simons–de Weger 2005 https://doi.org/10.4064/aa117-1-3 is limited m-cycles; Rozier–Terracol 2026 https://doi.org/10.1016/j.disc.2026.115167 still refers to Terras CST as conjectural; Niu 2026 https://arxiv.org/abs/2605.13886 does not resolve it.
- NO_LEAN_VERIFIED: neither lean nor lake exists in the available local runtime, no Lean file compiled, no Lean-specific CI. Exact proof-ready Nat-domain specification in research/S020_LEAN_SPEC.md; subsequent formalisation action required. No Palomar, preprint, journal or independent refereed mathematical priority claim.
- The owner's target ALL composite integers resolve to1 is EQUIVALENT to full all-positive Collatz, still OPEN. The theorem treats selected finite words with arbitrary block changes but does not exhaust possible paths.