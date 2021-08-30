def addr(registers, values):
    registers[values[2]] = registers[values[0]] + registers[values[1]]
def addi(registers, values):
    registers[values[2]] = registers[values[0]] + values[1]
def mulr(registers, values):
    registers[values[2]] = registers[values[0]] * registers[values[1]]
def muli(registers, values):
    registers[values[2]] = registers[values[0]] * values[1]
def banr(registers, values):
    registers[values[2]] = registers[values[0]] & registers[values[1]]
def bani(registers, values):
    registers[values[2]] = registers[values[0]] & values[1]
def borr(registers, values):
    registers[values[2]] = registers[values[0]] | registers[values[1]]
def bori(registers, values):
    registers[values[2]] = registers[values[0]] | values[1]
def setr(registers, values):
    registers[values[2]] = registers[values[0]]
def seti(registers, values):
    registers[values[2]] = values[0]
def gtir(registers, values):
    if values[0] > registers[values[1]]:
        registers[values[2]] = 1
    else:
        registers[values[2]] = 0
def gtri(registers, values):
    if registers[values[0]] > values[1]:
        registers[values[2]] = 1
    else:
        registers[values[2]] = 0
def gtrr(registers, values):
    if registers[values[0]] > registers[values[1]]:
        registers[values[2]] = 1
    else:
        registers[values[2]] = 0
def eqir(registers, values):
    if values[0] == registers[values[1]]:
        registers[values[2]] = 1
    else:
        registers[values[2]] = 0
def eqri(registers, values):
    if registers[values[0]] == values[1]:
        registers[values[2]] = 1
    else:
        registers[values[2]] = 0
def eqrr(registers, values):
    if registers[values[0]] == registers[values[1]]:
        registers[values[2]] = 1
    else:
        registers[values[2]] = 0

functions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def part1():
    ans = 0
    with open("2018/inputs/day16a.txt") as inp:
        for line in inp:
            line = line.replace('\n', '')
            if "Before:" in line:
                before = [int(num) for num in line[9:-1].split(', ')]
            elif "After:" in line:
                after = [int(num) for num in line[9:-1].split(', ')]
                count = 0
                for function in functions:
                    before_copy = before.copy()
                    function(before_copy, vals)
                    if before_copy == after:
                        count += 1

                if count >= 3:
                    ans += 1
            else:
                if line != '':
                    vals = [int(num) for num in line.split(' ')]
                    vals = vals[1:]

    return ans


def part2():
    # Figure out what each opcode is
    opcodes = {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None,
        11: None,
        12: None,
        13: None,
        14: None,
        15: None
    }
    while None in opcodes.values():
        with open("2018/inputs/day16a.txt") as inp:
            for line in inp:
                line = line.replace('\n', '')
                if "Before:" in line:
                    before = [int(num) for num in line[9:-1].split(', ')]
                elif "After:" in line:
                    if opcodes[opcode] == None:
                        after = [int(num) for num in line[9:-1].split(', ')]
                        count = 0
                        for function in functions:
                            before_copy = before.copy()
                            function(before_copy, vals)
                            # If the function gives the correct value and we don't already know what opcode it is
                            if before_copy == after and not function in opcodes.values():
                                count += 1
                                correct_function = function

                        if count == 1:
                            opcodes[opcode] = correct_function
                else:
                    if line != '':
                        vals = [int(num) for num in line.split(' ')]
                        opcode = vals[0]
                        vals = vals[1:]

    # Now that I know what the opcodes are, I can do the test program
    registers = [0,0,0,0]
    with open("2018/inputs/day16b.txt") as inp:
        for line in inp:
            vals = [int(num) for num in line.split(' ')]
            opcode = vals[0]
            vals = vals[1:]
            opcodes[opcode](registers, vals)

    return registers[0]


print (part1())
print (part2())