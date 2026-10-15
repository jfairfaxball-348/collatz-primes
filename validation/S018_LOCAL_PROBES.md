# S018 finite local validation — STRICTLY finite

- Local fresh standalone Python 3 script: /mnt/data/s018/independent_s018.py; SHA256 01b5d72969272b410df8c1258833a3a84302d9c5768ff683ef45b7c88a8eb060. This path is a scratch script, NOT a GitHub checkout. Exact integer arithmetic only.
- Command: python /mnt/data/s018/independent_s018.py ; enumerates ALL first coefficient crossings length<=24, checks canonical modular inverse and exact trajectory, and three lifts for multi-E-prefix words. Output: 81,118 first-crossing words, 78,303 targeted multiblock cases; only nonstrict OE/n=1 (outside theorem); named hostile starts 7,15,27,31,39,43,91,155,251 matched prior exact descent checkpoints. No finite test establishes all-U result.
- New committed tests/test_s018_math.py independently codes bounded checks, exact B_U upper bound, CRT sign, examples, adversarial towers. It is NOT byte-identical to standalone scratch.
- Prior ORIGINAL merged-main CI pre-S018, run38771277023 job116547419358, all individually SUCCESS: Unit tests; Finite parity and orbit sanity S000 byte match; Recreate finite residue stream and cross-check original manifest (S001 depths10–16, independent checker, JSONL). This is NOT new S018 CI.
- Original local checkout unavailable (container DNS github.com failed). Any S018 branch/PR/main hosted status must be read separately AFTER the S018 commit. Tests and prior CI do not validate global convergence, novelty, external deep source proofs or the math with Lean.


## S018 INDEPENDENT hosted PR and postmerge attestation — 2026-10-15

ORIGINAL S018 source branch research/s018-initial-run-carry-budget commit 973e87cded78616114438b642e0a314e30362183 had ACTUAL underlying Git tree 5c06492a8c3c8bcda3e3aae3767f251855f26b14 and SOLE ordered parent 5255e2a5fcd134e81d67ec55885b57cf69e0a166. Pull request #30 https://github.com/jfairfaxball-348/collatz-primes/pull/30 had stable head and original main base, mergeable=true/clean. After independent HEAD/base safety check, GitHub merge_method=merge, expected_head_sha returned merged=true and merged main SHA ef5de1e4244179a2884c60261728997ed64ec0ed. Independently read live main ref SAME SHA, true tree 5c06492a8c3c8bcda3e3aae3767f251855f26b14, ordered parents [5255e2a5fcd134e81d67ec55885b57cf69e0a166,973e87cded78616114438b642e0a314e30362183]; and independently read S018 STATE, full S019 FUTURE/UNEXECUTED prompt and S018 CLOSEOUT on merged main.

NEW ORIGINAL S018 CI FULLY observed independently, EACH workflow status completed SUCCESS and EACH of the three substantive hosted steps individually success:
- Branch PUSH run 38813444589, job 116692112628.
- PR #30 run 38813504285, job 116692314128.
- NEW merged-main PUSH run 38813591529, job 116692615159.

PR and main raw job logs show 86 tests / OK, all SIX S018 tests individually ok, S003 corruption tests remain under original unittest discovery. S000 regenerated exact byte cmp succeeded and SHA256 45a4ee995384ec9154bf092e272562172797e78bf771611b1d31376627498084. S001 depths10–16 separate regenerated records and checker report INDEPENDENT CHECK PASS: 7 depths; JSONL consumer STREAM CONSUMER PASS; manifest SHA256 d4686d95c47107af29d939accb8d161684f929eb348426f2d39ea8b1819b2b37, records SHA256 adec6e2b05d0671170ced97304a69f25a518ad0cd658be7feaa8238f0eafc1f9.

This NEW attestation-only documentation writeback triggers its OWN separate checks: do NOT infer those from PR #30. None of these CI results proves Collatz, Terras CST, novelty, a 53-page Matveev proof, formal Lean/Palomar or peer review. S019 remains FUTURE / UNEXECUTED.
