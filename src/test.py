import unittest
from unittest.mock import mock_open
from collections import defaultdict
from src.main import build_adjacency_list, min_depth_with_path, write_to_output


class TestAlg(unittest.TestCase):
    def test_build_adjacency_list(self):
        file_name = 'input.txt'
        mock_file = mock_open(read_data='10\n20,30')
        with unittest.mock.patch('builtins.open', mock_file):
            root, adjacency_list = build_adjacency_list(file_name)
            self.assertEqual(root, 10)
            self.assertEqual(adjacency_list[20], [30])

    def test_min_depth_with_path(self):
        adjacency_list = defaultdict(list)
        adjacency_list[10] = [20, 30]
        adjacency_list[20] = [40]
        adjacency_list[30] = [50]
        min_depth_value, path = min_depth_with_path(10, adjacency_list)
        self.assertEqual(min_depth_value, 3)


if __name__ == '__main__':
    unittest.main()