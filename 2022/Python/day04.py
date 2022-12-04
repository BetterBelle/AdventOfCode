inp = [line.strip() for line in open("2022/inputs/day04.txt")]
assign_pairs = [line.split(',') for line in inp]
jobs = [[set(range(int(elf.split('-')[0]), int(elf.split('-')[1])+1)) for elf in pair] for pair in assign_pairs]


def part1():
    fully_contained = 0
    for job in jobs:
        fully_contained += 1 if len(job[0] & job[1]) == min(len(job[0]), len(job[1])) else 0

    return fully_contained

def part2():
    overlapping = 0
    for job in jobs:
        overlapping += 1 if len(job[0] & job[1]) > 0 else 0

    return overlapping


print(part1())
print(part2())