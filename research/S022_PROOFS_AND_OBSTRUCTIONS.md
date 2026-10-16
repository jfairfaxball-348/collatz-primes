# S022 — mixed O² odd-run admission via a certified paired macro

Date: 2026-10-16. Shortened Collatz: T(x)=(3x+1)/2 for odd x; x/2 for even x. Parity O/E always refers to the INPUT. The composite-to-1 target and Terras coefficient stopping-time conjecture are OPEN. Novelty NOT ESTABLISHED.

## CP-0074 — PROVED_INTERNAL, strict extension of CP-0073

Let U be an arbitrary NONEMPTY finite concatenation of the following ATOMS in any order:
- L_a=O^a E, with arbitrary integer a>=3 (unbounded and variable);
- M=O^4 E O^2 E, in that ORDER, as a combined macro.

For a parity word V, let (A_V,Q_V,B_V) be determined by (1,1,0), O:(A,Q,B)->(3A,2Q,3B+Q), E:(A,Q,B)->(A,2Q,B). Thus actual parity-cylinder n satisfies Q_V T^|V|(n)=A_V n+B_V.

**Theorem.** For every U of this grammar, including any mixture and arbitrarily many M atoms:
(1) Psi(U):=19 A_U-11 B_U-19 Q_U >= 0;
(2) H(U):=(B_U+Q_U)/A_U < 19/11 < 7/3;
(3) every nonempty prefix V of U is coefficient-overcritical, A_V>Q_V;
(4) there exists a selected d in {1,2} such that with r=#O(U), m=r+d, j=bitlength(3^m), b=j-|U|-d>=1 and W=U O^d E^b, the first coefficient crossing occurs exactly at position j, and T^j(n)<n for EVERY positive integer with actual W input parity word; these W-cylinders include infinitely many positive composite inputs.

**Proof.** Composition of exact affine parameters gives for a block L_a: (A',Q',B')=(3^a A,2^(a+1)Q,3^a B+(3^a-2^a)Q). Direct expansion of its slack yields Psi'=3^a Psi+(8*3^a-27*2^a)Q, whose second coefficient is >=0 for a>=3 (equality a=3). For M compute O^4E=(81,32,65), O^2E=(9,8,5), and their ordered composition M=(729,256,745). Therefore (A',Q',B')=(729 A,256 Q,729 B+745 Q) and exact Psi'=729 Psi+792 Q. The empty word has Psi=0, Q=1. Induction over arbitrary mixed atoms proves Psi>=0. Rearranging: 11(B+Q) <= 19 A-8 Q <19 A since Q>0, proving H<19/11. Each L_a multiplies A/Q by 3^a/2^(a+1)>=27/16>1. The complete M multiplies it by 729/256>1; INSIDE M, O^4E gives 81/32>1 at its E, while the subsequent O^2E gives a further factor 9/8>1, and O steps only increase A/Q. Starting with an O^a (a>=3) or O^4, all nonempty prefixes are overcritical.

S020 CP-0071 gives for r+1 or r+2 some m with delta=(2^bitlength(3^m)-3^m)/3^m>1/3. Overcriticality before the trailing E implies b>=1 and makes its final position j the FIRST coefficient crossing, as earlier coefficients are overcritical and each earlier tail position t<j satisfies 2^t<=2^(j-1)<3^m. Appending O^d E^b gives exact B_W/3^m=H(U)-2^(|U|+d)/3^m < H(U) <7/3. Every positive W representative begins OOO, so n=8v-1>=7. Hence delta*n > 7/3 > B_W/3^m, so D*n>B_W with D=2^j-3^m>0. In the exact affine equation 2^j*T^j(n)=3^m n+B_W, this proves T^j(n)<n. Every finite input parity word determines exactly one residue modulo 2^j (the odd 3^r coefficient makes the next parity bit toggle when input is translated by 2^i), so there is a unique least positive representative and infinitely many lifts n0+q*2^j. As gcd(2^j,3)=1, infinitely many such lifts are multiples of 3 exceeding 3, hence composite. QED.

**New content:** M includes a genuine O^2E run and is not a CP-0073 standard atom. The linear weighted invariant allows this shorter run when paired in the specified order with a preceding O^4E. Still nonselective INTEGER admission is unproved: this theorem selects parity extensions rather than proving any given positive integer follows them, and implies no universal convergence or known-integer divergent example.

## CP-0075 — PROVED_INTERNAL negative boundary; exact quantified countermodel to a stronger budget assertion

The reverse two-block macro M_rev=O^2E O^4E has affine parameters (729,256,925). From initial (1,1,0), its weighted budget violates the claimed uniform inequality by
    11*925 +19*256 -19*729 = 1188 >0.
Conversely M has a positive slack exactly 792. Thus any theorem allowing ALL permutations of the two individual short-run blocks without qualification, while asserting the SAME 11/19 budget, is FALSE. This is NOT evidence of actual first-coefficient overshoot or failure of Collatz/Terras CST. Also requiring BOTH d choices to pass delta>1/3 remains false already at m=5 (old S021 control).

## Formal scope

Checked-in S022 Lean declarations appendFourTwo, carry_budget_four_two, CarryAtom, carry_budget_atom, mixed_runs_budget; the actual two-consecutive-gap algebra is encoded CONDITIONED on a bitlength bracket (consecutive_gap_from_bracket, two_choice_gap_from_bracket). The all-lifts affine descent implication is encoded (all_lifts_strict_descent). The exact m->bitlength bracket existence, parity-step semantics, unique integer cylinder residue, precise first crossing and complete CP-0074 remain NOT FULLY ENCODED. "FORMAL_VERIFIED" is reserved solely for statements shown to compile on the pinned hosted toolchain at a specified source SHA; this mathematical proof alone does not make Lean claims.

## Finite hostile testing

Independent standard-library scratch script /mnt/data/s022/probe.py SHA256 ed94e237402ff44496b3916abbbf3ec65aa25c61a2d33a082d226af005850858; JSON output SHA256 0e010543d7e1f9a7f074a5fdbda779b321aa6ed35bf8d7d44251c36d7f822463. It checks all 3905 strings of 1..5 atoms from {L_3,L_4,L_5,L_6,M}, including 2541 with M; 2251 use selected d1 and 1654 use d2; 11715 actual positive trajectories (canonical least representative + two lifts), all first crossing and strict descent. 3329 words have an UNSELECTED other d that fails the simple delta>1/3 margin; these are not overshoot counterexamples. Minimum tested exact descent margin D*n0-B_W is 256. Hostile 71/512 early residual = 5041 ordered pairs remain. The original full GitHub Actions finite-sanity-checks job must be scoped to its exact PR commit.

## Source novelty gate

Riho Terras 1976 12pp original publisher metadata and CC-BY open-download link https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/30/3/101028/a-stopping-time-problem-on-the-positive-integers inspected, but publisher PDF and EU-DML https://eudml.org/doc/205476 are access-denied (HTTP403); ORIGINAL FULL TEXT NOT READ. Bernstein–Lagarias 1996 original authors' 16-page PDF https://websites.umich.edu/~lagarias/doc/bernstein.pdf p2 equations (1.5)–(1.6) directly inspected: the 2-adic parity coding is CLASSICAL. Rozier–Terracol 2026 publisher abstract https://www.sciencedirect.com/science/article/abs/pii/S0012365X26001913 concerns paradoxical behaviour and presents Terras' coefficient stopping-time as conjectural; it does NOT establish novelty for our restricted carry inequality. Steiner 1978 original not acquired. Until full independent prior-art audit, intrinsic originality/publication readiness UNCHECKED.

Global composite/all-positive Collatz convergence, Terras CST, priority, Palomar and independent referee certification all remain OPEN / UNCLAIMED.
