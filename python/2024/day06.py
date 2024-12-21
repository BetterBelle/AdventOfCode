import cmath
input: list[list[str]] = [list(line.strip()) for line in open("2024/day06.txt")]
START_I: int 
START_J: int

for i, line in enumerate(input):
    for j, char in enumerate(line):
        if char != '#' and char != '.':
            START_I = i
            START_J = j
            input[i][j] = '.'

class Guard:
    def __init__(self, i_pos: int, j_pos: int):
        # complex value gives row, real value gives column
        self._position: complex = complex(j_pos, i_pos)
        # facing up, basically reflected along the real axis
        self._direction: complex = complex(0, -1)

    @property 
    def position(self) -> complex:
        return self._position

    @property
    def i_pos(self) -> int:
        return int(self._position.imag)

    @property
    def j_pos(self) -> int:
        return int(self._position.real)

    def move(self):
        self._position += self._direction

    def next_position(self) -> complex:
        return self._position + self._direction

    @property 
    def direction(self) -> complex:
        return self._direction

    def rotate(self):
        # rotate counter clockwise (clockwise on the mirrored map because -i goes up, not down)
        self._direction *= complex(0, 1)

    def traverse_map(self, map) -> (set, bool):
        visited: set = set()
        visited.add((self.position, self.direction))
        looped = False

        while True:
            next_position = self.next_position()
            if next_position.real < 0 or next_position.real >= len(map):
                break
            elif next_position.imag < 0 or next_position.imag >= len(map[self.i_pos]):
                break
            elif map[int(next_position.imag)][int(next_position.real)] == '#':
                self.rotate()
                continue

            self.move()
            if (self.position, self.direction) in visited:
                looped = True
                break
            else:
                visited.add((self.position, self.direction))

        return (visited, looped)


def part1(map: list[list[str]]) -> int:
    guard: Guard = Guard(START_I, START_J)
    visited, looped = guard.traverse_map(map)
    visited = set([step[0] for step in visited])

    return len(visited)


def part2(map: list[list[str]]) -> int: 
    num_loops: int = 0
    # obstacles can only be put on the original path to cause a loop because otherwise
    # the guard wouldn't reach it. so first, trace out the path, then go through
    # each position along that path and add obstacles to see if it causes a loop

    guard: Guard = Guard(START_I, START_J)
    original_path, looped = guard.traverse_map(map)
    original_path = set([step[0] for step in original_path])

    for position in original_path:
        map[int(position.imag)][int(position.real)] = '#'

        guard = Guard(START_I, START_J)
        visited, looped = guard.traverse_map(map)
        if looped:
            num_loops += 1

        map[int(position.imag)][int(position.real)] = '.'

    return num_loops


print(part1(input.copy()))
print(part2(input.copy()))
