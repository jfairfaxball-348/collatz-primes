# S013 finite local tests and external theorem provenance — 2026-10-15

Standalone Python 3 isolated file /tmp/test_s013_math.py invoked by "python -m unittest -v /tmp/test_s013_math.py": 4 methods PASS, ~0.076 seconds in that environment; original full GitHub repository checkout was NOT cloned locally. The committed tests/test_s013_math.py is separately authored to match the four tested methods; local file byte identity and local full-original-suite PASS are NOT claimed.

Finite bounds: a=2..10, c=1..7, m=a+1..150, subject to exact 3^a>2^(a+c), b>=1, 3^m>2^(m+c). 3,854 exact parameter triples PASS; D<K 43, D>=K 3,811. Check positive t0, modular inverse, two-modulus explicit CRT h, exact strict sign and integrality. Full parity input at EVERY i<j and exact endpoint for q=0 and q=1 on nine hand-picked triples, including (2,1,971), (2,1,1636), and D>=K short examples. Exact odd-run valuation and output on twelve odd inputs. Six least-counterexample mod48 examples plus 91/155/251 exact first-drop, 11-step expanding r27 family k=0,1,3,9. Nothing in 4 tests proves the asymptotic universal-in-m Matveev implication: its mathematical proof is in research/S013_PROOFS_AND_OBSTRUCTIONS.md.

Sources: Matveev lower bound was read AS RESTATED in https://link.springer.com/article/10.1007/s40993-021-00252-2 (explicit 3*30^(t+4)... constant). Original Matveev primary paper not separately inspected; theorem is accepted as published SOURCE_STATED, and derivation into CP-0050 is PROVED_INTERNAL relative to it. Original 1978 Steiner pages not obtained/read. No new priority claim.

GitHub-hosted ORIGINAL suite, S000 byte cmp/SHA256, S001 depths10–16 regenerated manifest, independent checker, JSONL consumer and S003 corruption cases: must be observed on this S013 branch/PR and merged main by exact workflow runs/jobs/steps, and not inferred from this standalone local test.


### S013 hosted full-suite CI and merged-main verification — 2026-10-15

Original FULL GitHub-hosted repository Python suite and workflow, NOT standalone local evidence:
- branch push run 38748744680, job 116469213101; 59 unit tests PASS; substantive steps Unit tests, Finite parity and orbit sanity, Recreate finite residue stream and cross-check original manifest each SUCCESS.
- pull request #20 run 38748780774, job 116469340254; 59 unit tests PASS; same three substantive steps each SUCCESS. PR mergeability inspected CLEAN; premerge main unchanged. Rulesets [] and branch protection 403 (policy NOT fully observable).
- ordinary nonforce PR #20 merge to main SHA 76b0bcc89e485d67dd7799250593c277ec5068dd, ACTUAL git tree 526680f937ebc2003444650f33251cbd871f2a31, ordered parents cee8936245d497bdd51cc817c8283c8bd41b2839 and 15573dbd8ba30c13215e614e4da800ba0ccbd7c1. Main ref readback matched and STATE, full S014 prompt, S013 closeout and test source read back.
- merged main run 38748940596, job 116469898271; 59 Python tests OK including four S013 and legacy S003 corruption scenarios; individual Unit tests, S000 exact byte cmp/hash, S001 regenerated manifest byte cmp + independent checker + canonical JSONL consumer each SUCCESS. Seven certificate depths confirmed by independent checker. SHA256 from ACTUAL merged-main logs: S000 audit 45a4ee995384ec9154bf092e272562172797e78bf771611b1d31376627498084 ; S001 regenerated manifest d4686d95c47107af29d939accb8d161684f929eb348426f2d39ea8b1819b2b37 ; JSONL adec6e2b05d0671170ced97304a69f25a518ad0cd658be7feaa8238f0eafc1f9 .

These attest specific finite Python and file-regeneration checks only; CP-0050's universal-in-m proof is on paper relative to the published Matveev theorem. Collatz/CST OPEN, originality, independent proof refereeing, Lean, Palomar, arXiv and publication NOT established. The subsequent attestation commit creates its own CI run and cannot be described as checked until observed.

