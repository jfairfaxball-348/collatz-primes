"""S014 exact FINITE checks. CP-0053/54 require a published Matveev bound,
which is NOT established by these tests. Full Collatz and Terras CST OPEN."""
import math
import unittest

C0=10**12
def T(n):
    return (3*n+1)//2 if n&1 else n//2

def affine(word):
    a=b=0
    for j,ch in enumerate(word):
        if ch=='O':
            b=3*b+2**j
            a+=1
        else:
            assert ch=='E'
    return a,b

def first_cross(word):
    a=0
    for j,ch in enumerate(word,1):
        a+=(ch=='O')
        if 3**a<2**j:return j
    return None

def minimum(word):
    a,b=affine(word)
    modulus=2**len(word)
    n=(-b*pow(3**a,-1,modulus))%modulus
    return n or modulus

def verify(word,n):
    x=n
    for ch in word:
        assert ('O' if x&1 else 'E')==ch,(ch,x,n)
        x=T(x)
    a,b=affine(word)
    assert 2**len(word)*x==3**a*n+b
    return x

def word_for(U,d):
    r,_=affine(U);m=r+d;j=(3**m).bit_length()
    b=j-len(U)-d
    return U+'O'*d+'E'*b,b

class S014Math(unittest.TestCase):
    def test_many_three_plus_block_prefixes(self):
        checked=0
        for U in ('OOOE','OOOOEOO','OOOEOOEOOE','OOOOEOOOEOOEOOE'):
            self.assertIsNone(first_cross(U))
            for d in range(6,101):
                W,b=word_for(U,d)
                self.assertGreaterEqual(b,1)
                self.assertEqual(first_cross(W),len(W))
                n=minimum(W)
                self.assertLess(verify(W,n),n)
                checked+=1
        self.assertEqual(checked,380)

    def test_multiblock_positive_lifts_and_examples(self):
        U='OOOEOOEOOE'
        self.assertEqual((len(U),*affine(U)),(10,7,2899))
        for d in (12,19,40,73,101,200):
            W,b=word_for(U,d)
            self.assertGreaterEqual(b,1)
            self.assertEqual(first_cross(W),len(W))
            n=minimum(W)
            for q in (0,1):
                v=n+q*2**len(W)
                self.assertLess(verify(W,v),v)
            if d==12:
                self.assertEqual((len(W),b,n,verify(W,n)),(31,9,1633475239,884069749))
            if d==19:
                self.assertEqual((len(W),b,n,verify(W,n)),(42,13,2267417467559,1310461579885))

    def test_failed_unguarded_prefix(self):
        self.assertEqual(first_cross('OE'),2)
        W,b=word_for('OE',40)
        self.assertGreater(b,0)
        self.assertEqual(first_cross(W),2)

    def test_effective_matveev_integer_margin(self):
        for a,c in ((2,1),(3,1),(5,2),(20,1),(100,30),(300,100)):
            self.assertGreater(3**a,2**(a+c))
            m0=(4*(C0+a+c+10))**2
            S=math.isqrt(m0)
            self.assertEqual(S*S,m0)
            self.assertGreater(S*S,5*a+2*C0*(1+S)+2)
            self.assertGreater(m0,4*(a+c+1))

    def test_adversarial_integer_controls(self):
        controls={7:(7,5),15:(7,10),27:(59,23),31:(56,23),
                  39:(8,38),43:(5,37),91:(45,61),155:(40,122),
                  251:(27,244),393243:(37,269366),917531:(26,588548)}
        for n,(j,z) in controls.items():
            x=n
            for i in range(1,j+1):
                x=T(x)
                if i<j:self.assertGreaterEqual(x,n)
            self.assertEqual(x,z)
        for k in (0,1,3,9):
            n=393243+524288*k
            x=n
            for _ in range(11):x=T(x)
            self.assertEqual(x,1259803+1679616*k)
            self.assertGreater(x,n)
            self.assertEqual(((n+1)&-(n+1),(x+1)&-(x+1)),(4,4))
        for H in (6,12,24,48):
            u=next(u for u in range(3,30,2) if (2**H*u-1)%5==0)
            n=2**H*u-1
            for _ in range(H):
                self.assertTrue(n&1)
                n=T(n)

if __name__=='__main__':
    unittest.main()
