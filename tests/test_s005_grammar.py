"""S005 delimited exact integer checks; not a Collatz universality certificate."""
import unittest

def T(n):
    return (3*n+1)//2 if n & 1 else n//2

def b_of(a):
    b = 1
    while 1 << (a+b) <= 3**a:
        b += 1
    return b

def word(start, j):
    x = start
    bits = []
    for _ in range(j):
        bits.append("O" if x & 1 else "E")
        x = T(x)
    return "".join(bits), x

def U(x):
    y = 3*x+1
    while y % 2 == 0:
        y //= 2
    return y

def v2(x):
    z = 0
    while x % 2 == 0:
        x //= 2
        z += 1
    return z

class S005GrammarTests(unittest.TestCase):
    def test_exact_O_run_nonovershoot_and_complement(self):
        new = old = equal = 0
        for a in range(2, 257):
            b = b_of(a)
            j = a+b
            m = 1 << b
            D = (1 << j) - 3**a
            t0 = pow(3**a, -1, m)
            self.assertEqual((D*t0+1) % m, 0)
            self.assertGreaterEqual(D*t0, m-1)
            if D*t0 == m-1: equal += 1
            if 4*3**a <= 3*(1 << j): old += 1
            if a >= 3 and 4*3**a > 3*(1 << j) and (3**a)**5 <= (1 << (5*(a+b-1)+4)):
                self.assertGreater(D, m)
                new += 1
            for q in (0, 1, 2):
                t = t0 + q*m
                n = (1 << a)*t-1
                w, x = word(n, j)
                self.assertEqual(w, "O"*a+"E"*b)
                self.assertEqual(x, (3**a*t-1)//m)
                self.assertEqual(n-x, (D*t+1)//m-1)
                if q: self.assertLess(x, n)
        self.assertEqual((old,new,equal), (149,55,0))

    def test_six_class_word_lifting(self):
        rows = (
            (7,7,4,5,"OOOEOEE"),
            (15,7,4,10,"OOOOEEE"),
            (27,59,37,23,"OOEOOOOOEOEOOEOOOEOOOOEOEEOOOEOOEOOOOOOEEOOOOEEEOEOEOEEEOEE"),
            (31,56,35,23,"OOOOOEOEOOEOOOEOOOOEOEEOOOEOOEOOOOOOEEOOOOEEEOEOEOEEEOEE"),
            (39,8,5,38,"OOOEOOEE"),
            (43,5,3,37,"OOEOE"),
        )
        for r,j,a,s,w in rows:
            bits,x = word(r,j)
            self.assertEqual((bits,x,bits.count("O")),(w,s,a))
            self.assertLess(x,r)
            self.assertGreater((1 << j)-3**a,0)
            for q in (0,1,2,7):
                n = r + 3*(1 << j)*q
                bits,z = word(n,j)
                self.assertEqual(bits,w)
                self.assertEqual(z,s+3**(a+1)*q)
                self.assertLess(z,n)
                self.assertEqual(n%48,r)

    def test_composite_factor_state_rank_family(self):
        for q in range(1,2000):
            x = 96*q+15
            y = 144*q+23
            self.assertEqual(U(x),y)
            self.assertEqual((x%48,v2(x+1)),(15,4))
            self.assertEqual((y%48,v2(y+1)),(23,3))
            self.assertEqual(y-x,48*q+8)
            self.assertEqual(x%3,0)

    def test_hostile_controls(self):
        self.assertEqual((U(15),U(U(15))),(23,35))
        self.assertEqual(U(121),91)
        self.assertEqual(U(27),41)
        self.assertTrue(all(U(12*t+3)>12*t+3 for t in range(1,100)))
        z=7
        for _ in range(8): z=T(z)
        self.assertEqual(z,8)
        z=27
        for _ in range(59): z=T(z)
        self.assertEqual(z,23)
        for k in range(3,15):
            n=1+(1<<k)*7
            self.assertLess(T(T(n)),n)

if __name__ == "__main__":
    unittest.main()
