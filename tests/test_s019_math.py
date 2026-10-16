"""S019 independently rerunnable bounded exact unit tests; no global inference."""
import unittest
from itertools import product

def affine(w):
    b=0
    for i,x in enumerate(w):
        if x=="O": b=3*b+(1<<i)
    return 3**w.count("O"),1<<len(w),b

def overcritical(w):
    a=q=1
    for x in w:
        if x=="O":a*=3
        q*=2
        if a<=q:return False
    return True

def canonical(w):
    A,Q,B=affine(w)
    return (-B*pow(A,-1,Q))%Q,B

def execute(w,n):
    v=n
    for x in w:
        assert x==("O" if v&1 else "E")
        v=(3*v+1)//2 if v&1 else v//2
    return v

class S019Exact(unittest.TestCase):
    def test_periodicity_all_short_words(self):
        for l in range(1,9):
            for p in map("".join,product("OE",repeat=l)):
                A,Q,B=affine(p)
                for k in range(1,5):
                    n,_=canonical(p*k)
                    self.assertEqual(((A-Q)*n+B)%(Q**k),0)

    def test_periodic_overcritical_bound(self):
        patterns=cases=0
        for l in range(2,11):
            for p in map("".join,product("OE",repeat=l)):
                if "E" not in p or not overcritical(p):continue
                patterns+=1
                A,Q,B=affine(p);F=A-Q
                for k in range(1,13):
                    n,_=canonical(p*k)
                    self.assertEqual((F*n+B)%(Q**k),0)
                    self.assertGreaterEqual(F*n+B,Q**k)
                    cases+=1
        self.assertEqual((patterns,cases),(143,1716))

    def test_first_crossing_8580_exact_cylinders(self):
        count=certified=0
        for l in range(2,11):
            for p in map("".join,product("OE",repeat=l)):
                if "E" not in p or not overcritical(p):continue
                A,Q,B=affine(p);F=A-Q
                for k in range(1,13):
                    for d in (1,2,3,5,9):
                        m=k*p.count("O")+d
                        j=(3**m).bit_length()
                        b=j-l*k-d
                        self.assertGreaterEqual(b,1)
                        w=p*k+"O"*d+"E"*b
                        n,BW=canonical(w)
                        self.assertGreater(n,0)
                        self.assertEqual((F*n+B)%(Q**k),0)
                        self.assertGreater(((1<<j)-3**m)*n,BW)
                        self.assertLess(execute(w,n),n)
                        if ((1<<j)-3**m)*(Q**k-B)>3**m*max(F,B):
                            certified+=1
                        count+=1
        self.assertEqual((count,certified),(8580,7854))

    def test_multi_lifts(self):
        for p,k,d in (("OOOE",4,1),("OOEOO",3,2),("OOOOE",5,5)):
            m=k*p.count("O")+d;j=(3**m).bit_length()
            w=p*k+"O"*d+"E"*(j-k*len(p)-d)
            n,_=canonical(w)
            for t in (0,1,3,7):
                x=n+t*(1<<j)
                self.assertLess(execute(w,x),x)

    def test_oooe_literal(self):
        p="OOOE"
        self.assertEqual(affine(p),(27,16,19))
        for k,expected in ((1,7),(2,231),(3,17127)):
            m=3*k+1;j=(3**m).bit_length()
            w=p*k+"O"+"E"*(j-4*k-1)
            n,_=canonical(w)
            self.assertEqual(n,expected)
            self.assertEqual((11*n+19)%(16**k),0)

    def test_tower_and_exceptional(self):
        for h in (5,6,16,32):
            u=5 if h&1 else 7
            n=(1<<h)*u-1
            self.assertEqual(n%3,0)
            v=n
            for _ in range(h):
                self.assertTrue(v&1)
                v=(3*v+1)//2
                self.assertGreater(v,n)
        residual=0
        for n in range(11,8192,16):
            v=n;no_drop=True
            for _ in range(13):
                v=(3*v+1)//2 if v&1 else v//2
                if v<n:no_drop=False
            residual+=no_drop
        self.assertEqual(residual,71)

if __name__=="__main__":
    unittest.main()
