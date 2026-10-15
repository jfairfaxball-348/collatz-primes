# S018 — initial-odd-run versus even-budget theorem for arbitrarily many E-blocks

Date: 2026-10-15. Shortened Collatz T(n)=(3n+1)/2 for odd n, and n/2 for even n. O and E denote INPUT parity. For any word W of length j with m O, define B_W by 2^j T^j(n)=3^m n+B_W on its exact cylinder. An overcritical word U means 3^(#O(V))>2^|V| for EVERY nonempty prefix V, not merely U itself. A coefficient crossing need NOT be an integer descent without an additional argument.

## Entry provenance
Live main entry ref 5255e2a5fcd134e81d67ec55885b57cf69e0a166, underlying git tree 579ca0edc3ff789b3311ffe1b0cede299a6e33c9, ordered parents 1bc9606f563ce2d37e392eefe0fc27d113224328 and 57b643c64fddff53ff45008cb15902f535ce5f49. Open PRs []; rulesets []; branch-protection API 403 FORBIDDEN (UNKNOWN, not absent). S017 attestation merged-main run 38771277023 job 116547419358 independently COMPLETED SUCCESS: individual Unit tests, Finite parity and orbit sanity, Recreate finite residue stream and cross-check original manifest steps all SUCCESS. These are PRE-S018 checks. GitHub clone from local container DNS-blocked. Research proof uses established published Matveev bound, not source proof rederivation.

## CP-0066 — PROVED_INTERNAL, effective multi-block first-crossing all-lifts theorem (analytic corollary uses SOURCE_STATED Matveev)

Let U be ANY nonempty finite overcritical O/E parity word starting with its maximal initial O^a (a>=1), r=#O(U)>=1, e=#E(U)>=0, ell=r+e. Let d>=1, m=r+d, j=bit_length(3^m), b=j-ell-d and W=U O^d E^b. Define D=2^j-3^m>0 and delta=D/3^m. THEN b>=1, the cylinder W is nonempty and its UNIQUE coefficient crossing occurs at step j. More importantly, if

   D*(2^a-1) > 3^m*2^e,                                    (EXACT)

then T^j(n)<n for EVERY positive n in the cylinder, including its least representative. Infinitely many such n are composite. No restriction at all on r/d, e, the number or placement of E-blocks, or d beyond d>=1; the displayed sufficient inequality IS a substantive structural restriction.

A uniform explicit way to guarantee EXACT is

   a >= e+2+ceil[ C*(1+ln(4m))/ln2 ],  where C=10^10.       (ANALYTIC)

This second implication uses SOURCE_STATED primary Matveev (2000) as recorded in CP-0056 and does not independently reproduce its deep proof.

**Proof — true first crossing and cylinders.** Every prefix of U has 3^(#O)>2^length; O^d increases its coefficient, so 3^m>2^(ell+d). The integer j=bit_length(3^m) satisfies 2^(j-1)<3^m<2^j, whence j>ell+d and b>=1. All earlier E-tail prefixes (length<=j-1) remain overcritical; so j is EXACTLY the first coefficient crossing. Parity-cylinder bijection yields the unique residue n0=(-B_W*(3^m)^(-1) mod2^j), chosen 1..2^j-1 because B_W is odd for O-starting words. Every positive representative n=n0+q2^j realizes W. Since gcd(2^j,3)=1, infinitely many representatives are composite multiples of3 greater than3.

**Proof — sharp arbitrary-prefix intercept budget.** CP-0060, valid for EVERY U regardless of block count, states B_U<=2^e(3^r-2^r). Thus B_U+2^ell<=2^e 3^r and H_U:=(B_U+2^ell)/3^r <=2^e. The exact concatenation affine intercept is
   B_W=3^d(B_U+2^ell)-2^(ell+d).
Therefore
   B_W/3^m = H_U-2^(ell+d)/3^m < 2^e.
All starts with initial O^a satisfy n=2^a u-1 with u an odd positive integer (the first a iterates are odd), so n>=2^a-1. The sign equation for the actual first crossing is
   T^j(n)<n iff D*n>B_W iff delta*n>B_W/3^m.
EXACT forces delta*n >=delta*(2^a-1)>2^e>B_W/3^m, yielding strict descent for every lift. This proof of EXACT is ENTIRELY ELEMENTARY; no source assumption.

**Proof — Matveev corollary.** The earlier directly read ORIGINAL Matveev 2000 §2 Corollary 2.3 supplies for every m>=1
   ln(delta)>-C(1+ln(4m)), C=10^10.
Do not mistake Matveev's original log|L| bound (L=j ln2-m ln3>0) for a direct product-minus-one statement; delta=e^L-1>L, so the transferred bound is valid. For a>=1, 2^a-1>=2^(a-1). Under ANALYTIC,
   (a-e-1)ln2 >= ln2+C(1+ln(4m)).
Thus ln[delta*(2^a-1)/2^e] > (a-e-1)ln2-C(1+ln(4m)) >=ln2>0.
So EXACT follows (with comfortable strict slack). The threshold is astronomically large, not an effective small-range guarantee.

**Arbitrarily many E-blocks and r/d unbounded.** For each integer k>=K0=[16(C+10)]^2 put U_k=O^(2k)(OOOE)^k and d=1. Then ell=6k, r=5k, e=k, a=2k+3, m=5k+1; the word has k separate E-blocks and every prefix is overcritical (OOOE slope multiplier 27/16>1). For k>=K0, ln(4m)<=ln(24k)<=sqrt(k), so (a-e-1)ln2=(k+2)ln2>(k+2)/2>C(1+sqrt(k)). Thus ANALYTIC holds and all W_k cylinders strictly descend at first crossing. Yet r/d=5k and #E-blocks=k both grow without bound. This cannot be inferred from S016's bounded r/d hypothesis and is distinct from S017's single-E-block intermediate prefix. K0 is a deliberately huge conservative constant.

## CP-0067 — PROVED_INTERNAL exact necessary arithmetic and modular obstruction for any future counterexample

Under the above U,d assumptions, n0=(-B_W*(3^m)^(-1) mod2^j), 1<=n0<2^j, is the LEAST positive cylinder member. Since D>0 and adding q2^j strictly increases D*n, ALL-LIFT strict descent is equivalent to D*n0>B_W; this is the exact S017 CP-0065 CRT criterion. Any ACTUAL non-dropping example must therefore obey the joint inequalities

   D*n0 <= B_W < 3^m*2^e,
   2^a-1 <= n0 < 2^e/delta,
   (2^j-3^m)*(2^a-1) < 3^m*2^e.

The final strict inequality follows because the upper bound B_W<3^m2^e is strict. These are necessary conditions for a REAL counterexample, not counterparameters themselves. A failed EXACT/ANALYTIC sufficient condition does not imply overshoot. The remaining all-U regime includes bounded a with many E-blocks, especially U=(OOOE)^k and d=1. We do NOT possess a uniform CRT lower bound on n0 strong enough to settle it.

## Global universal-certificate adversarial check — OPEN
A direct total verifier would have to show for EVERY n>=2 a finite first smaller iterate. The exact cylinder sign test is decisive for a SELECTED W but has no exhaustive inclusion proof for all n. An unbounded enumeration of certificates would require proving termination for every input, equivalent to original Collatz. Finite 71-state 5041-edge transducers permit every fixed exceptional itinerary along infinitely many composite lifts; they are not a single infinite orbit. Forced-O towers 2^H u-1 obstruct every FIXED horizon; the expanding 393243+524288k and n=64k+59 ->72k+67 same-v2 families obstruct naive decreasing ranks. Numbers 7,15,27,31,39,43 and 91,155,251 are checks, not globally closed residue classes. Prime/composite convergence remains equivalent to full Collatz.

## Independent EXACT finite validation and limitations
Standalone local Python 3 scratch script at /mnt/data/s018/independent_s018.py, SHA256 01b5d72969272b410df8c1258833a3a84302d9c5768ff683ef45b7c88a8eb060, enumerated 81,118 first coefficient crossing words of length <=24. A total of 78,303 had a multi-E-block U before the final O^d E^b; EACH had strict actual canonical and sampled lifts 0,1,7. The ONLY non-strict first crossing in the full enumeration was W=OE, n0=T^2(n0)=1, which is NOT an overcritical U O^d E^b example. Hostile positive checks: 7->5 in 7, 15->10 in 7, 27->23 in59, 31->23 in56, 39->38 in8, 43->37 in5, 91->61 in45, 155->122 in40, 251->244 in27. Exactly reconstructed finite multi-E examples (U,d,b,j,n0,T^j(n0)) include (OOEOOEOOE,1,2,12,1019,545), (OOOEOOOE,1,3,12,231,124). These observations do NOT prove a universal parity-word inequality or the infinite theorem. The new checked-in unittest module is a distinct reproducible, bounded validation artifact; isolated original checkout was NOT available.

## Source audit and boundaries
Matveev (2000) original English source https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng, §2 Corollary2.3 printed page1219, was DIRECTLY read by S015–S017; S018 repeated link attempt TIMED OUT, so this session relies on their already documented precise original quotation rather than claiming a new successful original-PDF inspection. Original 53-page proof is NOT independently reproduced.
Steiner (1978) original Congressus Numerantium XX pp553–559 still not acquired: indirect scholarly Lagarias bibliography only. Terras (1976) Acta Arith. 30 241–252, Rozier/Terracol (October 2026) Discrete Math. 349 115167, Tong Niu (May 2026) arXiv:2605.13886 and Simons/de Weger (2005) finite cycle exclusions checked by publicly accessible abstract/metadata, not full theorem priority audit. Rozier/Terracol and Niu explicitly leave Terras coefficient-stopping-time question unresolved. Mathematical PRIORITY OF CP-0066/67 NOT ESTABLISHED; no independent referee, Lean, Palomar, preprint, journal or claim of all-positive Collatz.
