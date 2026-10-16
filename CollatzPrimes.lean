import Mathlib

/-!
S021: a Nat-only formal certificate for exact affine conjugation and
a uniform weighted carry budget under arbitrary block transitions.
The Collatz word-realisation and first-crossing theorems are NOT
formalized here. No sorry, custom axioms, or native_decide.
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
      simpa only [Nat.add_succ, Nat.succ_eq_add_one] using
        carry_weight_next (3 + k) ih
  have hn' : n = 3 + (n - 3) := by omega
  rw [hn']
  exact h (n - 3)

def oddRunBlock (n : ℕ) (hn : 3 ≤ n) : WeightedBlock where
  u := 3 ^ n
  v := 2 ^ n
  t := 3 ^ n - 2 ^ n
  split := by
    dsimp
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

end CollatzPrimes
