"""S010: exceptional transducer / genuine near-resonant two-run tests, exact only."""
import unittest
from collections import Counter

def step(n):
    return (3*n+1)//2 if n&1 else n//2

def run(n,j):
    odd=0; states=[]
    for i in range(1,j+1):
        odd+=n&1
        n=step(n)
        states.append((n,odd))
    return n,odd,states

def exceptional():
    e={}
    for r in range(11,8192,16):
        y,a,p=run(r,13)
        if all(3**od>=2**j for j,(_,od) in enumerate(p,1)):
            e[r]=(y,a)
    return e

def realise(path):
    n=path[0]
    for i,target in enumerate(path[1:],1):
        j=13*i
        y,a,_=run(n,j)
        h=((target-y)*pow(3**a,-1,8192))%8192
        n+=(1<<j)*h
        for k,r in enumerate(path[:i+1]):
            assert run(n,13*k)[0]%8192==r
    return n

class S010Math(unittest.TestCase):
    def test_complete_exceptional_transducer(self):
        e=exceptional()
        self.assertEqual(len(e),71)
        self.assertEqual(Counter(r%256 for r in e),{27:26,91:15,155:15,251:15})
        self.assertEqual(Counter(a for _,a in e.values()),{9:37,10:25,11:8,12:1})
        count=0
        for r,(z,a) in e.items():
            for target in e:
                q=((target-z)*pow(3**a,-1,8192))%8192
                n=r+8192*q
                y,_,p=run(n,13)
                self.assertEqual(y%8192,target)
                self.assertEqual(y,z+3**a*q)
                self.assertTrue(all(v>n for v,_ in p))
                count+=1
        self.assertEqual(count,5041)

    def test_arbitrary_exceptional_paths_and_composites(self):
        e=exceptional()
        paths=[[27,91,155,251,27,91,27,27],
               [27]*5, [91,27,91,27], [155,251,155]]
        for path in paths:
            self.assertTrue(all(r in e for r in path))
            n=realise(path)
            j=13*(len(path)-1)
            self.assertEqual([run(n,13*k)[0]%8192 for k in range(len(path))],path)
            self.assertTrue(all(v>n and 3**a>=2**i
                                for i,(v,a) in enumerate(run(n,j)[2],1)))
            modulus=1<<(13*len(path))
            q=next(t for t in range(3) if (n+modulus*t)%3==0)
            comp=n+modulus*(q+3)
            self.assertEqual(comp%3,0)
            self.assertGreater(comp,3)
            self.assertEqual([run(comp,13*k)[0]%8192 for k in range(len(path))],path)
            self.assertTrue(all(v>comp for v,_ in run(comp,j)[2]))
        self.assertEqual(realise(paths[0]),12124259581827701884828674203675)

    def test_two_run_near_resonant_exact(self):
        for a,c,d,b,M,V in ((3,1,26,16,2**43,18195423120),
                             (4,2,25,15,2**42,36390846240)):
            j=a+c+d+b;P=3**(a+d)
            K=3**d*(2**c-1)-2**(c+d)
            D=2**j-P
            t0=(-K*pow(P,-1,M))%M
            self.assertEqual((j,D,K,t0),(46,1738366812781,2541731610601,92068390381))
            self.assertLess(D,K)
            self.assertEqual((D*t0-K)//M,V)
            for q in (0,1,3):
                t=t0+M*q;n=2**a*t-1
                y,_,prefix=run(n,j)
                self.assertEqual(y,(P*t+K)//M)
                self.assertEqual(n-y,V-1+D*q)
                self.assertEqual("".join("O" if x&1 else "E" for x in self._inputs(n,j)),
                                 "O"*a+"E"*c+"O"*d+"E"*b)
                self.assertTrue(all(3**od>=2**i for i,(_,od) in enumerate(prefix[:-1],1)))
                self.assertLess(3**prefix[-1][1],2**j)
                self.assertLess(y,n)

    @staticmethod
    def _inputs(n,j):
        for _ in range(j):
            yield n
            n=step(n)

    def test_bounded_parameter_falsifier_grid(self):
        valid=0; exceptions=[]
        for a in range(3,141):
            for c in range(1,30):
                if 3**a<=2**(a+c): continue
                for d in range(1,30):
                    P=3**(a+d);K=3**d*(2**c-1)-2**(c+d)
                    j=a+c+d+1
                    while 2**j<=P:j+=1
                    b=j-a-c-d
                    if P<2**(j-1):continue
                    M=2**(c+d+b);D=2**j-P
                    t=(-K*pow(P,-1,M))%M
                    self.assertGreater(t,0)
                    valid+=1
                    if D<=K:
                        exceptions.append((a,c,d,b))
                        self.assertGreaterEqual((D*t-K)//M,1)
        self.assertEqual(valid,96570)
        self.assertEqual(exceptions,[(3,1,26,16),(4,2,25,15)])

    def test_old_controls(self):
        self.assertEqual((run(7,7)[0],run(7,8)[0]),(5,8))
        self.assertEqual((run(15,1)[0],run(15,2)[0]),(23,35))
        self.assertEqual(run(27,59)[0],23)
        self.assertEqual(run(91,45)[0],61)
        self.assertEqual(run(121,2)[0],91)
        self.assertEqual(run(175,8)[0],167)
        self.assertEqual(run(681,2)[0],511)
        self.assertEqual(run(393243,11)[0],1259803)
        for k in (0,1,3):
            self.assertEqual(run(393243+524288*k,11)[0],1259803+1679616*k)
