import unittest
from src.main import find_needle


class TestFindNeedle(unittest.TestCase):
    def test_needle_first(self):
        haystack = "needle in a haystack"
        needle = "needle"
        expected_result = (0, 21)
        result_index, comparison_count = find_needle(haystack, needle)
        self.assertEqual((result_index, comparison_count), expected_result)

    def test_empty(self):
        haystack = "There is empty"
        needle = "needle"
        expected_result = (-1, 9)
        result_index, comparison_count = find_needle(haystack, needle)
        self.assertEqual((result_index, comparison_count), expected_result)

    def test_needle_last(self):
        haystack = "A needle in needle"
        needle = "needle"
        expected_result = (12, 24)
        result_index, comparison_count = find_needle(haystack, needle)
        self.assertEqual((result_index, comparison_count), expected_result)


if __name__ == '__main__':
    unittest.main()