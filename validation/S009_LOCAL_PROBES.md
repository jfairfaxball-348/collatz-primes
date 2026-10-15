# S009 validation — 2026-10-15

Original git checkout: NOT ACCESSIBLE. `git ls-remote https://github.com/jfairfaxball-348/collatz-primes.git HEAD` returned `Could not resolve host: github.com` (container DNS). Original local complete unittest, S000 bytes/hash, original S001 checker/JSONL and S003 corruptions are NOT claimed locally; hosted CI separately executes these.

Independent local exact Python 3 standard-library isolated regression: 3 PASS, 0 failures, `python -m unittest discover -s /mnt/data/collatz_s009 -v` with test classes all fixed (c,d) in 1..5 except (1,1), eligible 4<=a<160 with congruence, q=0/1/3, expanding return k={0,1,2,3,7,24}, and controls 7,15,27,91,121,175,681 and y<100 odd mod3 inverse. The final in-repo regression `tests/test_s009_math.py` includes an added all-a (2,1)/(1,2) loop a=4..250; it must be checked by hosted CI, not mislabelled as originally locally run. These are finite exact tests, not a theorem of global convergence.

Independent S008 historical PR #11 (head 350dd68bfbea09c739777604dbb6f3b5225e1f5b) hosted workflow SUCCESS run 38722885181 job 116381535706, with all eight steps successful: setup, checkout, Python, Unit tests, Finite parity and orbit sanity (S000 bytes/hash), Recreate finite residue stream and cross-check original manifest (S001 exact generation independent checker JSONL consumer), post-setup, post-checkout, Complete. S008 merged main b75d7a8097ab60dc0f22196bacc575214c81d29b hosted SUCCESS run 38722974056 job 116381837438 same all successful steps. The whole original unittest includes S003 corruption tests; individual test case names are not exposed by step summary. S009 PR/main runs to be inspected independently after creation, NOT anticipated as PASS.

No independent formal verifier, published priority confirmation, Lean, Palomar or all-integers proof.

## S009 actual post-merge GitHub attestation (separately observed)

PR #12 https://github.com/jfairfaxball-348/collatz-primes/pull/12 merged by ordinary nonforce merge. Authored head `8bc59b2dabe099df460fbb55f74cb4779b5be5f2`; initial merged main `1d2ce79b85862fb84bab15bbfb8a4fcce7ca8cea`; actual tree `241617465fbca7c1f9139294b63ba7526f97f01b`; parents `b75d7a8097ab60dc0f22196bacc575214c81d29b` and `8bc59b2dabe099df460fbb55f74cb4779b5be5f2`. Remote main, STATE and S010 full next prompt were read back after merge.

Author branch push hosted SUCCESS run `38725062735`, job `116388736429`; PR hosted SUCCESS run `38725112600`, job `116388900909`; merged main hosted SUCCESS run `38725193059`, job `116389167019`. All each run's individual job steps observed SUCCESS, including full unit tests, S000 exact bytes/hash compare, S001 manifest regeneration/independent checker and JSONL consumer. The existing unittest discovery includes S003 corruption regression, but this attestation does not assert observing individual unittest testcase names. No local original checkout; isolated S009 exact Python three tests PASS and hosted checked-in four tests included in whole unit step.

**Attestation maintenance:** this append is after initial merged main; any later attestation-only commit has its own SHA and should not be confused with the initial research merge. No new research theorem, no S010 execution.
