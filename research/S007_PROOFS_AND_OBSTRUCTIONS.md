# S007 — 30 residual cylinders, two-block first crossings, and an unbounded-prefix obstruction

2026-10-15. ENTRY main commit `2161fb31a385a13a8923e43756ad68c68bd77fb9`, Git commit tree `4843d167c36aef659aa95327ea277f48b13db861`, parents `5074485f78b0c84746607ef7054f9ec0e5263fa7` and `afc1178a5b416ce6595b6682f7c96499d98aa8cf`. Global Collatz/composite convergence CP-0007 and Terras CST CP-0019 are **OPEN**. All three results below are PROVED_INTERNAL elementary, originality **NOT ESTABLISHED**. FINITE_TEST results are supplementary, not proofs of the quantified statements.

## Elementary parity-cylinder lemma (common foundation)

Let `T(n)=n/2` if n even, `T(n)=(3n+1)/2` if n odd. Given a j-bit input parity word w realised by positive r, put a=#O(w). For any q>=0, n=r+2^j*q has **exactly the same first j parities**, and `T^j(n)=T^j(r)+3^a*q`. Proof by induction: after i<j steps, the two iterates differ by `3^(number of odd inputs in first i)*2^(j-i)*q`, which is even, so the next parities agree and the appropriate affine branch preserves the formula. At i=j this yields the asserted affine lift. Therefore if `T^j(r)<r` and `3^a<2^j`, **every** positive n≡r mod2^j drops strictly at step j because
`n-T^j(n) = (r-T^j(r))+(2^j-3^a)q >0`.
This is a finite *certificate for an infinite arithmetic progression*, not an all-integers argument. It also gives the exact affine intercept `B=2^j*T^j(r)-3^a*r`, so `T^j(n)=(3^a*n+B)/2^j`.

## CP-0033 — exact NEW +89/512 coverage in each r27/r43 class

S006 CP-0031 already certifies disjoint n≡11 mod32, n≡59 mod128, n≡123 mod256, counting 8+2+1=11 of 16 mod256 possibilities within each r=27,43 mod48. The residual r mod256 set is exactly `{27,91,155,219,251}`. Beginning with precisely those five classes at depth8, test each full cylinder at that depth using the lemma; retain noncertified classes and split them into r and r+2^j at the next depth. The entire NEW certified frontier at depths <=13 is in the following explicit table (no hidden rows):

| residue r modulo 2^j | j | exact parity word | a | T^j(r) | r−T^j(r) |
|---:|---:|---|---:|---:|---:|
| 219 | 8 | OOEOOOEE | 5 | 209 | 10 |
| 347 | 10 | OOEOOOEOEE | 6 | 248 | 99 |
| 923 | 10 | OOEOOOOEEE | 6 | 658 | 265 |
| 507 | 10 | OOEOOEOOEE | 6 | 362 | 145 |
| 2587 | 12 | OOEOOOOOEEEE | 7 | 1382 | 1205 |
| 3675 | 12 | OOEOOOEOOEEE | 7 | 1963 | 1712 |
| 2907 | 12 | OOEOOOEOEOEE | 7 | 1553 | 1354 |
| 2203 | 12 | OOEOOOOEOEEE | 7 | 1177 | 1026 |
| 1435 | 12 | OOEOOOOEEOEE | 7 | 767 | 668 |
| 1787 | 12 | OOEOOEOOOEEE | 7 | 955 | 832 |
| 1019 | 12 | OOEOOEOOEOEE | 7 | 545 | 474 |
| 2075 | 13 | OOEOOOOOEOEEE | 8 | 1663 | 412 |
| 539 | 13 | OOEOOOOOEEEOE | 8 | 433 | 106 |
| 1563 | 13 | OOEOOOOOEEOEE | 8 | 1253 | 310 |
| 2331 | 13 | OOEOOOOOOEEEE | 8 | 1868 | 463 |
| 7259 | 13 | OOEOOOEOOOEEE | 8 | 5815 | 1444 |
| 6747 | 13 | OOEOOOEOOEOEE | 8 | 5405 | 1342 |
| 5723 | 13 | OOEOOOEOOEEOE | 8 | 4585 | 1138 |
| 4955 | 13 | OOEOOOEOEOEOE | 8 | 3970 | 985 |
| 5979 | 13 | OOEOOOEOEOOEE | 8 | 4790 | 1189 |
| 4251 | 13 | OOEOOOOEOEEOE | 8 | 3406 | 845 |
| 5275 | 13 | OOEOOOOEOEOEE | 8 | 4226 | 1049 |
| 5787 | 13 | OOEOOOOEOOEEE | 8 | 4636 | 1151 |
| 4507 | 13 | OOEOOOOEEOOEE | 8 | 3611 | 896 |
| 3483 | 13 | OOEOOOOEEOEOE | 8 | 2791 | 692 |
| 5371 | 13 | OOEOOEOOOOEEE | 8 | 4303 | 1068 |
| 4859 | 13 | OOEOOEOOOEOEE | 8 | 3893 | 966 |
| 3835 | 13 | OOEOOEOOOEEOE | 8 | 3073 | 762 |
| 3067 | 13 | OOEOOEOOEOEOE | 8 | 2458 | 609 |
| 4091 | 13 | OOEOOEOOEOOEE | 8 | 3278 | 813 |

For every table row, the parity word, a and output are verified by the elementary j-step arithmetic (explicit values above). The words have exactly the asserted number of Os; `3^a<2^j` at all four depths: j8,a5 (243<256); j10,a6 (729<1024); j12,a7 (2187<4096); j13,a8 (6561<8192). Every listed seed strictly drops; the lemma proves each entire congruence class. All rows lie within the original five 27-mod32 residual classes modulo256; no two rows overlap because they come from a prefix-free parity-residue refinement. None intersects the previous S006 three cylinders.

At common depth13 each new row of depth j occupies `2^(13-j)` distinct classes, hence the **exact** new count is `1*32 + 3*8 + 7*2 + 19*1=89` of 512. Old count `11/16=352/512`; disjoint total `(352+89)/512=441/512` or 86.1328125%; remaining `71/512` or 13.8671875%. Both r=27,43 mod48 are congruent 11 mod16; CRT with 2^j gives the same count in each, since gcd(48,2^j)=16 and each of the 512 possible mod2^13 classes is represented exactly once in the 512 consecutive starts r+48m (m=0..511). Thus the fractions are exact relative natural densities and exact finite CRT counts, **not** convergence probabilities. For each certified cylinder, infinite composites exist within either r27 (all multiples3) or r43 (impose the additional independent congruence n≡0 mod7 using CRT and take n>7). The 71/512 remains unproved; these cylinders neither exclude a whole hypothetical least-counterexample class nor establish global Collatz.

## CP-0034 — infinite fully strict first-crossing TWO-O-RUN cylinders

Fix integer a>=3. Let b=b(a) be the least **positive** integer with `X=2^(a+b+2)>P=3^(a+1)`. Since `3^(a+1)>2^(a+3)` for a>=3, b>=2. The word is `O^a E O E^b`, two O-runs separated by one E. Let `M=2^(b+2)`, and t run over the positive integers satisfying `P*t≡1 (mod M)`, or `t=t0+M*q`, q>=0, `t0=P^(-1) mod M` the unique representative in [1,M]. Set `n=2^a*t-1`.

**Exact parity/algebra:** for i<=a, after i initial odd steps the value is `3^i*2^(a-i)*t-1`, hence a initial odd inputs. The inverse congruence implies `3^a*t≡3 (mod4)`, so `3^a*t-1` is even and its half is odd; the following parity letters are E,O. After this O the iterate is `(P*t-1)/4`, divisible by 2^b, and the next b input letters are E. The end value is
`T^(a+b+2)(n)=(P*t-1)/M`.
Exactly,
`n-T^(a+b+2)(n) = ((X-P)*t -(M-1))/M`.
The odd-input coefficient equals `P/X<1` for the first time at the final (bth) E: at the prior E it is >=1 by minimality b; earlier O and single E prefixes also have slope >1 since a>=3.

**Positive strict descent on an infinite set of a:** Suppose `4X>=5P` (equivalently X/P>=5/4). Then `X-P>=X/5`, while `M-1=X/2^a-1<=X/8-1`. Therefore `(X-P)*t-(M-1)>0` for EVERY positive admissible t, including the least representative. Equality `(X-P)*t=M-1` is impossible in this range, **by our direct inequality** (no imported cycle theorem).

**Infinitely many eligible a without irrational-distribution assumptions:** Put `Q_a=X_a/P_a`, where b(a) is minimal; thus 1<Q_a<2. If Q_a>=5/4, a is eligible. If Q_a<5/4, then at a+1 keeping b(a) gives ratio `(2/3)Q_a<1`, whereas increasing b by one gives ratio `(4/3)Q_a` in (4/3,5/3), hence b(a+1)=b(a)+1 and **a+1 is eligible**. At least one of every consecutive pair a,a+1 (a>=3) is eligible. Each has infinitely many positive t and, by CRT, infinitely many composite starts (choose t lifts yielding n multiple of any odd prime not dividing 2^a*M, e.g. 7). Therefore this gives an infinite exponent family of positive multi-block first-crossing strict-descent cylinders. It does NOT cover all two-run words, the near-resonant bad-a exponents, or arbitrary Collatz starts. This is separate from Steiner's published 1-cycle theorem and is **not asserted novel**. Simons/de Weger already study 2-cycles; we do not claim that our specific direct sufficient inequality generalises their cycle exclusion.

## CP-0035 — every fixed first-descent horizon fails inside the hard 27 mod256 subtree

For every integer H>=8, there exists a unique residue `r_H mod2^H` whose initial H parity word is
`w_H=OOEOOOOO O^(H-8)`.
The first eight letters are those of n=27, so `r_H≡27 (mod256)`. To extend any j-bit parity cylinder by an intended next odd letter, choose uniquely between its two lifts r and r+2^j: their jth iterates differ by `3^a`, an odd integer, and hence have opposite next parity. This constructs every r_H without assuming a divergent *integer*.

For j=1..8, w8 has O counts 1,2,2,3,4,5,6,7. Consequently `3^(a_j)>2^j` for EVERY one of the eight prefixes (e.g. at j8, 2187>256). Every later input is O, which multiplies the coefficient by 3/2 at each further step, so `3^(a_j)>2^j` persists for all j<=H. By the parity-affine identity `T^j(n)=(3^(a_j)n+B_j)/2^j`, with B_j>=0, **every positive n≡r_H mod2^H satisfies T^j(n)>n for all 1<=j<=H**.

For either r=27 or43 (mod48), CRT yields infinitely many n≡r_H mod2^H because `r_H≡27≡43 (mod16)`. In r27 the numbers are multiples3 and can be taken >3; in r43 impose also n≡0 mod7 and n>7. Therefore each of the TWO difficult least-counterexample classes contains infinitely many COMPOSITES also congruent 27 mod256 with no descent in any of the first H steps, for arbitrary H. It is logically impossible to derive a **uniform** fixed bound H for first descent even on this residual subtree.

The nested r_H describe a **2-adic parity path**; they need NOT correspond to one ordinary finite positive integer which never descends. Their existence is NOT a divergent Collatz orbit or a counterexample to eventual per-start descent. This kills bounded-horizon/finite-depth residue completion of this subtree, but NOT adaptive unbounded-time ranks or globally valid per-start descent.

## Attack C / falsifiers / remaining logical gap

The only actual decreasing rank proved in the certified cylinders is the elementary endpoint value R(n)=n after a prescribed finite cylinder-specific block; repeated descent globally is NOT proved because the union does not cover all positive integers. No global multi-step, terminal-state, nonlinear or lexicographic well-founded rank has been constructed. CP-0035 decisively falsifies any proposed fixed-H completion for the 27 mod256 residual; CP-0032 remains the independent no-go for separable one-U potentials. Adversarial controls 7 (the j8 paradoxical extension is AFTER its j7 descent), 27 (j59 first descent), 91 (j45 first descent), 121->91 (prime-factor growth), 15->23->35 (prime re-entry), 681->511 (valuation jump), 12t+3, and y≡0,1 mod3 inverse-source obstructions do not follow from cylinder density and must be explicitly faced by S008. In particular, a nested coefficient-noncrossing prefix does not establish existence of a divergent n.

## Source and test status

S007 primary literature search did NOT retrieve the complete original Steiner, *A Theorem on the Syracuse Problem*, Congressus Numerantium XX (1978), 553–559. Thus S006's exact positive 1-circuit theorem remains **SOURCE_STATED through Lagarias' annotated bibliography**, NOT original-text verified. Simons/de Weger primary author manuscript v1.43 (2007) was opened at https://www.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.43%5B2007%5D.pdf , pp1–3, and explicitly says Steiner excluded nontrivial 1-cycles, Simons excluded nontrivial 2-cycles; their 2-cycle theorem is background, not the proof of CP-0034. Terras' paper publisher record https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/30/3/101028/a-stopping-time-problem-on-the-positive-integers and Rozier–Terracol article https://www.sciencedirect.com/science/article/pii/S0012365X26001913 re-confirm coefficient stopping time is a known open problem. No priority claim is made for the arithmetic refinement or multi-block band.

Independent local exact Python `/mnt/data/s007_independent.py`, SHA256 `ae653f33a162f3c256d3c2e03a1e1873a351ced451490e6907023ce736fb6cb0`, tested all 30 rows and seven lifts, 512 CRT start representatives in each mod48 class, good a in 3..200 and 3 q lifts, full fixed-prefix constructions H8..128, both composite CRT intersections. Audit JSON SHA256 `4bda38601fdc6874c36b125696ea5c37a594ec40d4b7a4d63bcc0a2b3e56e8c8`. Local git clone unavailable (DNS resolution failure); original repository unittest/S000 manifest/JSONL consumer and corruption suite were **NOT** run in the independent container. New in-repo `tests/test_s007_math.py` is intended for hosted CI, which must be observed separately at PR and merged main. Proofs above are exact quantified algebra + finite explicit certificates, not extrapolation from the finite probes. Universal CP-0007 and CST CP-0019 remain OPEN.
