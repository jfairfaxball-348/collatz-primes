# S006 independent finite probes — 2026-10-15

Environment: local Python 3 container; NO local GitHub checkout or original repo unittest execution (DNS resolution failed). Algebraic proof is in research/S006_PROOFS_AND_OBSTRUCTIONS.md.

Local script: /tmp/s006_independent.py, SHA256 ab513edebf8141d427b650691e264107501c16e33900befd8bdd93a76d9a6e8e; locally ran python /tmp/s006_independent.py. Verified exact first descent 11 at j5 (10), 59 at j7 (38), 123 at j8 (118), 27 j59 (23), 91 j45 (61). Verified n=11+32q for 11<=n<100000; H,K=3..100 on the two composite obstruction families; one-block inverses a=2..1000 showed no equality FINITELY (no implication for all a). The script prints its own SHA256 and was unchanged when SHA recorded.

Independent second shell probe (NOT included in above script digest) verified 5000 integer samples per row of:
  r=11,m=32,j=5, word OOEOE, T^j=(27n+23)/32;
  r=59,m=128,j=7, word OOEOOEE, T^j=(81n+85)/128;
  r=123,m=256,j=8, word OOEOOEOE, T^j=(243n+319)/256;
and exact class membership 176/256 for each r27,r43 mod48 on 256 successive elements.

The unlimited statements are proved via parity affine lifting and contradiction of inequalities, NOT these finite probes. S006 repo test added: tests/test_s006_math.py. Hosted S006 CI must be independently observed after actual PR and merged-main push.

Rechecked earlier S005 runs: PR 38713158631 job 116349307535 SUCCESS, main 38713250568 job 116349613788 SUCCESS, including individual unit/S000 orbit/regeneration/checker/consumer steps. Their command bodies are those in .github/workflows/ci.yml; no claimed local manifest hash regeneration in S006.
