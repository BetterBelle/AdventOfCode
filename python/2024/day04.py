input = [line for line in open("2024/day04.txt")]

def scan_word(word_search: list[str], direction: str, i: int, j: int) -> int:
    i_diff = 0
    j_diff = 0
    word_to_find = 'XMAS'

    
    if 'left' in direction:
        j_diff = -1
    if 'right' in direction:
        j_diff = 1
    if 'top' in direction:
        i_diff = -1
    if 'bottom' in direction:
        i_diff = 1

    for letter_index in range(len(word_to_find)):
        new_i = i + (letter_index * i_diff)
        new_j = j + (letter_index * j_diff)
        if new_i < 0 or new_i >= len(word_search) or new_j < 0 or new_j >= len(word_search[i]):
            return 0
        if word_search[new_i][new_j] != word_to_find[letter_index]:
            return 0

    return 1

def part1(word_search: list[str]) -> int:
    result = 0

    for i in range(len(word_search)):
        for j in range(len(word_search[i])):
            if word_search[i][j] == 'X':
                result += scan_word(word_search, 'left', i, j)
                result += scan_word(word_search, 'top left', i, j)
                result += scan_word(word_search, 'top', i, j)
                result += scan_word(word_search, 'top right', i, j)
                result += scan_word(word_search, 'right', i, j)
                result += scan_word(word_search, 'bottom right', i, j)
                result += scan_word(word_search, 'bottom', i, j)
                result += scan_word(word_search, 'bottom left', i, j)

    return result


def part2(word_search: list[str]) -> int: 
    result = 0

    for i in range(len(word_search)):
        for j in range(len(word_search[i])):
            if word_search[i][j] == 'A':
                # make sure all corners are in-bounds
                if i - 1 >= 0 and i + 1 < len(word_search) and j - 1 >= 0 and j + 1 < len(word_search):
                    # S on top 
                    if word_search[i-1][j-1] == 'S' and word_search[i-1][j+1] == 'S' and word_search[i+1][j-1] == 'M' and word_search[i+1][j+1] == 'M':
                        result += 1

                    # S on right 
                    if word_search[i-1][j-1] == 'M' and word_search[i-1][j+1] == 'S' and word_search[i+1][j-1] == 'M' and word_search[i+1][j+1] == 'S':
                        result += 1

                    # S on bottom 
                    if word_search[i-1][j-1] == 'M' and word_search[i-1][j+1] == 'M' and word_search[i+1][j-1] == 'S' and word_search[i+1][j+1] == 'S':
                        result += 1

                    # S on left 
                    if word_search[i-1][j-1] == 'S' and word_search[i-1][j+1] == 'M' and word_search[i+1][j-1] == 'S' and word_search[i+1][j+1] == 'M':
                        result += 1

    return result

print(part1(input.copy()))
print(part2(input.copy()))
