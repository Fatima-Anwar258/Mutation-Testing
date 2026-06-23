import unittest
from percentage import calculate_percentage

class TestPercentageCalculator(unittest.TestCase):

    def test_valid_percentage(self):
        self.assertEqual(calculate_percentage(425, 500), 85.0)

    def test_full_marks(self):
        self.assertEqual(calculate_percentage(500, 500), 100.0)

    def test_zero_marks(self):
        self.assertEqual(calculate_percentage(0, 500), 0.0)
