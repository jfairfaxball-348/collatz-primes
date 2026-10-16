# S024 exact finite / source / CI provenance — 2026-10-16

## Local tests
- Python 3.13 local isolated standard-library file (same algorithm checked into tests/test_s024_math.py) executed with `python -m unittest discover -s /mnt/data/s024 -v`; five S024 tests PASS (separate from full original repo checkout, unavailable).
- 2-adic 7n≡5 mod16^k roots for k=1..12; actual 4k parity steps (OOEE)^k and 16-adic projection, CRT composite lifts; r1=3, r2=147, r3=1171, r4=9363. Illustrative composite n: k1 51, k2 147, k3 9363.
- Six hard classes 7,15,27,31,39,43 mod48: horizons H=10,13,...,64 (=19 horizons ×6=114 class/horizon configurations), independently constructed canonical H-bit residue and CRT positive composite n≡0 mod5; every actual T^j(n)>n through H. These are separate witnesses for separate horizons, NOT one orbit never descending.
- Reversed S=OOEOOOE triple (243,128,287), H(S^3)=32673271/14348907 <7/3, H(S^4)=8300314997/3486784401 >7/3, k=1..13 fraction recurrence audited. Carry bound failure alone does NOT imply actual first-crossing overshoot.
- Recomputed 71 exceptions/512 n≡11 mod16, 5041 abstract pair count, 64k+59→72k+67 (k<120), 2^H u−1 h1..12 with u=1,3,5; 27/43/91/155/251 and 393243+524288k and all six residue controls. Scope: finite only. S003 corruption tests are in original hosted unit discovery, not locally reproduced.

## Entry-main hosted reproducibility, exact SHA
- SHA 7505909a42709294367dd8f3275fca648ac80d06: Python push run38891847861/job116942978029 SUCCESS all steps, log 112 tests; S000 SHA256 45a4ee995384ec9154bf092e272562172797e78bf771611b1d31376627498084, S001 7 depth10–16 checker and canonical JSONL consumer PASS; manifest d4686d95c47107af29d939accb8d161684f929eb348426f2d39ea8b1819b2b37, records adec6e2b05d0671170ced97304a69f25a518ad0cd658be7feaa8238f0eafc1f9.
- Same entry SHA: Lean pinned 4.24.0 Mathlib job116942979408/run38891848208 SUCCESS all steps incl build; 403 branch protection UNKNOWN, rulesets [].
- S024 first source SHA cdf366f2404af40ce986a28420808791e1841f09: original Python push run38894936713 and PR run38894970753 SUCCESS; original pinned Lean push run38894936751 and PR run38894970810 SUCCESS. New full source + documentation head REQUIRES OWN fresh hosted CI; don't transfer earlier statuses to changed SHA.
- Original repo clone and Lean executable unavailable locally. Do not claim an independent main/full source proof check from scratch.
