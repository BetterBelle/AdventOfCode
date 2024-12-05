import re
input = open("2024/day05.txt").read()
rules_and_updates: list[str] = re.findall("[0-9][0-9]\|[0-9][0-9]|[0-9][0-9],|[0-9][0-9]\n", input)

rule_list: list[str] = [rule for rule in rules_and_updates if '|' in rule]

# gets only the updates, splits per line, then gets rid of the last one because it's going to be empty due to eof newline
updates_list: list[str] = ''.join([update for update in rules_and_updates if '|' not in update]).split('\n')[:-1]
# apply [int(num) for num in x.split(',')] on every list in updates_list, generating all the list of updates as lists of ints
UPDATES: list[list[int]] = list(map(lambda x : [int(num) for num in x.split(',')], updates_list))

# create a rule dictionary where every key is a page and the values are a list of pages that come after it
RULES: dict[list] = {}
for rule in rule_list:
    first, second = [int(page) for page in rule.split('|')]
    if first not in RULES:
        RULES[first] = [second]
    else:
        RULES[first].append(second)


def part1() -> int:
    result = 0
    for update in UPDATES:
        is_valid = True
        for i, page in enumerate(update[:-1]):
            if page in RULES[update[i+1]]:
                is_valid = False

        if is_valid:
            result += update[len(update) // 2]

    return result


def part2() -> int: 
    result = 0
    for update in UPDATES:
        is_valid = True
        for i, page in enumerate(update[:-1]):
            if page in RULES[update[i+1]]:
                is_valid = False

        if not is_valid:
            correct_update = []
            # go through every page in the current update which is incorrectly ordered
            for page in update:
                inserted = False
                # go through every page in the correctly ordered update
                for i, correct_page in enumerate(correct_update):
                    # if page does not come after the correct one, we insert it
                    if page not in RULES[correct_page]:
                        correct_update.insert(i, page)
                        inserted = True
                        break

                # if we haven't inserted, it's the last page (of the current list)
                if not inserted:
                    correct_update.append(page)

            result += correct_update[len(correct_update) // 2]


    return result

print(part1())
print(part2())
