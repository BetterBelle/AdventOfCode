import cmath
input = [line.strip() for line in open("2024/day06.txt")]

class Guard:
    def __init__(self, i_pos: int, j_pos: int):
        self._position: complex = complex(i_pos, j_pos)
        self._direction: complex = complex(0, 1)

    @property 
    def position(self) -> complex:
        return self._position

    @property
    def i_pos(self) -> int:
        return int(self._position.real)

    @property
    def j_pos(self) -> int:
        return int(self._position.imag)

    def move(self):
        self._position += self._direction

    def next_position(self) -> complex:
        return self._position + self._direction

    @property 
    def direction(self) -> complex:
        return self._direction

    def rotate(self):
        self._direction *= complex(0, -1)


def part1(map: list[str]) -> int:
    visited: set = set()
    # find guard 
    guard: Guard = None
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            print(char)
            if char != '#' and char != '.':
                guard = Guard(i, j) 
                visited.add(guard._position)
                
    # guard moves around
    while True:
        print(guard.position)
        print(guard.direction)
        next_position = guard.next_position()
        if next_position.real < 0 or next_position.real >= len(map):
            break
        elif next_position.imag < 0 or next_position.imag >= len(map[guard.i_pos]):
            break

        if map[int(next_position.real)][int(next_position.imag)] == '#':
            print('ROTATE')
            # rotate clockwise
            guard.rotate()
            print(guard.position)
            print(guard.direction)
        else:
            guard.move()
            visited.add(guard.position)

    return len(visited)


def part2(map: list[str]) -> int: 
    pass

print(part1(input.copy()))
print(part2(input.copy()))
