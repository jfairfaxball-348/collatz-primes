"""S015 finite arithmetic tests. All-parameter Matveev implications are NOT proved by tests."""
import math
import unittest

C = 10**10

def T(n): return (3*n+1)//2 if n&1 else n//2

def affine(w):
    r=B=0
    for i,c in enumerate(w):
        if c=='O': r+=1; B=3*B+(1<<i)
        else: assert c=='E'
    return r,B

def first_cross(w):
    r=0
    for j,c in enumerate(w,1):
        r+=(c=='O')
        if 3**r<1<<j: return j
    return None

def family(U,d):
    r,B=affine(U); ell=len(U); m=r+d; j=(3**m).bit_length(); b=j-ell-d
    assert b>=1
    w=U+'O'*d+'E'*b
    R,Q=affine(w)
    assert R==m
    mod=1<<j
    n=(-Q*pow(3**m,-1,mod))%mod or mod
    x=n
    for c in w:
        assert ('O' if x&1 else 'E')==c,(c,x,n)
        x=T(x)
    assert (1<<j)*x==3**m*n+Q
    return (j,b,n,x,n-x,first_cross(w))

class S015Math(unittest.TestCase):
    def test_primary_matveev_constants(self):
        self.assertLess(2**32*math.log(2)*math.log(3), C)
        self.assertTrue(math.log(2)-math.log(3)/2>1/8)
        for d in (int((64*(C+10))**2), int((64*(C+10))**2)+7):
            s=math.isqrt(d)
            self.assertGreater(s,64*C)
            self.assertGreater(s*s/8,C*(1+s)+math.log(8))
    def test_affine_bound_all_overcritical_short_words(self):
        for ell in range(1,13):
            for mask in range(1<<ell):
                U=''.join('O' if mask>>i&1 else 'E' for i in range(ell))
                if first_cross(U) is not None: continue
                r,B=affine(U)
                if r==0: continue
                self.assertLessEqual(4*B,(1<<ell)*(3**r-1))
    def test_growing_multiblock_prefixes_and_positive_lifts(self):
        for k in range(1,25):
            U='OOOE'*k; d=6*k
            self.assertIsNone(first_cross(U))
            r,B=affine(U)
            self.assertEqual(r,d//2)
            j,b,n,x,drop,fc=family(U,d)
            self.assertEqual(fc,j)
            self.assertGreater(drop,0)
            for q in (1,3):
                m=n+q*(1<<j)
                self.assertLess(T_word(m,U+'O'*d+'E'*b),m)
    def test_bad_prefix_and_noncoverage(self):
        self.assertEqual(first_cross('OE'),2)
        p='OOEOOOOOEOEOO'
        self.assertIsNone(first_cross(p))
        x=27
        for c in p:
            self.assertEqual('O' if x&1 else 'E',c)
            x=T(x)
        self.assertEqual(x,206)
        self.assertEqual(x%2,0)
    def test_full_71_5041_and_hostile_integer_controls(self):
        exceptional=[]
        for z in range(11,1<<13,16):
            x=z; odd=0; bad=False
            for j in range(1,14):
                if x&1: odd+=1
                x=T(x)
                if 3**odd < 1<<j:bad=True;break
            if not bad: exceptional.append(z)
        self.assertEqual(len(exceptional),71)
        for z in exceptional:
            x=z
            for _ in range(13):x=T(x)
            o=0;y=z
            for _ in range(13):
                o+=y&1;y=T(y)
            self.assertEqual(x,y)
            P=3**o
            self.assertEqual(math.gcd(P,8192),1)
            seen={(x+P*q)%8192 for q in range(8192)}
            self.assertEqual(len(seen.intersection(exceptional)),71)
        controls={7:(7,5),15:(7,10),27:(59,23),31:(56,23),39:(8,38),43:(5,37),91:(45,61),155:(40,122),251:(27,244),393243:(37,269366),917531:(26,588548)}
        for n,(j,expected) in controls.items():
            x=n
            for i in range(1,j+1):
                x=T(x)
                if i<j:self.assertGreaterEqual(x,n)
            self.assertEqual(x,expected)
        for k in (0,1,3,9):
            n=393243+524288*k
            self.assertEqual(T_power(n,11),1259803+1679616*k)
        for H in (6,12,24,48,96):
            u=next(v for v in range(3,30,2) if ((1<<H)*v-1)%5==0)
            n=(1<<H)*u-1
            for _ in range(H):
                self.assertTrue(n&1)
                self.assertGreater(T(n),n)
                n=T(n)

def T_word(n,w):
    x=n
    for c in w:
        assert ('O' if x&1 else 'E')==c
        x=T(x)
    return x

def T_power(n,j):
    for _ in range(j):n=T(n)
    return n

if __name__=='__main__':unittest.main()
