# https://github.com/NavajS/lab10-NS-JP
# Partner 1: Jenish Patel
# Partner 2: Navaj Sivakumar

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-5, 5), 0)
        self.assertAlmostEqual(add(10, 8), 18)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(-5, 5), -10)
        self.assertAlmostEqual(subtract(9, 2), 7)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1, 0), 0)
        self.assertEqual(mul(-4, 2), -8)
        self.assertAlmostEqual(mul(4, 1), 4)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(0, 1), 0)
        self.assertEqual(div(4, 4), 1)
        self.assertAlmostEqual(div(8, 4), 2)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 2), 1)
        self.assertEqual(logarithm(3, 9), 2)
        self.assertEqual(logarithm(4, 64), 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-1, 5)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(4, 3), 5)
        self.assertEqual(hypotenuse(-4, 3), 5)
        self.assertEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(16), 4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
