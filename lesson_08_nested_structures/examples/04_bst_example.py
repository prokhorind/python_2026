class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):

        if self.root is None:
            self.root = Node(value)
            return

        current = self.root

        while True:

            if value < current.value:

                if current.left is None:
                    current.left = Node(value)
                    return

                current = current.left

            else:

                if current.right is None:
                    current.right = Node(value)
                    return

                current = current.right
    def print_tree(self):
        current = self.root
        self.inorder(current)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)


bst = BinarySearchTree()

numbers = [8, 3, 10, 1, 6, 14]

for n in numbers:
    bst.insert(n)

print("Tree created")

print("Inorder traversal:")
bst.print_tree()