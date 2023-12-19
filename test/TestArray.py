import unittest
from src.main import *


class TestArray(unittest.TestCase):
    def test_kth_largest_1(self):
        arr = [3, -2, 0, 1, 2]
        k = 1
        expected_result = [3, 4]
        self.assertEqual(bigger_element(arr, k), expected_result)

    def test_kth_largest_2(self):
        arr = [10, 8, 5, 3, 1]
        k = 1
        expected_result = [10, 4]
        self.assertEqual(bigger_element(arr, k), expected_result)

    def test_kth_largest_3(self):
        arr = [4, 4, 4, 4, 4]
        k = 3
        expected_result = [4, 0]
        self.assertEqual(bigger_element(arr, k), expected_result)

    def test_kth_largest_4(self):
        arr = []
        k = 2
        with self.assertRaises(ValueError):
            bigger_element(arr, k)


if __name__ == '__main__':
    unittest.main()
