"""S004 exact finite hostile tests; no claim of universal Collatz proof."""
from math import gcd
import unittest


def T(n):
    return (3*n+1)//2 if n & 1 else n//2


def v2(n):
    return (n & -n).bit_length()-1


def first_b(a):
    b=0
    while (1 << (a+b)) <= 3**a:
        b+=1
    return b


class TestS004(unittest.TestCase):
    def test_first_crossing_certified_family_and_adjacent_pair(self):
        count=0
        for a in range(2,130):
            b=first_b(a)
            qualifies=4*3**a <= 3*(1<<(a+b))
            if not qualifies:
                next_a=a+1
                next_b=first_b(next_a)
                self.assertLessEqual(4*3**next_a,3*(1<<(next_a+next_b)))
                continue
            count+=1
            t0=pow(3**a,-1,1<<b)
            for q in (0,1,3):
                t=t0+q*(1<<b)
                n=(1<<a)*t-1
                self.assertGreater(n,1)
                x=n; mult=1; den=1
                for j in range(1,a+b+1):
                    self.assertEqual(x&1,1 if j<=a else 0)
                    if x&1:
                        mult*=3
                    x=T(x)
                    den*=2
                    if j<a+b:
                        self.assertGreaterEqual(mult,den)
                self.assertLess(mult,den)
                self.assertLess(x,n)
                self.assertEqual((n-x)*(1<<b),
                    ((1<<(a+b))-3**a)*t-((1<<b)-1))
        self.assertEqual(count,75)

    def test_composite_mixed_mod48_no_horizon(self):
        for H in (4,5,8,12,20):
            for r in (15,31):
                j=0
                while True:
                    n0=r+48*j
                    if n0>1 and n0%(1<<(H+1)) == (1<<H)-1:
                        break
                    j+=1
                L=48*(1<<(H+1))//gcd(48,1<<(H+1))
                for q in (1,2):
                    n=n0*(1+q*L)
                    self.assertEqual(n%48,r)
                    self.assertEqual(v2(n+1),H)
                    self.assertGreater(n,n0)
                    x=n
                    for step in range(1,H+2):
                        x=T(x)
                        self.assertGreater(x,n,(H,r,q,step))

    def test_unbounded_valuation_jump_composite(self):
        for K in range(3,30):
            y=(1<<K)-1
            while y%9 != 7:
                y+=1<<K
            x=(4*y-1)//3
            self.assertGreater(x,3)
            self.assertEqual(x%3,0)
            self.assertEqual(v2(x+1),1)
            self.assertGreaterEqual(v2(y+1),K)
            self.assertEqual(3*x+1,4*y)
            self.assertEqual(T(T(x)),y)
            self.assertLess(y,x)
        self.assertEqual((3*681+1)//4,511)
        self.assertEqual((v2(681+1),v2(511+1)),(1,9))

    def test_m_step_offsets_and_fixed_m_all_o(self):
        from math import gcd
        for n in (15,35,121,27,3,51,243,231,681,(1<<20)*7-1):
            x=n;F=0;A=0
            for m in range(1,9):
                v=3*x+1
                ai=v2(v)
                y=v>>ai
                F=3*F+(1<<A)
                A+=ai
                self.assertEqual((1<<A)*y,3**m*n+F)
                self.assertEqual(gcd(n,y),gcd(n,F))
                x=y
        for H in (4,8,12):
            t=7
            n=(1<<H)*t-1
            x=n
            for m in range(1,H):
                v=3*x+1
                self.assertEqual(v2(v),1)
                x=v//2
                self.assertEqual(x,3**m*(1<<(H-m))*t-1)
                self.assertGreater(x,n)

    def test_prior_hostile_controls(self):
        self.assertEqual([T(x) for x in (3,4)], [5,2])
        self.assertEqual([T(T(x)) for x in (1,5)], [1,4])
        self.assertEqual((3*7+1)//2,11)
        for k in range(2,16):
            n=1+(1<<k)*3
            self.assertLess(T(T(n)),n)


if __name__ == '__main__':
    unittest.main()
