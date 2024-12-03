import re
input = [line for line in open("2024/day03.txt")]

def part1(corrupted_mem: list[str]) -> int:
    result = 0

    for mem_line in corrupted_mem:
        matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', mem_line)

        for match in matches:
            a, b = (int(item) for item in re.findall(r'[0-9]{1,3}', match))
            result += a * b

    return result


def part2(corrupted_mem: list[str]) -> int: 
    result = 0
    enabled = True

    for mem_line in corrupted_mem:
        matches = re.findall(r'do\(\)|don\'t\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)', mem_line)

        for match in matches:
            if match == 'do()':
                enabled = True
            elif match == 'don\'t()':
                enabled = False
            elif enabled:
                a, b = (int(item) for item in re.findall(r'[0-9]{1,3}', match))
                result += a * b


    return result

print(part1(input.copy()))
print(part2(input.copy()))
