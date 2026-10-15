import unittest
from itertools import product


def intercept(word):
    B = 0
    for i, c in enumerate(word):
        if c == "O":
            B = 3 * B + (1 << i)
    return B


def canon(word):
    m = word.count("O")
    j = len(word)
    mod = 1 << j
    B = intercept(word)
    n = (-B * pow(3 ** m, -1, mod)) % mod
    return n, B, mod - 3 ** m


def orbit(word, n):
    val = n
    for c in word:
        assert ("O" if val & 1 else "E") == c, (word, n, c, val)
        val = (3 * val + 1) // 2 if val & 1 else val // 2
    return val


class S018ExactFiniteTests(unittest.TestCase):
    def test_sharp_intercept_all_words_upto_nine(self):
        for length in range(1, 10):
            for word in map("".join, product("OE", repeat=length)):
                r = word.count("O")
                if r:
                    e = length - r
                    B = intercept(word)
                    self.assertLessEqual(B, (1 << e) * (3 ** r - (1 << r)))
                    self.assertLessEqual(B + (1 << length), (1 << e) * (3 ** r))

    def test_arbitrary_multiblock_exact_cylinders(self):
        for k in range(1, 32):
            U = "O" * (2 * k) + "OOOE" * k
            r, e = U.count("O"), U.count("E")
            a = len(U) - len(U.lstrip("O"))
            d = 1
            m = r + d
            j = (3 ** m).bit_length()
            b = j - len(U) - d
            self.assertGreaterEqual(b, 1)
            w = U + "O" * d + "E" * b
            n, B, D = canon(w)
            self.assertGreater(n, 0)
            self.assertGreater(D * ((1 << a) - 1), 3 ** m * (1 << e))
            self.assertGreater(D * n, B)
            for q in (0, 1, 7):
                nn = n + q * (1 << j)
                self.assertLess(orbit(w, nn), nn)

    def test_multiblock_small_leading_run_has_no_implied_failure(self):
        for U, d in (("OOOEOOOE", 1), ("OOOEOOOEOOOE", 2), ("OOEOOEOOE", 1)):
            m = U.count("O") + d
            j = (3 ** m).bit_length()
            b = j - len(U) - d
            w = U + "O" * d + "E" * b
            n, B, D = canon(w)
            self.assertGreater(D * n, B)
            self.assertLess(orbit(w, n), n)

    def test_all_first_crossings_up_to_length_eighteen(self):
        stack = [("", 0, 0)]
        total = 0
        bad = []
        while stack:
            w, m, B = stack.pop()
            if len(w) >= 18:
                continue
            for c in "OE":
                mm = m + (c == "O")
                bb = 3 * B + (1 << len(w)) if c == "O" else B
                ww = w + c
                j = len(ww)
                if 3 ** mm > (1 << j):
                    stack.append((ww, mm, bb))
                elif 3 ** mm < (1 << j) and ww.startswith("O"):
                    total += 1
                    n = (-bb * pow(3 ** mm, -1, 1 << j)) % (1 << j)
                    if ((1 << j) - 3 ** mm) * n <= bb:
                        bad.append((ww, n))
        self.assertEqual(bad, [("OE", 1)])
        self.assertGreater(total, 1000)

    def test_exact_crt_equivalence_and_necessary_filter(self):
        for U, d in (("OOOEOOOE", 1), ("OOOEOOOEOOOE", 2), ("OOEOOEOOE", 1)):
            m = U.count("O") + d
            j = (3 ** m).bit_length()
            w = U + "O" * d + "E" * (j - len(U) - d)
            n, B, D = canon(w)
            Hnumerator = intercept(U) + (1 << len(U))
            e = U.count("E")
            self.assertLessEqual(Hnumerator, (1 << e) * 3 ** U.count("O"))
            self.assertEqual(orbit(w, n) < n, D * n > B)
            self.assertLess(B * (3 ** U.count("O")), 3 ** m * (1 << e) * 3 ** U.count("O"))

    def test_fixed_horizon_composite_towers(self):
        for H in (8, 16, 32):
            u = 7 if H % 2 == 0 else 5
            n = (1 << H) * u - 1
            self.assertEqual(n % 3, 0)
            v = n
            for j in range(1, H + 1):
                self.assertEqual(v & 1, 1)
                v = (3 * v + 1) // 2
                self.assertGreater(v, n)


if __name__ == "__main__":
    unittest.main()
