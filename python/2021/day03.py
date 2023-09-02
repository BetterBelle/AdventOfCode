inp = open("2021/day03.txt")
diagnostics = [int(line, 2) for line in inp]

def part1():
    compare = 0b100000000000
    gamma = 0
    epsilon = 0

    while compare > 0:
        count = [0, 0]
        for diag in diagnostics:
            if diag & compare:
                count[1] += 1
            else:
                count[0] += 1

        if count[1] > count[0]:
            gamma = gamma ^ compare
        else:
            epsilon = epsilon ^ compare

        compare = compare >> 1

    return gamma * epsilon


def part2():
    compare = 0b100000000000
    oxygen_diags = diagnostics

    while compare > 0 and len(oxygen_diags) > 1:
        ones = []
        zeros = []

        for diag in oxygen_diags:
            if diag & compare:
                ones.append(diag)
            else:
                zeros.append(diag)

        if len(ones) >= len(zeros):
            oxygen_diags = ones
        else:
            oxygen_diags = zeros
        
        compare = compare >> 1

    compare = 0b100000000000
    co2_diags = diagnostics

    while compare > 0 and len(co2_diags) > 1:
        ones = []
        zeros = []

        for diag in co2_diags:
            if diag & compare:
                ones.append(diag)
            else:
                zeros.append(diag)

        if len(ones) < len(zeros):
            co2_diags = ones
        else:
            co2_diags = zeros
        
        compare = compare >> 1

    return oxygen_diags[0] * co2_diags[0]



print (part1())
print (part2())