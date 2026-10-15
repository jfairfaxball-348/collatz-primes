"""S017 exact finite hostile controls; finite tests do not prove global Collatz."""
from itertools import combinations
import unittest


def intercept(word):
    b = 0
    r = 0
    for i, parity in enumerate(word):
        if parity == "O":
            b = 3 * b + 2**i
            r += 1
    return b, r


def canonical(word):
    b, r = intercept(word)
    mod = 2**len(word)
    return (-b * pow(3**r, -1, mod)) % mod


def iterate_with_parities(n, word):
    for letter in word:
        assert ("O" if n % 2 else "E") == letter
        n = (3*n+1)//2 if n % 2 else n//2
    return n


class S017ExactMath(unittest.TestCase):
    def test_all_ratio_two_run_small_grid(self):
        count = 0
        for r in range(3, 26):
            for c in range(1, r+1):
                if 2**(r+c) >= 3**r:
                    break
                for d in range(1, 26):
                    m = r+d
                    j = (3**m).bit_length()
                    b = j-(r+c+d)
                    self.assertGreaterEqual(b, 1)
                    word = "O"*r + "E"*c + "O"*d + "E"*b
                    n0 = canonical(word)
                    self.assertGreater(n0, 0)
                    affine, odds = intercept(word)
                    self.assertEqual(odds, m)
                    for q in (0, 1, 2, 7):
                        n = n0+q*2**j
                        t = iterate_with_parities(n, word)
                        self.assertEqual(t*2**j, 3**m*n+affine)
                        self.assertLess(t, n)
                    count += 1
        self.assertEqual(count, 4425)

    def test_sharp_intercept_extrema(self):
        for ell in range(1, 12):
            for r in range(1, ell+1):
                lo = 3**r-2**r
                hi = 2**(ell-r)*lo
                self.assertEqual(intercept("O"*r+"E"*(ell-r))[0], lo)
                self.assertEqual(intercept("E"*(ell-r)+"O"*r)[0], hi)
                if ell <= 9:
                    for inds in combinations(range(ell), r):
                        word = "".join("O" if i in inds else "E" for i in range(ell))
                        self.assertTrue(lo <= intercept(word)[0] <= hi)

    def test_exact_lift_threshold(self):
        for word in ("O", "OE", "OOEOEE", "OOOEOEE", "OOOEEOEEEE"):
            b, m = intercept(word)
            j = len(word)
            d = 2**j-3**m
            if d <= 0:
                continue
            n0 = canonical(word)
            if n0 == 0:
                n0 = 2**j
            qmin = max(0, (b-d*n0)//(d*2**j)+1)
            for q in range(0, 20):
                n=n0+q*2**j
                self.assertEqual((d*n>b), q>=qmin)
                self.assertEqual(iterate_with_parities(n, word)*2**j,
                                 3**m*n+b)

    def test_expanding_same_v2_renewal(self):
        for k in range(200):
            n=64*k+59
            t=iterate_with_parities(n, "OOE")
            self.assertEqual(t, 72*k+67)
            self.assertGreater(t, n)
            self.assertEqual((n+1)&-(n+1), 4)
            self.assertEqual((t+1)&-(t+1), 4)

    def test_forced_odd_composite_unbounded_depth(self):
        for h in range(1, 40):
            u=7 if h%2==0 else 5
            n=2**h*u-1
            self.assertEqual(n%3, 0)
            self.assertGreater(n, 3)
            for k in range(1, h+1):
                self.assertGreater(3**k*2**(h-k)*u-1, n)
            self.assertEqual(iterate_with_parities(n,"O"*h),
                             3**h*u-1)

    def test_analytic_threshold_algebra_sanity(self):
        c=10**10
        x=16*(c+10)
        self.assertGreater(x*x//8 - c*(1+x), 2)
        self.assertEqual(x*x, (16*(c+10))**2)


if __name__ == "__main__":
    unittest.main()
