input = [line for line in open("2024/day01.txt")]
FIRST_LIST = [int(line.split('   ')[0]) for line in input]
SECOND_LIST = [int(line.split('   ')[1]) for line in input]


def part1(first_list: list[int], second_list: list[int]) -> int:
    dist_score = 0
    
    while len(first_list) != 0 and len(second_list) != 0:
        dist_score += abs(min(first_list) - min(second_list))
        first_list.remove(min(first_list))
        second_list.remove(min(second_list))

    return dist_score


def part2(first_list: list[int], second_list: list[int]) -> int: 
    simi_score = 0

    for item in first_list:
        simi_score += item * second_list.count(item)

    return simi_score

print(part1(FIRST_LIST.copy(), SECOND_LIST.copy()))
print(part2(FIRST_LIST.copy(), SECOND_LIST.copy()))
