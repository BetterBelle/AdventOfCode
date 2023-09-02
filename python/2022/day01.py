inp = open("2022/day01.txt")
calorie_list = list()
for line in inp:
    calorie_list.append(line)

def solutions():
    max_calories = [0, 0, 0]
    current_calories = 0

    for line in calorie_list:
        if line != '\n':
            current_calories += int(line)
        else:
            if current_calories > min(max_calories):
                max_calories.remove(min(max_calories))
                max_calories.append(current_calories)
            current_calories = 0

    return max_calories

print(f'Part 1: {max(solutions())}')
print(f'Part 2: {sum(solutions())}')