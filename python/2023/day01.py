import regex as re

input = [line for line in open("2023/day01.txt")]

MATCHER = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        }


def get_num(string: str) -> int:
    if string.isdigit():
        return int(string)
    
    return MATCHER[string]


def process(regex_str: str, line: str) -> int:
    digits: list[str] = re.findall(regex_str, line, overlapped=True)
    return get_num(digits[0]) * 10 + get_num(digits[-1])


def part1() -> str:
    sum = 0
    for line in input:
        sum += process("[0-9]", line) 

    return str(sum)

def part2() -> str: 
    sum = 0

    for line in input:
        sum += process("[0-9]|one|two|three|four|five|six|seven|eight|nine", line)

    return str(sum)


print(part1())
print(part2())
