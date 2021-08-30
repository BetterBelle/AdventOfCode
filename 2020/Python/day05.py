inp = open('2020/inputs/day05.txt')
boarding_passes = []
for line in inp:
    boarding_passes.append(line)

def get_seat_ids():
    seat_ids = []
    for boarding_pass in boarding_passes:
        seatrow = [0, 127]
        seatcol = [0, 7]
        for char in boarding_pass:
            if char == 'F':
                seatrow = [seatrow[0], seatrow[1] - int((seatrow[1] - seatrow[0]) / 2 + 1)]
            if char == 'B':
                seatrow = [seatrow[0] + int((seatrow[1] - seatrow[0]) / 2 + 1), seatrow[1]]
            if char == 'R':
                seatcol = [seatcol[0] + int((seatcol[1] - seatcol[0]) / 2 + 1), seatcol[1]]
            if char == 'L':
                seatcol = [seatcol[0], seatcol[1] - int((seatcol[1] - seatcol[0]) / 2 + 1)]
        
        seat_ids.append(seatrow[0] * 8 + seatcol[0])

    return seat_ids

def part1():
    return max(get_seat_ids())

def part2():
    seat_ids = get_seat_ids()
    seat_ids.sort()

    my_seat_id = 0
    for i in range(1, len(seat_ids)):
        if seat_ids[i] - seat_ids[i-1] > 1:
            my_seat_id = seat_ids[i] - 1

    return my_seat_id

print(part1())
print(part2())