import Mathlib

/-!
S021: a Nat-only formal certificate for exact affine conjugation and
a uniform weighted carry budget under arbitrary block transitions.
The Collatz word-realisation and first-crossing theorems are NOT
formalized here. The displayed proofs have no admitted placeholders.
-/
namespace CollatzPrimes

theorem conjugate_step (A Q B F x y : ℕ)
    (hA : A = Q + F) (hstep : Q * y = A * x + B) :
    Q * (F * y + B) = A * (F * x + B) := by
  calc
    Q * (F * y + B) = F * (Q * y) + Q * B := by ring
    _ = F * (A * x + B) + Q * B := by rw [hstep]
    _ = A * (F * x + B) := by rw [hA]; ring

theorem conjugate_iterate (A Q B F : ℕ) (x : ℕ → ℕ)
    (hA : A = Q + F)
    (hstep : ∀ i : ℕ, Q * x (i + 1) = A * x i + B)
    (k : ℕ) :
    Q ^ k * (F * x k + B) = A ^ k * (F * x 0 + B) := by
  induction k with
  | zero => simp
  | succ k ih =>
    have hk := conjugate_step A Q B F (x k) (x (k + 1)) hA (hstep k)
    calc
      Q ^ (k + 1) * (F * x (k + 1) + B)
          = Q ^ k * (Q * (F * x (k + 1) + B)) := by simp [pow_succ]; ring
      _ = Q ^ k * (A * (F * x k + B)) := by rw [hk]
      _ = A * (Q ^ k * (F * x k + B)) := by ring
      _ = A * (A ^ k * (F * x 0 + B)) := by rw [ih]
      _ = A ^ (k + 1) * (F * x 0 + B) := by simp [pow_succ]; ring

structure AffineState where
  A : ℕ
  B : ℕ
  Q : ℕ

/-- An abstract O^a E block: u = 3^a, v = 2^a, t = u-v.
    The weight inequality is precisely what preserves 11 B + 19 Q ≤ 19 A. -/
structure WeightedBlock where
  u : ℕ
  v : ℕ
  t : ℕ
  split : u = v + t
  admissible : 27 * v ≤ 8 * u

def appendBlock (s : AffineState) (p : WeightedBlock) : AffineState :=
  { A := p.u * s.A
    B := p.u * s.B + p.t * s.Q
    Q := 2 * p.v * s.Q }

theorem carry_budget_step (s : AffineState) (p : WeightedBlock)
    (hs : 11 * s.B + 19 * s.Q ≤ 19 * s.A) :
    11 * (appendBlock s p).B + 19 * (appendBlock s p).Q
      ≤ 19 * (appendBlock s p).A := by
  change 11 * (p.u * s.B + p.t * s.Q) + 19 * (2 * p.v * s.Q)
    ≤ 19 * (p.u * s.A)
  have hmul : p.u * (11 * s.B + 19 * s.Q) ≤ p.u * (19 * s.A) :=
    Nat.mul_le_mul_left p.u hs
  have hgap : (27 * p.v) * s.Q ≤ (8 * p.u) * s.Q :=
    Nat.mul_le_mul_right s.Q p.admissible
  have hsplit : p.u * s.Q = p.v * s.Q + p.t * s.Q := by
    rw [p.split]
    ring
  nlinarith only [hmul, hgap, hsplit]

theorem carry_budget_fold (ps : List WeightedBlock) (s : AffineState)
    (hs : 11 * s.B + 19 * s.Q ≤ 19 * s.A) :
    11 * (ps.foldl appendBlock s).B + 19 * (ps.foldl appendBlock s).Q
      ≤ 19 * (ps.foldl appendBlock s).A := by
  induction ps generalizing s with
  | nil => simpa using hs
  | cons p ps ih =>
    exact ih (appendBlock s p) (carry_budget_step s p hs)

theorem pow_two_le_three (n : ℕ) : 2 ^ n ≤ 3 ^ n := by
  induction n with
  | zero => norm_num
  | succ n ih =>
    calc
      2 ^ (n + 1) = 2 ^ n * 2 := by simp [pow_succ]
      _ ≤ 3 ^ n * 2 := Nat.mul_le_mul_right 2 ih
      _ ≤ 3 ^ n * 3 := Nat.mul_le_mul_left (3 ^ n) (by norm_num)
      _ = 3 ^ (n + 1) := by simp [pow_succ]

theorem carry_weight_next (n : ℕ) (h : 27 * 2 ^ n ≤ 8 * 3 ^ n) :
    27 * 2 ^ (n + 1) ≤ 8 * 3 ^ (n + 1) := by
  calc
    27 * 2 ^ (n + 1) = (27 * 2 ^ n) * 2 := by simp [pow_succ]; ring
    _ ≤ (8 * 3 ^ n) * 2 := Nat.mul_le_mul_right 2 h
    _ ≤ (8 * 3 ^ n) * 3 := Nat.mul_le_mul_left (8 * 3 ^ n) (by norm_num)
    _ = 8 * 3 ^ (n + 1) := by simp [pow_succ]; ring

theorem carry_weight_ge_three (n : ℕ) (hn : 3 ≤ n) :
    27 * 2 ^ n ≤ 8 * 3 ^ n := by
  have h : ∀ k : ℕ, 27 * 2 ^ (3 + k) ≤ 8 * 3 ^ (3 + k) := by
    intro k
    induction k with
    | zero => norm_num
    | succ k ih =>
      simpa only [Nat.add_assoc] using
        carry_weight_next (3 + k) ih
  have hn' : n = 3 + (n - 3) := by omega
  rw [hn']
  exact h (n - 3)

def oddRunBlock (n : ℕ) (hn : 3 ≤ n) : WeightedBlock where
  u := 3 ^ n
  v := 2 ^ n
  t := 3 ^ n - 2 ^ n
  split := by
    have hp := pow_two_le_three n
    omega
  admissible := carry_weight_ge_three n hn

def initialState : AffineState := ⟨1, 0, 1⟩

def variableRunState (runs : List {n : ℕ // 3 ≤ n}) : AffineState :=
  (runs.map (fun n => oddRunBlock n.1 n.2)).foldl appendBlock initialState

/-- Uniform bound for every finite, arbitrarily ordered sequence of O^a E blocks,
    a ≥ 3. This does not assert any particular integer realizes the extension. -/
theorem variable_runs_budget (runs : List {n : ℕ // 3 ≤ n}) :
    11 * (variableRunState runs).B + 19 * (variableRunState runs).Q
      ≤ 19 * (variableRunState runs).A := by
  unfold variableRunState
  apply carry_budget_fold
  norm_num [initialState]


/-!
S022 extension: the combined block O⁴ E O² E has exact parameters
(A,Q,B) = (729,256,745). Unlike a single O² E block, this whole
two-block macro preserves the weighted carry inequality.
-/
def appendFourTwo (s : AffineState) : AffineState :=
  { A := 729 * s.A
    B := 729 * s.B + 745 * s.Q
    Q := 256 * s.Q }

theorem carry_budget_four_two (s : AffineState)
    (hs : 11 * s.B + 19 * s.Q ≤ 19 * s.A) :
    11 * (appendFourTwo s).B + 19 * (appendFourTwo s).Q
      ≤ 19 * (appendFourTwo s).A := by
  change 11 * (729 * s.B + 745 * s.Q) + 19 * (256 * s.Q)
    ≤ 19 * (729 * s.A)
  have h := Nat.mul_le_mul_left 729 hs
  nlinarith only [h, Nat.zero_le s.Q]

inductive CarryAtom where
  | standard (n : {a : ℕ // 3 ≤ a})
  | fourTwo

def appendCarryAtom (s : AffineState) : CarryAtom → AffineState
  | .standard n => appendBlock s (oddRunBlock n.1 n.2)
  | .fourTwo => appendFourTwo s

theorem carry_budget_atom (s : AffineState) (p : CarryAtom)
    (hs : 11 * s.B + 19 * s.Q ≤ 19 * s.A) :
    11 * (appendCarryAtom s p).B + 19 * (appendCarryAtom s p).Q
      ≤ 19 * (appendCarryAtom s p).A := by
  cases p with
  | standard n =>
    exact carry_budget_step s (oddRunBlock n.1 n.2) hs
  | fourTwo =>
    exact carry_budget_four_two s hs

def mixedRunState (bs : List CarryAtom) : AffineState :=
  bs.foldl appendCarryAtom initialState

/-- Every ordering of long odd-run atoms and (O⁴ E O² E) macros
    preserves the same rational carry budget, including unbounded lists. -/
theorem mixed_runs_budget (bs : List CarryAtom) :
    11 * (mixedRunState bs).B + 19 * (mixedRunState bs).Q
      ≤ 19 * (mixedRunState bs).A := by
  have h :
      ∀ (xs : List CarryAtom) (s : AffineState),
        11 * s.B + 19 * s.Q ≤ 19 * s.A →
        11 * (xs.foldl appendCarryAtom s).B + 19 * (xs.foldl appendCarryAtom s).Q
          ≤ 19 * (xs.foldl appendCarryAtom s).A := by
    intro xs
    induction xs with
    | nil =>
      intro s hs
      simpa using hs
    | cons x xs ih =>
      intro s hs
      exact ih (appendCarryAtom s x) (carry_budget_atom s x hs)
  exact h bs initialState (by norm_num [initialState])

/-- Arithmetic heart of the CP-0071 two-consecutive-gap argument.
    Here j is the exponent of the power *below* 3^m; the actual
    bitlength existence lemma has NOT been formalized. -/
theorem consecutive_gap_from_bracket (m j : ℕ)
    (hlo : 2 ^ j < 3 ^ m)
    (hhi : 3 ^ m < 2 ^ (j + 1))
    (hnot : 3 * 2 ^ (j + 1) ≤ 4 * 3 ^ m) :
    2 ^ (j + 2) < 3 ^ (m + 1) ∧
    3 ^ (m + 1) < 2 ^ (j + 3) ∧
    4 * 3 ^ (m + 1) < 3 * 2 ^ (j + 3) := by
  have e1 : 2 ^ (j + 1) = 2 * 2 ^ j := by
    simp [pow_succ]
    ring
  have e2 : 2 ^ (j + 2) = 4 * 2 ^ j := by
    simp [pow_succ, pow_add]
    ring
  have e3 : 2 ^ (j + 3) = 8 * 2 ^ j := by
    simp [pow_succ, pow_add]
    ring
  have e4 : 3 ^ (m + 1) = 3 * 3 ^ m := by
    simp [pow_succ]
    ring
  rw [e2, e4, e3]
  have hpos : 0 < 3 ^ m := pow_pos (by norm_num) m
  rw [e1] at hnot hhi
  constructor
  · nlinarith only [hnot, hpos]
  constructor
  · nlinarith only [hhi, Nat.zero_le (2 ^ j)]
  · nlinarith only [hhi]

theorem two_choice_gap_from_bracket (m j : ℕ)
    (hlo : 2 ^ j < 3 ^ m)
    (hhi : 3 ^ m < 2 ^ (j + 1)) :
    4 * 3 ^ m < 3 * 2 ^ (j + 1) ∨
      (2 ^ (j + 2) < 3 ^ (m + 1) ∧
       3 ^ (m + 1) < 2 ^ (j + 3) ∧
       4 * 3 ^ (m + 1) < 3 * 2 ^ (j + 3)) := by
  by_cases h : 4 * 3 ^ m < 3 * 2 ^ (j + 1)
  · exact Or.inl h
  · exact Or.inr (consecutive_gap_from_bracket m j hlo hhi (Nat.le_of_not_gt h))

/-- If an actual parity-word cylinder has affine coefficient A,
    modulus Q=A+D and B intercept, a bound B<D*n gives descent
    for EVERY individual positive lift satisfying that affine law.
    Parity-realisation and canonical residue existence are separate. -/
theorem all_lifts_strict_descent (A Q B D n y : ℕ)
    (hQ : Q = A + D)
    (hword : Q * y = A * n + B)
    (hmargin : B < D * n) :
    y < n := by
  have hlt : Q * y < Q * n := by
    rw [hQ] at hword ⊢
    nlinarith only [hword, hmargin]
  have hpos : 0 < Q := by
    by_contra hn
    have hzero : Q = 0 := by omega
    rw [hzero] at hlt
    omega
  exact (Nat.mul_lt_mul_left hpos).mp hlt


end CollatzPrimes
