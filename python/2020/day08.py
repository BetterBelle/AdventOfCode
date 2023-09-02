inp_file = open('2020/day08.txt')
temp_program = []
jmp_nop_instructions = []
nop_instructions = []

for line in inp_file:
    temp_program.append(line)

for i in range(len(temp_program)):
    if temp_program[i].split(' ')[0] == 'jmp' or temp_program[i].split(' ')[0] == 'nop':
        jmp_nop_instructions.append(i)



def run_program(program):
    instruction_pointer = 0
    acc = 0
    lines_accessed = []

    while True:
        if instruction_pointer in lines_accessed:
            return (acc, -1)
        elif instruction_pointer >= len(program):
            return (acc, 0)

        instruction, number = program[instruction_pointer].split(' ')
        number = int(number)

        if instruction == 'nop':
            lines_accessed.append(instruction_pointer)
            instruction_pointer += 1
        elif instruction == 'acc':
            lines_accessed.append(instruction_pointer)
            acc += number
            instruction_pointer += 1
        elif instruction == 'jmp':
            lines_accessed.append(instruction_pointer)
            instruction_pointer += number

    return (acc, -2)



def part1():
    return run_program(temp_program)[0]



def part2():
    for instr_to_change in jmp_nop_instructions:
        instruction = temp_program[instr_to_change].split(' ')[0]
        line_before_change = temp_program[instr_to_change]

        if instruction == 'jmp':
            temp_program[instr_to_change] = temp_program[instr_to_change].replace('jmp', 'nop')
        else:
            temp_program[instr_to_change] = temp_program[instr_to_change].replace('nop', 'jmp')

        program_value = run_program(temp_program)

        if program_value[1] == -1:
            temp_program[instr_to_change] = line_before_change
        else:
            return program_value[0]

    return program_value



print (part1())
print (part2())