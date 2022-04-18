def code():
    input = open('2016/inputs/day02.txt')
    keypad = [['1','2','3'],['4','5','6'],['7','8','9']]
    position = [1,1]
    code = ''
    for line in input:
        for c in line:
            if c == 'U' and position[0] - 1 > -1:
                position[0] -= 1
            elif c == 'L' and position[1] - 1 > -1:
                position[1] -= 1
            elif c == 'R' and position[1] + 1 < 3:
                position[1] += 1
            elif c == 'D' and position[0] + 1 < 3:
                position[0] += 1
    
        code += keypad[position[0]][position[1]]

    return code

def spec_code():
    input = open('2016/inputs/day02.txt')
    keypad = [['0','0','1','0','0'],['0','2','3','4','0'],['5','6','7','8','9'],['0','A','B','C','0'],['0','0','D','0','0']]
    position = [2,0]
    code = ''
    for line in input:
        for c in line:
            if c == 'U' and position[0] - 1 > -1:
                position[0] -= 1
                if keypad[position[0]][position[1]] == '0':
                    position[0] += 1
            elif c == 'L' and position[1] - 1 > -1:
                position[1] -= 1
                if keypad[position[0]][position[1]] == '0':
                    position[1] += 1
            elif c == 'R' and position[1] + 1 < 5:
                position[1] += 1
                if keypad[position[0]][position[1]] == '0':
                    position[1] -= 1
            elif c == 'D' and position[0] + 1 < 5:
                position[0] += 1
                if keypad[position[0]][position[1]] == '0':
                    position[0] -= 1

        code += keypad[position[0]][position[1]]

    return code

def main():
    print (code())
    print (spec_code())


if __name__ == '__main__':
    main()