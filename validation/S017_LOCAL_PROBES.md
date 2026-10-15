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
