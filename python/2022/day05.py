"""
[N] [G]                     [Q]    
[H] [B]         [B] [R]     [H]    
[S] [N]     [Q] [M] [T]     [Z]    
[J] [T]     [R] [V] [H]     [R] [S]
[F] [Q]     [W] [T] [V] [J] [V] [M]
[W] [P] [V] [S] [F] [B] [Q] [J] [H]
[T] [R] [Q] [B] [D] [D] [B] [N] [N]
[D] [H] [L] [N] [N] [M] [D] [D] [B]
 1   2   3   4   5   6   7   8   9 

These are the stacks, I hard code these because I can't be asked to parse through them properly
"""
stacks = [
    ['D','T','W','F','J','S','H','N'],
    ['H','R','P','Q','T','N','B','G'],
    ['L','Q','V'],
    ['N','B','S','W','R','Q'],
    ['N','D','F','T','V','M','B'],
    ['M','D','B','V','H','T','R'],
    ['D','B','Q','J'],
    ['D','N','J','V','R','Z','H','Q'],
    ['B','N','H','M','S']
]

inp = [line.strip() for line in open("2022/day05.txt")]
instructions = [[int(line.split(' ')[1]), int(line.split(' ')[3]) - 1, int(line.split(' ')[5]) - 1] for line in inp]

def part1():
    local_stacks = [stack.copy() for stack in stacks.copy()]
    for instruction in instructions:
        to_move = list()
        for _ in range(instruction[0]):
            to_move.append(local_stacks[instruction[1]].pop())

        local_stacks[instruction[2]].extend(to_move)

    return ''.join([stack[-1] for stack in local_stacks])

def part2():
    local_stacks = [stack.copy() for stack in stacks.copy()]
    for instruction in instructions:
        to_move = list()
        for _ in range(instruction[0]):
            to_move.append(local_stacks[instruction[1]].pop())

        to_move.reverse()
        local_stacks[instruction[2]].extend(to_move)

    return ''.join([stack[-1] for stack in local_stacks])


print(part1())
print(part2())