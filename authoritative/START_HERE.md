# Authoritative status — Collatz Primes

**Date:** 2026-10-15. **Completed sessions:** S000 and **S001**. **Next executable:** S002, FUTURE / UNEXECUTED, full prompt in `authoritative/NEXT_SESSION_PROMPT.md`. No second confirmation needed for a fresh explicit owner run request. Execute one session only.

**Target:** every composite positive n eventually reaches 1 under shortened Collatz T; CP-0001 proves that equivalent to full all-positive Collatz. **Global theorem OPEN / UNPROVED.** S001 did NOT prove the conjecture, find a diverging orbit, close all reverse basins or establish originality.

**New S001 math:** See `research/S001_PROOFS_AND_OBSTRUCTIONS.md`. CP-0008 factor erasure (gcd(n,U(n))=1) elementary, CP-0009 global strict descent equivalence, CP-0010 exact inverse exponent/parity theorem and least-counterexample cannot be 5 mod6, CP-0011 exact finite affine class criterion, CP-0012 exceptional ancestor projection and arbitrarily long initial no-descent family n≡-1 mod2^k, CP-0013 reverse grammar soundness but missing all-positive completeness. Infinite composite `12t+3` refutes naïve U numeric descent; `121->91` refutes monotone distinct-factor count.

**Finite validation (S001, not universal proof):** k=16 has **30653** strict-all-member descent certificates, **one** BASE_1 class (r=1, except n=1), and **2114** not certified in first j<=16, split 395/395/1324 across r≡7/11/15 mod16. Report's 30654 covered count is reconciled via BASE_1. `validation/S001_manifest.json` (SHA256 d4686d95c47107af29d939accb8d161684f929eb348426f2d39ea8b1819b2b37), with record-stream hashes. Finite r=27 descends after T-step 59, not within 16.

New scripts and independent code-path checker:

    python -m unittest discover -s tests -v
    python tools/trajectory.py --limit 10000 --depth 8
    python tools/residue_certificates.py --output /tmp/S001_manifest.json --records /tmp/S001_records.jsonl
    cmp validation/S001_manifest.json /tmp/S001_manifest.json
    python tools/check_residue_certificates.py /tmp/S001_manifest.json

S001 local new unit tests passed; actual branch/main CI must be verified live from GitHub run output, not presumed by this status document. No Lean, Palomar, external human review, novelty certificate or paper exists from S001.

**Governing plan:** `research/PROGRAMME_PLAN.md`; report provenance `research/REPORT_INTEGRATION.md`; S001 proof/obstruction note and closeout; `research/CLAIMS.md` / `FAILURE_LEDGER.md`; `sessions/LEDGER.md`; `docs/SESSION_PROTOCOL.md`. S002 focuses on exceptional tower exact lift, reverse-parent mod3 gap and prime transitions. Do not automatically start S002 now.
