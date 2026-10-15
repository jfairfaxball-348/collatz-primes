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

| CP-0030 | SOURCE_STATED classical Steiner 1978 + PROVED_INTERNAL application | Published no-nontrivial-1-circuit theorem excludes equality in ALL positive O^a E^b first crossings with a>=2; hence EVERY such cylinder strictly descends at crossing. Exact Steiner proof NOT locally rederived; NOT novel. | research/S006_PROOFS_AND_OBSTRUCTIONS.md; Lagarias annotated bibliography |
| CP-0031 | PROVED_INTERNAL elementary; novelty NOT ESTABLISHED | Three FULL parity residue cylinders n≡11 mod32 (j5), n≡59 mod128 (j7), n≡123 mod256 (j8) are strictly descending; their disjoint union covers EXACTLY 11/16 of each r=27,43 mod48 class. Not all residues. | research/S006_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s006_math.py |
| CP-0032 | PROVED_INTERNAL scoped no-go; novelty NOT ESTABLISHED | For ANY p>0 and positive function f(h), no one-U-step strictly decreasing potential R(n)=n^p f(v2(n+1)) exists for ALL odd composite inputs. High-h O-runs and composite high-h output jumps contradict. | research/S006_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s006_math.py |

S006: Full Collatz and Terras CST remain OPEN. Steiner's classical theorem is explicitly imported, not original; no novelty or formal validation claimed. 

| CP-0033 | PROVED_INTERNAL elementary; novelty UNESTABLISHED | Thirty disjoint new full j=8/10/12/13 strict-descent cylinders cover additional 89/512 of EACH r27/r43 mod48 class, total with S006 441/512, residual 71/512. Complete table/CRT proof. | research/S007_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s007_math.py |
| CP-0034 | PROVED_INTERNAL elementary, scoped two-run; novelty UNESTABLISHED | For a>=3 with X=2^(a+b+2)>3^(a+1)=P, minimal b, and 4X>=5P, EVERY positive O^a E O E^b parity-cylinder start strictly descends at first coefficient crossing. At least one of any consecutive pair a,a+1 qualifies; infinitely many a and composite witnesses. | research/S007_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s007_math.py |
| CP-0035 | PROVED_INTERNAL elementary no-uniform-horizon obstruction; novelty UNESTABLISHED | For every H>=8, infinitely many composite n≡27 mod256 in EACH 27 and43 mod48 class have T^j(n)>n for ALL 1<=j<=H. Nested 2-adic parity residues do NOT imply divergent integer; eliminates uniform finite descent bound only. | research/S007_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s007_math.py |

S007: 441/512 is NOT full coverage; Collatz and Terras CST OPEN. Independent Python probes FINITE_TEST (local script SHA and output hash in validation/S007_LOCAL_PROBES.md). No novelty/Lean/Palomar.

| CP-0036 | PROVED_INTERNAL exact exhaustive finite symbolic certificate, infinite congruence implication; novelty UNESTABLISHED | On ALL positive n≡11 mod16, 441/512 residue mod8192 slots have first-coefficient-crossing strict descent j<=13, while EXACTLY 71/512 have 3^{a_j}>=2^j and T^j(n)>n for EVERY 1<=j<=13. The 71 group into 26+15+15+15 modulo256 x=27,91,155,251. Does not imply eventual descent. | research/S008_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s008_math.py |
| CP-0037 | PROVED_INTERNAL weak all-a + SOURCE_STATED literature strict corollary; novelty UNESTABLISHED | For EVERY a>=3, first crossing of O^a E O E^b has D*t≡-1 modM, hence T^j(n)<=n for ALL admissible positive t; q>=1 strict unconditionally. q=0 equality would be nontrivial two-cycle; existing Simons no-two-cycle SOURCE_STATED excludes it, so strict if that classical source is accepted. Does NOT prove all two-run words/CST. | research/S008_PROOFS_AND_OBSTRUCTIONS.md |
| CP-0038 | PROVED_INTERNAL algebraic identity + scoped obstruction | For admissible O^a E^c O^d E^b, exact endpoint (3^(a+d)t+K)/M with K=3^d(2^c-1)-2^(c+d); K=-1 iff (c,d)=(1,1), otherwise K>=1. First-crossing overshoot in other words still OPEN, no proof of existence. | research/S008_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s008_math.py |

S008 novelty NOT established. Terras CST and full Collatz OPEN; local isolated 4/4 finite tests, original repo local tests unavailable; S008 hosted CI verify independently.

| CP-0039 | PROVED_INTERNAL elementary weak + SOURCE_STATED strict q=0 | For EVERY fixed c,d>=1 other than (1,1), sufficiently large a satisfying a+d=0 mod phi(2^s), 2^s-1>K, yield first-crossing O^a E^c O^d E^b weak descent on ALL positive lifts, strict q>=1. q=0 strict follows from published no-2-cycle theorem; novelty UNCHECKED. | research/S009_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s009_math.py |
| CP-0040 | PROVED_INTERNAL elementary weak + SOURCE_STATED strict q=0 | For ALL a>=4, (c,d)=(2,1) and (1,2) have first coefficient crossing weak descent for all t; q>=1 strictly. K=1 and D≡5/7 mod8. | research/S009_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s009_math.py |
| CP-0041 | PROVED_INTERNAL elementary | Infinite exact expanding 11-step same-residue return 393243+524288k ->1259803+1679616k, both 27 mod256; infinitely many composite starts. Does NOT give infinite divergent orbit. | research/S009_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s009_math.py |

S009: full Collatz and CST OPEN, 71/512 residual untouched by universal rank. Novelty UNCHECKED, no formal verification.

| CP-0042 | PROVED_INTERNAL elementary exact exceptional graph and arbitrary finite lift lemma; originality UNESTABLISHED | All 71 depth13 exceptional residues admit EVERY directed 13-step successor among same 71 via q mod8192; 5041 graph edges. Every prescribed finite exceptional itinerary occurs for infinitely many positive COMPOSITE starts with strict no-descent and no coefficient crossing through every prescribed block. Refutes state-only well-founded rank and bounded state-dependent exceptional budget, not adaptive unbounded n-dependent rank or full Collatz. | research/S010_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s010_math.py |
| CP-0043 | PROVED_INTERNAL exact finite-parameter infinite-lift theorem; originality UNESTABLISHED | Authentic first-crossing two-run grammars (a,c,d,b)=(3,1,26,16),(4,2,25,15) have D<K but ALL admissible lifts strictly descend at j46; least-lift drops 18195423119 and 36390846239. D>K is not necessary, unrestricted D<=K classification/CST OPEN. | research/S010_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s010_math.py |

S010: Full Collatz and Terras CST remain OPEN; no novelty, Lean, Palomar or publication claim. Standalone exact local finite tests distinct from original hosted repo suite.

| CP-0044 | PROVED_INTERNAL elementary; novelty UNESTABLISHED | For every admissible first-crossing two-run O^a E^c O^d E^b, 2^(c+d) divides [3^a*t0+(2^c-1)], giving exponential least-lift lower bound and a D<=K-capable strict descent sufficient test; exact least-lift necessary-and-sufficient test is D*t0>M+K. | research/S011_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s011_math.py |
| CP-0045 | PROVED_INTERNAL quantified infinite composite SUBPROGRESSIONS; novelty UNESTABLISHED | For each N>=1, full parity word p^N E^(4N) with p=27's 13-bit word produces arbitrarily many composites in BOTH 27/43 mod48 exceptional classes with no descent/crossing through 13N and strict descent at actual first crossing by <=17N; no full E coverage. | research/S011_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s011_math.py |
| CP-0046 | PROVED_INTERNAL elementary + irrational-rotation density; novelty UNESTABLISHED | Infinitely many m give two genuine D<K first-crossing two-run families (3,1,m-3,j-m-1) and (4,2,m-4,j-m-2) with strict least-lift descent, all lifts, and infinitely many composite subprogressions in EACH 7/15/31/39 mod48 class. | research/S011_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s011_math.py |

S011: universal composite/positive Collatz and Terras CST OPEN; no external novelty, independent formal certificate, Lean, Palomar or publication. Original local repo inaccessible; isolated checks do not substitute for hosted full suite.


| CP-0047 | PROVED_INTERNAL elementary irrational-rotation + exact two-run algebra; originality UNESTABLISHED | EVERY fixed a,c>=1 with 3^a>2^(a+c), κ=(2^c-1)/3^a, and any 0<ε<η<κ yield infinitely many m with δ_m in (ε,η), TRUE first-crossing O^a E^c O^(m-a) E^b, D<K and strict descent for ALL positive lifts q>=0, including infinitely many composites. NOT all m/n/CST. | research/S012_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s012_math.py |
| CP-0048 | PROVED_INTERNAL scoped nonexhaustion/equivalence | The explicit S011 W_N=p^N E^(4N) union does NOT include n=27: after p=13 letters its next four are EOOO and next p cannot start odd. The naive algorithm stopping at first iterate <n terminates on all n iff global Collatz. This proves failure of that covering candidate, not failure of arbitrary integer-dependent renewals. | research/S012_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s012_math.py |
| CP-0049 | PROVED_INTERNAL elementary composite forced-O bound | For every H>=6 there is a composite n=2^H u-1, odd 3<=u<=29, n multiple of5, all first H input steps odd and T^i(n)>n for every 1<=i<=H, with bitlength n<=H+5. No bitlength-independent shallow descent bound; no divergence claim. | research/S012_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s012_math.py |

S012 full Collatz and Terras CST OPEN, all six mod48 exceptional classes unresolved. Internal mathematical proof, standalone FINITE_TEST and independently observed preceding-hosted CI are separate evidence categories. Originality NOT ESTABLISHED, no Lean/Palomar.

| CP-0050 | PROVED_INTERNAL deriving from SOURCE_STATED published Matveev bound; originality UNESTABLISHED | Every FIXED a,c>=1 with 3^a>2^(a+c) admits m0 such that ALL m>=m0 yield true-first-crossing O^a E^c O^(m-a) E^b with STRICT descent for ALL positive lifts q>=0, including near-zero delta and complementary delta>=kappa. NOT all words, all n, CST or Collatz. | research/S013_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s013_math.py |
| CP-0051 | PROVED_INTERNAL elementary CRT, exact conditional classification; originality UNESTABLISHED | For each two-run valid first-crossing grammar the minimal carry h is explicit via h≡3^(-d) mod2^b and h≡(2^c-1)*2^(-(c+d)) mod3^a; strict/equal/overshoot is an exact integer comparison. Does NOT classify arbitrary words or establish CST. | research/S013_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s013_math.py |
| CP-0052 | PROVED_INTERNAL elementary odd-run length; originality UNESTABLISHED | For each positive odd n, maximal initial O run has length exactly v2(n+1) and growth T^h(n)=3^h*(n+1)/2^h-1 even; strictly decreasing valuation terminates each run but NOT an infinite sequence of mixed runs. | research/S013_PROOFS_AND_OBSTRUCTIONS.md; tests/test_s013_math.py |

S013 research finite grid 3854 (43 D<K, 3811 D>=K), 4 isolated tests PASS; new hosted full-suite CI separate. Global Collatz and Terras CST OPEN, no novel priority or formal verification.

