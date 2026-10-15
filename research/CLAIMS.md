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
