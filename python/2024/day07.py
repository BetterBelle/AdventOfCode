import re
ADD, MUL, CAT = [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(str(x) + str(y))]
EQUATIONS: list[list[int]] = [[int(num) for num in re.findall('[0-9]+', line.strip())] for line in open("2024/day07.txt")]

def evaluate(equation, operations):
    solution, first, *operands = equation
    temp_solutions = [first]
    for operand in operands:
        temp_solutions = [op(temp_solution, operand) for temp_solution in temp_solutions for op in operations]

    return solution in temp_solutions

print(sum([equation[0] * evaluate(equation, [ADD, MUL]) for equation in EQUATIONS]))
print(sum([equation[0] * evaluate(equation, [ADD, MUL, CAT]) for equation in EQUATIONS]))
