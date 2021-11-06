class Person:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []
        self.height = None

    def add_child(self, child):
        self.children.append(child)

    def set_parent(self, parent):
        self.parent = parent


class Pedigree:
    def __init__(self):
        self.ancestry = {}

    def add(self, child, parent):
        if parent not in self.ancestry:
            self.ancestry[parent] = Person()
        if child in self.ancestry:
            self.ancestry[child].set_parent(self.ancestry[parent])
        else:
            self.ancestry[child] = Person(self.ancestry[parent])
        self.ancestry[parent].add_child(self.ancestry[child])

    def set_heights(self):
        forefather = None
        for name, person in self.ancestry.items():
            if person.parent is None:
                forefather = person
                break

        def set_heights_recursive(person, height):
            person.height = height
            for child in person.children:
                set_heights_recursive(child, height + 1)

        set_heights_recursive(forefather, 0)

    def get_relation(self, person1, person2):
        ancestor = self.ancestry[person1]
        descendant = self.ancestry[person2]
        if ancestor.height < descendant.height:
            relation = 1
        else:
            relation = 2
            ancestor, descendant = descendant, ancestor
        current = descendant

        while current.height != ancestor.height:
            current = current.parent

        if current == ancestor:
            return relation
        return 0


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(1500)

    num_persons = int(input())
    tree = Pedigree()
    for _ in range(num_persons - 1):
        child, parent = input().split()
        tree.add(child, parent)

    tree.set_heights()

    ans = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        p1, p2 = line.split()
        ans.append(str(tree.get_relation(p1, p2)))

    print(" ".join(ans))
