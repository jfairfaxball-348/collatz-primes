# S005 — exact O-run first crossing, six-class forward grammar and additive-state-rank obstruction

Date: 2026-10-15. Map T(n)=n/2 (even), (3n+1)/2 (odd), U(x)=(3x+1)/2^v2(3x+1) (odd x); omega(x)=number of distinct positive prime divisors, omega(1)=0. CP-0007 full Collatz and CP-0019 Terras CST remain OPEN. All new claims below are **PROVED_INTERNAL elementary**, not priority/originality assertions; independent finite checking has a separate evidence tier.

## CP-0026: every O^a E^b first crossing is non-increasing; equality is the ONLY obstruction

Fix any integer a>=2 and b the least positive integer such that 2^(a+b)>3^a; write j=a+b and D=2^j-3^a>0. Let M=2^b, t0 be the unique integer in [1,M] such that 3^a*t0=1 (mod M); necessarily 1<=t0<M (M>=4) and odd.

The **entire positive O^a E^b parity cylinder** is n=2^a*t-1 for t=t0+q*M, q>=0. Proof: the initial a odd steps force n=-1 (mod2^a), and T^a(n)=3^a*t-1; b consecutive even input steps are equivalent to 3^a*t=1 (mod M). No earlier coefficient crossing is possible, by minimality of b and the initial all-O growth.

At j, T^j(n)=(3^a*t-1)/M. Therefore
    n-T^j(n)=(D*t-(M-1))/M=(D*t+1)/M-1.
Since D*t=-3^a*t=-1 (mod M), the positive integer D*t+1 is a positive multiple of M. Thus n-T^j(n) is an **integer >=0**. In particular there is NO overshoot T^j(n)>n at the first coefficient crossing for ANY positive member of these cylinders. Further,
    drop(q)=drop(0)+D*q,  drop(0)=(D*t0+1)/M-1 >=0.
Consequently ALL q>=1 descend STRICTLY at their first coefficient crossing. The only possible equality is q=0 and **D*t0=M-1**. In that event T^j(n0)=n0 where n0=2^a*t0-1>=3, hence a nontrivial positive shortened-Collatz periodic orbit, not an allowable conclusion that equality cannot occur. Conversely equality has exactly that Diophantine equation. The special a=1,t=1 gives base 1->2->1; do not extend the strict claim to base1. No theorem here proves absence of nontrivial cycles or Terras CST.

This is sharper than CP-0023 for complementary a in that it proves no overshoot for ALL their positive representatives, while preserving the unresolved equality case. It also supplies strict infinite q>=1 subfamilies for every a, including complementary a. These follow from classical affine-cylinder arithmetic; originality NOT established.

## CP-0027: a proved infinite subband of the previously uncovered exponents

Write alpha=log_2(3/2), f_a={a*alpha}, b=floor(a*alpha)+1. Irrationality of alpha follows from unique prime factorisation: alpha=p/q would imply 3^q=2^(p+q). Since 3^a/2^(a+b)=2^(f_a-1),
    D/M=2^a*(1-2^(f_a-1)).
For a>=3 with f_a<=4/5,
    D/M >=8*(1-2^(-1/5))>1
because (8/7)^5=32768/16807<2. Thus D>M, and EVERY positive member, including q=0, descends STRICTLY at its first crossing. In particular every a>=3 with **alpha<f_a<=4/5** belongs to S004's previously UNcertified f_a>alpha region but is now uniformly certified. The interval (alpha,4/5) is nonempty (alpha<4/5 follows (3/2)^5<2^4), and irrational rotation a*alpha mod1 visits every nonempty interval infinitely often (classical elementary density of irrational rotations). Hence there are **infinitely many** distinct complementary a satisfying the new full-cylinder strict theorem, with no finite experiment used in this proof. This does not certify the near-resonant f_a>4/5 tail and does not solve the one-block equality question.

## CP-0028: explicit mixed forward grammar for ALL six potential least-counterexample residues (restricted, not universal)

**Finite word lifting lemma.** If an integer r>1 follows an admissible length-j parity word w with a O steps and T^j(r)=s<r, then for every q>=0, n=r+3*2^j*q has exactly the same first j parities, satisfies n=r (mod48) whenever r is any of the odd residues below and j>=4, and
    T^j(n)=s+3^(a+1)*q,
    n-T^j(n)=(r-s)+3*(2^j-3^a)*q>0.
Proof by induction: n-r multiple of 2^j and, at time i<j, the difference is 3^(a_i)*3*2^(j-i)*q, an even integer, so parity agrees; after j steps the exact difference is 3^(a+1)*q. D=2^j-3^a>0 because s<r and the affine offset is nonnegative. Since 3*2^j is a multiple of48 for j>=4, the mod48 residue is held. Each progression contains infinitely many **composites**: set q=r*m for m>=1 so n=r*(1+3*2^j*m).

The following exact direct integer certificates (w is the sequence of T input parities; zero earlier strict descent is checked by the same recurrence) instantiate the rule:

| r mod48 | j first descent | #O a | T^j(r)=s | D=2^j-3^a | parity word |
|---|---:|---:|---:|---:|---|
| 7 | 7 | 4 | 5 | 47 | OOOEOEE |
| 15 | 7 | 4 | 10 | 47 | OOOOEEE |
| 27 | 59 | 37 | 23 | 126176846412426125 | OOEOOOOOEOEOOEOOOEOOOOEOEEOOOEOOEOOOOOOEEOOOOEEEOEOEOEEEOEE |
| 31 | 56 | 35 | 23 | 22026048938928229 | OOOOOEOEOOEOOOEOOOOEOEEOOOEOOEOOOOOOEEOOOOEEEOEOEOEEEOEE |
| 39 | 8 | 5 | 38 | 13 | OOOEOOEE |
| 43 | 5 | 3 | 37 | 5 | OOEOE |

This produces genuinely quantified infinite strict-descent sets in ALL six classes, but they are sparse cylinders contained in known classical affine lift machinery. No complete class, and no global least-counterexample class, has been removed. The 27 subfamily is contained in (not stronger than) CP-0015's exact n=27+2^59*q theorem.

**Adaptive O-exit rule.** For arbitrary H>=2, use unbounded state (H,t) with n=2^H*t-1, t odd; after H consecutive O steps the value is 3^H*t-1. Let b(H) minimal with 2^(H+b)>3^H. When 3^H*t=1 (mod2^b(H)) and t=t0+q2^b with q>=1, CP-0026 proves strict descent at H+b. This explicitly tracks v2(n+1)=H and the mixed output residue 3^H*t modulo2^b. For each H>=4 choose t by CRT additionally so n is 15 or 31 mod48 (t=(-1)^H mod3 for r=15, t=2*(-1)^H mod3 for r=31); arbitrarily large q exists meeting both, giving infinite strict composites with arbitrarily high H in BOTH classes. For H=3, the input condition t=3 mod4 (because 3^3*t=1 mod4) is compatible with r=7 or39 mod48 via mod3 selection. Conversely for r=27/43, H=2 forces t=3 mod4 whereas b(2)=2 requires t=1 mod4: the adaptive O-exit rule does NOT cover those entire classes; only their explicitly certified finite-word subfamilies above. Reverse U sources y=0 mod3 have NO odd predecessor; y=1 mod3 have only larger ones; this forward grammar does not erase those obstructions.

## CP-0029: an infinite composite obstruction to additive adaptive size/valuation/factor/residue ranks

Let R(n)=n+A_(r,h)+B_(r,h)*omega(n), with r=n mod48 and h=v2(n+1), and with **arbitrary fixed finite real** A_(r,h), B_(r,h) (state-dependent, even unbounded as h varies). Proposing one-step strict monotonicity R(U(x))<R(x) for ALL positive odd composite x is false. For every integer q>=1 choose
    x=96*q+15=16*(6*q+1)-1=3*(32*q+5) (composite),
    y=144*q+23=24*(6*q+1)-1.
Since 3*x+1=2*y with y odd, U(x)=y. Their exact states are (x mod48,v2(x+1))=(15,4) and (y mod48,v2(y+1))=(23,3). Yet y-x=48*q+8. Hence
    R(y)-R(x)=48*q+8+A_(23,3)-A_(15,4)+B_(23,3)*omega(y)-B_(15,4)*omega(x).
For positive z>=2, omega(z)<=log_2 z (each distinct prime factor >=2). Therefore the absolute value of the penalty terms is O(log q), with constants fixed by the two states; 48q+8 dominates. R(y)>R(x) for all sufficiently large q. This refutes even arbitrary real fixed additive state/valuation/prime-support weights for **one-U-step** descent; it does NOT refute nonlinear, increasing-depth, multiple-step, or lexicographic well-founded ranks and does not establish divergence.

Hostile checks: 15->23->35 returns factor5; 121->91 increases omega from1 to2; 27->41->31 and then first strict T descent at j59; every 12t+3 (t>=1) grows under first U; x=2^H*t-1 has H initial O steps of growth; odd multiples3 have no odd U predecessor; 7 reaches 5 at j7, then 8>7 at later j8 (not a first-crossing counterexample); 1+2^k*q with k>=2, q>=1 descends in two T steps. All are consistent with the delimited positive theorems.

## Independent finite checks, sources and missing global step

Independent container Python 3 arithmetic executed 2026-10-15 outside a checkout: a=2..256 (149 S004-band eligible and **55 newly complementary-band eligible**, no equality case observed in 255 starts, finite ONLY), all q=0,1,2 exact parity and drop checks; exact six row certificates and q=0,1,2,7 lifts; 1999 composite additive-rank witnesses; mandatory hostile controls. Independent script SHA256 62e3a17befa81030bafd8b8c80628f8d53c28edf2f58150653bc7f41c3432711 (local /tmp/s005_independent.py; not in original checkout). New in-repo tests/test_s005_grammar.py reproduces bounded claims; original repository tests/audit/manifest/checker/consumer cannot be claimed locally since GitHub clone DNS failed. Github-hosted PR and merged-main steps must be observed separately. There is NO numerical or algorithmic universal conclusion.

Direct source audit 15 October 2026: Terras 1976 Acta Arithmetica 30 pp241-252 publisher bibliographic page (original full text NOT independently reconstructed); Rozier–Terracol Discrete Mathematics 349 (2026) 115167 publisher article explicitly identifies OPEN CST and affine paradoxical sequences; Tao 2022 almost all in logarithmic density; Bařina J Supercomputing 81:810 (2025) finite <2^71 published; Angeltveit arXiv:2602.10466 finite improved algorithms; Hercher June 2026 both-page corrigendum explicitly corrects a Theorem 21 inequality derivation with convex-polytope maxima. No primary source proves global Collatz. No specific one-block-cycle priority survey was completed and no originality claim is made; independent one-cycle literature is an S006 target.

OPEN: Can equality D*t0=2^b-1 occur for some a>=2? Can the thin r=27/43 progressions be enlarged to all members by a NONCIRCULAR rank/grammar? Can a nonlinear block-valued potential handle all six least-counterexample classes, source residues mod3 and unbounded H? No complete answers here.
