# S003 — coefficient stopping time, exceptional ranks, and m-step factor re-entry

**Date:** 2026-10-15. Map T(n)=n/2 for even n; (3n+1)/2 for odd n. U(x)=(3x+1)/2^{v_2(3x+1)} on positive odd x. Evidence levels: CP-0019 OPEN / known Terras conjecture; CP-0020, CP-0021, CP-0022 PROVED_INTERNAL elementary; finite tests separate. Global composite / full Collatz conjecture CP-0007 **OPEN**.

## A. Critical novelty kill: CP-0019 is Terras' Coefficient Stopping Time conjecture (OPEN; SOURCE_STATED)

Let a_j(n) be the odd inputs in the first j shortened T steps. Define j_c(n)=min{j>=1:3^{a_j(n)}<2^j}, j_s(n)=min{j>=1:T^j(n)<n}; undefined minima treated as infinity. The proposed equality j_s(n)=j_c(n) for ALL n>=2 is exactly **Terras' coefficient stopping time (CST) conjecture**, discussed by Lagarias and currently open. Primary modern independent treatment: Olivier Rozier and Claude Terracol, *Paradoxical behavior in Collatz sequences*, *Discrete Mathematics* 349(10) (October 2026), article 115167, doi:10.1016/j.disc.2026.115167, also arXiv:2502.00948. Its abstract and definitions identify this very conjecture. **NO proof or universal counterexample was produced in S003; this is not new.**

Crucial distinction: slope <1 at an arbitrary LATER j does **not** force descent. For n=7:
T^0..T^8: 7,11,17,26,13,20,10,5,8.
At j=7 there are four odd inputs and 3^4=81<2^7=128, T^7(7)=5<7: j_c(7)=j_s(7)=7.
At j=8 there are five odd inputs, coefficient 3^5/2^8=243/256<1, but T^8(7)=(243*7+347)/256=8>7. This is a known finite **paradoxical** prefix, but NOT a CST counterexample (first coefficient crossing is j=7).

## CP-0020: exact first-crossing intercept criterion and extremal bound (PROVED_INTERNAL, elementary; classical structure)

For any admissible parity word w of length j with a odd steps, let odd positions (0-indexed) be 0<=t_1<...<t_a<j. The affine branch is 2^j T^j(n)=3^a n+b_j, with
b_j = sum_{i=1}^a 3^{a-i} 2^{t_i} >=0.
Proof: each O at position t adds 2^{t} to the numerator before all later O multiplications; induction or linear composition yields the expression. Swapping adjacent O,E to E,O increases b_j while preserving j and a; hence
**3^a-2^a <= b_j <= 2^{j-a}(3^a-2^a)** for a>=1, with equality on all O's earliest/latest respectively (for a=0 b=0).

For n>=2 and finite first coefficient crossing j=j_c(n), every earlier prefix has 3^{a_i}>=2^i and b_i>=0, so T^i(n)>=n for i<j. Define D=2^j-3^{a_j}>0. Then
**j_s(n)=j iff D*n>b_j.**
If D*n<=b_j, then j_s(n)>j or is infinite: this is a CST exception candidate, not a contradiction. For the unique least positive parity-residue representative r in [1,2^j), every n=r+q2^j, q>=0, has the same first j parities, j_c=j, and
j_s(n)=j exactly when D(r+q2^j)>b_j.
The potentially bad q form the **exact finite interval**
0<=q<=floor((b_j-D*r)/(D*2^j)) if b_j>=D*r; otherwise empty. In particular every coefficient-crossing cylinder eventually has j_s=j_c. This is a rederivation of the classical finite-exception principle, NOT a new novelty claim.

For r=1, the first crossing occurs at j=2, with D=1, b=1; n=1 is nonstrict T^2(1)=1, but every lift n=1+q*4 with q>=1 descends at j=2. Arbitrarily long O prefixes on 2^k t-1 have no coefficient crossing in their first k steps. None of these calculations proves j_c(n) finite for each n>1 or CST globally.

A worked S002 branch: for the first crossing j=59 at n=27, a=37, D=126176846412426125, b=1100931843921811423. Here 27*D>b, and every n=27+q2^59 (q>=0) has first descent at j=59. Do not extend this to 27 mod 2^16.

## B. Exceptional transfer and CP-0022 fixed-modulus no-go (PROVED_INTERNAL, scoped)

For r>1 at depth k, OPEN means no i<=k satisfies 2^i T^i(r)<2^i*r. By the affine identity, an OPEN representative may have a subunit slope only if it is a CST exception to equality at its first crossing; this possibility is **not ruled out universally**. The empirical equality OPEN iff every prefix slope >=1 for r>1 up to k16 is finite evidence, and proving it for all r,k would imply the unsolved CST conjecture.

**CP-0022:** Fix a modulus 2^k, k>=1. There exists NO assignment of a finite nonnegative step bound h(r) for each residue r mod2^k such that every positive n>1 has some j<=h(n mod2^k) with T^j(n)<n. Proof: take r=-1 mod2^k and H=max(k,h(r)) (if h(r)=0 choose H>=1). Choose n=2^H t-1>1, with t large enough (e.g. t=2); its first H inputs are O, and for 1<=j<=H,
T^j(2^H t-1)=3^j 2^{H-j}t-1, as induction through the O branch shows: an odd input of the form 2^h c-1, h>=1, maps to 3*2^{h-1}c-1. For 1<=j<=H the multiplier ratio (3/2)^j>1, so T^j(n)>n. Thus it never descends during h(r). This kills **finite per-residue stopping-time tables for fixed k**, not adaptive parity depth, valuation/mixed-modulus automata or every possible well-founded rank. The 2-adic infinite all-O path -1 is not a positive integer.

No genuinely descending universal exceptional rank was found. For reverse U, y divisible3 lacks predecessors and y≡1 mod3 has only larger positive odd predecessors; these cases do not imply nonconvergence (3->5->1). Six hypothetical least counterexample residues remain 7,15,27,31,39,43 mod48 without elimination.

## C. CP-0021: m-step accelerated odd factor re-entry (PROVED_INTERNAL, elementary)

For x=x_0 positive odd, set x_{i+1}=U(x_i), a_i=v_2(3x_i+1)>=1 and A_i=sum_{t=0}^{i-1}a_t (A_0=0). For every m>=1:
**2^{A_m}x_m = 3^m x_0 + F_m, F_m=sum_{i=0}^{m-1} 3^{m-1-i}2^{A_i}.**
Proof: F_1=1; multiplying 2^{a_m}x_{m+1}=3x_m+1 by 2^{A_m} yields F_{m+1}=3F_m+2^{A_m}, which unfolds as stated. Since x_0 is odd, 2^{A_m} is invertible mod x_0, so
**gcd(x_0,U^m(x_0))=gcd(x_0,F_m).**
The m=1 offset 1 recovers coprimality. m=2 yields F_2=3+2^{a_0}, CP-0016. m=3 yields 9+3*2^{a_0}+2^{a_0+a_1}. This identity constrains re-entry but has no sign or monotone factor-count implication. Hostile trajectories: 15->23->35 (5 returns); 121->91 (new distinct factors 7,13); 27->41->31; 12t+3->18t+5 (t>=1, first U increases); y divisible3 has no odd U-predecessor. No adaptive or bounded m rank shown.

## D. Direct exact finite execution (EXPERIMENT, not theorem)

S003 preregistered discovery n=2..100000 and disjoint holdout n=100001..1000000, each checking up to 1000 shortened steps for j_s and j_c (independent affine recurrence each step). Both ranges had **zero unequal pairs and zero capped starts**. This is finite support for known CST, not a proof.

Separate exact direct enumeration of **positive odd r>1** at k=10..16 produced OPEN representative counts 64,128,226,367,734,1295,2114; among those zero had a coefficient crossing at any j<=k. These reproduce S001 totals but provide no universal inference. The direct 27 parity-word audit returned x_59=23, odd count37, offset b above. Independent Python recurrence checked the m-step formula and gcd for m=1..6 on x in {15,35,121,27,3,51,243,231}. No claim this alone ran or compared the original repository's producer or consumer; GitHub hosted CI will be observed separately.

## Sources and priority kill

Terras R. (1976), *A stopping time problem on the positive integers*, Acta Arithmetica 30; Jeffrey Lagarias *3x+1* surveys; Rozier–Terracol above are **direct prior art** to CP-0019/CST, prefix affine remainders and finite exceptions. No originality for CP-0020/21/22: elementary corollaries of standard formulas/CP-0012. The current source review also read Christian Hercher's two-page June 14 2026 *Corrigendum to Article 23.3.5* at https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf . It explicitly corrects an erroneous inequality derivation **in Theorem 21**, replacing it with a convex-polytope maximisation argument. No technical m-cycle bound or global claim was imported; Simons–de Weger, Tao 2022 logarithmic almost-all, Bařina 2025 finite verification, Angeltveit 2026 finite algorithm remain background, not proof inputs. Source-to-claim dependencies are elementary algebra except CP-0019's external identification. **Global theorem OPEN; no Lean/Palomar, novelty or publication certificate.**
