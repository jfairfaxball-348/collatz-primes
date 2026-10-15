# S004 independent local arithmetic probes (finite; not original checkout)

Date: 2026-10-15. An independent Python 3 script executed in a local container with no checkout of the GitHub repo. All assertions passed. Exact console summary:

    S004 independent exact finite probes PASS; a=2..129, certified 75 of 128, pair property; CRT H=4,5,8,12,20; valuation K=3..29; U offsets m<=8

Implementation: integer-only shortened T; exact b(a) computed by incrementing b while 2^(a+b)<=3^a; for each a in 2..129 validated the adjacent-pair condition. For eligible a, took t0=pow(3^a,-1,2^b) and t=t0+q2^b (q=0,1,3), checked every individual O^a E^b parity, exact coefficient crossing at a+b, strict numerical descent, and the affine difference identity. Eligible count was 75 among 128; ineligible a were not called counterexamples.

For mixed mod48, for H in 4,5,8,12,20 and r=15,31 solved n0=r+48j congruent 2^H-1 mod2^(H+1). With L=lcm(48,2^(H+1)), tested n=n0*(1+qL) for q=1,2: positive composite, n mod48=r, v2(n+1)=H, every T^i(n)>n for 1<=i<=H+1.

For K=3..29 solved y=-1 mod2^K and y=7 mod9, used x=(4y-1)/3, asserted x divisible3, v2(x+1)=1, v2(y+1)>=K, U(x)=y, x>y. Crosschecked the exact offset / gcd recurrence for 8 U steps on x=15,35,121,27,3,51,243,231,681,2^20*7-1. Additional exact automated tests in tests/test_s004_boundaries.py reproduce these scoped probes under the repository's existing Python unittest workflow.

Original S000 audit, S001 manifest regeneration, independent certificate checker and direct canonical JSONL consumer were NOT run in this local container because the original repository checkout was inaccessible (github.com DNS error). The existing .github/workflows/ci.yml prescribes their re-execution in hosted CI alongside tests; only verified run and step results may be reported as PASS. The frozen S001 manifest and digest were NOT changed.

No probe checks infinitely many inputs; universal proofs are the separately written modular and algebraic arguments in research/S004_PROOFS_AND_OBSTRUCTIONS.md.

