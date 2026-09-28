"""Compatibility test entry point for the current validation suite."""
import unittest
from validate_publication import main
from build_forecast_financials import get_2025_value, get_assumption
import pandas as pd
class PublicationChecks(unittest.TestCase):
    def test_publication_data(self): self.assertEqual(main()['status'],'PASS')
    def test_duplicate_values_are_rejected(self):
        data=pd.DataFrame([dict(period='2025A',metric='Net income',value=1018.6)]*2)
        with self.assertRaises(ValueError):get_2025_value(data,'Net income')
    def test_duplicate_assumptions_are_rejected(self):
        data=pd.DataFrame([{'scenario':'Base','assumption':'Cost of risk','2026E':40}]*2)
        with self.assertRaises(ValueError):get_assumption(data,'Base','Cost of risk','2026E')
if __name__=='__main__':unittest.main(verbosity=2)
