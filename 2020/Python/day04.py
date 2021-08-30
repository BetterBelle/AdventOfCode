import re
inp = open("2020/inputs/day04.txt")

passports = []
for line in inp:
    passports.append(line)

NUM_NEEDED_KEYS = 7

def keys_present(passport_keys):
    if (not 'cid' in passport_keys and len(passport_keys) == NUM_NEEDED_KEYS) or (len(passport_keys) == NUM_NEEDED_KEYS + 1):
        return True

    return False

def is_valid_passport(passport):
    valid_eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    num_valid_fields = 0

    if passport['byr'].isnumeric() and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
        num_valid_fields += 1
    if passport['iyr'].isnumeric() and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020:
        num_valid_fields += 1
    if passport['eyr'].isnumeric() and 2030 >= int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030:
        num_valid_fields += 1
    if passport['hgt'][-2:] == 'cm' and int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193:
        num_valid_fields += 1
    elif passport['hgt'][-2:] == 'in' and int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76:
        num_valid_fields += 1
    if re.fullmatch('#[0-9a-f]{6}', passport['hcl']):
        num_valid_fields += 1
    if passport['ecl'] in valid_eye_colours:
        num_valid_fields += 1
    if re.fullmatch('[0-9]{9}', passport['pid']):
        num_valid_fields += 1
        
    return num_valid_fields == 7

def full_solution():
    num_valid = 0
    num_fully_valid = 0
    seen = {}

    for passport in passports:
        if passport == '\n':
            if keys_present(seen.keys()):
                if is_valid_passport(seen):
                    num_fully_valid += 1
                num_valid += 1
            
            seen = {}
            continue

        keyval_pairs = passport.split(' ')
        for keyval in keyval_pairs:
            seen[keyval.split(':')[0]] = keyval.split(':')[1].strip()

    if keys_present(seen.keys()):
        if is_valid_passport(seen):
            num_fully_valid += 1
        num_valid += 1

    return num_valid, num_fully_valid

print(full_solution())
