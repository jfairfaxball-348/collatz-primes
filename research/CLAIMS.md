# Claim register

| ID | Status | Statement | Evidence |
|---|---|---|---|
| CP-0001 | PROVED_INTERNAL; elementary | All composite integers reach 1 iff all positive integers reach 1 | research/S000_FOUNDATIONS.md |
| CP-0002 | PROVED_INTERNAL; elementary | Even n>1, n=1 mod4 >1, and n=3 mod16 descend in 1, 2, and 4 shortened steps respectively | research/S000_FOUNDATIONS.md |
| CP-0003 | PROVED_INTERNAL; elementary | Odd n has gcd(n,T(n))=1; certain prime transitions are composite | research/S000_FOUNDATIONS.md |
| CP-0004 | PROVED_INTERNAL; elementary | Parity-class affine iteration formula and eventual descent criterion | research/S000_FOUNDATIONS.md |
| CP-0005 | PROVED_INTERNAL dependent on standard Dirichlet theorem | Every odd 2^k residue contains infinitely many primes and composites | research/S000_FOUNDATIONS.md |
| CP-0006 | FINITE_TEST ONLY | [2,10000] orbit steps to 1, prime/composite counts and 4790 residue-sanity assertions | tools/trajectory.py; validation/S000_audit.json |
| CP-0007 | OPEN | Every composite reaches 1; equivalently full Collatz | authoritative/STATE.json |

Originality of CP-0001 through CP-0005 is **not claimed**. Universal theorem CP-0007 remains open.
