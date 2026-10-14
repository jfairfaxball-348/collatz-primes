# Authoritative status — Collatz Primes

**Date:** 2026-10-14.
**Completed:** S000 bootstrap, foundations, bounded sanity audit.
**Next:** S001 future / unexecuted; read authoritative/NEXT_SESSION_PROMPT.md.
**Headline target:** forall composite n>=4, there exists k>=0 with T^k(n)=1.
**Global status:** OPEN. This is equivalent to the full Collatz conjecture and is not resolved by S000.
**Evidence tier:** internal elementary proofs plus a Python finite sanity check. No Lean proof, Palomar verification, external referee, independent replay or universal convergence certificate is asserted.

Main elementary mathematical points:
- Composite-only convergence iff full Collatz convergence: for prime p, 2p is composite and T(2p)=p.
- All n>1 even descend in one step; all n>1 with n=1 mod 4 descend in two shortened-map steps; all n=3 mod 16 descend in four steps.
- For odd n, gcd(n,T(n))=1; no multiplicative behavior of T(n) follows.
- If a least counterexample exists, it lies in classes 7,11,15 modulo 16 (necessary, far from sufficient).
- A finite modulus 2^k cannot distinguish primality from compositeness on its odd residue classes: each contains infinitely many composites, and infinitely many primes by Dirichlet's theorem.

Run:
python -m unittest discover -s tests -v
python tools/trajectory.py --limit 10000 --depth 8

S000 local run: four unittest cases PASS; 4790 finite assertions; [2,10000] has 1229 primes, 8770 composites. Exact checked output at validation/S000_audit.json. These are sanity results, not a proof of all starts.

Primary reading: research/S000_FOUNDATIONS.md, research/RESEARCH_ROUTES.md, research/SOURCES.md and sessions/S000/CLOSEOUT.md. The future prompt is the authoritative next instruction, not evidence S001 already ran.
