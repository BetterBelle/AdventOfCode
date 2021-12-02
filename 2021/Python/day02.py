inp = open("2021/inputs/day02.txt")
instructions = list()

for line in inp:
    inst = line.split(' ')
    instructions.append((inst[0], int(inst[1])))

class Submarine():
    def __init__(self):
        self.depth = 0
        self.position = 0

    def move(self, instruction):
        if instruction[0] == 'forward':
            self.position += instruction[1]
        elif instruction[0] == 'down':
            self.depth += instruction[1]
        else:
            self.depth -= instruction[1]

    def result(self):
        return self.depth * self.position


class ComplexSubmarine(Submarine):
    def __init__(self):
        super(ComplexSubmarine, self).__init__()
        self.aim = 0

    def move(self, instruction):
        if instruction[0] == 'forward':
            self.position += instruction[1]
            self.depth += instruction[1] * self.aim
        elif instruction[0] == 'down':
            self.aim += instruction[1]
        else:
            
            self.aim -= instruction[1]

def part1():
    sub = Submarine()
    for instruction in instructions:
        sub.move(instruction)

    return sub.result()


def part2():
    sub = ComplexSubmarine()
    for instruction in instructions:
        sub.move(instruction)

    return sub.result()


print (part1())
print (part2())