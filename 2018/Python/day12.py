def calculate_sum(state, offset):
    sum = 0
    for i in range(len(state)):
        if state[i] == '#':
            sum += i - offset

    return sum

def calculate_gen(gens, rules, pots):
    for _ in range(gens):
        nextGen = '..'

        for j in range(len(pots) - 5):
            current = pots[j:j+5]
            for rule in rules:
                if current == rule[0]:
                    nextGen += rule[1]
                    break

        pots = nextGen + '....'

    return pots

def find_pattern(pots,rules,offset):
    last_pots = pots
    for i in range(1,140):
        new_pots = calculate_gen(1,rules,last_pots)
        print (calculate_sum(new_pots,offset) - calculate_sum(last_pots,offset), ':', i, ':', calculate_sum(new_pots,offset))
        last_pots = new_pots

def main():
    pots = "#...#####.#..##...##...#.##.#.##.###..##.##.#.#..#...###..####.#.....#..##..#.##......#####..####..."
    offset = 2

    # Creating starting state
    for _ in range(offset):
        pots += '.'
        pots = '.' + pots

    # Creating array of rule => new state
    in_put = open('2018/inputs/day12.txt')
    rules = []
    for line in in_put:
        if line[0] == '.' or line[0] == '#':
            rules.append((line[:5],line[9]))
    
    '''
    Find where pattern emerges manually
    find_pattern(pots,rules,offset)
    sum: 11873, gen: 134, pattern: +86
    '''

    pots = calculate_gen(20,rules,pots)
    print (calculate_sum(pots,offset))
    print (11873 + (50000000000 - 134) * 86)


if __name__ == '__main__':
    main()