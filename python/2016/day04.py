"""
Incomplete, gotta figure out what's going wrong
"""

def id_sum_real():
    input = open('2016/day04.txt')
    ans = 0
    for line in input:
        temp_current = line.split('-')[:len(line.split('-'))-1]
        current = ''
        for string in temp_current:
            current += string

        id = int(line.split('-')[len(line.split('-'))-1].split('[')[0])
        checksum = line.split('-')[len(line.split('-'))-1].split('[')[1][:5]

        last_count = 1000
        last_char = ''
        is_real = True
        for char in checksum:
            if current.count(char) > last_count:
                is_real = False
                break

            if current.count(char) == last_count and  last_char > char:
                is_real = False
                break

            last_count = current.count(char)
            last_char = char

        if is_real:
            ans += id

    return ans


def main():
    print (id_sum_real())


if __name__ == '__main__':
    main()