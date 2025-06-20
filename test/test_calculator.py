import unittest
import sys
import os

# Asegurar que src/ esté en el path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculator import suma, resta

class CalculatorTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)

if __name__ == '__main__':
    unittest.main()
