# S024 — integer-dependent admission barrier and formal Bool parity-word semantics

Date 2026-10-16. Global Collatz, all-composite convergence and Terras coefficient stopping-time conjecture **OPEN**. CP-0079/80/81 **PROVED_INTERNAL** (elementary/classical apparatus, novelty not established); CP-0082 exact new conditional Lean semantics verified only at a hosted SHA that actually compiled.

## Definitions and quantifier discipline

T(n)=n/2 for even n, (3n+1)/2 for odd n. Input parity words use O for odd and E for even. Every finite word V of length L and r odd symbols has an integer-affine triple A=3^r, Q=2^L and nonnegative B, with Q T^L(n)=A n+B for any actual orbit following V. Classical parity lifting supplies a unique n mod Q for each prescribed finite V; no such selected finite cylinder covers *all* positive n. S023's admission atoms: L_a=O^aE for a≥3, P=O³EO²E, F=O⁴EO²E, R=O²EO⁴E; only selected cylinder extensions have proven strict descent.

## CP-0079 — a periodic 2-adic shadow defeats bounded grammar admission

Define V=OOEE. On its parity cylinder n≡3 (mod16), four genuine T steps yield F(n)=(9n+5)/16; check n=16a+3 has orbit 16a+3 ->24a+5 ->36a+8 ->18a+4 ->9a+2, thus OOEE. The rational F-fixed point is **5/7**, a 2-adic integer because 7 is odd, but **NOT** a positive integer T-cycle.

For each k≥1, let r_k be the unique residue 0≤r_k<16^k with 7r_k≡5 (mod16^k). It exists by gcd(7,16)=1 and r_k≡3 (mod16). Whenever 7n≡5 (mod16^k), its first four input parity bits are OOEE and, setting n'=F(n), exact identity

    16(7n'−5)=9(7n−5)

makes 7n'−5 divisible by 16^(k−1). By induction the first **4k** parity bits of any positive such n equal (OOEE)^k. Exact iterate F^k(n)=[9^k n+5(16^k−9^k)/7]/16^k; the division by7 is exact since 16^k≡9^k (mod7).

Any four-symbol subword of infinite (OOEE)^∞ is one of OOEE, OEEO, EEOO, EOOE. Every S023 atom starts OOO or OOEO. Neither occurs. For any proposed time horizon H choose k with 4k≥H+4. No S023 atom can start **and complete** within first 4k bits at any start time i≤H (indeed none of the required first 3/4 bits appears). Since gcd(3,16^k)=1, the progression r_k+t16^k includes infinitely many **composite** multiples of3 greater than3. Thus NO finite uniform bound H on initial or delayed admission of all composites to an S023 atom can be justified by bounded-prefix membership. Quantifiers: ∀H ∃infinitely many *different finite positive* n avoiding admission up to H; NOT ∃a single positive n avoiding admission forever. The coherent infinite itinerary belongs to the 2-adic 5/7, and cannot be called a positive divergent orbit.

This is an application of classical parity/2-adic conjugacy, especially Bernstein–Lagarias 1996, not an independent novelty claim.

## CP-0080 — all six hard mod48 classes have arbitrary overcritical composite prefixes

Fix arbitrary H≥6. For each r in {7,15,27,31,39,43} define the H-bit word

- r≡7 mod16: V_H=OOOE O^(H−4).
- r≡15 mod16: V_H=OOOOE O^(H−5).
- r≡11 mod16: V_H=OOE O^(H−3).

(The spaces only indicate concatenation.) The first 4,5,3 bits force n mod16 to be respectively 7,15,11. The standard 2-adic parity-lifting induction yields one residue modulo2^H realising the full V_H: if n realizes the first i bits, n+2^i retains those bits and changes the parity of T^i(n), because its affine odd coefficient 3^#O is invertible mod2; induction is constructive. CRT with mod3 selects the prescribed r mod48. CRT with mod5 (coprime to 48*2^H) further selects n≡0 mod5, providing **infinitely many composite** positive lifts in EVERY r class; no assumption about the convergence of those integers is used.

For every nonempty prefix of these words, A=3^#O > Q=2^length: before the lone E this is immediate; immediately after E it is respectively 27/16, 81/32, or 9/8, all >1, and following O factors multiply A/Q by 3/2. Since B≥0, the exact actual-word affine equation implies T^j(n)>n for **all** 1≤j≤H. Thus each hard class has infinitely many composite witnesses of no strict descent through any *specified finite* H. This rules out uniformly bounded descent or fixed finite-state horizons in all six classes. It is compatible with eventual descent for every fixed positive integer and is closely related to previously recorded CP-0035, CP-0049; no originality is asserted.

Specific grammar caveat: r≡7 and15 mod16 already possess L3/L4 initial atoms. CP-0080 refutes bounded **strict descent**, not initial grammar-atom admission in those classes. In r≡11 mod16, the word OOE O^tail starts neither OOO nor OOEOOOOE and has no complete later L_a block by horizon H; it strengthens the delayed nonadmission barrier in the two r27/r43 hard classes.

## CP-0081 — exact reversed O²E O³E 7/3-budget failure threshold

The reversed atom S=O²EO³E has (A,Q,B)=(243,128,287), A−Q=115. For U=S^k, recurrence under block concatenation yields
  H(U)=(B_U+Q_U)/A_U=287/115+(1−287/115)(128/243)^k.
Because 1−287/115<0 and 0<128/243<1, H(U) is strictly increasing to 287/115 (>7/3). Exact values H(S³)=32673271/14348907 <7/3 and H(S⁴)=8300314997/3486784401 >7/3. Hence **k=4 is the exact first failure** of the fixed H<7/3 carry sufficient bound for repetition of S. This does **not** imply a true Collatz overshoot, failure of every possible certificate or the existence of a nonconvergent orbit. Hostile selected-W tests for k=1..12 still give actual positive least-lift descent.

Compared to CP-0078: four initial L3 bank atoms suffice for unlimited following L2 atoms *in that fixed order* to preserve H<7/3; arbitrary interleavings and S blocks can destroy this particular budget. The fraction of short atoms tends to 1 only for the ordered banked construction, not an optimal density over all viable encodings. No universal optimality is proved.

## CP-0082 — incremental formal theorem (scoped)

Appended executable 'shortenedT', 'runWord', 'wordAffine', and 'wordAgrees' in CollatzPrimes.lean. wordAffine recurses from the head of arbitrary 'List Bool': prepending E sends (A,Q,B) to (A,2Q,2B), prepending O to (3A,2Q,A+2B). Structural induction using 2*T(n)=n (even) or 3n+1 (odd) proves

    wordAgrees n bs → (wordAffine bs).Q * runWord n bs
      = (wordAffine bs).A*n + (wordAffine bs).B.

This is an exact theorem about *actual matching words*, not proof that every word is realised by an integer or that its residue is unique. Earlier abstract carry-state fold and conditional all-lifts descent remain separately scoped. Nat bitlength bracket existence/uniqueness, unconditional CP-0071 gap, positive parity-cylinder existence/uniqueness, first-crossing bridge, CP-0076/78 fully compiled end-to-end and all-positive admission are **NOT YET FORMALISED**. A hosted Lean SUCCESS on specific checked-in source is required for FORMAL_VERIFIED; no sorry/admit/native_decide/unscoped axioms.

## Validation, source gates and conclusion

New exact stdlib Python S024 five tests: k=1..12 16^k-adic roots, CRT composite lifts, all finite OOEE horizons, H=10..64 step3 and six hard residue classes, reversed-macro rational fractions k≤13, historical 71/5041, 64k+59→72k+67, forced 2^H u−1 and 27/43/91/155/251/393243+524288k controls. Finite tests corroborate **separate mathematical proofs** and do not verify infinite existence independently. S000 fixture, S001 depths10–16 and S003 corruption are original hosted unit/CI gates, not reconstructed locally.

Primary source reinspection: Bernstein–Lagarias (1996) original author PDF p1–3 (equations (1.5)–(1.6), parity coding 2-adic conjugacy) actually accessible; no entire 16pp proof re-derived. Terras 1976 publisher article and full-text link available but publisher PDF 403; indexed historical matwbn mirror shows original first page in search excerpt but its full PDF direct fetch also 403: **NO full original 12pp article read**. Steiner 1978 original not obtained; Lagarias annotated secondary theorem description only. Rozier–Terracol 2026 publisher full HTML abstract/introduction confirms CST conjectural, parity-affine remainder classical. This is NOT a source-complete novelty audit. No originality or publication claims.

**Conclusion:** New exact families obstruct specified bounded-time integer-admission/descent mechanisms; they do not supply a single infinite positive orbit, unbounded integer-dependent well-founded rank or global Collatz proof. The 71/512 early residual, 5041-edge transducer and all six hard mod48 *eventual* problems remain.
