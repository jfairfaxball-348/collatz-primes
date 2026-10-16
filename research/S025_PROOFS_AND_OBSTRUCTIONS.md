# S025 — bitlength-dependent Collatz no-go results and formal conditional bridge

Date: 2026-10-16. CP-0083 and CP-0084: PROVED_INTERNAL, novelty UNCHECKED. CP-0085: SCOPED FORMAL_VERIFIED on original source commit 62c72b40df3b3c501e6298ae903a286aaefd8bb3 with pinned Lean run 38902175738/job116976832661 and successful compilation. No universal Collatz proof.

## Classical parity-cylinder lemma (proved here algebraically; not in Lean)

Shortened T maps even x to x/2 and odd x to (3x+1)/2. Each finite word w in O,E of length L has affine triple (A,Q,B), Q=2^L, A=3^(number of O), B≥0 such that Q T^L(n)=A n+B for each input actually following w. Every word specifies EXACTLY ONE residue modulo 2^L: induct on prefix length i. Two lifts of its unique length-i residue differ by 2^i, preserve the first i parities, and their i-th outputs differ by odd A. They therefore have opposite next parity; exactly one of the two lifts gives each desired (i+1)-st bit. This is classical two-adic parity coding (Bernstein–Lagarias 1996); it does not show any fixed positive integer follows a freely selected extension.

## CP-0083: every hard residue class has no descent for nearly its own bitlength

Write R={7,15,27,31,39,43} mod48. For any r in R and H>=6, define the length-H parity word:

- If r≡7 mod16: OOOE followed by H−4 O symbols.
- If r≡15 mod16: OOOOE followed by H−5 O symbols.
- If r≡11 mod16: OOE followed by H−3 O symbols.

The first four/five parity bits force the canonical residue v modulo2^H to satisfy v≡r mod16 (for OOE, the fourth O distinguishes 11 from 3 modulo16). By the preceding lifting lemma v is unique.

By CRT there is exactly one n modulo 15·2^H satisfying n≡v mod2^H, n≡r mod3, and n≡0 mod5. Take its canonical representative 0<n<15·2^H: nonzero because v mod16 is 7,15 or11. Since none of the six r equals 5 mod48, the representative is not 5; it is a composite multiple of 5 and lies in residue r modulo48. With b(n)=floor(log2 n)+1, n<15·2^H<2^(H+4) implies b(n)≤H+4.

Every nonempty prefix has A_j/Q_j=3^(number of O)/2^j>1: before the single E, it equals (3/2)^j; immediately after E, it is 27/16 (three initial O), 81/32 (four initial O), or 9/8 (two initial O). Every subsequent O multiplies the ratio by 3/2. The intercept B_j is nonnegative. Thus 2^j T^j(n)=A_j n+B_j > 2^j n and T^j(n)>n for ALL 1≤j≤H.

Exact conclusion:

FOR ALL H≥6, FOR ALL r in R, there EXISTS a composite n≡r (mod48) with b(n)≤H+4 and FOR ALL 1≤j≤H, T^j(n)>n.

Infinitely many DISTINCT such positive composites exist per fixed r as H increases. Indeed if a fixed n appeared for unbounded H, after the same fixed a initial odd steps and one even step, x=T^(a+1)(n)>0 would undergo arbitrarily long all-odd runs. For t consecutive odd steps, 2^t(T^t(x)+1)=3^t(x+1), so 2^t divides x+1. That is impossible for fixed x as t grows. Pigeonhole excludes any finite witness set.

Therefore the proposed universal size-dependent claim “every such composite descends within b(n)−4 iterations” is REFUTED (for witnesses with b−4≥1). This does NOT refute an eventual first descent, a B(n)=b(n)+C or superlinear deadline, a different rank, or the conjecture itself.

## CP-0084: OOEE nonadmission at bitlength-scale

For k≥2 let Q=16^k and v be the unique residue 0≤v<Q with 7v≡5 modQ. S024's exact four-step OOEE macro F(n)=(9n+5)/16 has 2-adic fixed point 5/7 and the identity 16(7F(n)−5)=9(7n−5). Induction gives initial word (OOEE)^k for every n≡v modQ. Choose the unique representative 0<n<3Q satisfying n≡v modQ and n≡0 mod3 by CRT. It is >3, since 7·3−5=16 is not divisible by Q for k≥2. Therefore n is composite and b(n)≤4k+2.

Every certified S023 grammar atom begins OOO or OOEO. Every four-symbol cyclic phase of OOEE avoids both patterns; no atom starts at any time i≤4k−4, in particular none at i≤b(n)−6. The selected n depends on k; the limit 5/7 belongs to the 2-adic integers, NOT an indefinitely growing positive integer. This refutes only the specific grammar's proposed admission-by-(bitlength−6) claim.

## Failed adaptive renewal attempts and hostile cases

The strengthened obstructions eliminate a near-input-bitlength stopping bound and a bounded-size grammar-admission promise. They do not eliminate B(n)=C·bitlength(n) for C>1, larger variable precision, or any well-founded n-dependent rank. No proof of an integer-dependent rank decreasing at all regeneration steps was obtained; a selected good parity extension is not the actual trace of every n.

For the historic 71/512 early residual and 5041 directed pair states, the S025 script recomputes the 71 count and enumerates 71 squared ordered pairs. It does NOT prove transition-graph eventual exit or attach a rank to those pairs. Controls 64k+59→72k+67 (exact three-step expanding macro), 393243+524288k, n=2^H u−1 (long all-odd prefixes), and 27,43,91,155,251 remain hostile. No inference from the 2-adic OOEE shadow to divergent positive integers is allowed. All-composite convergence equals full Collatz and remains OPEN.

## CP-0085 conditional Lean theorem

S024 already compiled executable shortenedT, runWord, wordAffine, wordAgrees and word_affine_correct (assuming the actual parity trace). The new checked-in Lean theorem matching_word_strict_descent instantiates existing all_lifts_strict_descent: for each n,D and Bool word bs, from wordAgrees n bs, (wordAffine bs).Q = (wordAffine bs).A + D, and (wordAffine bs).B < D*n, conclude runWord n bs < n. It is *conditional* on an actual matching word and positive margin. Original source branch pinned hosted Lean run 38902175738/job116976832661 completed SUCCESS, including build and no-admit guard. Missing: Nat unique bitlength bracket for 3^m; unconditional CP-0071 two-choice gap; positive existence+uniqueness modulo2^L; strict first crossing and end-to-end CP-0076/78. None is claimed FORMAL_VERIFIED.

## Checks and sources

Five local standalone Python3.13 tests PASS, covering all six residues, H=6,7,8,12,16,31,64,129, prefix A>Q, OOEE k=2,3,4,5,8,16,32, 71/5041 enumeration and named hostile input families. The original checked-in branch source Python run38902175614/job116976832282 completed SUCCESS for full unit suite, exact S000 fixture and independently generated S001 depth10–16 manifest/records checker. Later documentation/PR/merged-main SHAs require separate observations.

Bernstein–Lagarias, The 3x+1 Conjugacy Map (1996), original full 16-page author PDF https://websites.umich.edu/~lagarias/doc/bernstein.pdf, inspected across sections 1–5, Theorems 3.1, 4.1, 5.1 and appendix description: parity coding is unequivocally classical; the core theorems concern conjugacy permutation cycles and high-bit behaviour. We did not independently reprove the whole 16 pages or establish originality of a size-dependent corollary. Terras 1976 original 12pp primary text remained inaccessible via publisher and indexed matwbn mirror; only metadata confirmed. Steiner 1978 original 7pp still unavailable, secondary Lagarias bibliography only. Rozier–Terracol 2026 full publisher HTML was reattempted unsuccessfully; prior S024 inspection says coefficient stopping-time remains conjectural. No source-complete novelty gate, independent external verification, Palomar, arXiv or journal submission.
