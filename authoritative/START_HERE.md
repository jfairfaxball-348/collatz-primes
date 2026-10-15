# Authoritative status — Collatz Primes

**Date:** 2026-10-15 (planning update only).
**Completed research sessions:** S000.
**Next executable research session:** S001, FUTURE / UNEXECUTED. See authoritative/NEXT_SESSION_PROMPT.md.
**Headline target:** for every composite n>=4 there is j>=0 with T^j(n)=1, equivalent by CP-0001 to all-positive Collatz.
**Global theorem status:** OPEN / UNPROVED. The S001 planning revision makes NO new universal claim and does not execute S001.

**Governing roadmap:** research/PROGRAMME_PLAN.md.
**Owner report source transfer / facts to check:** research/REPORT_INTEGRATION.md.

Proof-first priority is a noncircular global strict-descent theorem or a complete reverse-basin cover. Parallel tracks: exact affine-residue certificates and exceptional-family dynamics; prime-factor erasure/transition constraints; inverse-graph parameterisation and compact grammar; source/Lean/cycle theory audit. Large finite checks are supporting work only.

S000 mathematics remains as recorded: composite equivalence, elementary descent classes, gcd reset, affine parity identity and odd-residue prime/composite mixing. No substantial new Collatz theorem, Lean proof, Palomar verification or independent audit is claimed for this planning update.

**CI reconciliation:** The original S000 STATE.json marked hosted CI not observed. At planning entry, the LIVE main-branch finite-sanity-checks workflow run 38641993543 for commit efec7756f47364f1da0b7d2e6ff1c54f51804c94 was observed completed with SUCCESS on 2026-10-14. This is an S000 finite test, NOT a universal proof and NOT a claim that later workflow runs succeeded.

Run for existing local finite checks:

    python -m unittest discover -s tests -v
    python tools/trajectory.py --limit 10000 --depth 8

At S001 entry pin live main anew and read AGENTS.md, docs/SESSION_PROTOCOL.md, docs/EVIDENCE_POLICY.md, authoritative/STATE.json, research/PROGRAMME_PLAN.md, research/REPORT_INTEGRATION.md, research/CLAIMS.md, research/FAILURE_LEDGER.md, and the full next-session prompt. User invocation of S001's prompt authorises S001 immediately with no second confirmation. Do not run S002 unless subsequently instructed.
