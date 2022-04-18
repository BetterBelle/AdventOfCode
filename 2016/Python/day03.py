def possible_triangles():
    input = open('2016/inputs/input3.txt')
    count = 0
    for line in input:
        nums = [int(line[:5]),int(line[5:10]),int(line[10:15])]
        nums.sort()
        if nums[0] + nums[1] > nums[2]:
            count += 1

    return count

def vertical_read():
    input = open('2016/inputs/input3.txt')
    count = 0
    read = 0
    nums = []
    for line in input:
        nums.append([int(line[:5]),int(line[5:10]),int(line[10:15])])
        read += 1

        if read == 3:
            for i in range(3):
                tri = []
                for j in range(3):
                    tri.append(nums[j][i])

                tri.sort()
                if tri[0] + tri[1] > tri[2]:
                    count += 1

            nums = []
            read = 0
    
    return count

def main():
    print (possible_triangles())
    print (vertical_read())

if __name__ == '__main__':
    main()