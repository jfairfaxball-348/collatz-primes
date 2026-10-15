"""S013 finite exact checks. Infinite Matveev argument is NOT a computation."""
import unittest

def T(n):
    return (3*n+1)//2 if n&1 else n//2

def params(a,c,m):
    P=3**m;j=P.bit_length();d=m-a;b=j-m-c
    if not (a>=1 and c>=1 and 3**a>2**(a+c) and d>=1 and b>=1 and P>2**(m+c)):
        raise ValueError('not in the fixed-initial-run first-crossing family')
    M=2**(j-a);D=2**j-P;K=3**d*(2**c-1)-2**(c+d)
    t=(-K*pow(P,-1,M))%M
    return j,d,b,P,M,D,K,t

class S013Math(unittest.TestCase):
    def test_crt_exact_threshold_exhaustive_grid(self):
        checked=near=far=0
        for a in range(2,11):
            for c in range(1,8):
                if 3**a<=2**(a+c):continue
                for m in range(a+1,151):
                    P=3**m;j=P.bit_length();b=j-m-c
                    if b<1 or P<=2**(m+c):continue
                    j,d,b,P,M,D,K,t=params(a,c,m)
                    self.assertTrue(0<t<M)
                    u=pow(3**d,-1,2**b)
                    v=(2**c-1)*pow(2**(c+d),-1,3**a)%(3**a)
                    h=u+2**b*((v-u)*pow(2**b,-1,3**a)%(3**a))
                    self.assertEqual(h,(3**a*t+2**c-1)//2**(c+d))
                    self.assertGreater(D*t,M+K)
                    self.assertEqual((D*t-(M+K))%M,0)
                    if D<K:near+=1
                    else:far+=1
                    checked+=1
        self.assertEqual((checked,near,far),(3854,43,3811))

    def test_shrinking_and_complement_real_prefix(self):
        for a,c,m in ((2,1,17),(2,1,971),(2,1,1636),(3,1,41),
                      (4,2,41),(6,3,253),(7,3,306),(2,1,3),(3,1,5)):
            j,d,b,P,M,D,K,t=params(a,c,m)
            word='O'*a+'E'*c+'O'*d+'E'*b
            self.assertEqual(len(word),j)
            for q in (0,1):
                n=2**a*(t+M*q)-1
                x=n;od=0
                for i,ch in enumerate(word,1):
                    self.assertEqual('O' if x&1 else 'E',ch)
                    od+=ch=='O'
                    if i<j:self.assertGreaterEqual(3**od,2**i)
                    x=T(x)
                self.assertEqual(od,m)
                self.assertLess(3**m,2**j)
                self.assertEqual(x,(P*(t+M*q)+K)//M)
                self.assertEqual(n-x,(D*t-(M+K))//M+D*q)
                self.assertLess(x,n)

    def test_exact_odd_run_integer_potential(self):
        for n in (7,15,27,31,39,43,91,155,251,393243,393243+524288,2**48*13-1):
            self.assertTrue(n&1)
            y=n+1;h=(y&-y).bit_length()-1;u=y//2**h
            x=n
            for i in range(h):
                self.assertTrue(x&1)
                x=T(x)
                self.assertEqual(x,3**(i+1)*2**(h-i-1)*u-1)
                self.assertEqual(((x+1)&-(x+1)).bit_length()-1,h-i-1)
            self.assertFalse(x&1)
            self.assertEqual(x,3**h*u-1)

    def test_exception_witnesses_and_same_val_expansion(self):
        expected=((7,7,5),(15,7,10),(27,59,23),(31,56,23),
                  (39,8,38),(43,5,37),(91,45,61),(155,40,122),(251,27,244))
        for n,j,z in expected:
            x=n
            for i in range(1,j+1):
                x=T(x)
                if i<j:self.assertGreaterEqual(x,n)
            self.assertEqual(x,z)
            self.assertLess(x,n)
        for k in (0,1,3,9):
            n=393243+524288*k;z=1259803+1679616*k
            x=n
            for i in range(11):x=T(x)
            self.assertEqual(x,z)
            self.assertGreater(z,n)
            self.assertEqual(((n+1)&-(n+1),(z+1)&-(z+1)),(4,4))

if __name__=='__main__':unittest.main()
