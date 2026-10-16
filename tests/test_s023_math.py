"""S023 exact finite hostile checks: NOT a universal theorem."""
import itertools
import unittest
from fractions import Fraction

ATOM = ["OOOE","OOOOE","OOOOOE","OOOEOOE","OOOOEOOE","OOEOOOOE"]

def affine(w):
    a,q,b=1,1,0
    for c in w:
        if c=="O": a,b=3*a,3*b+q
        q*=2
    return a,q,b

def canonical(w):
    n,a,q,b=0,1,1,0
    for c in w:
        bit=((a*n+b)//q)&1
        n+=((int(c=="O")-bit)%2)*q
        if c=="O": a,b=3*a,3*b+q
        q*=2
        assert (a*n+b)%q==0
    return n or q

def orbit(n,w):
    x=n
    for c in w:
        assert (x&1)==int(c=="O"),(n,c,x)
        x=(3*x+1)//2 if x&1 else x//2
    return x

class S023Math(unittest.TestCase):
    def test_macro_arithmetic_and_sharpness(self):
        self.assertEqual(affine("OOOEOOE"),(243,128,251))
        self.assertEqual(affine("OOOOEOOE"),(729,256,745))
        self.assertEqual(affine("OOEOOOOE"),(729,256,925))
        self.assertEqual(affine("OOEOOOE"),(243,128,287))
        self.assertEqual(Fraction(251,115),Fraction(251,243-128))
        self.assertLess(Fraction(251,115),Fraction(7,3))
        self.assertGreater(Fraction(287,115),Fraction(7,3))
        for v in ATOM:
            a,q,b=affine(v)
            self.assertLessEqual(115*b+251*q,251*a)

    def test_mixed_words_first_crossing_actual_lifts(self):
        count={1:0,2:0}; margins=[]
        for length in range(1,6):
            for parts in itertools.product(ATOM,repeat=length):
                u="".join(parts)
                a,q,b=affine(u)
                self.assertLessEqual(115*b+251*q,251*a)
                for t in range(1,len(u)+1):
                    aa,qq,_=affine(u[:t])
                    self.assertGreater(aa,qq)
                for d in (1,2):
                    m=u.count("O")+d
                    j=(3**m).bit_length()
                    if 3*(2**j-3**m)>3**m:break
                else:self.fail("gap")
                tail=j-len(u)-d
                self.assertGreaterEqual(tail,1)
                w=u+"O"*d+"E"*tail
                aw,qw,bw=affine(w)
                self.assertEqual((aw,qw),(3**m,2**j))
                for t in range(1,j):
                    aa,qq,_=affine(w[:t])
                    self.assertGreater(aa,qq)
                n0=canonical(w)
                self.assertGreaterEqual(n0,7)
                margin=(qw-aw)*n0-bw
                self.assertGreater(margin,0)
                margins.append(margin)
                for v in (0,1,3):
                    n=n0+v*qw
                    self.assertLess(orbit(n,w),n)
                count[d]+=1
        self.assertEqual(count,{1:5337,2:3993})
        self.assertEqual(len(margins),9330)
        self.assertEqual(min(margins),256)

    def test_composite_initial_nonadmission(self):
        for k in range(1,501):
            n=3+48*k
            self.assertEqual(n%3,0)
            x=n; bits=""
            for _ in range(4):
                bits+="O" if x&1 else "E"
                x=(3*x+1)//2 if x&1 else x//2
            self.assertEqual(bits,"OOEE")
            self.assertFalse(any(w.startswith(bits) for w in ATOM))

    def test_four_bank_density_threshold(self):
        p,q=Fraction(16,27),Fraction(8,9)
        self.assertEqual(Fraction(19,11)+Fraction(36,11)*p**4,Fraction(125825,59049))
        self.assertLess(Fraction(125825,59049),Fraction(7,3))
        self.assertEqual(Fraction(19,11)+Fraction(36,11)*p**3,Fraction(5267,2187))
        self.assertGreaterEqual(Fraction(19,11)+Fraction(36,11)*p**3-4*p**3*q**21,Fraction(7,3))

    def test_residual_and_expanding_controls(self):
        residual=[]
        for n in range(11,8192,16):
            x=n
            for _ in range(13):
                x=(3*x+1)//2 if x&1 else x//2
                if x<n:break
            else:residual.append(n)
        self.assertEqual(len(residual),71)
        self.assertEqual(len(residual)**2,5041)
        for k in range(100):
            x=64*k+59
            for _ in range(3):x=(3*x+1)//2 if x&1 else x//2
            self.assertEqual(x,72*k+67)
        for h in range(1,13):
            for v in (1,3,5):
                x=2**h*v-1
                for j in range(h+1):
                    self.assertEqual(x,3**j*2**(h-j)*v-1)
                    if j<h:x=(3*x+1)//2

if __name__=="__main__":unittest.main()
