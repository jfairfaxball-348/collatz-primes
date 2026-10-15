# S016 local finite audit — 2026-10-15

Test environment: Python 3, standalone /mnt/data/s016_work/test_s016_math.py (NOT a local checkout of the full original GitHub repository). Five independent unittest methods PASS, elapsed 0.124 seconds; script SHA256 b6d3efaf3dde18d66cfa88a16371e2e73137214bc4a7d72a7ad8cea934b5cc43. The GitHub-hosted committed tests must be observed separately and are NOT assumed green.

Finite checks:
- ALL parity words ell=1..12, r>=1: sharp 3^r-2^r <=B_U<=2^(ell-r)(3^r-2^r), exact integer-normalised A bound; all lengths/masks. Algebraic proof CP-0060 is unbounded.
- U=(OOOE)^k for k=1..31, d=2k,3k,6k: exact coefficient first crossing and actual full parity input for canonical minimal n0 and q=1,2,7 lifts; EVERY sampled candidate decreases. Not a universal theorem.
- SAME-v2 renewal n=64k+59 to72k+67, k=0,1,4,7,13,30,100; infinite proof uses algebra, not these samples. k≡1 mod3 gives composite starts.
- Complete exceptional 71 states in z≡11 mod16, MOD8192, all 5041 potential directed pairs via invertible affine q-permutations; independently checked original 27/43/91/155/251 etc actual first-descents and 393243+524288k for k=0,1,3,9. H=6,12,24,48,96 forced-O composite controls.
- Inverse predecessor mod3 rule y=1..299. High-ratio U=O^(2d), d=1..39, defeats method's uniform domination inequality even though its sampled canonical cylinder strictly descends.

Proved universal algebra: CP-0060, CP-0062, CP-0063; CP-0061 also uses published PRIMARY Matveev Corollary 2.3, whose analytic proof was NOT reproduced. Tests are FINITE_TEST only. Any PASS from hosted CI must be recorded with exact run/job/step and is about software, not all-positive Collatz.
