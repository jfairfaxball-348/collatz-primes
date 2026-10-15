"""S007 regression: exact finite certificates; not a proof of universal Collatz."""
import unittest

def T(n):
    return (3*n+1)//2 if n&1 else n//2

def tr(n,j):
    z=n; w=""; a=0
    for _ in range(j):
        o=z&1
        w+="O" if o else "E"
        a+=o
        z=T(z)
    return z,w,a

GROUPS={
    8: [219],
    10: [347,923,507],
    12: [2587,3675,2907,2203,1435,1787,1019],
    13: [2075,539,1563,2331,7259,6747,5723,4955,5979,4251,5275,5787,4507,3483,5371,4859,3835,3067,4091]
}
ROWS=[(r,j) for j,rs in GROUPS.items() for r in rs]
OLD=[(11,5),(59,7),(123,8)]

class S007MathTests(unittest.TestCase):
    def test_new_full_residue_cylinders(self):
        self.assertEqual(len(ROWS),30)
        self.assertEqual(sum(2**(13-j) for r,j in ROWS),89)
        for i,(r,j) in enumerate(ROWS):
            z,w,a=tr(r,j)
            self.assertLess(z,r)
            self.assertLess(3**a,2**j)
            self.assertIn(r%256,(27,91,155,219,251))
            for r2,j2 in ROWS[i+1:]:
                self.assertNotEqual(r%(2**min(j,j2)),r2%(2**min(j,j2)))
            for q in (0,1,2,11):
                out,word,odd=tr(r+(2**j)*q,j)
                self.assertEqual((out,word,odd),(z+3**a*q,w,a))
                self.assertLess(out,r+(2**j)*q)

    def test_exact_441_of_512_each_mod48_class(self):
        for residue in (27,43):
            old=new=0
            for m in range(512):
                n=residue+48*m
                oldhit=any(n%(2**j)==r for r,j in OLD)
                newhit=any(n%(2**j)==r for r,j in ROWS)
                self.assertFalse(oldhit and newhit)
                old+=oldhit
                new+=newhit
            self.assertEqual((old,new,old+new),(352,89,441))

    def test_infinite_parameter_band_finite_samples(self):
        good=set()
        for a in range(3,201):
            b=1
            while 2**(a+b+2)<=3**(a+1):
                b+=1
            X=2**(a+b+2); P=3**(a+1)
            if 4*X>=5*P:
                good.add(a)
                M=2**(b+2); t0=pow(P,-1,M)
                self.assertGreater(X-P,M-1)
                for q in (0,1,2):
                    t=t0+M*q
                    n=2**a*t-1
                    z,w,_=tr(n,a+b+2)
                    self.assertEqual(w,"O"*a+"EO"+"E"*b)
                    self.assertEqual(z,(P*t-1)//M)
                    self.assertLess(z,n)
        self.assertTrue(all(a in good or a+1 in good for a in range(3,200)))

    def test_arbitrarily_long_composite_prefix_finite_samples(self):
        r=27
        for H in range(8,97):
            z,w,a=tr(r,H)
            self.assertEqual(w,"OOEOOOOO"+"O"*(H-8))
            self.assertEqual(r%256,27)
            odd=0
            for j,letter in enumerate(w,1):
                odd+=(letter=="O")
                self.assertGreater(3**odd,2**j)
            for residue in (27,43):
                n=next(r+(2**H)*k for k in range(3) if (r+(2**H)*k)%3==residue%3)
                if residue==43:
                    mod=3*2**H
                    n+=mod*((-n*pow(mod,-1,7))%7+7)
                    self.assertEqual(n%7,0)
                self.assertEqual(n%48,residue)
                self.assertEqual(n%256,27)
                self.assertGreater(n,7)
                self.assertTrue(all(tr(n,j)[0]>n for j in range(1,H+1)))
            if H<96 and z%2==0:
                r+=2**H

    def test_adversarial_historical_controls(self):
        cases=[(7,7,5),(27,59,23),(91,45,61)]
        for n,j,result in cases:
            self.assertEqual(tr(n,j)[0],result)
            self.assertTrue(all(tr(n,i)[0]>=n for i in range(1,j)))
        self.assertEqual(tr(7,8)[0],8)
        self.assertEqual((121*3+1)//4,91)
        self.assertEqual((15*3+1)//2,23)
        self.assertEqual((23*3+1)//2,35)
        self.assertEqual((681*3+1)//4,511)

if __name__=="__main__":
    unittest.main()
