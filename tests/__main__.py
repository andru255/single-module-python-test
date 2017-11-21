import lib
import unittest

class TestCalculator(unittest.TestCase):
  def test_total(self):
    total = lib.calculator.total(4,4)
    self.assertEqual(8, total)

if __name__ == '__main__':
    unittest.main()
