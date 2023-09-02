import string

def count_occurences(char, s):
    count = 0
    for element in s:
        if char == element:
            count += 1

    return count


def part1():
    twos = 0
    threes = 0
    alphabet = string.ascii_lowercase
    with open("2018/day02.txt") as inp:
        for line in inp:
            two_flag = False
            three_flag = False
            for char in alphabet:
                if count_occurences(char, line) == 2 and not two_flag:
                    two_flag = True
                    twos += 1
                if count_occurences(char, line) == 3 and not three_flag:
                    three_flag = True
                    threes += 1
                if three_flag and two_flag:
                    break

    return twos * threes


def part2():
    inp = open("2018/day02.txt")
    box_ids = [line for line in inp]
    correct_ids = None
    for i in range(len(box_ids)-1):
        for j in range(i+1, len(box_ids)):
            diff_chars = 0
            for k in range(len(box_ids[i])):
                if box_ids[i][k] != box_ids[j][k]:
                    diff_chars += 1
                if diff_chars > 1:
                    break
            if diff_chars == 1:
                correct_ids = (box_ids[i], box_ids[j])
                break
        if correct_ids != None:
            break

    correct_str = ""
    for i in range(len(correct_ids[0])):
        if correct_ids[0][i] == correct_ids[1][i]:
            correct_str += correct_ids[0][i]
            
    return correct_str


print (part1())
print (part2())