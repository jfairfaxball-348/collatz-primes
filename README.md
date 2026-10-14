# Collatz Primes

**Mission:** Prove that every composite positive integer eventually reaches 1 under the Collatz map by investigating prime/composite transitions, factorization structure and residue-class descent.

**Mathematical warning:** This is exactly as strong as the full Collatz conjecture. If every composite reaches 1, then for every prime p the composite 2p reaches 1; because T(2p)=p, p reaches 1 too. No general convergence proof is known or claimed here.

We use the shortened map T(n)=n/2 for even positive n and T(n)=(3n+1)/2 for odd positive n. The usual Collatz map and this map have the same convergence-to-1 question.

## Start here

- [Live authoritative state](authoritative/START_HERE.md)
- [Machine-readable state](authoritative/STATE.json)
- [Full next research session](authoritative/NEXT_SESSION_PROMPT.md)
- [Session protocol](docs/SESSION_PROTOCOL.md)
- [Proof and evidence policy](docs/EVIDENCE_POLICY.md)
- [Foundational results and barriers](research/S000_FOUNDATIONS.md)
- [Research questions](research/RESEARCH_ROUTES.md)
- [Sources](research/SOURCES.md)
- [Claim ledger](research/CLAIMS.md)
- [Failure ledger](research/FAILURE_LEDGER.md)
- [S000 closeout](sessions/S000/CLOSEOUT.md)

## Reproduce finite sanity checks

Requires Python 3.10+ and no external packages.

~~~sh
python -m unittest discover -s tests -v
python tools/trajectory.py --limit 10000 --depth 8
~~~

The frozen [finite S000 result](validation/S000_audit.json) is **not** an all-integers theorem; neither are trajectories in other repositories. No external Collatz frontier has been independently certified by this repository.

## Execution authority

A user instruction to run the text or URL of the current numbered next-session prompt authorises immediate execution of **that one session**. Do not seek a second permission or execute a subsequent numbered session on the strength of the same instruction. Research results must be clearly marked proof, external source, finite computation or conjecture. An actual session ends with a complete future prompt, exact published refs where available and a transparent validation/closeout.
