"""S016 exact integer sanity tests; tests alone prove no infinite or Collatz claim."""
import unittest

def T(n): return (3*n+1)//2 if n&1 else n//2
def affine(w):
    r=B=0
    for i,c in enumerate(w):
        if c=="O":r+=1; B=3*B+(1<<i)
        else:assert c=="E"
    return r,B
def over(w):
    r=0
    for j,c in enumerate(w,1):
        r+=(c=="O")
        if 3**r <= 1<<j:return False
    return bool(w)
def cyl(U,d):
    ell=len(U);r,B=affine(U);m=r+d;j=(3**m).bit_length();b=j-ell-d
    assert b>=1
    w=U+"O"*d+"E"*b
    _,Q=affine(w);mod=1<<j
    n=(-Q*pow(3**m,-1,mod))%mod or mod
    x=n
    for c in w:
        assert c==("O" if x&1 else "E")
        x=T(x)
    assert mod*x==3**m*n+Q
    return j,b,n,x,w
class S016Math(unittest.TestCase):
    def test_sharp_all_words(self):
        for ell in range(1,13):
            for mask in range(1<<ell):
                w="".join("O" if mask>>i&1 else "E" for i in range(ell))
                r,B=affine(w)
                if not r:continue
                lo=3**r-2**r;hi=(1<<(ell-r))*lo
                self.assertTrue(lo<=B<=hi)
                self.assertLessEqual((1<<r)*((1<<ell)+B),(1<<ell)*3**r)
            for r in range(1,ell+1):
                self.assertEqual(affine("O"*r+"E"*(ell-r))[1],3**r-2**r)
                self.assertEqual(affine("E"*(ell-r)+"O"*r)[1],(1<<(ell-r))*(3**r-2**r))
    def test_expanded_growing_lifts(self):
        for k in range(1,32):
            U="OOOE"*k
            self.assertTrue(over(U))
            for d in (2*k,3*k,6*k):
                j,b,n,x,w=cyl(U,d)
                self.assertLess(x,n)
                odd=0
                for i,c in enumerate(w,1):
                    odd+=(c=="O")
                    if i<j:self.assertGreater(3**odd,1<<i)
                self.assertLess(3**odd,1<<j)
                for q in (1,2,7):
                    z=n+q*(1<<j);v=z
                    for c in w:
                        self.assertEqual(c,"O" if v&1 else "E")
                        v=T(v)
                    self.assertLess(v,z)
    def test_expanding_same_valuation_one_renewal(self):
        for k in (0,1,4,7,13,30,100):
            n=64*k+59;v=T(T(T(n)))
            self.assertEqual(v,72*k+67)
            self.assertEqual((n+1)&-(n+1),4)
            self.assertEqual((v+1)&-(v+1),4)
            self.assertGreater(v,n)
        for k in (1,4,7,10):self.assertEqual((64*k+59)%3,0)
    def test_exceptional_graph_witnesses(self):
        ex=[]
        for n in range(11,1<<13,16):
            x=n;odds=0;cross=False
            for i in range(1,14):
                odds+=x&1;x=T(x)
                if 3**odds<(1<<i):cross=True;break
            if not cross:ex.append((n,x,3**odds))
        self.assertEqual(len(ex),71)
        for n,x,P in ex:
            self.assertEqual(len({(x+P*q)%8192 for q in range(8192)}),8192)
        self.assertEqual(len(ex)**2,5041)
        for n,j,answer in ((7,7,5),(15,7,10),(27,59,23),(31,56,23),
                           (39,8,38),(43,5,37),(91,45,61),(155,40,122),(251,27,244)):
            x=n
            for i in range(1,j+1):
                x=T(x)
                if i<j:self.assertGreaterEqual(x,n)
            self.assertEqual(x,answer)
        for k in (0,1,3,9):
            x=393243+524288*k
            for _ in range(11):x=T(x)
            self.assertEqual(x,1259803+1679616*k)
        for H in (6,12,24,48,96):
            u=next(v for v in range(3,30,2) if ((1<<H)*v-1)%5==0)
            n=(1<<H)*u-1
            for _ in range(H):
                self.assertEqual(n&1,1)
                nxt=T(n);self.assertGreater(nxt,n);n=nxt
    def test_reverse_and_ratio_boundary(self):
        for y in range(1,300):
            x=(2*y-1)//3
            self.assertEqual(y%3==2, y%3==2 and x>0 and x&1==1 and T(x)==y)
        for d in range(1,40):
            self.assertGreater(9**d,8**d)
            self.assertLess(cyl("O"*(2*d),d)[3],cyl("O"*(2*d),d)[2])
if __name__=="__main__":unittest.main()
