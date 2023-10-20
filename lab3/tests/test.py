import unittest
from src.main import *


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(1)
        self.root.left = BinaryTree(2)
        self.root.right = BinaryTree(3)
        self.root.left.left = BinaryTree(4)
        self.root.left.right = BinaryTree(5)
        self.root.right.left = BinaryTree(6)
        self.root.right.right = BinaryTree(7)

    def test_in_order(self):
        result = []
        self.root.in_order(self.root, result)
        self.assertEqual(result, [4, 2, 5, 1, 6, 3, 7])

    def test_empty_tree(self):
        empty_tree = BinaryTree(None)
        result = []
        empty_tree.in_order(empty_tree, result)
        self.assertEqual(result, [None])

    def test_single_node_tree(self):
        single_node_tree = BinaryTree(42)
        result = []
        single_node_tree.in_order(single_node_tree, result)
        self.assertEqual(result, [42])

    def test_right_skewed_tree(self):
        right_skewed_tree = BinaryTree(1)
        right_skewed_tree.right = BinaryTree(2)
        right_skewed_tree.right.right = BinaryTree(3)
        result = []
        right_skewed_tree.in_order(right_skewed_tree, result)
        self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()