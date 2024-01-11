input = [line.strip() for line in open("2023/day03.txt")]

def create_number(i, j):
    number = input[i][j]
    # scan right
    for x in range(j+1, len(input)):
        if not input[i][x].isnumeric():
            break
        
        number += input[i][x] 

    # scan left
    for x in range(j-1, -1, -1):
        if not input[i][x].isnumeric():
            break

        number = input[i][x] + number

    return int(number)

def get_adjacent_numbers(i, j):
    numbers = []
    check_top_right = True 
    check_bottom_right = True 

    # left side
    if j-1 >= 0:
        if i-1 >= 0 and input[i-1][j-1].isnumeric():
            numbers.append(create_number(i-1, j-1))
            # if there's a number in the middle, any number on the right must be part of this number
            if input[i-1][j].isnumeric():
                check_top_right = False 
        if input[i][j-1].isnumeric():
            numbers.append(create_number(i, j-1))
        if i+1 < len(input) and input[i+1][j-1].isnumeric():
            numbers.append(create_number(i+1, j-1))
            # if there's a number in the middle, any number on the right must be part of this number
            if input[i+1][j].isnumeric():
                check_bottom_right = False 

    if j+1 < len(input):
        if i-1 >= 0 and input[i-1][j+1].isnumeric() and check_top_right:
            numbers.append(create_number(i-1, j+1))
        if input[i][j+1].isnumeric():
            numbers.append(create_number(i, j+1))
        if i+1 < len(input) and input[i+1][j+1].isnumeric() and check_bottom_right:
            numbers.append(create_number(i+1, j+1))

    if i-1 >= 0 and input[i-1][j].isnumeric():
        new_number = create_number(i-1, j)
        # if there's a number here and it's greater than 9, we've already found it
        # because it either stretches to the left (where it would've been caught)
        # or to the right (which also would have been caught)
        if new_number < 10:
            numbers.append(new_number)
    if i+1 < len(input[i]) and input[i+1][j].isnumeric():
        new_number = create_number(i+1, j)
        if new_number < 10:
            numbers.append(new_number)

    return numbers 

def part1():
    total = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if not input[i][j].isnumeric() and not input[i][j] == '.':
                total += sum(get_adjacent_numbers(i, j))

    return total

def part2():
    sum = 0
    nums = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "*":
                nums = get_adjacent_numbers(i, j)
                if len(nums) == 2:
                    sum += nums[0] * nums[1]
    
    return sum 

print(part1())
print(part2())
