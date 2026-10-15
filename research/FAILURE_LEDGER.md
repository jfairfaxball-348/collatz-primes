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

- F-0047 — S010 REFUTED every finite-state well-founded E→W rank decreasing along every exceptional 13-step successor: CP-0042 has all 5041 edges including 71 self-loops. Does NOT refute a state+integer adaptive potential.
- F-0048 — S010 REFUTED any bounded number of exceptional 13-blocks / first-coefficient-crossing time depending ONLY on the initial 71-state: arbitrary finite sequences of exceptional states (including repeated self-states) have infinitely many positive composite realisers, all prefixes through prescribed horizon have coefficient>=1 and output>start. Compatible infinite 2-adic paths are NOT positive divergent Collatz integers.
- F-0049 — S010 REFUTED overstrong converse "first-crossing weak descent REQUIRES D>K" in two-O-run O^a E^c O^d E^b: (3,1,26,16),(4,2,25,15) both have D=1738366812781<K=2541731610601 but strict first-crossing integer descent for every lift. General D<=K and potential equality D*t0=M+K still OPEN.
- F-0050 — S010 OPEN positive-integer adaptive renewal/least-counterexample proof: existence of any fixed-length finite exceptional itinerary is not a single positive infinite orbit, cannot yield divergence; no proof of a finite strict integer decrease for every positive exceptional lift. Failure to distinguish coefficient threshold from strict endpoint descent remains a risk (7 j8 overshoots after prior j7 descent).

- F-0050 — S011 NO-GO for size-plus-valuation rank on prescribed CP-0041 11-step returns: 393243+524288k ->1259803+1679616k strictly grows while v2(n+1)=2 at BOTH ends. Any F(n,v2(n+1)) strictly increasing in n for fixed valuation cannot decrease on all such returns. NOT a refutation of using later steps or richer adaptive states.
- F-0051 — S011 NOT-COMPLETE parity-tail certificate: W_N=p^N E^(4N) proves first-crossing descent for infinitely many composites after arbitrary long finite exceptional prefixes, but quantifiers ∀N∃infinitely many n DO NOT entail ∀n∃N. The extra E tail imposes infinitely many disjoint high-bit conditions; an arbitrary fixed n may miss them.
- F-0052 — S011 INVALID alleged global D<=K conclusion: parameter criterion from CP-0044 is SUFFICIENT and exact modular inverse test is NECESSARY/SUFFICIENT for specific parameters; paired density subfamily does NOT classify all first crossings or settle Terras CST. Finite scan 30,987 has zero first-crossing overshoots but cannot prove universal absence.
- F-0053 — S011 INVALID treating repeated 13-bit parity WORD as forcing the final checkpoint ≡27 (mod8192): the next parity block imposes residue 27 at the *preceding* checkpoint; after the last block, the endpoint can vary with unused high bits. Regression expectation corrected before PASS; CP-0045 proof uses checkpoints i=0..N-1 only.


- F-0054 — S012 REFUTED exhaustive-family claim for p^N E^(4N): explicit composite n=27 has the first p but at T^13(27)=206 its next parities are EOOO, not EEEE; N>=2 would require an odd second p, impossible since 206 even. Therefore n27 lies in no W_N. Other, adaptively chosen families remain OPEN.
- F-0055 — S012 CIRCULAR `iterate until lower` alleged algorithm termination: termination for all positive n>=2 is logically equivalent to all-positive Collatz by strong induction. A computable semi-decision procedure without a termination theorem cannot give a decreasing global rank.
- F-0056 — S012 SHALLOW BITLENGTH no-go: for every H>=6 there is composite multiple of5 n=2^H u-1 with bitlength<=H+5 and every first H iteration strictly above n. This does not exclude rank/stopping bounds longer than about log2 n nor any all-input adaptive algorithm.
- F-0057 — S012 STILL OPEN shrinking near-resonance δ_m→0 for fixed a,c: CP-0047 covers ANY fixed positive δ interval strictly contained in (0,κ), but the lower bound δ_m*t0 used to prove descent need not win if δ_m tends to zero too rapidly. No general two-run CST, universal coefficient-first-crossing descent, or exceptional branch-exhaustive renewal established.

- F-0058 — S013 DISCHARGED the S012 fixed-(a,c) shrinking-delta concern in a SPECIFIED grammar using Matveev's published logarithmic-form bound: exponential lower bound of t0 dominates any polynomial small delta, eventually for ALL m. Does NOT establish a first-crossing result for arbitrary words, CST or Collatz.
- F-0059 — S013 OPEN all-positive integer-dependent certificate covering lemma: signed-affine forward search and block-skipping v2 algorithm each verify their finite outputs but totality on all n remains equivalent to a global descent proof. Every finite exceptional graph itinerary is possible and cannot establish universal positive n termination.
- F-0060 — S013 REFUTED global rank from only finite maximal-O-run potential v2(n+1): valuation descends across each O step but can be renewed on E; exact CP-0041 11-step same-valuation growing return contradicts any size-monotone same-valuation rank on all such returns.
- F-0061 — S013 OPEN constructive exact bound m0(a,c): Matveev gives explicit massive theoretical polynomial lower bound but no practical uniformly small cutoff, and with a,c growing with m the fixed-parameter exponential domination proof does not automatically extend.



- F-0062 — S014 DISCHARGED the lack of an explicit threshold for the TWO-RUN grammar: CP-0053 supplies m0(a,c)=[4(10^12+a+c+10)]², absurdly large but explicit. This is a SUFFICIENT bound for a narrow word family, not a global stopping-time or polynomial-in-input guarantee.
- F-0063 — S014 REFUTED unrestricted arbitrary-prefix FIRST-crossing claim: U=OE has coefficient crossing at its second letter. The long appended O^d/E^b tail cannot make the last index its first crossing. CP-0054 crucially assumes EVERY nonempty prefix of U stays overcritical.
- F-0064 — S014 OPEN growth of PREFIX U with d: CP-0054 holds for fixed U and has bound depending on its ell,r,B_U; letting U vary arbitrarily with d can destroy the exponential versus Matveev polynomial comparison. A uniform B_U and depth relation must be proved before asserting any variable-U theorem.
- F-0065 — S014 OPEN actual all-positive exceptional exit: multi-run first-crossing cylinders remain thin sets, and the finite 71-vertex 5041-edge graph has no single positive-trajectory divergence implication. Both forward block-run rank and finite inverse-basin membership have no noncircular ALL-n termination proof. At y=3, no odd immediate inverse and even inverse6>3 disprove "every y has an immediate smaller reverse predecessor".
- F-0066 — S014 SOURCE GAP: Matveev's original 2000 primary paper was identified bibliographically but not read; exact inequality was checked against a 2021 published secondary statement. Steiner 1978 original seven pages likewise not acquired. Novelty is NOT established.

- F-0067 — S015 PARTIAL DISCHARGE of F-0064 for GROWING U_d: CP-0058 gives uniform affine B_U bound; CP-0057 rigorously proves all-large-d descent when #O(U)<=d/2 and every prefix overcritical. Does NOT cover U_d with unconstrained odds/run ratios or arbitrary starting n.
- F-0068 — S015 REFUTED huge-threshold cylinder COVERAGE: even allowing U to grow with d, all starts in CP-0057 satisfy n>(2/sqrt(3))^d/2 and hence none of 7/15/27/31/39/43 can be covered. Any claim it closes a whole mod48 class is false. This does NOT refute other smaller-d cylinders.
- F-0069 — S015 FORWARD/INVERSE all-integer bridge still OPEN: finite individual run halting/finite reverse BFS membership cannot be promoted to uniform total descent, and 71/5041 arbitrary finite paths plus expanding same-v2 returns hostile-audit candidate ranks. Reverse y=3 has only larger immediate predecessor6. No positive integer divergent orbit established.
- F-0070 — S015 CORRECTED FINITE TEST DOMAIN: naive scan over all 8192 residues gives 367 without coefficient crossing through13; the historic 71 is counted only among z≡11 (mod16), 512 candidates. Exact corrected script 71 and all 5041 exceptional pairs PASS. Never relabel 367 as contradiction.
- F-0071 — S015 PARTIALLY CLOSED SOURCE GAP: ORIGINAL Matveev 2000 full English paper obtained, primary §2 Corollary 2.3 actually read; this is not an independent audit of all 53 pages. ORIGINAL Steiner 1978 seven pages still unacquired; priority unestablished.


- F-0072 — S016 DISCHARGED loose S015 affine-intercept budget: CP-0060's SHARP bound lowers normalized A from <2*3^r to <=(3/2)^r. Valid for ALL U, not only overcritical prefixes.
- F-0073 — S016 PARTIAL extension CP-0061 beyond r/d<=1/2: every fixed rho<ln2/ln(3/2) works for gigantic effective d by PRIMARY Matveev. However the bound n>exp(epsilon*d)/2 ensures the family is nonexhaustive and misses ALL small hard representatives; no whole residue proven.
- F-0074 — S016 REFUTED extension of the SPECIFIC dominance inequality delta*2^d>2(3/2)^r at rho=2: for U=O^(2d), A=(9/4)^d>2^d and 0<delta<1. This does NOT refute actual descent of such cylinders, nor establish sharpness of the theorem's TRUE scope.
- F-0075 — S016 REFUTED EVERY-run-decrease in size-plus-v2 ranks: n=64k+59 -> 72k+67 after OOE expands with SAME v2(n+1)=2 for all k, infinitely many composite. A rank F(n,h) strictly increasing in n for h=2 cannot fall at every compressed odd-run completion. It might fall at later checkpoints.
- F-0076 — S016 INVERSE mod3 completeness still OPEN: reverse from any y multiple3 is forced doubling forever, so a greedy smaller reverse predecessor at every node is false. This does NOT exclude reaching such y from root1 through a different reverse path. Blanket all-n inverse-basin coverage would resolve Collatz and has not been proven.
- F-0077 — S016 SOURCE boundary: Matveev original English Cor.2.3 direct recheck but 53-page analytic proof not reproduced; Steiner 1978 original still unavailable; S016 claims not priority-cleared or independently refereed.


- F-0078 — S017 PARTIAL CLOSED S016 rho threshold as a limitation of METHOD, not actual endpoint: CP-0064 proves ratio-free all-lift first-crossing descent for long O^r E^c O^d E^b, including arbitrarily large r/d, from the actual n=2^r u-1 integrality and SOURCE_STATED Matveev. Arbitrary MULTI-E-block U still unproved; no CST.
- F-0079 — S017 INSUFFICIENT proposed blanket coverage by long two-run cylinders: every member with m>=M0 satisfies n>(4/3)^(M0/2)/2, excluding all small hard witnesses and whole complete positive residue classes. The finite-grid success does not remove missing ALL-n entrance.
- F-0080 — S017 REFUTED bounded maximum certificate horizon: for each H there are infinitely many composite n=2^H u-1, u odd chosen for n≡0 mod3, with first H iterates strictly ABOVE n. Unbounded integer-dependent certificates remain possible, and finite compatible exception paths are not divergent orbits.
- F-0081 — S017 SOURCE/PRIORITY LIMIT: Matveev original Cor2.3 checked but 53-page proof not independently reproduced; Steiner 1978 still indirect; ratio-free two-run statement not priority-cleared, no formal external verification.
