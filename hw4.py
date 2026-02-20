class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if node is None:
                return TreeNode(value)
            if value < node.data:
                node.left = _insert(node.left, value)
            elif value > node.data:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.data, end=" ")
                _inorder(node.right)

        _inorder(self.root)
