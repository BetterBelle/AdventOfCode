# Create dictionary containing all coordinates
coordinates = {}
with open("2018/inputs/day06.txt") as inp:
    i = 0
    for line in inp:
        coordinates[i] = (int(line.split(", ")[0]), int(line.split(", ")[1]))
        i += 1


# Create the 2d list of tuples (closest_coordinate, sum_of_distances)
# Where -1 is a tie for closest_coordinate
AREA_SIZE = 500
play_area = [[[-1, 0] for i in range(AREA_SIZE)] for j in range(AREA_SIZE)]
for i in range(len(play_area)):
    for j in range(len(play_area[i])):
        distances = []
        for k in coordinates:
            distance = abs(i - coordinates[k][0]) + abs(j - coordinates[k][1])
            play_area[i][j][1] += distance
            
            if len(distances) == 0:
                play_area[i][j][0] = k
            elif distance == min(distances):
                play_area[i][j][0] = -1
            elif distance < min(distances):
                play_area[i][j][0] = k

            distances.append(distance)


def part1():
    infinite_areas = [-1]

    # Left side
    for left in play_area[0]:
        if not left[0] in infinite_areas:
            infinite_areas.append(left[0])

    # Right side
    for right in play_area[-1]:
        if not right[0] in infinite_areas:
            infinite_areas.append(right[0])

    # Top and bottom
    for col in play_area:
        if not col[0][0] in infinite_areas:
            infinite_areas.append(col[0][0])
        if not col[-1][0] in infinite_areas:
            infinite_areas.append(col[-1][0])

    # Non infinite areas
    finite_areas = {}
    for coor in coordinates:
        if not coor in infinite_areas:
            finite_areas[coor] = 0

    for i in range(len(play_area)):
        for j in range(len(play_area[i])):
            if play_area[i][j][0] in finite_areas:
                finite_areas[play_area[i][j][0]] += 1

    ans = 0
    for area in finite_areas:
        if finite_areas[area] > ans:
            ans = finite_areas[area]
            
    return ans


def part2():
    ans = 0
    for i in range(len(play_area)):
        for j in range(len(play_area[i])):
            if play_area[i][j][1] < 10000:
                ans += 1
    return ans


print (part1())
print (part2())