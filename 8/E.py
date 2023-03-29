
class Node:
    def __init__(self, left=None, right=None, up=None, is_right=False):
        self.left = left
        self.right = right
        self.up = up
        self.is_right = is_right


class HTree:
    def __init__(self, serialized):
        self.tree = Node()
        current = self.tree
        for c in serialized:
            if c == 'D':
                new = Node(up=current)
                current.left = new
                current = new
            elif c == 'U':
                while current.is_right:
                    current = current.up
                current = current.up
                new = Node(up=current, is_right=True)
                current.right = new
                current = new

    def __traverse(self, root, prefix):
        if root.left is None:
            return ["".join(prefix)]
        prefix.append('0')
        codes = self.__traverse(root.left, prefix)
        prefix.pop()
        prefix.append('1')
        codes.extend(self.__traverse(root.right, prefix))
        prefix.pop()
        return codes

    def print_alphabet(self):
        codes = self.__traverse(self.tree, [])
        print(len(codes), '\n'.join(codes), sep='\n')


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        serialized = input()
        tree = HTree(serialized)
        tree.print_alphabet()
