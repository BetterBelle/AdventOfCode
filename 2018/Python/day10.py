points = []
with open("2018/inputs/day10.txt") as inp:
    for line in inp:
        position = (int(line.split(", ")[0][10:]), int(line.split(", ")[1].split(">")[0]))
        velocity = (int(line.split(", ")[1].split("<")[1]), int(line.split(", ")[2].replace(">", "")))
        points.append([position, velocity])

def bounded():
    ys = []
    for point in points:
        ys.append(point[0][1])

    return abs(max(ys) - min(ys)) < 12


def both_parts():
    was_bounded = False
    iterations = 0
    while True:
        if not bounded():
            for point in points:
                point[0] = (point[0][0] + point[1][0], point[0][1] + point[1][1])

        elif was_bounded:
            iterations -= 1
            break

        else:
            was_bounded = True
            max_y = 0
            max_x = 0
            for point in points:
                if point[0][0] > max_x:
                    max_x = point[0][0]
                if point[0][1] > max_y:
                    max_y = point[0][1]

            sky = [['.' for i in range(max_y + 1)] for j in range(max_x + 1)]
            for point in points:
                sky[point[0][0]][point[0][1]] = '#'

            for i in range(len(sky[0])):
                row = ''
                for j in range(len(sky)):
                    row += sky[j][i]
                print (row)

        iterations += 1

    return iterations


print (both_parts())