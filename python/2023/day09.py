import re
import functools

input_contents = [list(map(int, re.findall('-?[0-9]+', line.strip()))) for line in open("2023/day09.txt")]
input = []
for history in input_contents:
    all_diffs = [history]
    new_diffs = history
    while not all(i == 0 for i in new_diffs):
        new_diffs = [new_diffs[i+1] - new_diffs[i] for i in range(len(new_diffs) - 1)]
        all_diffs.append(new_diffs)

    input.append(all_diffs)

def part1(input):
    lasts = [[diff[-1] for diff in all_diffs] for all_diffs in input]
    return sum([sum(last) for last in lasts])

def part2(input):
    firsts = [[diff[0] for diff in all_diffs] for all_diffs in input]
    return sum([functools.reduce(lambda acc, val: val - acc, reversed(first)) for first in firsts])

print(part1(input))
print(part2(input))
