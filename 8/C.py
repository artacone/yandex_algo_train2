class Pedigree:
    def __init__(self):
        self.ancestry = {}

    def add(self, child, parent):
        self.ancestry[child] = parent

    def get_lca(self, person1, person2):
        ancestors1 = set()
        ancestor = person1
        while ancestor in self.ancestry:
            ancestors1.add(ancestor)
            ancestor = self.ancestry[ancestor]
        ancestors1.add(ancestor)

        lca = person2
        while lca not in ancestors1:
            lca = self.ancestry[lca]
        return lca


if __name__ == "__main__":
    num_persons = int(input())
    tree = Pedigree()
    for _ in range(num_persons - 1):
        child, parent = input().split()
        tree.add(child, parent)

    lca_list = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        p1, p2 = line.split()
        lca_list.append(tree.get_lca(p1, p2))

    print("\n".join(lca_list))
