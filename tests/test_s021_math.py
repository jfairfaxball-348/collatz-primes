"""S021 exact finite cross-checks of variable O^a E alphabets; NOT a universal proof."""
from itertools import product
import unittest

def affine(word):
    a, q, b = 1, 1, 0
    for c in word:
        if c == 'O':
            a *= 3
            b = 3*b+q
        q *= 2
    return a, q, b

def witness(word):
    r = word.count('O')
    for d in (1, 2):
        m = r+d
        j = (3**m).bit_length()
        if 3*((1 << j)-3**m) > 3**m:
            return d, word+'O'*d+'E'*(j-len(word)-d), j
    raise AssertionError('gap')

class S021TheoremTests(unittest.TestCase):
    def test_variable_all_runs_3_to_8(self):
        totals = {1:0, 2:0}
        for k in range(1, 7):
            for seq in product(range(3, 9), repeat=k):
                u = ''.join('O'*a+'E' for a in seq)
                a,q,b = affine(u)
                self.assertLessEqual(11*b+19*q, 19*a)
                self.assertLess(11*(b+q), 19*a)
                d,w,j = witness(u)
                aw,qw,bw = affine(w)
                self.assertEqual(qw, 1 << j)
                n0 = (-bw * pow(aw, -1, qw)) % qw or qw
                self.assertGreater((qw-aw)*n0, bw)
                totals[d] += 1
        self.assertEqual(totals,{1:32766,2:23220})

    def test_threshold_at_two_is_not_certified(self):
        u = 'OOE'
        a,q,b = affine(u)
        self.assertGreater(11*b+19*q, 19*a)
        self.assertGreater(27*2**2, 8*3**2)

    def test_gap_failure_of_nonselective_rule(self):
        m=5
        j=(3**m).bit_length()
        self.assertLessEqual(3*((1<<j)-3**m), 3**m)
        self.assertGreater(3*((1<<(3**(m+1)).bit_length())-3**(m+1)), 3**(m+1))

    def test_hostile_finite_exception_controls(self):
        count=0
        for n in range(11,8192,16):
            x=n
            seen=False
            for _ in range(13):
                x=(3*x+1)//2 if x&1 else x//2
                seen|=(x<n)
            count+=not seen
        self.assertEqual(count,71)
        for k in (0,1,4,10):
            x=64*k+59
            for _ in range(3):
                x=(3*x+1)//2 if x&1 else x//2
            self.assertEqual(x,72*k+67)

if __name__=='__main__':
    unittest.main()
