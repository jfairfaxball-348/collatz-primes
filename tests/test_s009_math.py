"""S009 scoped exact integer regression; no universal Collatz or CST proof."""
import unittest

def T(n):
    return (3*n+1)//2 if n&1 else n//2

def sample(a,c,d):
    P=3**(a+d)
    K=3**d*(2**c-1)-2**(c+d)
    b=1
    while 2**(a+c+d+b)<=P:b+=1
    M=2**(c+d+b)
    D=2**a*M-P
    t0=(-K*pow(P,-1,M))%M
    assert 1<=t0<M
    return b,P,K,M,D,t0,2**a*t0-1

def orbit(n,j):
    bits=[]
    for _ in range(j):
        bits.append("O" if n&1 else "E")
        n=T(n)
    return n,"".join(bits)

class S009Math(unittest.TestCase):
    def test_all_fixed_middle_pairs_in_progressions(self):
        checks=0
        for c in range(1,6):
            for d in range(1,6):
                if (c,d)==(1,1):continue
                K=3**d*(2**c-1)-2**(c+d)
                s=max(3,(K+1).bit_length())
                phi=2**(s-1)
                for a in range(4,160):
                    if (a+d)%phi or 3**a<=2**(a+c):continue
                    b,P,k,M,D,t0,n=sample(a,c,d)
                    self.assertEqual(k,K)
                    self.assertEqual(D%2**s,2**s-1)
                    self.assertGreater(D,K)
                    j=a+c+d+b
                    self.assertTrue(2**(j-1)<=P<2**j)
                    self.assertEqual((D*t0-K)%M,0)
                    self.assertGreaterEqual(D*t0,M+K)
                    for q in (0,1,3):
                        t=t0+M*q;x=2**a*t-1
                        y,w=orbit(x,j)
                        self.assertEqual(w,"O"*a+"E"*c+"O"*d+"E"*b)
                        self.assertEqual(y,(P*t+K)//M)
                        self.assertGreaterEqual(x,y)
                        if q:self.assertGreater(x,y)
                        checks+=1
        self.assertGreater(checks,50)

    def test_unit_offset_all_a_sample(self):
        for c,d in ((2,1),(1,2)):
            for a in range(4,251):
                b,P,K,M,D,t0,n=sample(a,c,d)
                self.assertEqual(K,1)
                self.assertGreater(D,1)
                self.assertGreaterEqual(D*t0,M+1)
                if a<=40:
                    y,w=orbit(n,a+c+d+b)
                    self.assertEqual(w,"O"*a+"E"*c+"O"*d+"E"*b)
                    self.assertLessEqual(y,n)

    def test_expanding_residue_return(self):
        y,w=orbit(27,11)
        self.assertEqual(y,91)
        self.assertEqual(w.count("O"),8)
        for k in (0,1,2,3,7,24):
            n=393243+524288*k
            after=1259803+1679616*k
            self.assertEqual((n%256,after%256),(27,27))
            self.assertEqual(orbit(n,11)[0],after)
            self.assertGreater(after,n)
        for k in (0,3,6):self.assertEqual((393243+524288*k)%3,0)

    def test_old_controls_and_mod3_inverse(self):
        self.assertEqual(orbit(175,8)[0],167)
        self.assertEqual((orbit(7,7)[0],orbit(7,8)[0]),(5,8))
        self.assertEqual(orbit(27,59)[0],23)
        self.assertEqual(orbit(91,45)[0],61)
        self.assertEqual(orbit(121,2)[0],91)
        self.assertEqual(orbit(15,2)[0],35)
        self.assertEqual(orbit(681,2)[0],511)
        for y in range(1,100,2):
            ks=[k for k in range(1,20) if (2**k*y-1)%3==0]
            if y%3==0:self.assertFalse(ks)
            if y%3==1 and y>1:
                self.assertTrue(all((2**k*y-1)//3>y for k in ks))
            if y%3==2 and y>1:self.assertLess((2*y-1)//3,y)
