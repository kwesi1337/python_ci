import unittest
from src1.math import Math


class MathTest(unittest.TestCase):
    def test_addition(self):
        #Make test fail
        self.assertEqual(Math.addition(3,4), 8)
