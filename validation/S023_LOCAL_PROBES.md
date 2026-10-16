# S023 independent finite and formal audit — 2026-10-16

- Local original GitHub clone DNS FAILED; local Lean/Lake not installed. S023 dedicated standard-library code tested independently in a local Python3.13 runtime (4 suite cases in local precursor; checked-in extended suite has five cases, hosting REQUIRED for final attestation).
- Checked 9330 words of 1–5 atoms from {O³E,O⁴E,O⁵E,O³EO²E,O⁴EO²E,O²EO⁴E}; 5337 d=1, 3993 d=2, 27990 exact positive trajectories (least representative + lifts q=1,3), all first crossings and strict descents, minimum Dn−B=256. These bounds are FINITE.
- CP-0076 weighted invariant ratio 251/115 is mathematically proved for unbounded words; P=(243,128,251) saturates; R=(729,256,925) passes; reverse of three/two R3=(243,128,287) violates 7/3 uniform-block invariant but NOT known to overshoot.
- CP-0077 counterexamples: n=3+48k, k≥1, all composite; 500 specific n checked and symbolic OOEE prefix proof.
- CP-0078 tail H limit with four L3 is 125825/59049 <7/3 for arbitrarily many O²E, whereas three L3 limit 5267/2187 >7/3 and first finite boundary N=21. Sharp for this fixed scheme only.
- Legacy 71/512 and 5041 edges independently recalculated; 64k+59→72k+67 first 3 T-steps for k=0..99. The full S000 fixture, S001 depths10–16 JSONL independent checker and S003 corruption tests are exercised by original GitHub workflow (observe exact job statuses after PR/main). Finite control points 27,43,91,155,251, family 393243+524288k, forced odd 2^H u−1 and all six hard mod48 classes remain without all-n proof.
- Developer precursor source SHA256 75799eba5b166498b049fa0f9e415fc1c36e244b206d3e0fe36b7b277b595569; checked-in extended test source is separately identified by Git blob SHA; do not mislabel precursor checksum as exact checked-in source checksum.
- Git/CI evidence: S023 head, PR and exact postmerge jobs must be filled by observed GitHub data only. Never turn missing source or job into PASS.
