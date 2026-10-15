#!/usr/bin/env python3
"""S001 exact affine certificates for odd shortened-Collatz residues; finite only.

Canonical per-class record: JSON object dumped with sort_keys=True, separators=(',',':'),
followed by '\n'; order k increasing, then odd r increasing. SHA256 digests cover
ALL class records (including uncovered), not just the summary manifest.
"""
import argparse
from collections import Counter
import hashlib
import json


def record(k, r):
    if k < 2 or not (1 <= r < (1 << k) and r % 2):
        raise ValueError('k>=2; odd positive representative r < 2**k')
    x, a, b, word = r, 0, 0, ''
    for j in range(1, k + 1):
        bit = x & 1
        word += 'O' if bit else 'E'
        if bit:
            b = 3 * b + (1 << (j - 1))
            a += 1
            x = (3 * x + 1) // 2
        else:
            x //= 2
        d = 1 << j
        if d > 3 ** a and (3 ** a) * r + b < d * r:
            return dict(k=k, r=r, j=j, a=a, b=b, parity_word=word, status='STRICT')
        if r == 1 and j == 2 and k >= 2:
            # Exceptional base n=1 does NOT strictly descend; all n>1 in class do.
            return dict(k=k, r=r, j=2, a=1, b=1, parity_word='OE', status='BASE_1')
    return dict(k=k, r=r, j=0, a=0, b=0, parity_word='', status='OPEN')


def generate(lo=10, hi=16):
    out = {'map':'shortened_T', 'classification': 'STRICT;BASE_1;OPEN',
           'range_k_inclusive':[lo,hi], 'records_encoding':'JSONL sorted keys compact newline',
           'depths':[]}
    for k in range(lo, hi + 1):
        h = hashlib.sha256()
        counts = Counter()
        splits = Counter()
        examples = {}
        for r in range(1, 1 << k, 2):
            rec = record(k, r)
            h.update((json.dumps(rec, sort_keys=True, separators=(',', ':'))+'\n').encode())
            counts[rec['status']] += 1
            if rec['status']=='OPEN':
                splits[str(r%16)] += 1
            if r in (1,7,11,15,23,27,(1<<k)-1):
                examples[str(r)] = rec
        out['depths'].append({'k':k, 'odd_classes':1<<(k-1),
           'strict':counts['STRICT'], 'base_1':counts['BASE_1'],
           'uncovered':counts['OPEN'], 'uncovered_mod16':dict(sorted(splits.items(),key=lambda z:int(z[0]))),
           'records_sha256':h.hexdigest(), 'examples':examples})
    return out


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--lo',type=int,default=10)
    p.add_argument('--hi',type=int,default=16)
    p.add_argument('--output')
    p.add_argument('--records',help='optional complete reproducible JSONL records output for all depths')
    args=p.parse_args()
    if args.lo < 2 or args.hi < args.lo:
        p.error('require 2<=lo<=hi')
    report=generate(args.lo,args.hi)
    body=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.output:
        with open(args.output,'w') as f:f.write(body)
    else:print(body,end='')
    if args.records:
        with open(args.records,'w') as f:
            for k in range(args.lo,args.hi+1):
                for r in range(1,1<<k,2):
                    f.write(json.dumps(record(k,r),sort_keys=True,separators=(',',':'))+'\n')
