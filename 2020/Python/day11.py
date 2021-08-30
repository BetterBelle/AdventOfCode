inp_file = open('2020/inputs/day11.txt')
seats = []
for line in inp_file:
    seats.append(line.strip())


def part1():
    current_seats = []
    next_seats = []
    answer = 0
    for line in seats:
        current_seats.append(line)

    while current_seats != next_seats:
        if next_seats != []:
            current_seats = next_seats

        next_seats = []
        for row in range(len(current_seats)):
            next_row = ''
            for column in range(len(current_seats[row])):
                if current_seats[row][column] == '.':
                    next_row += '.'
                    continue

                num_adj_seats = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dy == dx == 0:
                            continue
                        if 0 <= row + dy < len(current_seats) and 0 <= column + dx < len(current_seats[row]):
                            if current_seats[row + dy][column + dx] == "#":
                                num_adj_seats += 1

                if current_seats[row][column] == 'L' and num_adj_seats == 0:
                    next_row += '#'
                elif current_seats[row][column] == '#' and num_adj_seats >= 4:
                    next_row += 'L'
                else:
                    next_row += current_seats[row][column]

            next_seats.append(next_row)

    for line in current_seats:
        answer += line.count('#')
                
    return answer


def part2():
    current_seats = []
    next_seats = []
    answer = 0
    for line in seats:
        current_seats.append(line)

    while current_seats != next_seats:
        if next_seats != []:
            current_seats = next_seats

        next_seats = []
        for row in range(len(current_seats)):
            next_row = ''
            for column in range(len(current_seats[row])):
                if current_seats[row][column] == '.':
                    next_row += '.'
                    continue

                num_close_seats = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        increment = 1
                        if dx == 0 and dy == 0:
                            continue

                        while 0 <= row + dy * increment < len(current_seats) and 0 <= column + dx * increment < len(current_seats[row]):
                            if current_seats[row + dy * increment][column + dx * increment] == "#":
                                num_close_seats += 1
                                break
                            elif current_seats[row + dy * increment][column + dx * increment] == "L":
                                break
                            increment += 1

                if current_seats[row][column] == 'L' and num_close_seats == 0:
                    next_row += '#'
                elif current_seats[row][column] == '#' and num_close_seats >= 5:
                    next_row += 'L'
                else:
                    next_row += current_seats[row][column]

            next_seats.append(next_row)

    for line in current_seats:
        answer += line.count('#')
                
    return answer



print (part1())
print (part2())