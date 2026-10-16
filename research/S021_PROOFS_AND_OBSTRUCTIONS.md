# S021 — arbitrary odd-run alphabet and formal affine-carry invariant

Date 2026-10-16. Shortened Collatz T(n)=(3n+1)/2 if odd, n/2 if even. O/E always refer to INPUT parities. Global Collatz and Terras' coefficient stopping-time conjecture remain OPEN.

## CP-0073 — PROVED_INTERNAL (inductive, exact, novelty UNCHECKED)

Let k ≥ 1 and let a₁,…,a_k be ANY integers ≥3, without any upper bound or periodicity requirement. Define U=(O^{a₁}E)…(O^{a_k}E). Write (A,Q,B) for its affine word parameters: 2^{|U|}T^{|U|}(n)=A n+B for an actual U-cylinder, A=3^{#O}, Q=2^{|U|}, and B updated by O: B↦3B+Q, E:B↦B. Then the **sharp block-preserved linear invariant**
    11 B + 19 Q ≤ 19 A
holds for every k (including k=0 with (A,Q,B)=(1,1,0)). In particular Q>0 and
    H(U)=(B+Q)/A ≤19/11−(8/11)(Q/A) <19/11<7/3.
All nonempty prefixes of U are overcritical: within each O run A/Q multiplies by 3/2, at E ending O^a E it is multiplied by 3^a/2^{a+1}≥27/16>1.

**Complete proof.** Appending O^a E to a state (A,Q,B) maps it to
    A'=3^a A, Q'=2^{a+1}Q,
    B'=3^a B+(3^a−2^a)Q.
The intercept expression follows by induction on a using (3^{a+1}−2^{a+1})=3(3^a−2^a)+2^a. Suppose 11B+19Q≤19A. Then
    11B'+19Q' = 3^a(11B+19Q) + (27·2^a−8·3^a)Q
              ≤3^a(11B+19Q)≤19·3^a A=19A'.
The penultimate inequality holds because 27·2^a≤8·3^a for every a≥3: equality at a=3, and multiplying an inequality by 2 vs 3 preserves it at the next exponent. Initial equality holds. Thus induction proves the stated invariant for ANY block ordering. Since Q>0, subtracting the positive term 8Q from 19A yields 11(B+Q)<19A. There are infinitely many possible alphabets, not just {3,4}.

Apply S020's independently internally proved CP-0071 to m₀=#O(U)+1. Choose d∈{1,2} with δ(#O(U)+d)>1/3. Let j=bitlength(3^{#O(U)+d}), b=j−|U|−d≥1, and W=U O^d E^b. Every positive actual W-cylinder input n has n≥2³−1=7, and H(U)<19/11<7/3. CP-0072's fully quantified sufficient condition applies: W has its first coefficient crossing exactly at j and T^j(n)<n for **ALL** positive W-cylinders, including the canonical least representative. Infinitely many composite representatives exist by the parity residue bijection and CRT mod 3. This follows as a corollary without Matveev and without assuming bounded a_i, consecutive repetitions, or periodicity.

**Strength over S020:** CP-0072's previous corollary allowed only runs a_i∈{3,4}; CP-0073 covers arbitrary sequences of unbounded a_i≥3. The weighted one-step invariant is the intended Lean formalization; even a formalized budget alone is not a formalized full first-crossing theorem.

## Sharpness and failed inferences

The weighted criterion 27·2^a≤8·3^a is satisfied exactly for integer a≥3; it FAILS for a=2 (108>72). Hence the specific global budget with constants 11,19 cannot be extended freely to O²E blocks: starting from (1,1,0), the first O²E already violates it (11·5+19·8=207>171). This is sharpness **of this Lyapunov bound**, NOT a proof that all a=2 cylinders overshoot or that no different certificate works. Indeed finite canonical least lifts checked for repeated OOE can descend; do not claim a counterexample to CST.

The δ>1/3 guarantee cannot be demanded for BOTH consecutive exponents: for m=5, 3^5=243, j=8 and δ=13/243<1/3 while for m=6 the gap is large. The constant 1/3 is optimal as a uniform two-consecutive threshold: write q_m=2^{j(m)}/3^m∈(1,2). If q_m≤3/2, q_{m+1}=(4/3)q_m; otherwise q_{m+1}=(2/3)q_m. Thus max(q_m,q_{m+1}) is ≥4/3, and is arbitrarily close to 4/3 for infinitely many m as q_m tends to 1 from above, by the classical density of fractional parts m log₂3 (irrationality follows from 2^r≠3^s for positive r,s). This sharpness invokes the classical irrational-rotation density theorem; not a new Collatz theorem.

The theorem certifies only CHOSEN parity extensions. It gives no rule that a fixed positive integer follows one, no all-integer admission/exit bound, no convergent-orbit certificate for the residual 71 of 512 or their 5041 compatible transition pairs. The expanding 393243+524288k, 64k+59→72k+67, 2^H u−1 and hard 27/43/91/155/251 families remain obstructions to naive global ranks; compatibility of all finite paths is NOT evidence for one infinite positive divergent orbit.

## Formalization scope

Lean 4 pinned to leanprover/lean4:v4.24.0, mathlib v4.24.0 in lakefile.toml. File CollatzPrimes.lean contains the Nat conjugated affine step and all-k product equality, abstract weighted-block carry preservation, arbitrary-list fold, 2^n≤3^n, 27·2^n≤8·3^n for n≥3, and the arbitrary length run-list budget. These are the formalization TARGETS. Only a successfully observed hosted Lean compilation may upgrade these to FORMAL_VERIFIED. Neither the full Collatz word-realization condition nor CP-0071 or CP-0072 first-crossing is encoded in Lean here; do not promote them.

Exact finite original Python tests cover 55,986 run-list sequences of lengths 1..6 with a_i∈[3,8], checking the weighted inequality, canonical first-crossing lifts, and descent. Additional local independent scratch script /mnt/data/s021/probe.py SHA256 c5ddd2d3a31c31df0802641cb223f0106e633b880aa3518058c1117b07302aaf and output log SHA256 c6a4b21ea362372b099f742212b2a3cfdac677371dd0264eeb41489734cd07302aaf cover controls; those scratch files are not claims about GitHub contents.

## Primary-source novelty gate

Bernstein–Lagarias, *The 3x+1 Conjugacy Map*, Canadian J. Math. 48 (1996) 1154–1169, ORIGINAL 16-page authors' PDF at https://websites.umich.edu/~lagarias/doc/bernstein.pdf, was accessed. At p2 equations (1.5),(1.6) it explicitly supplies the complete 2-adic parity-vector map and its conjugacy, so finite parity classes and affine transformations must be treated as CLASSICAL, not original. Terras, *A stopping time problem on the positive integers*, Acta Arith. 30 (1976), 241–252: ORIGINAL publisher listing and CC-BY PDF link at https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/30/3/101028/a-stopping-time-problem-on-the-positive-integers inspected, but the download endpoint returned HTTP403; 12-page article content NOT read. Specific novelty of the variable a≥3 weighted invariant NOT DETERMINED. Steiner 1978 full original remains unavailable. No publication readiness or independent referee inspection.

CP-0073 is mathematical internal proof only pending any formal CI result; the precise formal targets and CI provenance are tracked in validation/S021_LOCAL_PROBES.md and sessions/S021/CLOSEOUT.md.

## Completed hosted formal evidence, precisely scoped

On GitHub branch head 7f845a78e7c091979d78063dba9da357b61fc81e, the pinned **Lean 4 v4.24.0/mathlib v4.24.0** actual `lake build --wfail` successfully compiled `CollatzPrimes.lean` without `sorry`, `admit`, `native_decide` or new axioms (original branch run 38887018859/job116927112890; original PR #36 run 38887024972/job116927132157). Both jobs' build and no-admitted-marker steps individually passed. FORMAL_VERIFIED **ONLY**: `conjugate_step`, `conjugate_iterate`, `carry_budget_step`, `carry_budget_fold`, `pow_two_le_three`, `carry_weight_next`, `carry_weight_ge_three`, and `variable_runs_budget`. The encoded `variableRunState` uses abstract blocks and the algebraic parameters; full input parity realisation, CP-0071 exponent gap, full CP-0072 first-crossing theorem, infinite composite lifts, universal convergence, originality and Palomar are NOT formal-verified. The earlier first Lean CI failure was a missing Lake manifest, then two Lean tactic issues, both corrected and verified on this exact SHA. Separate CI on the subsequent provenance-only attestation SHA and merged main must still be observed.
