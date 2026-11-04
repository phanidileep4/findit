from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from backend import findit

class MemoryTests(unittest.TestCase):
    def test_validation(self):
        for value in ({'objects': 'keys'}, {'objects': [], 'verified': True},
            {'objects': [{'label':'keys','location':'table','confidence':True}]}):
            with self.assertRaises(ValueError): findit.validate(value)
        with self.assertRaises(ValueError): findit.timestamp('2026-01-01T00:00:00')

    def test_history_budget_integrity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            image = root / 'input.jpg'
            image.write_bytes(b'\xff\xd8\xfffixture')
            store = root / 'store'
            db = findit.connect(store)
            claim = [{'label':'keys','location':'table','confidence':.8}]
            with patch.object(findit, 'analyze', return_value=claim) as model:
                for day in range(1, 11):
                    findit.capture(db, store, image, '2026-01-%02dT00:00:00Z' % day, 'TEST_IMAGE', 'mock')
                with self.assertRaises(ValueError):
                    findit.capture(db, store, image, '2026-01-01T00:00:00Z', 'TEST_IMAGE', 'mock')
                self.assertEqual(10, model.call_count)
            results = findit.search(db, store, 'keys')
            self.assertEqual(10, len(results))
            self.assertIn('01-10', results[0]['captured_at'])
            self.assertEqual('MODEL_INFERRED', results[0]['claim_type'])
            self.assertEqual('UNKNOWN', results[0]['current_location'])
            self.assertTrue(results[0]['evidence_intact'])
            Path(results[0]['evidence']).write_bytes(b'tampered')
            self.assertFalse(findit.search(db, store, 'keys')[0]['evidence_intact'])
            self.assertEqual([], findit.search(db, store, 'ring'))
            db.close()

    def test_provider_failure_does_not_save_claim(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            image = root / 'input.jpg'
            image.write_bytes(b'\xff\xd8\xfffixture')
            db = findit.connect(root / 'store')
            with patch.object(findit, 'analyze', side_effect=ValueError('failure')):
                with self.assertRaises(ValueError):
                    findit.capture(db, root / 'store', image, '2026-01-01T00:00:00Z', 'TEST_IMAGE', 'mock')
            self.assertEqual(0, db.execute('SELECT COUNT(*) FROM captures').fetchone()[0])
            self.assertEqual(1, db.execute('SELECT COUNT(*) FROM attempts').fetchone()[0])
            db.close()
