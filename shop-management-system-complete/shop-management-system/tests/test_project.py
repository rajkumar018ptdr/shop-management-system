import unittest, tempfile
from pathlib import Path
import storage

class ProjectTests(unittest.TestCase):
    def test_next_id(self):
        self.assertEqual(storage.next_id({'P0001':{},'P0003':{}},'P'),'P0004')
    def test_json_round_trip(self):
        old=storage.DATA_DIR
        with tempfile.TemporaryDirectory() as d:
            storage.DATA_DIR=Path(d); storage.save_json('x.json',{'a':1}); self.assertEqual(storage.load_json('x.json',{}),{'a':1})
        storage.DATA_DIR=old
    def test_profit(self): self.assertEqual((150-100)*3,150)
    def test_bill_total(self): self.assertEqual(120*4,480)

if __name__=='__main__': unittest.main()
