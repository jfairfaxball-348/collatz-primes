#!/usr/bin/env python3
"""S001 independent audit of records from residue_certificates.py; no imports from producer.
Rechecks direct T branches, closed-form affine composition, and symbolic full-class
or base-exception inequalities. Infinite validity rests on algebra described in S001 note.
"""
import argparse
import hashlib
import json


def verify(rec):
    k,r,j,a,b,w,status = [rec[v] for v in ('k','r','j','a','b','parity_word','status')]
    assert k>=2 and 1<=r<2**k and r%2==1
    assert status in ('STRICT','BASE_1','OPEN')
    if status=='OPEN':
        assert j==0 and a==0 and b==0 and w==''
        # Independently check there is no descent certificate at any j<=k.
        y=r; M=1;N=0;A=0
        for t in range(1,k+1):
            if y%2:
                N=3*N+2**(t-1);M*=3;A+=1
                y=(3*y+1)//2
            else:y//=2
            assert M*r+N==2**t*y
            assert not (2**t>M and M*r+N<2**t*r)
        return
    assert 1<=j<=k and len(w)==j and a==w.count('O')
    y=r;M=1;N=0
    for i,ch in enumerate(w):
        assert ch in 'EO'
        # Parity of all class members agrees: at time i, their difference
        # is 3^(odd-prefix)*q*2^(k-i), which is even whenever i<k.
        assert (y%2==1)==(ch=='O')
        assert k-i>=1
        if ch=='O':
            y=(3*y+1)//2
            N=3*N+2**i
            M*=3
        else:y//=2
        assert M*r+N == 2**(i+1)*y
    assert M==3**a and N==b
    den=2**j
    if status=='STRICT':
        assert den> M
        assert M*r+N<den*r
        # For ALL q>=0, (den-M)*(r+q*2^k)-N>0
        # from positivity at q=0 and den-M>0.
        assert (den-M)*r-N>0
    else:
        assert r==1 and k>=2 and (j,a,b,w)==(2,1,1,'OE')
        assert (den-M)*r-N==0  # 1 is fixed only under T^2
        assert den>M and (den-M)*(r+2**k)-N>0


def verify_report(report):
    lo,hi=report['range_k_inclusive']
    assert 2<=lo<=hi
    assert [row['k'] for row in report['depths']]==list(range(lo,hi+1))
    for entry in report['depths']:
        k=entry['k'];h=hashlib.sha256(); counts={'STRICT':0,'BASE_1':0,'OPEN':0}; splits={}
        for r in range(1,2**k,2):
            # Source records reconstructed as self-contained data, then checked
            # independently using verify(), not the producer classification logic.
            y=r;M=1;N=0; word=''; certificate=None
            for j in range(1,k+1):
                bit=y%2
                word+=('O' if bit else 'E')
                if bit:
                    y=(3*y+1)//2;N=3*N+2**(j-1);M*=3
                else:y//=2
                if 2**j>M and M*r+N<2**j*r:
                    certificate={'k':k,'r':r,'j':j,'a':word.count('O'),'b':N,'parity_word':word,'status':'STRICT'}
                    break
                if r==1 and j==2:
                    certificate={'k':k,'r':r,'j':2,'a':1,'b':1,'parity_word':'OE','status':'BASE_1'}
                    break
            if certificate is None:
                certificate={'k':k,'r':r,'j':0,'a':0,'b':0,'parity_word':'','status':'OPEN'}
            verify(certificate)
            counts[certificate['status']]+=1
            if certificate['status']=='OPEN':
                key=str(r%16);splits[key]=splits.get(key,0)+1
            h.update((json.dumps(certificate,sort_keys=True,separators=(',',':'))+'\n').encode())
            if str(r) in entry['examples']:
                assert entry['examples'][str(r)]==certificate
        assert counts['STRICT']==entry['strict']
        assert counts['BASE_1']==entry['base_1']==1
        assert counts['OPEN']==entry['uncovered']
        assert entry['odd_classes']==2**(k-1)==sum(counts.values())
        assert splits==entry['uncovered_mod16']
        assert h.hexdigest()==entry['records_sha256']
    return True

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('manifest'); args=p.parse_args()
    with open(args.manifest) as f:data=json.load(f)
    assert verify_report(data)
    print('INDEPENDENT CHECK PASS:',len(data['depths']),'depths; SHA256 per complete record stream matched')
