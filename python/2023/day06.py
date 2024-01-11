import re
from functools import reduce
input = [line.strip() for line in open("2023/day06.txt")]

def part1(input):
    times = [int(item) for item in re.findall('[0-9]+', input[0])]
    distances = [int(item) for item in re.findall('[0-9]+', input[1])]
    wins = []

    for time, distance in zip(times, distances):
        speed = 0
        temp_total = 0
        for i in range(1, time):
            speed += 1
            boat_distance = speed * (time - i)
            if boat_distance > distance:
                temp_total += 1

        wins.append(temp_total)

    return reduce(lambda x, y: x*y, wins)

def part2(input):
    time = int("".join(re.findall('[0-9]+', input[0])))
    distance = int("".join(re.findall('[0-9]+', input[1])))

    speed = 0
    num_wins = 0
    for i in range(1, time):
        speed += 1
        boat_distance = speed * (time - i)
        if boat_distance > distance:
            num_wins += 1


    return num_wins

print(part1(input))
print(part2(input))
