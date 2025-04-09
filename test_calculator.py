import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1, 0), 0)
        self.assertEqual(mul(-4, 2), -8)
        self.assertAlmostEqual(mul(4.1, 1), 4)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(1, 0), 0)
        self.assertEqual(div(4, 4), 1)
        self.assertAlmostEqual(div(4.1, 8), 2)


    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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