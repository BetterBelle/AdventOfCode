inp = open("2020/inputs/day03.txt")
slope = []

for line in inp:
    slope.append(line.strip())

MOD_NUMBER = len(slope[0])


def count_trees(width_increment, height_increment):
    num_trees = 0
    width = 0
    height = 0

    while height < len(slope) - 1:
        width = (width + width_increment) % MOD_NUMBER
        height += height_increment

        if slope[height][width] == '#':
            num_trees += 1
    
    return num_trees
    

def part1():
    return count_trees(3, 1)


def part2():
    num_trees = [count_trees(1, 1), count_trees(3, 1), count_trees(5, 1), count_trees(7, 1), count_trees(1, 2)]

    answer = 1
    for tree_count in num_trees:
        answer *= tree_count
        
    return answer


print(part1())
print(part2())