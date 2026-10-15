import json
import unittest
from tools.check_residue_certificates import verify,verify_report
from tools.residue_certificates import record,generate

class TestS001(unittest.TestCase):
    def test_report_all_depths_and_hashes(self):
        with open('validation/S001_manifest.json') as f: m=json.load(f)
        self.assertTrue(verify_report(m))
        self.assertEqual([e['uncovered'] for e in m['depths']][-1],2114)
        self.assertEqual(m['depths'][-1]['uncovered_mod16'], {'7':395,'11':395,'15':1324})
        self.assertEqual(m['depths'][-1]['strict'],30653)
        self.assertEqual(m['depths'][-1]['base_1'],1)
    def test_edge_cases(self):
        for k in (2,3,4,10,16):
            for r in (1, (1<<k)-1):verify(record(k,r))
        for r in (7,11,15,23,27,65535):
            verify(record(16,r))
        self.assertEqual(record(16,27)['status'],'OPEN')
        self.assertEqual(record(16,1)['status'],'BASE_1')
        self.assertEqual(record(16,65535)['status'],'OPEN')
    def test_hostile_corruption(self):
        v=record(10,3)
        self.assertEqual(v['status'],'STRICT')
        v['b']+=1
        with self.assertRaises(AssertionError):verify(v)
        v=record(10,27);v['status']='STRICT'
        with self.assertRaises(AssertionError):verify(v)

if __name__=='__main__':unittest.main()
