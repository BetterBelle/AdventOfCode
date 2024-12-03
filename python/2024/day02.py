import itertools

input = [line for line in open("2024/day02.txt")]
REPORTS: list[list[int]] = [[int(item) for item in line.split(' ')] for line in input]
MINIMUM_SAFETY = 1
MAXIMUM_SAFETY = 3


def list_safe(report: list[int]) -> bool:
    difference = report[1] - report[0]
    is_safe = True
    for i in range(len(report) - 1):
        if not check_safe(report[i], report[i+1], difference):
            is_safe = False
            break

    return is_safe


def check_safe(first: int, second: int, difference: int) -> bool:
    current_difference = second - first

    if abs(current_difference) < MINIMUM_SAFETY or abs(current_difference) > MAXIMUM_SAFETY:
        return False

    # if the current difference and the first difference are same sign (i.e. both positive or both negative)
    # then it's positive and fine, but if they're different then it was either increasing then decreasing,
    # or decreasing then increasing. If it's 0 it's no difference and also unsafe, but that gets caught above.
    if current_difference * difference < 0:
        return False

    return True


def part1(reports: list[list[int]]) -> int:
    safe_reports = 0

    for report in reports:
        if list_safe(report):
            safe_reports += 1

    return safe_reports


def part2(reports: list[list[int]]) -> int: 
    safe_reports = 0
    
    for report in reports:
        check_lists = [list(comb) for comb in list(itertools.combinations(report, len(report) - 1))]
        check_lists.append(report)

        for new_report in check_lists:
            if list_safe(new_report):
                safe_reports += 1
                break

    return safe_reports

print(part1(REPORTS.copy()))
print(part2(REPORTS.copy()))
