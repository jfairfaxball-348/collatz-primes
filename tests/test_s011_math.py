"""S011 exact regression: proofs and universal quantifiers are in research/S011_PROOFS_AND_OBSTRUCTIONS.md."""
import unittest

def T(n):
    return n//2 if n%2==0 else (3*n+1)//2

def lift_word(w):
    r=0
    for j,ch in enumerate(w):
        v=r
        for _ in range(j):
            v=T(v)
        if (v&1)!=(ch=='O'):
            r+=1<<j
    return r

class S011Math(unittest.TestCase):
    def test_infinite_paired_family_finite_witnesses(self):
        for m in (41,188,241,294):
            P=3**m;j=P.bit_length();D=2**j-P;K=3**(m-3)-2**(m-2)
            self.assertTrue(P<100*D<2*P and 0<D<K)
            for a,c in ((3,1),(4,2)):
                d=m-a;b=j-m-c;M=1<<(j-a)
                t0=(-K*pow(P,-1,M))%M
                self.assertTrue(b>=1 and t0>=19)
                self.assertEqual((27*t0+1)%(1<<(m-2)),0)
                self.assertGreater(D*t0,M+K)
                w='O'*a+'E'*c+'O'*d+'E'*b
                self.assertEqual(len(w),j)
                n=(1<<a)*t0-1;v=n;od=0
                for i,ch in enumerate(w,1):
                    self.assertEqual('O' if v&1 else 'E',ch)
                    od+=ch=='O'
                    if i<j:self.assertGreaterEqual(3**od,1<<i)
                    v=T(v)
                self.assertLess(v,n)
                self.assertEqual(n-v,(D*t0-(M+K))//M)
                for target in ((7,39) if a==3 else (15,31)):
                    z=next(z for z in range(15) if ((1<<a)*(t0+M*z)-1)%48==target
                       and (target%3==0 or ((1<<a)*(t0+M*z)-1)%5==0))
                    nn=(1<<a)*(t0+M*(z+15))-1
                    self.assertEqual(nn%48,target)
                    self.assertTrue(nn%3==0 or nn%5==0)
                    vv=nn
                    for ch in w:
                        self.assertEqual('O' if vv&1 else 'E',ch)
                        vv=T(vv)
                    self.assertLess(vv,nn)

    def test_arbitrarily_deep_exceptional_to_first_crossing(self):
        x=27;p=''
        for _ in range(13):
            p+='O' if x&1 else 'E'
            x=T(x)
        self.assertEqual((p,x,p.count('O')),('OOEOOOOOEOEOO',206,10))
        for N in range(1,5):
            w=p*N+'E'*(4*N);J=17*N
            self.assertEqual(len(w),J)
            self.assertLess(3**(10*N),1<<J)
            r=lift_word(w)
            self.assertEqual(r%8192,27)
            odds=0;h=None
            for i,ch in enumerate(w,1):
                odds+=ch=='O'
                if 3**odds<1<<i:
                    h=i;break
            self.assertIsNotNone(h)
            self.assertGreater(h,13*N)
            v=r;at_h=None
            for i,ch in enumerate(w,1):
                self.assertEqual('O' if v&1 else 'E',ch)
                v=T(v)
                if i==h:at_h=v
                if i<=13*N:self.assertGreater(v,r)
                if i%13==0 and i<13*N:self.assertEqual(v%8192,27)
            gap=(1<<J)-(3**odds)*(1<<(J-h))
            self.assertGreater(gap,0)
            qmin=max(1,(at_h-r)//gap+1)
            for target,div in ((27,3),(43,5)):
                z=next(z for z in range(15) if (r+(1<<J)*z)%48==target
                       and (r+(1<<J)*z)%div==0)
                q=z+15*max(1,(qmin-z+14)//15)
                n=r+(1<<J)*q
                self.assertEqual(n%48,target)
                self.assertEqual(n%div,0)
                vv=n
                for i,ch in enumerate(w,1):
                    self.assertEqual('O' if vv&1 else 'E',ch)
                    vv=T(vv)
                    if i<=13*N:self.assertGreater(vv,n)
                    if i==h:self.assertLess(vv,n)
                self.assertLess(vv,n)

    def test_growing_same_valuation_return(self):
        for k in (0,1,3,6):
            n=393243+524288*k;v=n
            for _ in range(11):v=T(v)
            self.assertEqual(v,1259803+1679616*k)
            self.assertGreater(v,n)
            self.assertEqual((n%256,v%256),(27,27))
            self.assertEqual(((n+1)&-(n+1),(v+1)&-(v+1)),(4,4))

    def test_legacy_adversaries(self):
        for n,j,z in ((55,5,47),(15,7,10),(27,59,23),(175,8,167),
                      (39,8,38),(91,45,61),(121,2,91),(681,2,511)):
            v=n
            for _ in range(j):v=T(v)
            self.assertEqual(v,z,(n,j,z,v))

if __name__=='__main__':
    unittest.main()
