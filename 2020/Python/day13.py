import sys

inp_file = open('2020/inputs/day13.txt')
inp = []
for line in inp_file:
    inp.append(line.strip())

earliest = int(inp[0])
bus_ids = {int(bus_id) : 0 for bus_id in inp[1].split(',') if bus_id != 'x'}


def part1():
    for bus_id in bus_ids:
        while bus_ids[bus_id] < earliest:
            bus_ids[bus_id] += bus_id

    min_timestamp = sys.maxsize
    min_timestamp_bus = 0
    for bus_id in bus_ids:
        if bus_ids[bus_id] < min_timestamp:
            min_timestamp = bus_ids[bus_id]
            min_timestamp_bus = bus_id

    return min_timestamp_bus * (min_timestamp - earliest)

def part2():
    pass



print (part1())
print (part2())
