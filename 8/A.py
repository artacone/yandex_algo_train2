class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value=0):
        node = TreeNode(value)
        if self.root is None:
            self.root = node
            return node
        else:
            return self.insert_node(self.root, node)

    def insert_node(self, root, node):
        if node.value < root.value:
            if root.left is None:
                root.left = node
                return node
            else:
                return self.insert_node(root.left, node)
        elif node.value > root.value:
            if root.right is None:
                root.right = node
                return node
            else:
                return self.insert_node(root.right, node)
        else:
            return None

    def find(self, n):
        return self.find_node(self.root, n)

    def find_node(self, root, n):
        if root is None:
            return None
        if n == root.value:
            return root
        elif n < root.value:
            return self.find_node(root.left, n)
        else:
            return self.find_node(root.right, n)

    def print(self):
        if self.root is not None:
            self.print_subtree(self.root, 0)

    def print_subtree(self, root, height):
        if root is not None:
            self.print_subtree(root.left, height + 1)
            print("." * height, root.value, sep='')
            self.print_subtree(root.right, height + 1)


if __name__ == '__main__':
    import sys
    tree = BST()

    for line in sys.stdin:
        cmd = line.split()
        if cmd[0] == "ADD":
            if tree.insert(int(cmd[1])) is None:
                print("ALREADY")
            else:
                print("DONE")
        elif cmd[0] == "SEARCH":
            if tree.find(int(cmd[1])) is None:
                print("NO")
            else:
                print("YES")
        elif cmd[0] == "PRINTTREE":
            tree.print()
