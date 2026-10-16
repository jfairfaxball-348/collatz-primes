"""S024 finite checks of exact periodic nonadmission and sharpness.
Not a Collatz theorem; unbounded statements are proved algebraically in S024 manuscript.
"""
import unittest
from fractions import Fraction

GRAMMAR = ("OOOE", "OOOOE", "OOOOOE", "OOOEOOE", "OOOOEOOE", "OOEOOOOE")

def shortened(x):
    return (3*x+1)//2 if x & 1 else x//2

def trace(n, length):
    bits=[]
    for _ in range(length):
        bits.append('O' if n&1 else 'E')
        n=shortened(n)
    return ''.join(bits),n

def approx_root(k):
    assert k >= 1
    q=16**k
    return (5*pow(7,-1,q))%q

def affine(word):
    a,q,b=1,1,0
    for bit in word:
        if bit=='O':a,b=3*a,3*b+q
        q*=2
    return a,q,b

def ratio(word):
    a,q,b=affine(word)
    return Fraction(b+q,a)

class S024Math(unittest.TestCase):
    def test_exact_ooee_2adic_approximations(self):
        for k in range(1,13):
            q=16**k
            r=approx_root(k)
            self.assertEqual((7*r-5)%q,0)
            self.assertEqual(r%16,3)
            self.assertEqual(approx_root(k+1)%q,r)
            bits,x=trace(r+3*q,4*k)
            self.assertEqual(bits,'OOEE'*k)
            self.assertEqual(x,(9**k*(r+3*q)+5*((16**k-9**k)//7))//q)
            self.assertEqual((7*x-5)*q,9**k*(7*(r+3*q)-5))

    def test_composite_crt_lifts_and_no_grammar(self):
        for k in range(1,13):
            q=16**k; r=approx_root(k)
            starts=[r+t*q for t in range(0,7) if r+t*q>3 and (r+t*q)%3==0]
            self.assertTrue(starts)
            for n in starts:
                self.assertGreater(n,3)
                self.assertEqual(n%3,0)
                bits,_=trace(n,4*k)
                self.assertEqual(bits,'OOEE'*k)
                for i in range(4*k):
                    self.assertFalse(any(bits[i:].startswith(atom) for atom in GRAMMAR))

    def test_reversed_two_three_exact_threshold(self):
        w='OOEOOOE'
        self.assertEqual(affine(w),(243,128,287))
        c=Fraction(287,115)
        self.assertGreater(c,Fraction(7,3))
        for k in range(1,14):
            h=ratio(w*k)
            self.assertEqual(h,c+(1-c)*Fraction(128,243)**k)
            self.assertEqual(h>=Fraction(7,3),k>=4)
            self.assertLess(h,c)
        self.assertLess(ratio(w*3),Fraction(7,3))
        self.assertGreater(ratio(w*4),Fraction(7,3))

    def test_all_six_hard_classes_arbitrary_overcritical_prefix(self):
        for H in range(10,65,3):
            for residue in (7,15,27,31,39,43):
                if residue % 16 == 7:
                    word = 'OOOE' + 'O'*(H-4)
                elif residue % 16 == 15:
                    word = 'OOOOE' + 'O'*(H-5)
                else:
                    word = 'OOE' + 'O'*(H-3)
                # Classical parity-bit lifting: canonical representative of the H-cylinder.
                n,a,q,b=0,1,1,0
                for c in word:
                    bit=((a*n+b)//q)&1
                    n+=((int(c=='O')-bit)%2)*q
                    if c=='O':a,b=3*a,3*b+q
                    q*=2
                    self.assertEqual((a*n+b)%q,0)
                # CRT modulo 3, 5 and 2^H gives a composite lift in the r mod48 class.
                n=next(n+t*q for t in range(15,45)
                       if (n+t*q)%48==residue and (n+t*q)%5==0)
                self.assertGreater(n,5)
                self.assertEqual(n%48,residue)
                self.assertEqual(n%5,0)
                x=n
                for ch in word:
                    self.assertGreaterEqual(x,n)
                    self.assertEqual(x&1,int(ch=='O'))
                    x=shortened(x)
                    self.assertGreater(x,n)
                self.assertEqual(trace(n,H)[0],word)

    def test_old_exception_and_controls(self):
        residual=[]
        for n in range(11,8192,16):
            x=n
            for _ in range(13):
                x=shortened(x)
                if x<n:break
            else:residual.append(n)
        self.assertEqual(len(residual),71)
        self.assertEqual(len(residual)**2,5041)
        for k in range(120):
            self.assertEqual(trace(64*k+59,3)[1],72*k+67)
        for h in range(1,13):
            for u in (1,3,5):
                n=2**h*u-1
                for j in range(h+1):
                    self.assertEqual(n,3**j*2**(h-j)*u-1)
                    if j<h:n=shortened(n)
        for n in (27,43,91,155,251,393243,393243+524288):
            bits,end=trace(n,30)
            self.assertEqual(len(bits),30)
            self.assertGreater(end,0)
        for residue in (7,15,27,31,39,43):
            candidates=[n for n in range(residue,20000,48)
                        if n>3 and any(n%d==0 for d in range(2,int(n**0.5)+1))]
            self.assertTrue(candidates)
            n=candidates[0]; bits,_=trace(n,32)
            self.assertEqual(n%48,residue)
            self.assertEqual(len(bits),32)

if __name__=='__main__':unittest.main()
