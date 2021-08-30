import string

def part1(polymer):
    flag = False
    i = 1
    while i < len(polymer) - 1:
        if polymer[i].isupper():
            if polymer[i+1] == polymer[i].lower():
                polymer = polymer[:i] + polymer[i+2:]
                flag = True
        else:
            if polymer[i+1] == polymer[i].upper():
                polymer = polymer[:i] + polymer[i+2:]
                flag = True
        if i < len(polymer):
            if polymer[i].isupper():
                if polymer[i-1] == polymer[i].lower():
                    polymer = polymer[:i-1] + polymer[i+1:]
                    flag = True
            else:
                if polymer[i-1] == polymer[i].upper():
                    polymer = polymer[:i-1] + polymer[i+1:]
                    flag = True

        if flag:
            flag = False
            if i > 1:
                i -= 1
            continue
        i += 1

    return len(polymer)


def part2():
    low_alpha = string.ascii_lowercase
    high_alpha = string.ascii_uppercase
    lengths = []
    for i in range(len(low_alpha)):
        polymer = open("2018/inputs/day05.txt").read().replace(low_alpha[i], '').replace(high_alpha[i], '')
        lengths.append(part1(polymer))
    return min(lengths)


print (part1(open("2018/inputs/day05.txt").read()))
print (part2())