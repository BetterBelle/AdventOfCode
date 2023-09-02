class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def sum_metadata(self):
        ans = 0
        for child in self.children:
            ans += child.sum_metadata()

        for meta in self.metadata:
            ans += meta

        return ans

    def value(self):
        ans = 0
        if len(self.children) == 0:
            for data in self.metadata:
                ans += data
        else:
            for data in self.metadata:
                if data-1 in range(len(self.children)):
                    ans += self.children[data-1].value()
        return ans

# Create list of all info
with open("2018/day08.txt") as inp:
    info = [int(info) for info in inp.read().split(" ")]

def build_tree(num_children, num_metadata):
    root = Node([build_tree(info.pop(0), info.pop(0)) for _ in range(num_children)], [info.pop(0) for _ in range(num_metadata)])
    return root

# Build the full tree (starting from root)
tree = build_tree(info.pop(0), info.pop(0))

def part1():
    return tree.sum_metadata()


def part2():
    return tree.value()


print (part1())
print (part2())