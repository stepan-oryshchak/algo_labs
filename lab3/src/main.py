class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def in_order(self, node, list):
        if node is None:
            return list
        self.in_order(node.left, list)
        list.append(node.value)
        self.in_order(node.right, list)
