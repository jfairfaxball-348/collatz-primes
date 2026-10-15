"""S003: finite hostile checks. These DO NOT prove Collatz or Terras CST."""
import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tools.consume_residue_records import consume
from tools.residue_certificates import generate, record


def T(n):
    return (3*n+1)//2 if n & 1 else n//2


def U(n):
    t=3*n+1
    a=(t & -t).bit_length()-1
    return t>>a,a


def first_pair(n, cap=1000):
    x=n; multiplier=1; den=1; js=jc=None
    for j in range(1,cap+1):
        if x & 1:
            multiplier*=3
        x=T(x)
        den*=2
        if jc is None and multiplier<den: jc=j
        if js is None and x<n: js=j
        if js is not None and jc is not None: break
    return js,jc


class TestS003(unittest.TestCase):
    def test_slope_sample_predeclared_ranges(self):
        # Separate discovery/holdout. Finitely bounded observational result only.
        for lo,hi in ((2,100000),(100001,1000000)):
            for n in range(lo,hi+1):
                pair=first_pair(n)
                self.assertIsNotNone(pair[0])
                self.assertEqual(pair[0],pair[1])

    def test_paradoxical_later_slope_and_27(self):
        x=7
        trace=[x]
        for _ in range(8):
            x=T(x)
            trace.append(x)
        self.assertEqual(trace,[7,11,17,26,13,20,10,5,8])
        self.assertEqual(first_pair(7), (7,7))
        self.assertEqual(243*7+347,256*8)
        x=27;M=1;b=0;den=1;odd=0
        for j in range(1,60):
            if x & 1:
                M*=3; b=3*b+den; odd+=1
            den*=2;x=T(x)
            if j<59:
                self.assertGreaterEqual(M,den)
        self.assertEqual((x,odd,den-M,b),(23,37,126176846412426125,1100931843921811423))

    def test_offsets_1_to_6_steps(self):
        import math
        for n in (15,35,121,27,3,51,243,231):
            x=n;F=0;A=0
            for m in range(1,7):
                y,a=U(x)
                F=3*F+(1<<A)
                A+=a
                self.assertEqual((1<<A)*y,3**m*n+F)
                self.assertEqual(math.gcd(n,y),math.gcd(n,F))
                x=y

    def test_open_slope_observation_k10_to_16(self):
        expected={10:64,11:128,12:226,13:367,14:734,15:1295,16:2114}
        for k in expected:
            count=0
            for r in range(3,1<<k,2):
                x=r;M=1;den=1;cross=False;desc=False
                for _ in range(k):
                    if x&1: M*=3
                    x=T(x);den*=2
                    cross |= M<den
                    desc |= x<r
                if not desc:
                    count+=1
                    self.assertFalse(cross,(k,r))
            self.assertEqual(count,expected[k])

    def test_canonical_stream_corruptions(self):
        # Consumer imports NO generator: generator provides test fixtures only.
        manifest=generate(2,4)
        lines=[json.dumps(record(k,r),sort_keys=True,separators=(',',':'))+'\n'
               for k in range(2,5) for r in range(1,1<<k,2)]
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'stream.jsonl'
            p.write_text(''.join(lines),encoding='utf-8')
            self.assertTrue(consume(manifest,str(p)))
            variants={}
            variants['missing row']=lines[:-1]
            reordered=lines.copy();reordered[0],reordered[1]=reordered[1],reordered[0]
            variants['reordering']=reordered
            for name,field,newval in [('wrong parity','parity_word','XX'),('wrong status','status','STRICT')]:
                v=lines.copy();rec=json.loads(v[1]);rec[field]=newval
                v[1]=json.dumps(rec,sort_keys=True,separators=(',',':'))+'\n'
                variants[name]=v
            for name,variant in variants.items():
                with self.subTest(name=name):
                    p.write_text(''.join(variant),encoding='utf-8')
                    with self.assertRaises(AssertionError):
                        consume(manifest,str(p))
            p.write_text(''.join(lines),encoding='utf-8')
            damaged=copy.deepcopy(manifest)
            damaged['depths'][0]['records_sha256']='0'*64
            with self.assertRaises(AssertionError):
                consume(damaged,str(p))


if __name__ == '__main__':
    unittest.main()
