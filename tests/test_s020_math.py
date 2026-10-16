"""Finite exact S020 variable-block theorem checks. Not a universal proof."""
import itertools
import unittest

BLOCKS = ('OOOE', 'OOOOE')

def affine(word):
    a,q,b=1,1,0
    for letter in word:
        if letter=='O':
            b=3*b+q
            a*=3
        else:
            assert letter=='E'
        q*=2
    return a,q,b

def canonical(word):
    a,q,b=affine(word)
    x=(-b*pow(a,-1,q))%q
    return x if x else q

def execute(word,n):
    x=n
    for t,letter in enumerate(word):
        assert ('O' if x&1 else 'E')==letter,(n,word,t,x)
        x=(3*x+1)//2 if x&1 else x//2
    return x

def choose(u):
    r=u.count('O')
    for d in (1,2):
        m=r+d
        j=(3**m).bit_length()
        D=(1<<j)-3**m
        if 3*D>3**m:
            b=j-len(u)-d
            assert b>=1
            return d,j,u+'O'*d+'E'*b
    raise AssertionError('two-shot gap failure')

class S020TheoremTests(unittest.TestCase):
    def test_block_affines(self):
        self.assertEqual(affine('OOOE'),(27,16,19))
        self.assertEqual(affine('OOOOE'),(81,32,65))

    def test_gap_20000(self):
        for r in range(1,20001):
            assert any(3*((1<<(3**(r+d)).bit_length())-3**(r+d))>3**(r+d)
                       for d in (1,2))

    def test_every_block_choice_to_ten(self):
        count=[0,0,0]
        for k in range(1,11):
            for blocks in itertools.product(BLOCKS,repeat=k):
                u=''.join(blocks)
                a,q,b=affine(u)
                self.assertLess(11*(b+q),19*a)
                odds=0
                for i,letter in enumerate(u,1):
                    odds+=(letter=='O')
                    self.assertGreater(3**odds,1<<i)
                d,j,w=choose(u)
                count[d]+=1
                n0=canonical(w)
                self.assertGreaterEqual(n0,7)
                aw,qw,bw=affine(w)
                self.assertEqual(qw,1<<j)
                self.assertGreater(3*(qw-aw),aw)
                self.assertGreater((qw-aw)*n0,bw)
                self.assertEqual(execute(w,n0),(aw*n0+bw)//qw)
                for t in (0,1,3):
                    x=n0+t*qw
                    self.assertLess(execute(w,x),x)
        self.assertEqual(count[1:], [1225,821])

    def test_irregular_150_blocks(self):
        u=''.join('OOOOE' if (i*i+i+1)%7 in (0,1,3) else 'OOOE'
                  for i in range(150))
        a,q,b=affine(u)
        self.assertLess(11*(b+q),19*a)
        d,j,w=choose(u)
        n=canonical(w)
        for t in (0,1):
            x=n+t*(1<<j)
            self.assertLess(execute(w,x),x)

    def test_hostile_controls(self):
        residual=0
        for n in range(11,8192,16):
            x=n
            no_drop=True
            for _ in range(13):
                x=(3*x+1)//2 if x&1 else x//2
                if x<n:no_drop=False
            residual+=no_drop
        self.assertEqual(residual,71)
        for k in (0,1,4,10):
            self.assertEqual(execute('OOE',64*k+59),72*k+67)
        for H in (5,16,31):
            u=5 if H&1 else 7
            n=(1<<H)*u-1
            self.assertEqual(n%3,0)
            v=n
            for _ in range(H):
                self.assertEqual(v%2,1)
                v=(3*v+1)//2
                self.assertGreater(v,n)

    def test_noncoverage(self):
        self.assertEqual(2%2,0)
        for b in (('OOOE',), ('OOOOE','OOOE'), ('OOOOE',)*8):
            _,_,w=choose(''.join(b))
            self.assertEqual(w[:3],'OOO')

if __name__=='__main__':
    unittest.main()
