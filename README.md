# Collatz Primes

**Mission:** Attack the full Collatz conjecture by pursuing the logically equivalent target that every composite positive integer eventually reaches 1. Factorisation is a research angle, not a proof shortcut: T(2p)=p for all primes p, so composite convergence implies prime convergence.

Map: T(n)=n/2 if n is even and T(n)=(3n+1)/2 if n is odd. **Universal result: OPEN / UNPROVED.**

## Read first

- [Authoritative live status](authoritative/START_HERE.md)
- [Machine-readable status](authoritative/STATE.json)
- [Full next session prompt — S001, FUTURE/UNEXECUTED](authoritative/NEXT_SESSION_PROMPT.md)
- [Research programme / proof attack roadmap](research/PROGRAMME_PLAN.md)
- [Owner deep-research report integration ledger](research/REPORT_INTEGRATION.md)
- [Research routes](research/RESEARCH_ROUTES.md)
- [S000 foundations](research/S000_FOUNDATIONS.md)
- [Claim and failure registers](research/CLAIMS.md) / [failures](research/FAILURE_LEDGER.md)
- [Primary-source register](research/SOURCES.md)
- [Session protocol](docs/SESSION_PROTOCOL.md) / [evidence policy](docs/EVIDENCE_POLICY.md)
- [S000 closeout](sessions/S000/CLOSEOUT.md)

## Programme principle

The main routes are (1) a noncircular global strict-descent theorem, (2) a symbolic complete reverse-basin rule, and (3) an exact affine-residue certificate system with proof that every exceptional family closes. Prime-factor erasure and transition arithmetic constrain these routes. CEML and PRIMES support verification/experimental discipline; restricted cycle results and almost-all theorems do not imply full convergence.

The 14 October 2026 owner research report gives finite depth-16 residue statistics; they are **report-derived, not yet independently reproduced in this repository**. Do not promote them to a theorem without a certificate and independent checker.

## Reproduce existing S000 finite checks

Requires Python 3.10+; standard library only.

    python -m unittest discover -s tests -v
    python tools/trajectory.py --limit 10000 --depth 8

S000's [finite audit](validation/S000_audit.json) is a sanity check, not a universal theorem or a frontier certificate.

## Execution authority

S000 is completed. S001 remains **future/unexecuted** even after this planning-only update. When the owner pastes or links the current S001 session prompt and instructs it to run, that is immediate authority to execute exactly S001; no second confirmation. Do not automatically run S002. Each completed session must give a mathematically honest closeout, verified git links, and a FULL next-session prompt.
