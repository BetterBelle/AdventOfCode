map = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}
inp = [[map[line.strip().split(' ')[0]], map[line.strip().split(' ')[1]]] for line in open("2022/inputs/day02.txt")]


def part1():
    results = list()
    for match in inp:
        results.append((match[0] - match[1]) % 3)
    
    print(results)

def part2():
    pass


print(part1())
print(part2())