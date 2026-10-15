"""S006 exact scoped arithmetic tests; neither universal convergence nor Steiner reproof."""
import unittest


def T(n):
    return (3*n+1)//2 if n & 1 else n//2


def U(n):
    z=3*n+1
    while z%2==0:
        z//=2
    return z


def v2(n):
    h=0
    while n%2==0:
        n//=2
        h+=1
    return h


class S006ExactTests(unittest.TestCase):
    def test_full_parity_cylinders(self):
        specs=[
            (11,32,5,"OOEOE",27,23),
            (59,128,7,"OOEOOEE",81,85),
            (123,256,8,"OOEOOEOE",243,319),
        ]
        for r,m,j,w,coeff,intercept in specs:
            for q in range(0,400):
                n=r+m*q
                z=n
                word=""
                for _ in range(j):
                    word += "O" if z&1 else "E"
                    z=T(z)
                self.assertEqual(word,w)
                self.assertEqual(m*z,coeff*n+intercept)
                self.assertLess(z,n)
    def test_11_of_16_in_each_difficult_class(self):
        for r in (27,43):
            found=0
            for m in range(256):
                n=r+48*m
                if n%32==11 or n%128==59 or n%256==123:
                    found+=1
            self.assertEqual(found,176)
    def test_forced_multiplicative_rank_directions(self):
        for H in range(3,100):
            t=7 if H%2==0 else 5
            x=(1<<H)*t-1
            y=U(x)
            self.assertEqual(x%3,0)
            self.assertEqual((v2(x+1),v2(y+1)),(H,H-1))
            self.assertGreater(2*y,3*x)
        for K in range(3,100):
            s=5 if K%2==0 else 25
            y=(1<<K)*s-1
            self.assertEqual((4*y-1)%3,0)
            x=(4*y-1)//3
            self.assertEqual(x%5,0)
            self.assertEqual(U(x),y)
            self.assertEqual((v2(x+1),v2(y+1)),(1,K))
            self.assertGreater(4*y,3*x)
    def test_finite_one_circuit_probe_NOT_proof(self):
        for a in range(2,257):
            b=1
            while 1<<(a+b) <= 3**a:
                b+=1
            d=(1<<(a+b))-3**a
            m=1<<b
            t0=pow(3**a,-1,m)
            self.assertNotEqual(d*t0,m-1)  # finite check only, Steiner is external theorem


if __name__=="__main__":
    unittest.main()
