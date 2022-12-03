inp = [line.strip() for line in open("2022/inputs/day03.txt")]

prios = list()
for line in inp:
    next_prios = list()
    for char in line:
        if ord(char) >= 97:
            next_prios.append(ord(char) - 96)
        else:
            next_prios.append(ord(char) - 38)

    prios.append(next_prios)

def part1():
    sum_prios = 0
    next_found = 0
    for prio in prios:
        sack1, sack2 = prio[:int(len(prio)/2)], prio[int(len(prio)/2):]
        for item in sack1:
            if item in sack2:
                next_found = item

        sum_prios += next_found

    return sum_prios

def part2():
    sum_prios = 0
    next_found = 0
    next_group = list()
    for prio in prios:
        next_group.append(prio)

        if len(next_group) == 3:
            for item in next_group[0]:
                if item in next_group[1] and item in next_group[2]:
                    next_found = item
                    
            sum_prios += next_found
            next_group = list()

    return sum_prios


print(part1())
print(part2())