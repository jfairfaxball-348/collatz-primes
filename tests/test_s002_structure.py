"""S002: standalone exact algebra tests; experiments never imply global Collatz."""
import math
import unittest
from tools.trajectory import step

WORD='OOEOOOOOEOEOOEOOOEOOOOEOEEOOOEOOEOOOOOOEEOOOOEEEOEOEOEEEOEE'

def odd_jump(x):
    y=3*x+1
    a=(y&-y).bit_length()-1
    return y>>a,a

class S002Exact(unittest.TestCase):
    def test_27_infinite_cylinder(self):
        x=27;a=0;b=0
        self.assertEqual(len(WORD),59)
        for j,letter in enumerate(WORD,1):
            self.assertEqual(letter,'O' if x&1 else 'E')
            if x&1:
                a+=1;b=3*b+(1<<(j-1))
            x=step(x)
            self.assertEqual((3**a)*27+b,(1<<j)*x)
            if j<59:
                self.assertGreaterEqual(3**a,1<<j)
                self.assertGreater(x,27)
        self.assertEqual((x,a), (23,37))
        self.assertEqual(3**a,450283905890997363)
        for q in (0,1,2,7,100):
            n=27+(1<<59)*q
            y=n
            for j in range(1,60):
                y=step(y)
                self.assertEqual(y>=n,j<59)
            self.assertEqual(y,23+3**37*q)

    def test_prime_reentry_identity(self):
        for x in range(1,3000,2):
            y,a=odd_jump(x)
            z,b=odd_jump(y)
            self.assertEqual((1<<(a+b))*z,9*x+3+(1<<a))
            self.assertEqual(math.gcd(x,z),math.gcd(x,(1<<a)+3))
            self.assertNotEqual(y%3,0)
        for t in (0,1,2,10,1000):
            x=20*t+15
            y,a=odd_jump(x)
            z,b=odd_jump(y)
            self.assertEqual(a,1)
            self.assertEqual(math.gcd(x,z),5)

    def test_no_fixed_mod2_window_predicts_U_mod3(self):
        for k in range(1,17):
            a=2*((k+4)//2)
            if a<=k or a<=2: a+=2
            b=2*((k+3)//2)+1
            if b<=k or b<=2: b+=2
            x=(2**a-1)//3
            y=(5*2**b-1)//3
            self.assertGreater(x,1);self.assertGreater(y,1)
            self.assertEqual(x%(1<<k),y%(1<<k))
            self.assertEqual(odd_jump(x)[0],1)
            self.assertEqual(odd_jump(y)[0],5)

    def test_exact_child_affine_criterion(self):
        for k in range(3,11):
            for r in range(3,1<<k,2):
                for e in (0,1):
                    s=r+(e<<k)
                    x=s;a=0;b=0
                    for j in range(1,k+2):
                        bit=x&1
                        if bit:
                            a+=1;b=3*b+(1<<(j-1))
                        x=step(x)
                        exact=(1<<j)*x< (1<<j)*s
                        symbolic=((1<<j)-3**a)*s>b
                        self.assertEqual(exact,symbolic)
                        self.assertEqual((3**a)*s+b,(1<<j)*x)

if __name__=='__main__':
    unittest.main()
