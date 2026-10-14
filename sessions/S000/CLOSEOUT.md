# S000 CLOSEOUT — initial bootstrap (2026-10-14)

**Outcome:** Repository populated with session protocol, live authoritative status, source/claim/failure registers, mathematical foundation proofs, finite reproducible Python audit and next-session handover. FULL composite Collatz conjecture remains OPEN.

## Rigorous internal mathematics
CP-0001: all composite convergence iff full conjecture, via T(2p)=p.
CP-0002: descent classes even n, n=1 mod 4, n=3 mod 16; any least counterexample (if exists) restricted to 7,11,15 mod16.
CP-0003: gcd(n,T(n))=1 for odd n; primes p=1 mod4 move to composite at next T step.
CP-0004: exact affine parity-residue formula and its conditional eventual-descent criterion.
CP-0005: any odd modulo 2^k class has infinitely many composites, plus infinitely many primes using the classical Dirichlet theorem.
These are elementary and **not claimed novel**. No central global theorem proved.

## Bounded computational validation
Environment: Python 3, standard library only; no externally certified runner. Commands:
python -m unittest discover -s tests -v
python tools/trajectory.py --limit 10000 --depth 8

Local unit tests: 4/4 PASS, after correcting a mistaken test expectation for the shortened stopping time of 9 (actual value 13). The error was in the test expectation, not evidence of an algorithmic anomaly.
Finite audit: 1229 prime and 8770 composite starts in [2,10000] reaching 1 inside configured step cap, finite assertions 4790 at depth<=8, max prime steps 164 at start 9257, max composite steps 165 at start 6171. Output validation/S000_audit.json SHA-256:
45a4ee995384ec9154bf092e272562172797e78bf771611b1d31376627498084
This is only a finite sanity check; host CI and independent review should not be described as PASS without actual observation.

## Literature and limits
Primary sources Lagarias, Tao, Barina listed in research/SOURCES.md; computational upper bound is source-reported, not independently certified. No Lean, Palomar, arXiv submission, novelty certificate, journal correspondence or general proof.

## GitHub publication
S000 initialized a previously empty main and prepares the full scaffold in a dedicated branch/PR. Actual PR/merge hashes and check results must be read from GitHub after publication, not manufactured in this frozen note.

## Next session
S001 is FUTURE / UNEXECUTED. The COMPLETE S001 instruction is recorded verbatim in authoritative/NEXT_SESSION_PROMPT.md in this commit, and should be delivered to the owner with the closeout. Invoking that file as an instruction authorises S001 directly and only S001.
