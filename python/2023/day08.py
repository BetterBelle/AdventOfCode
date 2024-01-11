import re
import numpy as np

input_contents: list[str] = [line.strip() for line in open("2023/day08.txt")]
instructions: list[int] = [0 if instr == 'L' else 1 for instr in input_contents[0]]
map: dict[str, tuple[str, str]] = {str(line[0]): (str(line[1]), str(line[2])) for line in [re.findall('[A-Z][A-Z][A-Z]', line) for line in input_contents[2:]]}

def part1(instructions: list[int], map: dict[str, tuple[str, str]]) -> int:
    current: str = 'AAA'
    step: int = 0

    while current != 'ZZZ':
        current = map[current][instructions[step % len(instructions)]]
        step += 1

    return step

def part2(instructions: list[int], map: dict[str, tuple[str, str]]) -> int:
    currents: list[str] = [node for node in map if node[2] == 'A']
    loops: list[int] = [0 for _ in range(len(currents))]
    step: int = 0

    while np.count_nonzero(loops) < len(loops):
        for i, current in enumerate(currents):
            currents[i] = map[current][instructions[step % len(instructions)]]
            if currents[i][2] == 'Z' and loops[i] == 0:
                loops[i] = step + 1

        step += 1

    return np.lcm.reduce(loops)

print(part1(instructions, map))
print(part2(instructions, map))
