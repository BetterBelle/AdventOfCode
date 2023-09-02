inp = open("2020/day02.txt")
passwords = []
for line in inp:
    passwords.append(line.strip())


def part1():
    num_valid_passwords = 0

    for password_auth in passwords:
        occurs, letter_to_check, password = password_auth.split(" ")
        letter_to_check = letter_to_check[0]
        min_occurs, max_occurs = occurs.split("-")
        min_occurs = int(min_occurs)
        max_occurs = int(max_occurs)

        num_occurs = 0

        for letter in password:
            if letter_to_check == letter:
                num_occurs += 1
        
        if num_occurs >= min_occurs and num_occurs <= max_occurs:
            num_valid_passwords += 1

    return num_valid_passwords

def part2():
    num_valid_passwords = 0

    for password_auth in passwords:
        occurs, letter_to_check, password = password_auth.split(" ")
        letter_to_check = letter_to_check[0]
        first_index, second_index = occurs.split("-")
        first_index = int(first_index)
        second_index = int(second_index)

        if (letter_to_check == password[first_index-1] and letter_to_check != password[second_index-1]) or (letter_to_check != password[first_index-1] and letter_to_check == password[second_index-1]):
            num_valid_passwords += 1

    return num_valid_passwords
        
print (part1())
print (part2())