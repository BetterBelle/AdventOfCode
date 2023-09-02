inp = open("2021/day01.txt")
measurements = list()

for line in inp:
    measurements.append(int(line))

def part1():
    ans = 0
    for i in range(1, len(measurements)):
        if measurements[i - 1] < measurements[i]:
            ans += 1

    return ans


def part2():
    ans = 0
    for i in range(1, len(measurements) - 2):
        prev = sum(measurements[i-1:i+2])
        curr = sum(measurements[i:i+3])
        if prev < curr:
            ans += 1
            
    return ans


print (part1())
print (part2())