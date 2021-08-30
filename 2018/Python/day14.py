def part1():
    inp = int(open("2018/inputs/day14.txt").read())
    scores = '37'
    elf1 = 0
    elf2 = 1

    for _ in range(inp + 10):
        scores += str(int(scores[elf1]) + int(scores[elf2]))
        elf1 = (elf1 + int(scores[elf1]) + 1) % len(scores)
        elf2 = (elf2 + int(scores[elf2]) + 1) % len(scores)

    ans = ''
    for score in scores[inp:inp+10]:
        ans += str(score)

    return ans


def part2():
    inp = open("2018/inputs/day14.txt").read()
    scores = '37'
    elf1 = 0
    elf2 = 1

    while inp not in scores[-7:]:
        scores += str(int(scores[elf1]) + int(scores[elf2]))
        elf1 = (elf1 + int(scores[elf1]) + 1) % len(scores)
        elf2 = (elf2 + int(scores[elf2]) + 1) % len(scores)

    return scores.index(inp)


print (part1())
print (part2())