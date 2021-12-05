inp = open("2021/inputs/day05.txt")

class Vent():
    def __init__(self, point1, point2):
        self.line = []
        self.diag = False
        if point1[0] > point2[0]:
            point1, point2 = point2, point1
        
        dy = point2[1] - point1[1]
        dx = point2[0] - point1[0]
        if dy == 0:
            self.line = [(x, point1[1]) for x in range(point1[0], point2[0] + 1)]
        elif dx == 0:
            if point1[1] > point2[1]:
                point1, point2 = point2, point1
            self.line = [(point1[0], y) for y in range(point1[1], point2[1] + 1)]
        else:
            self.diag = True
            xs = [x for x in range(point1[0], point2[0] + 1)]
            if point1[1] > point2[1]:
                ys = [y for y in range(point1[1], point2[1] - 1, -1)]
            else:
                ys = [y for y in range(point1[1], point2[1] + 1)]

            for i in range(len(xs)):
                self.line.append((xs[i], ys[i]))

vents = []
for line in inp:
    points = line.split(' ')
    vents.append(Vent([int(n) for n in points[0].split(',')], [int(n) for n in points[2].split(',')]))

map = [[0 for _ in range(1000)] for _ in range(1000)]

def part1():
    for vent in vents:
        if not vent.diag:
            for point in vent.line:
                map[point[0]][point[1]] += 1

    ans = 0
    for col in map:
        for point in col:
            if point > 1:
                ans += 1

    return ans


def part2():
    for vent in vents:
        if vent.diag:
            for point in vent.line:
                map[point[0]][point[1]] += 1

    ans = 0
    for col in map:
        for point in col:
            if point > 1:
                ans += 1

    return ans


print (part1())
print (part2())