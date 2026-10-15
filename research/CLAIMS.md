# Claim register (actual evidence tier and novelty separate)

| ID | Status | Statement | Evidence |
|---|---|---|---|
| CP-0001 | PROVED_INTERNAL elementary | Composite convergence iff full Collatz via 2p->p | research/S000_FOUNDATIONS.md |
| CP-0002 | PROVED_INTERNAL elementary | Even, 1 mod4 and 3 mod16 strictly descend in <=4 steps, least nonconvergent must be 7/11/15 mod16 | research/S000_FOUNDATIONS.md |
| CP-0003 | PROVED_INTERNAL elementary | For odd n gcd(n,T(n))=1; selected prime transitions | research/S000_FOUNDATIONS.md |
| CP-0004 | PROVED_INTERNAL elementary | Fixed parity-prefix affine iterate identity and eventual descent | research/S000_FOUNDATIONS.md |
| CP-0005 | PROVED_INTERNAL conditional on classical Dirichlet | Every odd 2^k residue contains infinitely many primes and composites | research/S000_FOUNDATIONS.md |
| CP-0006 | FINITE_TEST ONLY | [2,10000] sanity to 1 and 4790 parity assertions | validation/S000_audit.json |
| CP-0007 | OPEN | Every positive/composite integer reaches 1 | authoritative/STATE.json |
| CP-0008 | PROVED_INTERNAL elementary | Odd n>0 and each odd p|n: p∤U(n), gcd(n,U(n))=1, with exact U/T and n=1 cases | research/S001_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0009 | PROVED_INTERNAL elementary | Global strict descent for all n>1 iff full convergence | research/S001_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0010 | PROVED_INTERNAL elementary | Complete inverse U formula and mod3 exponent parity; least positive nonconvergent cannot be 5 mod6 (necessary 6 classes mod48) | research/S001_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0011 | PROVED_INTERNAL algebra + FINITE_CERTIFICATE | Symbolic strict-class affine criterion; 30653 STRICT, 1 BASE_1, 2114 OPEN at k16 under j<=k | validation/S001_manifest.json; tools/check_residue_certificates.py |
| CP-0012 | PROVED_INTERNAL elementary | E_(k+1) projects inside E_k; for all k, composite integers ≡-1 mod2^k exist with no first-k descent; 2-adic -1 non-positive | research/S001_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0013 | PROVED_INTERNAL soundness; OPEN global completeness | Reverse grammar from 1 generates exactly convergent odd seeds and doubling descendants, coverage of all odd positives unproved | research/S001_PROOFS_AND_OBSTRUCTIONS.md |

**Originality:** no originality claim for CP-0001—CP-0013; prior art may subsume all elementary findings. Global CP-0007 still OPEN. Local exact finite computation is not external human proof verification or a Collatz theorem.

| CP-0014 | PROVED_INTERNAL elementary | Exact per-child E_k affine certificate transfer including early high-child thresholds and opposite new parities; no termination proof | research/S002_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0015 | PROVED_INTERNAL algebra, independently finite-word checked | Every n=27+2^59*q (q>=0) has first strict descent at shortened T-step59 | research/S002_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s002_structure.py |
| CP-0016 | PROVED_INTERNAL elementary | For odd x with a=v2(3x+1), gcd(x,U²(x))=gcd(x,2^a+3); factor5 reappears for 20t+15 | research/S002_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0017 | PROVED_INTERNAL elementary | For every odd x and j>=1, 3 does not divide U^j(x); odd multiples3 have no odd U-predecessor | research/S002_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0018 | PROVED_INTERNAL elementary | No fixed modulus 2^k alone determines U(x) mod3 on all positive odd x | research/S002_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0019 | OPEN / FINITE OBSERVATION ONLY | Does first strict descent occur exactly at first parity-slope 3^{a_j}<2^j for every positive n>1? S003 proof/refutation target | authoritative/NEXT_SESSION_PROMPT.md |

**S002 novelty:** not established for any CP-0014—CP-0018; algebra is elementary and likely classical in broader form. No global proof.

| CP-0020 | PROVED_INTERNAL elementary; known prior-art framework | Exact first coefficient-crossing intercept test and finite bad-lift cutoff; extremal fixed-(j,a) bound on intercept; no CST proof | research/S003_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0021 | PROVED_INTERNAL elementary | For all positive odd x and m>=1, 2^A U^m(x)=3^m x+F_m and gcd(x,U^m(x))=gcd(x,F_m) | research/S003_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0022 | PROVED_INTERNAL scoped no-go | No fixed 2^k residue table of finite first-descent horizons can cover all positive starts; not all adaptive/mixed automata | research/S003_PROOFS_AND_OBSTRUCTIONS.md |

**S003 prior-art correction:** CP-0019 is Terras' established OPEN Coefficient Stopping Time conjecture, not new; see Rozier–Terracol 2026, arXiv:2502.00948. Finite n<=1000000 agreement does not prove it. No originality claim for CP-0020—CP-0022.

| CP-0023 | PROVED_INTERNAL elementary; originality NOT ESTABLISHED | For first-crossing O^a E^b, a>=2, a suitable 3/4 slope band guarantees strict first-crossing descent for every positive representative; at least one of adjacent a qualifies. Exact criterion D*t>2^b-1. | research/S004_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s004_boundaries.py |
| CP-0024 | PROVED_INTERNAL scoped no-go | For any fixed M, finite per-residue first-descent horizon fails on any r=-1 mod2^v2(M); infinitely many positive composite counterexamples; in mod48 at r15 and31. Does not exclude adaptive state ranks. | research/S004_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0025 | PROVED_INTERNAL elementary | For all K>=3 infinitely many composite x with v2(x+1)=1 but v2(U(x)+1)>=K; e.g. 681->511. No decreasing valuation-only U rank. | research/S004_PROOFS_AND_OBSTRUCTIONS.md |

S004 novelty gate: CP-0023—0025 are elementary; no originality demonstrated; no Lean/Palomar or universal result.

| CP-0026 | PROVED_INTERNAL elementary | For every a>=2, O^a E^b first-crossing cylinder never overshoots: exact drop (D*t+1)/2^b-1>=0; ALL t=t0+q2^b, q>=1, strictly descend; equality at q=0 iff D*t0=2^b-1, implying a periodic orbit, NOT ruled out here. | research/S005_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0027 | PROVED_INTERNAL elementary + irrational-rotation density | For all a>=3 with {a log_2(3/2)}<=4/5, D>2^b and uniform strict O^a E^b first-cross descent; infinitely many complementary a have alpha<f<=4/5. Originality UNESTABLISHED. | research/S005_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0028 | PROVED_INTERNAL elementary, sparse coverage ONLY | Exact parity-word lift progressions give infinite strict-descent composite subfamilies for each r in 7,15,27,31,39,43 mod48; adaptive H O-exit covers additional r15/31/r7/39 subsets. Does NOT remove whole residue classes. | research/S005_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s005_grammar.py |
| CP-0029 | PROVED_INTERNAL scoped no-go | Every one-U-step rank R(n)=n+A_(n mod48,v2(n+1))+B_(state)*omega(n) with finite real fixed penalties increases on infinitely many composites x=96q+15 ->144q+23. Does not rule out nonlinear/block ranks. | research/S005_PROOFS_AND_OBSTRUCTIONS.md |

S005 originality NOT established; Collatz and Terras CST OPEN; 55 newly certified exponents among a2..256 and all six word checks are FINITE_TEST only; no Lean/Palomar.
