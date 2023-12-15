class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value < node.data:
            return node, parent, True

        if value < node.data:
            if node.data:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.data:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not s and fl_find:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

            return  obj

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)
