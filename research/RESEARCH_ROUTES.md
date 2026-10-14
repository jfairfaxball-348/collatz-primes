# Research programme — routes to composite convergence

**Global theorem:** forall n>=4 composite, exists k>=0: T^k(n)=1. CP-0001 shows equivalence with ordinary Collatz. Preserve this exact quantified target.

**Route A — composite descent via factor structure (priority).**
Search for a noncircular potential V(n) involving factors, least prime factor, v2(3n+1), smoothness, or prime-divisor changes. Prove that every odd composite n has a finite iterated T descent to a smaller certified integer or prove a safe structural dichotomy. Pressure-test against odd primes, 3 mod 4 classes and nonmultiplicativity. Do not assume prime factors of n control factors of 3n+1.

**Route B — residue/certificate compression.**
Construct exact affine parity certificates for progressively refined classes; mathematically characterise leftover classes where no shorter-start descent is forced. Test whether a finite symbolic graph, a well-founded ranking, or reverse-edge induction supplies a globally complete certificate. Identify why any finite 2-adic partition without a well-founded global argument is insufficient.

**Route C — prime/composite transition graph.**
Track primes, composites and special families under T and the accelerated odd map, including consecutive prime transitions, gcd reset and factorization. Separate primes guaranteed to reach composite from the still-open claim that all relevant trajectories converge.

**Route D — reverse basin and certified predecessor families.**
From a certified y, y->2y is always a predecessor; y->(2y-1)/3 requires y=2 mod 3 and produces a positive odd predecessor. Search for a compact complete inverse-graph or arithmetic parametrization with a **coverage proof** rather than generating only a subset.

**Route E — literature, hostile audit, formalisation.**
Compare with rigorous work by Lagarias, Tao and Barina; never treat almost-all results as all. For any plausible universal lemma run adversarial small examples and a proof review. Mature exact claims can be promoted to Lean/Palomar only after specifying a theorem that is actually new and proved.

Acceptance for a headline breakthrough: complete quantified proof over all composite n, genuine finite-to-infinite closure, hostile audit of equivalence and circularity, novelty check and independent verification. Reports must also explain what remains OPEN.
