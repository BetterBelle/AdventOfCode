inp_file = open('2020/day12.txt')
directions = []
for line in inp_file:
    line = line.strip()
    directions.append((line[0], int(line[1:])))

cards = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3,
}

card_vals = {
    0: (0, 1), # North
    1: (1, 0), # East
    2: (0, -1),# South
    3: (-1, 0),# West
}

class Ferry():
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.facing = 1
        self.waypointx = 10
        self.waypointy = 1

    def move_ferry(self, direction, value):
        self.posx += card_vals[direction][0] * value
        self.posy += card_vals[direction][1] * value
    
    def move_waypoint(self, direction, value):
        self.waypointx += card_vals[direction][0] * value
        self.waypointy += card_vals[direction][1] * value

    def move_ferry_forward(self, value):
        self.move_ferry(self.facing, value)

    def rotate_ferry(self, orientation, value):
        rotate_amount = value // 90
        if orientation == 'R':
            self.facing = (self.facing + rotate_amount) % 4
        else:
            self.facing = (self.facing - rotate_amount) % 4

    def rotate_waypoint(self, orientation, value):
        rotate_amount = value // 90
        if orientation == 'R':
            for _ in range(rotate_amount):
                hold = self.waypointx
                self.waypointx = self.waypointy
                self.waypointy = - hold
        else:
            for _ in range(rotate_amount):
                hold = self.waypointx
                self.waypointx = - self.waypointy
                self.waypointy = hold

    def move_to_waypoint(self, times):
        for _ in range(times):
            self.posx += self.waypointx
            self.posy += self.waypointy

    def __repr__(self):
        return "Ferry[x: " + str(self.posx) + ", y: " + str(self.posy) + ", facing: " + str(self.facing) + "]"


def part1():
    ferry = Ferry()
    for direction in directions:
        if direction[0] == 'F':
            ferry.move_ferry_forward(direction[1])
        elif direction[0] == 'R' or direction[0] == 'L':
            ferry.rotate_ferry(direction[0], direction[1])
        else:
            ferry.move_ferry(cards[direction[0]], direction[1])

    return abs(ferry.posx) + abs(ferry.posy)


def part2():
    ferry = Ferry()
    for direction in directions:
        if direction[0] == 'F':
            ferry.move_to_waypoint(direction[1])
        elif direction[0] == 'R' or direction[0] == 'L':
            ferry.rotate_waypoint(direction[0], direction[1])
        else:
            ferry.move_waypoint(cards[direction[0]], direction[1])

    return abs(ferry.posx) + abs(ferry.posy)


print (part1())
print (part2())