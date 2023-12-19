import unittest
from src.main import *


class TestMinEatingSpeed(unittest.TestCase):
    def test_example1(self):
        piles = [3, 6, 7, 11]
        H = 8
        self.assertEqual(minEatingSpeed(piles, H), 4)

    def test_example2(self):
        piles = [30, 11, 23, 4, 20]
        H = 5
        self.assertEqual(minEatingSpeed(piles, H), 30)

    def test_example3(self):
        piles = [30, 11, 23, 4, 20]
        H = 6
        self.assertEqual(minEatingSpeed(piles, H), 23)


if __name__ == '__main__':
    unittest.main()
