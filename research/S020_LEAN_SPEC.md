# S020 Lean 4 formalisation specification — NO_LEAN_VERIFIED

The toolchain check on the isolated scratch environment, 2026-10-16, gave no executable paths for either lean or lake. NO code in this document has been compiled or proof-checked. The following is a precise Nat-only specification and recommended proof order; not a fictitious Lean certificate.

## Shortest self-contained target: affine conjugated step, periodic divisibility (CP-0068)

Define the shortened Collatz step T : Nat -> Nat by odd/even cases. Define for words V : List Bool, with true denoting O: r(V):Nat, L(V):Nat, A(V)=3^r(V), Q(V)=2^L(V), and intercept B(V):Nat recursively by B([])=0, B(V++[false])=B(V), B(V++[true])=3*B(V)+2^L(V). The actual word-realisation condition says that the input parity of T^[i](n) equals V[i] for all 0<=i<L(V).

For a generic block step use NATURAL numbers A,Q,B,F,x,y with assumptions:
  (hA : A = Q+F)
  (hStep : Q*y = A*x+B)
Then the exact polynomial lemma is
  Q*(F*y+B) = A*(F*x+B).
No subtraction and no signed divisibility are required; prove by ring normalization after rewriting hA.

For k blocks, let (x : Nat -> Nat), (k:Nat), and
  (hStep : forall i:Nat, i<k -> Q*x(i+1)=A*x(i)+B).
Then induction yields the exact Nat equality
  Q^k * (F*x(k)+B) = A^k*(F*x(0)+B).
With (hcop : Nat.Coprime A Q), coprimality of powers and Euclid's lemma yield the exact Nat statement
  Q^k ∣ (F*x(0)+B).
Use positive Q, A; F=A-Q only if A>=Q (overcritical block case), so no Nat subtraction underflow. For general words with A<Q, the signed form may be written in Int explicitly and proven separately. The S019 general A-Q divisibility lives naturally in Int, whereas THIS Nat lemma targets A>Q. Follow with Q^k <= F*x(0)+B when F*x(0)+B >0, and x(0)>=1.

This is a proof target, NOT compiled Lean source. Any use of sorry, axiom or native_decide to evade general quantifiers fails the formal gate.

## Priority formal target CP-0070–0072

1. Carry as rationals H(V)=(B(V)+Q(V))/A(V) and S(V)=Q(V)/A(V), with A(V)>0. Prefer clearing denominators everywhere in Nat: a clean fixed-alphabet lemma is
    11*(B(U)+Q(U)) < 19*A(U)
   for U in {OOOE,OOOOE}^k, k>=1.
   Prove by induction on list of blocks, recording boundary scaled coefficient and the exact E increments, or by a strengthened Nat invariant.
2. Exponent-gap lemma: define j(m)=Nat.log2(3^m)+1 for m>=1, so 2^(j-1)<3^m<2^j. Prove
    exists d:Nat, (d=1 or d=2) and
    3*(2^j(m+d)-3^(m+d)) > 3^(m+d).
   Avoid Nat subtraction via
    3*2^j(m+d) > 4*3^(m+d).
   One exponent works; if first fails, show j(m+1)=j(m)+2 using 2*2^j<3^(m+1)<4*2^j.
3. General cylinder lemma: for a nonempty all-prefix-overcritical U beginning a O letters, assume
    3*(B(U)+Q(U)) < (2^a-1)*A(U).
   Choose d=1 or2 from the gap lemma; set m=r(U)+d, j=j(m), b=j-(L(U)+d) with a PROOF j>L(U)+d before using Nat subtraction. The parity word W=U++O^d++E^b has first coefficient crossing at j and for ALL positive actual cylinder n satisfies (T^[j])(n)<n.
   Prove with cleared denominators and the identity
    B(W)+2^(L(U)+d)=3^d*(B(U)+2^L(U)).
4. Existence of actual cylinder inputs: parity-code bijection modulo 2^j, derive the unique residue from invertible 3^m modulo 2^j. Infinitely many composites follow using Chinese remainder modulo3 and n>3. Keep this separate from the all-lifts descent lemma.
5. Keep finite Python tests and host CI classified FINITE_TEST, not FORMAL_VERIFIED.

No project CI presently installs Lean, so a future session must actually add a pinned elan/lake/mathlib toolchain and compile checked-in Lean code. Independently inspect the compiler log before updating the formalisation status.