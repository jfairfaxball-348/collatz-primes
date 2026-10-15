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

- F-0022 — S003 PRIOR ART: j_s=j_c for n>=2 is exactly Terras' open Coefficient Stopping Time conjecture (CST); not a new theorem, and neither proved nor refuted here.
- F-0023 — REFUTED stronger every-negative-coefficient-step-descends implication: 7->11->17->26->13->20->10->5->8; at j8 coefficient 243/256<1 but output 8>7. At first crossing j7 the start DID descend, so not a CST counterexample.
- F-0024 — INSUFFICIENT finite CST scan 2..1000000, no mismatches. Does not justify universal CST, exceptional tower exit or Collatz.
- F-0025 — PROVED SCOPED NO-GO: for any fixed modulus 2^k and arbitrary finite per-residue horizon h, all-O positive starts 2^H t-1 in the residue -1 break the proposed uniform bound; this does NOT eliminate adaptive/mixed automata.
- F-0026 — INSUFFICIENT m-step U gcd formula; offset contains valuation history and gives no numeric/factor count monotonicity, killed by 15->23->35, 121->91, 27->41, and 12t+3 growing.

- F-0027 — INSUFFICIENT / known CST context: CP-0023 proves a strict first-crossing subfamily, not every parity itinerary. a=3,b=2 is outside the sufficient 3/4 band yet n=23 strictly descends; do not infer counterexamples from failed sufficient inequalities.
- F-0028 — REFUTED mixed-modulus fixed horizon: for any fixed M and compatible residue r=-1 mod2^v2(M), there exist infinitely many composite starts with unbounded initial growth; mod48 classes 15 and31 are explicit, but growing-memory ranks remain possible.
- F-0029 — REFUTED valuation-only one-U-step decreasing rank: composite x=681 has v2(x+1)=1, U(x)=511 has v2(U(x)+1)=9, and arbitrarily large jumps exist. Size nevertheless decreases for this family; combined ranks not excluded.
- F-0030 — INSUFFICIENT m-step factor/size potential: for every fixed m there are composite starts with the first m U steps increasing and F_m=3^m-2^m; adaptive m remains open.

- F-0028 — INVALID strong inference that first coefficient crossing on O^a E^b must STRICTLY descend for all t: exact arithmetic establishes only nonovershoot universally. Exceptional equality D*t0=2^b-1 would be a periodic orbit; its absence has not been proved here. Treating finite no-equality a<=256 as proof is invalid.
- F-0029 — INSUFFICIENT sparse six-residue forward certificates: n=r+3*2^j*q descends for six seed r, but no FULL class coverage; r27/43 fail the simple H=2 O^H E^b inverse condition t mod4.
- F-0030 — REFUTED all-composite one-U-step monotonicity of any fixed additive size + (r,h)-valuation/prime-support penalties: x=96q+15 -> y=144q+23 yields y-x=48q+8 against O(log q) omega terms.
- F-0031 — INVALID leap from a vanishing rare near-resonance band f_a>4/5 to absence of one-block equality or of global cycles. The Diophantine equality remains unexcluded; the full Collatz theorem OPEN.

- F-0032 — SOURCE-RESOLVED S006: treating S005 one-block equality as a new open Diophantine subproblem ignores Steiner (published 1978), which solved EXACTLY (2^(k+l)-3^k)h=2^l-1 for positive k,l,h (only 1,1,1). The original text is NOT personally rederived; careful source import only.
- F-0033 — INSUFFICIENT S006: 11/16 density of first descent in BOTH 27 and43 mod48 is NOT full coverage; 5/16 residue subset remains, including starts 27,91 and infinite lift branches. Relative density is not a global proof.
- F-0034 — REFUTED S006: global one-U strictly decreasing n^p*f(v2(n+1)) with p>0 and f>0 even on odd composite starts; forced f(H)/f(H-1)>(3/2)^p conflicts with jump-family uniform f(K)/f(1)<(4/3)^p. Does not exclude arbitrary nonlinear/multi-step ranks.

- F-0035 — S007 INVALID inference: 441/512 density within each r27/r43 mod48 (CP-0033) removes either entire hypothetical least-nonconvergent class. Residual **71/512** at depth13 is still infinite; density cannot replace induction.
- F-0036 — S007 REFUTED any uniform finite first-descent horizon on n≡27 mod256 in either r27/r43 mod48: CP-0035 constructs composite witnesses whose every first H iterate increases relative to their own starts, for arbitrary H. The nested compatible 2-adic parity path does NOT exhibit one actual divergent integer.
- F-0037 — S007 INVALID generalisation from a selected 4X>=5P family O^a E O E^b to ALL multi-block coefficient first crossings. CP-0034's quantified inequality is only sufficient; near-resonant exponents, other c/d, and potential exceptional minimum representatives require proof. Two-cycle prior art already exists; do not advertise a no-two-cycle theorem.
- F-0038 — S007 INSUFFICIENT proposal of endpoint R(n)=n as a global well-founded descent rank: certified blocks are defined only on proper subsets, and the union is NOT invariant nor exhaustive. A single finite descent certificate cannot be iterated over arbitrary starting integers.

- F-0039 — S008 REFUTED depth13 endpoint-renewal claim: all 71 residual mod8192 classes have EVERY first 13 iterates strictly above their own start for ALL positive lifts, not merely lack of a certificate; 27->206 at step13 is a concrete falsifier. No finite depth13 proof of whole 11 mod16 possible. Does not exclude genuinely adaptive growth-dependent renewal.
- F-0040 — S008 INVALID inference from 2-adic compatible forced O tree to a single positive divergent orbit. CP-0035 furnishes arbitrarily long different composite CRT witnesses, not an infinite ordinary starting integer.
- F-0041 — S008 DISCHARGED scoped artificial near-resonance obstacle in S007 CP-0034: 4X>=5P is unnecessary for WEAK O^a E O E^b first-crossing nonovershoot; positivity plus D*t≡-1 modM proves it for ALL a>=3. Remaining equality at minimum is excluded only using existing 2-cycle prior art, NOT elementary here.
- F-0042 — S008 FAILED extension of congruence argument to arbitrary O^a E^c O^d E^b: correction K=-1 uniquely at c=d=1; otherwise K>=1 and congruence leaves an unresolved minimum representer inequality D*t0>M+K. No CST counterexample discovered or claimed.
- F-0043 — S008 no global well-founded rank: partial first-crossing bands plus 71/512 certified-growing-through13 and arbitrarily long 2-adic towers cannot be composed into noncircular exhaustion; a probabilistic renewal requiring eventual exceptional exit assumes missing claim. Other four mod48 least-counterexample classes unresolved.

- F-0044 — S009 REFUTED 'regenerative return to the same r mod256 must decrease n': CP-0041 exact composite 393243->1259803 after 11 shortened steps, BOTH 27 mod256, and every 393243+524288k expands to 1259803+1679616k. Does not generate a single divergent orbit by iteration.
- F-0045 — S009 INSUFFICIENT 'nonovershoot holds for ALL (a,c,d) simply from K>=1': the general congruence D*t=K (mod M) only yields weak descent from D*t>K. CP-0039 imposes an infinite explicit a-progression; CP-0040 treats two K=1 pairs for every a>=4. Unrestricted other exponents / CST remain OPEN.
- F-0046 — S009 OPEN adaptive 71-residual-tree induction: first13 no descent, arbitrary-H 2-adic forced-O towers, expanding same-residue return; no universally terminating rank/renewal or branch-completeness lemma. Density, smaller coefficient or formal 2-adic limit cannot be substituted for a smaller positive integer.
