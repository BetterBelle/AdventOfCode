map = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}
inp = [[map[line.strip().split(' ')[0]], map[line.strip().split(' ')[1]]] for line in open("2022/day02.txt")]


def part1():
    results = [(match[0] - match[1]) % 3 for match in inp]
    
    for i in range(len(results)):
        if results[i] == 0:
            results[i] = 1
        elif results[i] == 1:
            results[i] = 0

    scores = [result * 3 + choice[1] + 1 for result, choice in zip(results, inp)]
    return sum(scores)

def part2():
    required = [(match[0] + match[1] - 1) % 3 for match in inp]
    scores = [match[1] * 3 + require + 1 for match, require in zip(inp, required)]
    return sum(scores)



print(part1())
print(part2())