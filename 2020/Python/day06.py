inp_file = open('2020/inputs/day06.txt')

inp = []
for line in inp_file:
    inp.append(line)
        

def full_solution():
    yes_answers = {}
    num_people = 0
    sum_part1 = 0
    sum_part2 = 0
    
    for person in inp:
        if person == '\n':
            sum_part1 += len(yes_answers)
            for yes_answer in yes_answers:
                if yes_answers[yes_answer] == num_people:
                    sum_part2 += 1
            
            yes_answers = {}
            num_people = 0
            continue

        person = person.strip()
        num_people += 1
        for question in person:
            if question in yes_answers.keys():
                yes_answers[question] += 1
            else:
                yes_answers[question] = 1


    for yes_answer in yes_answers:
        if yes_answers[yes_answer] == num_people:
            sum_part2 += 1

    sum_part1 += len(yes_answers)
            
    return sum_part1, sum_part2


print (full_solution())

