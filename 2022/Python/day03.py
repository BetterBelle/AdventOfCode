inp = [line.strip() for line in open("2022/inputs/day03.txt")]

def get_val(char):
    return ord(char) - ord('a') + 1 if char.islower() else ord(char) - ord('A') + 27

def part1():
    sum_prios = 0
    for bag in inp:
        bag1, bag2 = bag[:len(bag)//2], bag[len(bag)//2:]
        found, = set(bag1) & set(bag2)
        sum_prios += get_val(found)

    return sum_prios

def part2():
    sum_prios = 0
    for i in range(0, len(inp), 3):
        elf1, elf2, elf3 = inp[i:i+3]
        found, = set(elf1) & set(elf2) & set(elf3)
        sum_prios += get_val(found)

    return sum_prios


print(part1())
print(part2())