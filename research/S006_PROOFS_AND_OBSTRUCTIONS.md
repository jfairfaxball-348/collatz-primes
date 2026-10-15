# S006 — one-block equality is classical; three full cylinders and a multiplicative-rank obstruction

Date 2026-10-15. Entry LIVE main commit 5074485f78b0c84746607ef7054f9ec0e5263fa7, true tree 873308b7dd1c0e45ecbb7a3e3d1e0bad24644fe0. Shortened map T(n)=(3n+1)/2 on odd n, n/2 on even n; accelerated odd map U(n)=(3n+1)/2^v2(3n+1). Global convergence CP-0007 and Terras Coefficient Stopping Time CP-0019 are OPEN, as ever. All new mathematics below is elementary and originality UNESTABLISHED, except the explicitly marked published-source import.

## CP-0030 — strict one-block first crossing, SOURCE_STATED theorem + PROVED_INTERNAL application, NOT ORIGINAL

For a>=2, let b>=1 be minimal with 2^(a+b)>3^a, let M=2^b and D=2^(a+b)-3^a>0. On the positive O^a E^b parity cylinder all starts n=2^a*t-1 where 3^a*t=1 mod M and t=t0+q*M, q>=0. S005 proved exact n-T^(a+b)(n)=(D*t+1)/M-1>=0, but equality was left OPEN internally. The equality condition is precisely

    (2^(a+b)-3^a)*t = 2^b-1.

Theorem imported (NOT re-proved): R. P. Steiner, A Theorem on the Syracuse Problem, Congressus Numerantium XX (1978), pp. 553–559, proves the only positive integral solution to

    (2^(k+l)-3^k)*h = 2^l-1, with 2^(k+l)>3^k,

is (k,l,h)=(1,1,1), equivalently the sole positive 1-circuit is (1,2). Authoritative J. C. Lagarias, 3x+1 annotated bibliography, https://websites.umich.edu/~lagarias/doc/3x%2B1bib.pdf, entry Steiner, EXPLICITLY quotes this exact equation and result; Simons/de Weger https://www.researchgate.net/publication/228846209_Theoretical_and_computational_bounds_for_m-cycles_of_the_3n1-problem independently summarises the 1-cycle theorem and matches our odd-run/even-run definition. The original seven-page Steiner proof itself was NOT available in this environment and was NOT independently rederived. Bibliographic warning: proceedings meeting was 1977 but PUBLICATION was 1978.

Consequently equality is impossible for a>=2 given Steiner, and *every* positive O^a E^b first-crossing start drops strictly below its initial value at step a+b. This is a precise partial strict-first-crossing result incorporating a known published theorem; it proves neither existence of first crossings for arbitrary parity words nor global CST or Collatz. Do NOT label the no-equality as an original theorem. Note Steiner is stronger than our particular minimal-b condition: his statement removes every positive integral equality even without minimality of b.

## CP-0031 — EXACT three disjoint full residue cylinders (PROVED_INTERNAL, elementary)

For every integer q>=0, each row has the specified exact first j input parity word w, exact affine iterate, and strict descent:

| n | j | w | T^j(n) | n-T^j(n) |
| --- | --- | --- | --- | --- |
| 11+32q | 5 | OOEOE | 10+27q = (27n+23)/32 | 1+5q |
| 59+128q | 7 | OOEOOEE | 38+81q = (81n+85)/128 | 21+47q |
| 123+256q | 8 | OOEOOEOE | 118+243q = (243n+319)/256 | 5+13q |

Proof: direct exact positive trajectories from 11,59,123 give row words and outputs. For n=r+2^j*q, induct on i<j: the integer difference of the i-th iterates is 3^(# odd inputs through i)*2^(j-i)*q, even for i<j, thus the first j input parity bits agree. At j difference is 3^a*q, yielding the explicit coefficients above. Every row has positive drop for ALL q>=0. This is infinitely quantified, not just finite verification, and works for composite as well as prime starts. The rows are disjoint: first ≡11 mod32 whereas the other two ≡27 mod32; the latter have distinct residues 59 and 123 mod128.

Both least-potential-counterexample residue classes r=27 and r=43 (mod48) are ≡11 mod16. Fix either r. Among the 16 residues modulo256 available within that class (CRT, gcd(48,256)=16), eight satisfy n≡11 mod32, two satisfy n≡59 mod128, and one satisfies n≡123 mod256. Exactly 8+2+1=11 of the 16 residue classes modulo lcm(48,256)=768 are certified: natural relative density **11/16 = 68.75%** inside EACH of 27 and43 modulo48, with drop in <=8 T steps. Equivalently among each 256 consecutive elements r+48m, 176 are in the union. The remaining 5/16 is NOT covered by this result. In particular 27 and 91 lie outside and have long first-descents; they are not counterexamples. Every certified progression contains infinitely many composites: mod r27 all starts are multiples3, while for r43 take a compatible multiple7 by CRT (step 768 coprime7).

This builds full (not thin lift) infinite families with stronger finite stopping-depth statement than S005's sparse cylinders. However finite parity cylinders and their density are classical tools, and their mathematical novelty has NOT been demonstrated. A 68.75% fraction cannot imply 100% or exclude any hypothesized least nonconvergent integer.

## CP-0032 — no multiplicative valuation potential for ALL odd composite U steps (PROVED_INTERNAL, scoped)

Let p>0 be real and f:{1,2,3,...}->(0,+infinity) be ANY function. Consider R(n)=n^p f(v2(n+1)) on positive odd n. It is impossible that R(U(x))<R(x) for every positive odd composite x>1. This kills a genuinely nonadditive rank family and needs NO regularity, growth bound or computability assumption on f.

Proof part I (forced exponential valuation growth): for every H>=3 put t_H=7 if H even and 5 if H odd, x_H=2^H*t_H-1. Since 2^H*t_H=1 (mod3), x_H is divisible3, >3 and composite. h(x_H)=H. Also 3x_H+1=2(3*2^(H-1)*t_H-1), whose bracket is odd; thus y_H=U(x_H)=3*2^(H-1)*t_H-1 has h(y_H)=H-1 and y_H/x_H>3/2. Proposed descent implies f(H)/f(H-1)>(y_H/x_H)^p>(3/2)^p, every H>=3. So f(K)>f(2)(3/2)^{p(K-2)} and tends to infinity.

Proof part II (arbitrarily large positive valuation jumps from composite): for K>=3 set s_K=5 if K even and 25 if K odd, y_K=2^K*s_K-1, and x_K=(4*y_K-1)/3. The parity choice ensures y_K≡1 mod3, so x_K is a positive odd integer; x_K is divisible5 (s_K multiple5) and x_K>5, composite. Since 3x_K+1=4y_K with odd y_K, U(x_K)=y_K; v2(x_K+1)=1 (x_K+1=2(2y_K+1)/3 with odd quotient) and v2(y_K+1)=K. Moreover y_K/x_K=3y_K/(4y_K-1)>3/4. The supposed strict drop gives f(K)/f(1)<(x_K/y_K)^p<(4/3)^p for every K>=3, contradicting part I for large K. QED.

Scope: only one-U-step global monotonicity on all odd COMPOSITE inputs, only ranks of the specified multiplicatively separated form. Does not rule out state(r,h), prime factors, block/multiple-step, piecewise ranks, or a rank justified only along hypothetical least-counterexample descendants. Does not show divergence or solve Collatz.

## Adversarial tests, reproduction and source boundary

Independent container Python 3 checked all three CP-0031 cylinder formulas, parity words and strict drops for q=0..4999, separately checked exact class proportions 176/256 for r27/r43; checked both CP-0032 composite families for H,K=3..100 with integer arithmetic, and checked no one-block equality for a=2..1000 (the latter finite test is not the proof; Steiner is the source-level theorem). Independent source script at /tmp/s006_independent.py SHA256 ab513edebf8141d427b650691e264107501c16e33900befd8bdd93a76d9a6e8e; the three-row 5000 tests were run as a separate shell probe and are NOT part of that SHA. Repo cloning via local container DNS failed (Could not resolve host github.com). Original repo unittest/S000 audit/residue stream were NOT run locally; S005 prior hosted PR run 38713158631 job 116349307535 and merged-main push run 38713250568 job 116349613788 independently had success for unit tests, finite parity/orbit sanity, and recreate/check/consume residue stream. New S006 tests and independent hosted checks require separately observed CI, not assumed success.

Source rechecks: Terras https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/30/3/101028/a-stopping-time-problem-on-the-positive-integers (1976 metadata); Rozier–Terracol https://www.sciencedirect.com/science/article/pii/S0012365X26001913 published 2026, CST OPEN; Tao https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F proves LOGARITHMIC almost-all only; Barina https://link.springer.com/article/10.1007/s11227-025-07337-0 proves finite verified frontier 2^71; Angeltveit https://arxiv.org/abs/2602.10466 improves finite verification algorithms. Hercher 2026 Theorem 21 corrigendum was checked in S005, not re-opened in S006 and no m<=91 result is a premise here. All these are strictly weaker than full Collatz and not used to pretend a proof.

Research gaps: remaining 5/16 of r27/r43 mod48, infinitely many unbounded H branches, mod3 odd-U inverse source asymmetry, all other least-counterexample classes, and genuinely adaptive well-founded rank for every positive start. CP-0030 one-cycle theorem also does NOT imply multi-block cycle exclusion or divergence exclusion. Originality review for CP-0031/0032 incomplete, no Lean/Palomar.
