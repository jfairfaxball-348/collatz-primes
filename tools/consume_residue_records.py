#!/usr/bin/env python3
"""Independently consume and check ALL canonical S001 JSONL records. No producer imports."""
import argparse
import hashlib
import json

def verify_row(rw, k, r):
    assert set(rw)=={'k','r','j','a','b','parity_word','status'}
    assert (rw['k'],rw['r'])==(k,r)
    x=r; odd=0; intercept=0; word=''; first=None
    for j in range(1,k+1):
        is_odd=x&1
        word+= 'O' if is_odd else 'E'
        if is_odd:
            odd+=1
            intercept=3*intercept+(1<<(j-1))
            x=(3*x+1)//2
        else:
            x//=2
        multiplier=3**odd
        assert (multiplier*r+intercept)==(1<<j)*x
        if (1<<j)>multiplier and (multiplier*r+intercept)<(1<<j)*r:
            first=(j,odd,intercept,word,'STRICT')
            break
        if r==1 and j==2:
            first=(2,1,1,'OE','BASE_1')
            break
    if first is None:
        expected=(0,0,0,'','OPEN')
    else:
        expected=first
    assert tuple(rw[v] for v in ('j','a','b','parity_word','status'))==expected
    return expected[-1]

def consume(report, records):
    lo,hi=report['range_k_inclusive']
    assert 2<=lo<=hi and len(report['depths'])==hi-lo+1
    with open(records,encoding='utf8') as fp:
        for entry in report['depths']:
            k=entry['k']
            assert lo<=k<=hi
            h=hashlib.sha256()
            counts={'STRICT':0,'BASE_1':0,'OPEN':0}
            splits={}
            for r in range(1,1<<k,2):
                line=fp.readline()
                assert line and line.endswith('\n'), ('missing/noncanonical record',k,r)
                rw=json.loads(line)
                assert line==json.dumps(rw,sort_keys=True,separators=(',',':'))+'\n'
                status=verify_row(rw,k,r)
                counts[status]+=1
                if status=='OPEN':
                    key=str(r%16)
                    splits[key]=splits.get(key,0)+1
                if str(r) in entry['examples']:
                    assert entry['examples'][str(r)]==rw
                h.update(line.encode('utf8'))
            assert h.hexdigest()==entry['records_sha256'], ('digest mismatch',k)
            assert entry['odd_classes']==1<<(k-1)
            assert counts=={'STRICT':entry['strict'],'BASE_1':entry['base_1'],'OPEN':entry['uncovered']}
            assert splits==entry['uncovered_mod16']
        assert fp.read()=='', 'extra records'
    return True

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('manifest');p.add_argument('records')
    a=p.parse_args()
    with open(a.manifest,encoding='utf8') as f: m=json.load(f)
    assert consume(m,a.records)
    print('STREAM CONSUMER PASS: canonical records, classes, witnesses and hashes')
