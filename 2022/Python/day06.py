inp = [line.strip() for line in open("2022/inputs/day06.txt")][0]

def part1():
    answer = 0
    for i in range(len(inp) - 3):
        current = inp[i:i+4]
        if len(set(current)) == len(current) and answer == 0:
            answer = i + 4

    return answer

def part2():
    answer = 0
    for i in range(len(inp) - 13):
        current = inp[i:i+14]
        if len(set(current)) == len(current) and answer == 0:
            answer = i + 14

    return answer

print(part1())
print(part2())