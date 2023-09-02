inp_file = open('2020/day07.txt')
inp = []
for line in inp_file:
    inp.append(line)

bag_rules = {}
for rule in inp:
    rule = rule.split(" ")
    container = rule[0] + " " + rule[1]
    bag_rules[container] = []
    i = 4
    while i < len(rule):
        if not rule[i].isnumeric():
            break
        number_of_bags = int(rule[i])
        bag_colour = rule[i+1] + " " + rule[i+2]
        bag_rules[container].append((number_of_bags, bag_colour))
        i += 4


def part1():
    bags_to_check = ['shiny gold']
    bags_to_contain = set()

    while len(bags_to_check) > 0:
        bag_to_check = bags_to_check[0]

        for container_bag in bag_rules:
            for contained_bag in bag_rules[container_bag]:
                if bag_to_check == contained_bag[1]:
                    bags_to_check.append(container_bag)
                    bags_to_contain.add(container_bag)

        bags_to_check.pop(0)


    return len(bags_to_contain)

def part2():
    required_bags = 0

    bags_to_check = [(1, 'shiny gold')]

    while len(bags_to_check) > 0:
        bag_to_check = bags_to_check[0]

        for contained_bag in bag_rules[bag_to_check[1]]:
            bags_to_check.append((bag_to_check[0] * contained_bag[0], contained_bag[1]))

        bags_to_check.pop(0)
        if len(bags_to_check) > 0:
            required_bags += bags_to_check[0][0]

    return required_bags


print (part1())
print (part2())