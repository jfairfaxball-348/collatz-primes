# Failure and obstruction ledger

- F-0001 — INVALID shortcut: composites are a logically weaker convergence target. Via T(2p)=p they are equivalent to full Collatz.
- F-0002 — REFUTED multiplicativity: T(9)=14 while T(3)T(3)=25.
- F-0003 — INVALID: immediate descent by even integers separately proves all even converge; an induction on smaller starts is required.
- F-0004 — INVALID: almost-all logarithmic/natural density implies all starts.
- F-0005 — INSUFFICIENT: odd 2^k parity residues separate primes from composites; Dirichlet + elementary products show both.
- F-0006 — INVALID: hitting an iteration cap proves divergence; it does not.
- F-0007 — REFUTED S001 Candidate F: every odd composite n>1 has U(n)<n; infinite composite family 12t+3 -> 18t+5 for every t>=1.
- F-0008 — REFUTED S001 factor-count monotonicity: ω(U(n))<=ω(n); n=121 -> U(n)=91=7·13, while 121=11².
- F-0009 — REFUTED S001 Candidate R: every odd y>1 has an odd U-predecessor x<y; no inverse for y divisible by3, and for y≡1 mod3 smallest inverse x=(4y-1)/3>y.
- F-0010 — INSUFFICIENT S001: 30654/32768 finite 'covered' classes are NOT all strict; r=1 is a BASE_1 exception. Even with corrected 30653 strict, 2114 classes are not certified at j<=16.
- F-0011 — REFUTED uniform fixed finite descent depth: for each k≥1, infinitely many composite n=2^k t-1 have all first k T iterates above n.
- F-0012 — INVALID compactness: infinite nested congruence exception -1 mod2^k determines 2-adic -1, not any positive integer failing Collatz.
- F-0013 — INSUFFICIENT reverse grammar: sound and exactly enumerates the convergent basin but cannot prove membership for every positive integer without a new noncircular quantifier.
- F-0014 — INSUFFICIENT 'prime factors erased' ⇒ rank decreases: 27->U(27)=41 and 121->91; older factors vanish while size/number of new factors can increase.
- F-0015 — INSUFFICIENT mixed bridge: odd y≡5 mod6 has smaller odd U-predecessor, but y≡0,1 mod3 cases and uncovered 27 remain.

- F-0016 — REFUTED prime-support monotonicity across two U steps: x=20t+15 (t>=0), gcd(x,U²(x))=5, despite gcd(x,U(x))=1.
- F-0017 — REFUTED fixed 2^k-only prediction of U(x) mod3: CP-0018 explicit pairs congruent modulo2^k map to1 vs5.
- F-0018 — INVALID inference odd U-predecessor-free y divisible3 cannot converge: 3->5->1.
- F-0019 — INSUFFICIENT exact cylinder around 27: every 27+2^59*q descends at step59, but no proof for all 27+2^16*q and no universal exceptional-tower exit.
- F-0020 — OPEN tempting first-descent/first-slope-threshold coincidence: finite sightings do not prove universally quantified equivalence; S003 must prove or refute adversarially.
- F-0021 — INSUFFICIENT exact E_(k+1) per-child transfer: exact recurrences give no well-founded termination for every positive starting integer.
