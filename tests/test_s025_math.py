"""S025: exact bitlength-adaptive prefix barriers (finite corroboration only).
Infinite existence is the elementary CRT proof in research/S025_PROOFS_AND_OBSTRUCTIONS.md.
"""
import unittest

HARD = (7, 15, 27, 31, 39, 43)
GRAMMAR = ('OOOE', 'OOOOE', 'OOOOOE', 'OOOEOOE', 'OOOOEOOE', 'OOEOOOOE')

def T(n):
    return (3 * n + 1) // 2 if n & 1 else n // 2

def affine_prefix(word):
    a, q, b = 1, 1, 0
    for ch in word:
        if ch == 'O':
            a, b = 3 * a, 3 * b + q
        q *= 2
    return a, q, b

def parity_residue(word):
    # Lift a residue one binary digit at a time, independently of any solver.
    n, a, q, b = 0, 1, 1, 0
    for ch in word:
        assert (a * n + b) % q == 0
        parity = ((a * n + b) // q) & 1
        n += (parity != (ch == 'O')) * q
        if ch == 'O':
            a, b = 3 * a, 3 * b + q
        q *= 2
    return n

def hard_word(r, h):
    assert h >= 6 and r in HARD
    if r % 16 == 7:
        return 'OOOE' + 'O' * (h - 4)
    if r % 16 == 15:
        return 'OOOOE' + 'O' * (h - 5)
    return 'OOE' + 'O' * (h - 3)

def hard_witness(r, h):
    q = 1 << h
    x = parity_residue(hard_word(r, h))
    c = [x + t * q for t in range(15)
         if (x + t * q) % 3 == r % 3 and (x + t * q) % 5 == 0]
    assert len(c) == 1
    return c[0]

class S025Math(unittest.TestCase):
    def test_bitlength_barrier_all_six_classes(self):
        for h in (6, 7, 8, 12, 16, 31, 64, 129):
            for r in HARD:
                n = hard_witness(r, h)
                self.assertTrue(5 < n < 15 * (1 << h))
                self.assertEqual(n % 48, r)
                self.assertEqual(n % 5, 0)
                self.assertLessEqual(n.bit_length(), h + 4)
                x = n
                for j, ch in enumerate(hard_word(r, h), 1):
                    self.assertEqual(x & 1, ch == 'O')
                    x = T(x)
                    self.assertGreater(x, n, (h, r, j))

    def test_all_prefixes_have_overcritical_coefficient(self):
        for h in (6, 7, 13, 64, 129):
            for r in HARD:
                w = hard_word(r, h)
                for j in range(1, h + 1):
                    a, q, b = affine_prefix(w[:j])
                    self.assertGreater(a, q)
                    self.assertGreaterEqual(b, 0)
                self.assertEqual(parity_residue(w) % 16, r % 16)

    def test_ooee_size_control_and_no_atom(self):
        for k in (2, 3, 4, 5, 8, 16, 32):
            q = 16 ** k
            root = 5 * pow(7, -1, q) % q
            options = [root + t*q for t in range(3) if (root + t*q) % 3 == 0]
            self.assertEqual(len(options), 1)
            n = options[0]
            self.assertGreater(n, 3)
            self.assertLess(n, 3*q)
            self.assertLessEqual(n.bit_length(), 4*k + 2)
            orbit_bits = []
            x = n
            for _ in range(4*k):
                orbit_bits.append('O' if x & 1 else 'E')
                x = T(x)
            s = ''.join(orbit_bits)
            self.assertEqual(s, 'OOEE' * k)
            for i in range(4*k-3):
                self.assertFalse(any(s[i:].startswith(a) for a in GRAMMAR))

    def test_adversarial_previous_cases_and_residual_graph(self):
        residual=[]
        for n in range(11,8192,16):
            x=n
            for _ in range(13):
                x=T(x)
                if x < n:
                    break
            else:
                residual.append(n)
        self.assertEqual(len(residual), 71)
        self.assertEqual(len([(a,b) for a in residual for b in residual]), 5041)
        for k in range(120):
            self.assertEqual(T(T(T(64*k+59))), 72*k+67)
        for h in (6, 13, 32):
            for u in (1, 3, 5, 7):
                n=(1<<h)*u-1
                x=n
                for j in range(h+1):
                    self.assertEqual(x,3**j*(1<<(h-j))*u-1)
                    if j < h:
                        x=T(x)
        for n in (27, 43, 91, 155, 251, 393243, 393243+524288):
            x=n
            for _ in range(200):
                self.assertGreater(x,0)
                x=T(x)

    def test_composite_witnesses_are_distinct_over_unbounded_horizon(self):
        for r in HARD:
            xs=[hard_witness(r,h) for h in range(10,51,5)]
            self.assertGreaterEqual(len(set(xs)),4)
            for h,n in zip(range(10,51,5),xs):
                self.assertGreaterEqual(n.bit_length(),2)
                self.assertEqual(n%48,r)

if __name__=='__main__':
    unittest.main()
