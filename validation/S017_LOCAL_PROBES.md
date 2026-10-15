# S017 exact local probes — research validation, not universal computation

Environment: standalone Python 3 in local container (not cloned GitHub: github.com DNS resolution blocked). Exact scratch script /mnt/data/s017_experiment.py SHA256 **3ce5dceb6baae591c07f9a986cc871daafc3bc80db8439b9cfac3f78dc899522**; this scratch path does not imply a GitHub checkout. It independently constructed recurrence intercepts, canonical parity residues using modular inverse, simulated every shortened T step, and compared 4 lifts per cylinder.

- Enumerated r=3..25, c>=1 satisfying 3^r>2^(r+c), d=1..25: **4,425 triples**, **17,700 lifts** q=0,1,2,7; all matched parity word and STRICT endpoint drop. This finite grid is far below effective M0 and by itself cannot verify the infinite large-m theorem.
- r17,c4,d1 gives b7, j29, n0=112590847 -> 81248584 (drop 31342263).
- r24,c9,d1 gives b6, j40, n0=503064821759 -> 387664016024 (drop 115400805735).
- r4,c1,d7 gives b6, j18, n0=173295 ->117107 (drop 56188).
- Exhaustive placement check ell<=9 and exact sharp equality words through ell11 PASS.
- Composite same-v2 hostile renewal n=64k+59 ->[OOE]72k+67 checked all 0<=k<200 PASS.
- Reproducible CHECKED-IN GitHub test module tests/test_s017_math.py uses only Python standard library, and rechecks the grid, sharp extrema, CRT exact all-lift threshold, and forced-O composite witnesses. New hosted full CI must be observed only AFTER its commit. Last pre-entry baseline main run 38768747419/job116538721403 separately verified successful substantive steps.
- S000 exact fixture SHA256 previously hosted 45a4ee995384ec9154bf092e272562172797e78bf771611b1d31376627498084; S001 original manifest d4686d95c47107af29d939accb8d161684f929eb348426f2d39ea8b1819b2b37; original JSONL adec6e2b05d0671170ced97304a69f25a518ad0cd658be7feaa8238f0eafc1f9. These historical hashes are NOT observations about NEW S017 checks.
- Universal positive/composite Collatz and Terras coefficient stopping time remain OPEN. No divergent example, originality, formal Lean/Palomar verification, or paper.

## S017 independently VERIFIED actual GitHub PR/merged-main CI and tree — 2026-10-15

Original S017 research branch commit `83ff5a9606723eabd51ca5e0e726604ec89626d8`, TRUE Git tree `a29ab17367bd18cea99e9da42367c7d80e4d27d0`, single parent `e183c3a2133b6154700c0cb989318865a1387b80`. PR #28 https://github.com/jfairfaxball-348/collatz-primes/pull/28 initially confirmed base and head matching this commit, then reviewed again just before merge as **mergeable=true / clean** with main unchanged and true Git parent checked. Ordinary GitHub nonforce `merge_method=merge` with `expected_head_sha` returned merged=true, merge SHA `1bc9606f563ce2d37e392eefe0fc27d113224328`. Independent live main readback returned the SAME SHA, underlying actual tree `a29ab17367bd18cea99e9da42367c7d80e4d27d0`, ordered parents [`e183c3a2133b6154700c0cb989318865a1387b80`, `83ff5a9606723eabd51ca5e0e726604ec89626d8`]. Remote main readback of STATE (S017 COMPLETE / S018 FUTURE), complete S018 prompt, S017 CLOSEOUT and S017 committed test succeeded.

**Full ORIGINAL hosted CI observations, each substantive step separately verified SUCCESS**:
- S017 BRANCH PUSH run `38770770589`, job `116545672885`, `COMPLETED SUCCESS`; 80 tests / OK.
- S017 PR run `38770812418`, job `116545821099`, `COMPLETED SUCCESS`; 80 tests / OK.
- NEW MERGED-MAIN PUSH run `38770957392`, job `116546315754`, `COMPLETED SUCCESS`; 80 tests / OK.

In ALL THREE hosted jobs the steps `Unit tests`, `Finite parity and orbit sanity` (S000 regenerated **byte-identical cmp**, SHA256 `45a4ee995384ec9154bf092e272562172797e78bf771611b1d31376627498084`), and `Recreate finite residue stream and cross-check original manifest` (S001 depths10–16 / independent `PASS: 7 depths`, JSONL `STREAM CONSUMER PASS`, manifest SHA256 `d4686d95c47107af29d939accb8d161684f929eb348426f2d39ea8b1819b2b37`, records SHA256 `adec6e2b05d0671170ced97304a69f25a518ad0cd658be7feaa8238f0eafc1f9`) were independently observed. All six new tests/test_s017_math.py methods individually appeared `ok`, and S003 corruption tests remain in original unittest discovery. These certify finite software/fixtures only, NOT the universal Collatz theorem, novelty or external mathematical review.

This is a subsequent **attestation-only branch** after original S017 research merge. This attestation commit itself creates new checks; their conclusions are NOT inferred from the earlier runs. Next S018 remains FUTURE / UNEXECUTED.
