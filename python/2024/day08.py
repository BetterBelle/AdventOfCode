MAP: list[str] = [line.strip() for line in open("2024/day08.txt")]
MAX_I: int = len(MAP)
MAX_J: int = len(MAP[0])


class Antenna():
    def __init__(self, i_coord: int, j_coord: int):
        self.i_coord = i_coord
        self.j_coord = j_coord

    def __eq__(self, other):
        if self.i_coord == other.i_coord and self.j_coord == other.j_coord:
            return True
        return False

    def __hash__(self):
        return hash((self.i_coord, self.j_coord))


class AntiNode(Antenna):
    def in_bounds(self):
        if self.i_coord >= 0 and self.i_coord < MAX_I and self.j_coord >= 0 and self.j_coord < MAX_J:
            return True 
        return False


def generate_antennas() -> dict[str]:
    antennas: dict[str] = {}
    for i, line in enumerate(MAP):
        for j, antenna in enumerate(line):
            if antenna != '\n' and antenna != '.':
                if antenna not in antennas:
                    antennas[antenna] = []
                antennas[antenna].append(Antenna(i, j))

    return antennas


def generate_antinodes(antennas: list[Antenna]) -> set[AntiNode]:
    new_antinodes = set()
    for i, antenna in enumerate(antennas):
        for other in antennas[i+1:]:
            # antenna diffs
            i_diff = other.i_coord - antenna.i_coord
            j_diff = other.j_coord - antenna.j_coord
            
            # create antinodes above and below
            above_antinode = AntiNode(antenna.i_coord - i_diff, antenna.j_coord - j_diff)
            below_antinode = AntiNode(other.i_coord + i_diff, other.j_coord + j_diff)

            # add them to new antinodes if in bounds
            if above_antinode.in_bounds():
                new_antinodes.add(above_antinode)
            if below_antinode.in_bounds():
                new_antinodes.add(below_antinode)

    return new_antinodes


def generate_resonant_antinodes(antennas: list[Antenna]) -> set[AntiNode]:
    new_antinodes = set()
    for i, antenna in enumerate(antennas):
        for other in antennas[i+1:]:
            # antenna diffs
            i_diff = other.i_coord - antenna.i_coord
            j_diff = other.j_coord - antenna.j_coord
            
            # create antinodes above and below
            above_antinode = AntiNode(antenna.i_coord, antenna.j_coord)
            below_antinode = AntiNode(other.i_coord, other.j_coord)

            # resonate; create nodes in the same direction until out of bounds
            while above_antinode.in_bounds():
                new_antinodes.add(above_antinode)
                above_antinode = AntiNode(above_antinode.i_coord - i_diff, above_antinode.j_coord - j_diff)

            while below_antinode.in_bounds():
                new_antinodes.add(below_antinode)
                below_antinode = AntiNode(below_antinode.i_coord + i_diff, below_antinode.j_coord + j_diff)

    return new_antinodes

    
def num_unique_antinodes() -> (int, int):
    antinodes_part_1: list[AntiNode] = set()
    antinodes_part_2: list[AntiNode] = set()
    antennas: dict[str] = generate_antennas()

    # create AntiNode without resonance
    for antenna_type in antennas:
        antinodes_part_1 |= generate_antinodes(antennas[antenna_type])

    # create AntiNodes with resonance
    for antenna_type in antennas:
        antinodes_part_2 |= generate_resonant_antinodes(antennas[antenna_type])

    return (len(antinodes_part_1), len(antinodes_part_2))

#part
print(num_unique_antinodes())
