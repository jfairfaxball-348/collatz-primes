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


## S002 update — 15 October 2026

Completed S000, S001 and S002. The full **next executable S003 prompt** is at [authoritative/NEXT_SESSION_PROMPT.md](authoritative/NEXT_SESSION_PROMPT.md); a linked or pasted owner run request is sufficient authority. Older README references to S001 as future and depth-16 statistics as report-only are historical/stale: S001 directly reproduced 30653 STRICT +1 BASE_1+2114 OPEN, and S002 added a canonical JSONL consumer to hosted CI. [S002 proof record](research/S002_PROOFS_AND_OBSTRUCTIONS.md) / [closeout](sessions/S002/CLOSEOUT.md). The conjecture **remains OPEN**.


## S003 update — 15 October 2026

The next executable **S004** handover is [authoritative/NEXT_SESSION_PROMPT.md](authoritative/NEXT_SESSION_PROMPT.md). S003 identified the proposed first-slope/first-descent identity as the **existing open Terras Coefficient Stopping Time conjecture**; it remains unproved. Elementary intercept/cylinder bounds (CP-0020), an m-step prime-return formula (CP-0021) and fixed-modulus stopping-time table obstruction (CP-0022) were proved internally; none settles Collatz. See [S003 proof/obstructions](research/S003_PROOFS_AND_OBSTRUCTIONS.md) and [closeout](sessions/S003/CLOSEOUT.md). Older text above referring to S001 as next is historical, not authoritative.

## S004 update — 15 October 2026

S004 completed a **restricted quantified** first-coefficient-crossing O^a E^b descent theorem CP-0023, a no-go for **any fixed mixed modulus** residue horizon CP-0024, and a composite valuation-jump family CP-0025. All are elementary and nonuniversal; neither full Collatz nor Terras CST is proved. The **next executable S005** is in authoritative/NEXT_SESSION_PROMPT.md, immediately authorised by the next owner run request. See research/S004_PROOFS_AND_OBSTRUCTIONS.md and sessions/S004/CLOSEOUT.md. Older headings above that identify S001/S003 as next are historical and not authoritative.

## S005 update — 15 October 2026

S005 internally proves nonovershoot for all positive O^a E^b first coefficient crossings (CP-0026), full-cylinder strict descent on a larger infinite complementary exponent band (CP-0027), sparse strict-descent composite progressions in all six least-counterexample mod48 residues (CP-0028), and a no-go for state-penalised additive one-step U ranks (CP-0029). None closes the global exception set or proves Collatz/Terras CST; no novelty or Lean/Palomar claim. See [S005 proofs](research/S005_PROOFS_AND_OBSTRUCTIONS.md), [closeout](sessions/S005/CLOSEOUT.md). The authoritative **S006** prompt is FUTURE/UNEXECUTED and executable immediately only on the owner's NEXT run instruction; older README session labels above are historical.
