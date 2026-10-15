"""S012: fixed-pair near-resonance, complete 71-state graph, adaptive obstructions; exact integers."""
import unittest
from collections import Counter

def step(n):
    return (3*n+1)//2 if n&1 else n//2

def run(n,j):
    a=0;states=[]
    for _ in range(j):
        a+=n&1
        n=step(n)
        states.append((n,a))
    return n,a,states

class S012Math(unittest.TestCase):
    def test_all_fixed_pair_examples_and_minimal_lifts(self):
        samples=((2,1,17),(2,1,58),(3,1,41),(4,2,41),
                 (5,2,200),(6,3,253),(7,3,306))
        for a,c,m in samples:
            P=3**m;j=P.bit_length();d=m-a;b=j-m-c
            assert d>=1 and b>=1
            k_num=2**c-1;k_den=3**a
            self.assertGreater(3**a,2**(a+c))
            D=2**j-P;K=3**d*(2**c-1)-2**(c+d);M=2**(j-a)
            self.assertTrue(0<D<K)
            self.assertGreater(4*D*k_den,P*k_num)
            self.assertLess(2*D*k_den,P*k_num)
            t=(-K*pow(P,-1,M))%M
            self.assertTrue(0<t<M)
            self.assertEqual((3**a*t+(2**c-1))%(2**(c+d)),0)
            self.assertGreater(D*t,M+K)
            word='O'*a+'E'*c+'O'*d+'E'*b
            for q in (0,1,3):
                n=(1<<a)*(t+M*q)-1
                v=n;od=0
                for i,ch in enumerate(word,1):
                    self.assertEqual('O' if v&1 else 'E',ch)
                    od+=ch=='O'
                    if i<j:self.assertGreaterEqual(3**od,2**i)
                    v=step(v)
                self.assertLess(3**od,2**j)
                self.assertEqual(v,(P*(t+M*q)+K)//M)
                self.assertEqual(n-v,(D*t-(M+K))//M+D*q)
                self.assertLess(v,n)
            q=next(z for z in range(3) if ((1<<a)*(t+M*z)-1)%3==0)
            n=(1<<a)*(t+M*(q+3))-1
            self.assertTrue(n>3 and n%3==0)
            self.assertLess(run(n,j)[0],n)

    def test_s011_even_tail_noncoverage_composite_27(self):
        n=27;w=''
        for _ in range(13):
            w+='O' if n&1 else 'E'
            n=step(n)
        self.assertEqual((w,n),('OOEOOOOOEOEOO',206))
        tail=''
        for _ in range(4):
            tail+='O' if n&1 else 'E'
            n=step(n)
        self.assertEqual(tail,'EOOO')
        self.assertEqual(run(27,13)[0]&1,0)

    def test_complete_71_5041_against_adaptive_candidates(self):
        e={}
        for r in range(11,8192,16):
            y,a,states=run(r,13)
            if all(3**od>=2**i for i,(_,od) in enumerate(states,1)):
                e[r]=(y,a)
        self.assertEqual(len(e),71)
        self.assertEqual(Counter(r%256 for r in e),{27:26,91:15,155:15,251:15})
        count=0
        for r,(y,a) in e.items():
            for target in e:
                q=((target-y)*pow(3**a,-1,8192))%8192
                n=r+8192*q
                z,_,states=run(n,13)
                self.assertEqual(z,y+3**a*q)
                self.assertEqual(z%8192,target)
                self.assertTrue(all(v>n for v,_ in states))
                count+=1
        self.assertEqual(count,5041)
        for k in (0,1,3,9):
            n=393243+524288*k;z=1259803+1679616*k
            self.assertEqual(run(n,11)[0],z)
            self.assertGreater(z,n)
            self.assertEqual((n%256,z%256),(27,27))
            self.assertEqual(((n+1)&-(n+1),(z+1)&-(z+1)),(4,4))
        for H in (6,12,24,48):
            u=next(u for u in range(3,30,2) if (2**H*u-1)%5==0)
            n=2**H*u-1;v=n
            self.assertTrue(n>5 and n%5==0)
            self.assertLessEqual(n.bit_length(),H+5)
            for i in range(1,H+1):
                self.assertTrue(v&1)
                v=step(v)
                self.assertEqual(v,3**i*2**(H-i)*u-1)
                self.assertGreater(v,n)

    def test_legacy_witness_trajectories_and_later_crossing(self):
        for n,j,z in ((55,5,47),(15,7,10),(27,59,23),(175,8,167),
                      (39,8,38),(91,45,61),(121,2,91),(681,2,511)):
            self.assertEqual(run(n,j)[0],z)
        self.assertEqual((run(7,7)[0],run(7,8)[0]),(5,8))

if __name__=='__main__':
    unittest.main()
