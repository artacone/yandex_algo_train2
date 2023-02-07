
class Tree:
    def __init__(self, n_nodes=1):
        self.nodes = [set() for _ in range(n_nodes+1)]

    def add_link(self, first, second):
        self.nodes[first].add(second)
        self.nodes[second].add(first)

    def get_furthest(self, root):
        from collections import deque
        max_h = 1
        furthest = root
        q = deque()
        visited = [False] * len(self.nodes)
        q.append((root, max_h))
        visited[root] = True
        while q:
            node, current_h = q.popleft()
            new_h = current_h + 1
            for n in self.nodes[node]:
                if not visited[n]:
                    if new_h > max_h:
                        furthest, max_h = n, new_h
                    q.append((n, new_h))
                    visited[n] = True

        return furthest, max_h

    def get_longest_chain(self):
        r1 = 1
        r2, _ = self.get_furthest(r1)
        _, diameter = self.get_furthest(r2)
        return diameter


if __name__ == '__main__':
    n = int(input())

    tree = Tree(n)
    for _ in range(n-1):
        f, s = map(int, input().split())
        tree.add_link(f, s)

    print(tree.get_longest_chain())
