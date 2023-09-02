inp = open("2020/day01.txt")
numbers_list = []
for line in inp:
    numbers_list.append(int(line))


def part1():
    numbers_list.sort()
    start_iter = 0
    end_iter = len(numbers_list) - 1

    while numbers_list[start_iter] + numbers_list[end_iter] != 2020:
        if numbers_list[start_iter] + numbers_list[end_iter] < 2020:
            start_iter += 1
        elif numbers_list[start_iter] + numbers_list[end_iter] > 2020:
            end_iter -= 1

    return numbers_list[start_iter] * numbers_list[end_iter]


def part2():
    numbers_list.sort()
    start_iter = 0
    fix_iter = 1
    end_iter = len(numbers_list) - 1

    while numbers_list[start_iter] + numbers_list[fix_iter] + numbers_list[end_iter] != 2020:
        if numbers_list[start_iter] + numbers_list[fix_iter] + numbers_list[end_iter] < 2020:
            start_iter += 1
        elif numbers_list[start_iter] + numbers_list[fix_iter] + numbers_list[end_iter] > 2020:
            end_iter -= 1
        if start_iter == fix_iter or end_iter == fix_iter:
            start_iter = 0
            fix_iter += 1
            end_iter = len(numbers_list) - 1

    return numbers_list[start_iter] * numbers_list[fix_iter] * numbers_list[end_iter]


print (part1())
print (part2())