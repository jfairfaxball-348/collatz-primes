"""S022 exact finite audit: mixed O^aE (a>=3) with the O^4EO^2E macro.
No finite test establishes an all-integer Collatz result or priority."""
import itertools
import unittest


def affine(word):
    A, Q, B = 1, 1, 0
    for ch in word:
        if ch == "O":
            A, B = 3 * A, 3 * B + Q
        Q *= 2
    return A, Q, B


def canonical(word):
    # Independent prefix-by-prefix parity-bit lift (not CRT from final affine).
    res, A, Q, B = 0, 1, 1, 0
    for ch in word:
        parity = (A * res + B) // Q % 2
        res += ((int(ch == "O") - parity) % 2) * Q
        if ch == "O":
            A, B = 3 * A, 3 * B + Q
        Q *= 2
        assert (A * res + B) % Q == 0
    return res or Q


def orbit_word(n, word):
    x = n
    for ch in word:
        assert x % 2 == int(ch == "O"), (n, word, x)
        x = (3 * x + 1) // 2 if x % 2 else x // 2
    return x


class S022MathTests(unittest.TestCase):
    def test_macro_exact_slack_and_reverse_failure(self):
        self.assertEqual(affine("OOOOEOOE"), (729, 256, 745))
        self.assertEqual(19 * 729 - (11 * 745 + 19 * 256), 792)
        self.assertEqual(affine("OOEOOOOE"), (729, 256, 925))
        self.assertEqual(11 * 925 + 19 * 256 - 19 * 729, 1188)

    def test_mixed_3905_words_full_cylinders(self):
        alphabet = ["O" * a + "E" for a in range(3, 7)] + ["OOOOEOOE"]
        counts = {1: 0, 2: 0}
        total = 0
        for k in range(1, 6):
            for blocks in itertools.product(alphabet, repeat=k):
                U = "".join(blocks)
                A, Q, B = affine(U)
                self.assertLessEqual(11 * B + 19 * Q, 19 * A)
                self.assertLess(11 * (B + Q), 19 * A)
                for t in range(1, len(U) + 1):
                    aa, qq, _ = affine(U[:t])
                    self.assertGreater(aa, qq)
                r = U.count("O")
                for d in (1, 2):
                    m = r + d
                    j = (3 ** m).bit_length()
                    if 3 * (2 ** j - 3 ** m) > 3 ** m:
                        break
                else:
                    self.fail("CP-0071 gap failed")
                b = j - len(U) - d
                self.assertGreaterEqual(b, 1)
                W = U + "O" * d + "E" * b
                Aw, Qw, Bw = affine(W)
                self.assertEqual((Aw, Qw), (3 ** m, 2 ** j))
                for t in range(1, j):
                    aa, qq, _ = affine(W[:t])
                    self.assertGreater(aa, qq)
                n0 = canonical(W)
                self.assertGreater((Qw - Aw) * n0, Bw)
                for shift in (0, 1, 3):
                    n = n0 + shift * Qw
                    self.assertLess(orbit_word(n, W), n)
                counts[d] += 1
                total += 1
        self.assertEqual(total, 3905)
        self.assertEqual(counts, {1: 2251, 2: 1654})

    def test_adjacent_gap_bracket_5000(self):
        for m in range(1, 5001):
            p = 3 ** m
            high = p.bit_length()
            low = high - 1
            self.assertLess(2 ** low, p)
            self.assertLess(p, 2 ** high)
            if 4 * p >= 3 * 2 ** high:
                self.assertLess(2 ** (low + 2), 3 ** (m + 1))
                self.assertLess(3 ** (m + 1), 2 ** (low + 3))
                self.assertLess(4 * 3 ** (m + 1), 3 * 2 ** (low + 3))

    def test_original_71_of_512_control(self):
        residual = []
        for n in range(11, 8192, 16):
            x = n
            visited_smaller = False
            for _ in range(13):
                x = (3 * x + 1) // 2 if x & 1 else x // 2
                visited_smaller |= x < n
            if not visited_smaller:
                residual.append(n)
        self.assertEqual(len(residual), 71)
        self.assertEqual(len(residual) ** 2, 5041)

    def test_hard_expanding_controls(self):
        for n in (27, 43, 91, 155, 251):
            self.assertGreater(n, 1)
        for k in (0, 1, 4, 10):
            n = 64 * k + 59
            x = n
            for _ in range(3):
                x = (3 * x + 1) // 2 if x & 1 else x // 2
            self.assertEqual(x, 72 * k + 67)


if __name__ == "__main__":
    unittest.main()
