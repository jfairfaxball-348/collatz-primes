# S005 independent finite exact arithmetic probes

2026-10-15. Separate local container script (not cloned repository): `python /tmp/s005_independent.py` with SHA256 `62e3a17befa81030bafd8b8c80628f8d53c28edf2f58150653bc7f41c3432711`. Output:

```
A a2..256 old_eligible 149 new_complement_certified 55 equality_cases 0
B 7 7 4 5 47 OOOEOEE
B 15 7 4 10 47 OOOOEEE
B 27 59 37 23 126176846412426125 OOEOOOOOEOEOOEOOOEOOOOEOEEOOOEOOEOOOOOOEEOOOOEEEOEOEOEEEOEE
B 31 56 35 23 22026048938928229 OOOOOEOEOOEOOOEOOOOEOEEOOOEOOEOOOOOOEEOOOOEEEOEOEOEEEOEE
B 39 8 5 38 13 OOOEOOEE
B 43 5 3 37 5 OOEOE
C 1999 exact-state factor/valuation witnesses PASS
Mandatory hostile controls PASS
```

Implemented with exact integers: b from while 2^(a+b)<=3^a, modular inversion pow(3^a,-1,2^b), parity-step iteration T, q=0/1/2 at a=2..256; certificate full words for six classes and q=0/1/2/7 lifts; composite state witnesses q=1..1999 and independent exact hostile trajectories. The new in-repo tests/test_s005_grammar.py encodes the same finite claims to run with repository CI (independent check was NOT an execution of the original repository suite). No equality case in this finite range is NOT evidence that an equality cannot exist. Proof of infinitely many exponents is a separate irrational-rotation argument. Proofs in research/S005_PROOFS_AND_OBSTRUCTIONS.md.

Original repository unavailable for local checkout: `git ls-remote https://github.com/jfairfaxball-348/collatz-primes.git HEAD` failed `Could not resolve host: github.com`. Hence **no local original unit tests, S000 audit, frozen k10..16 manifest bytewise comparison, checker, canonical JSONL consumer or corruption suite execution**. GitHub Actions workflow .github/workflows/ci.yml runs these on PR and main; observed job/step results must be reported separately. Frozen validation/S001_manifest.json unchanged.
