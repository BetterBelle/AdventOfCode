def paperFeetNeeded():
    sheetSize = 0
    input = open("2015/day02.txt")
    for line in input:
        dims = line.split('x')
        nums = [int(i) for i in dims]
        #Sorting to get the 2 smallest dimensions
        nums.sort()
        sheetSize += 2 * nums[0] * nums[1] + 2 * nums[1] * nums[2] + 2 * nums[2] * nums[0] + nums[0] * nums[1]
        
    return sheetSize

def ribbonFeetNeeded():
    ribbonLength = 0
    input = open("2015/day02.txt")
    for line in input:
        dims = line.split("x")
        nums = [int(i) for i in dims]
        #Again to get the smallest dimension
        nums.sort()
        ribbonLength += 2 * nums[0] + 2 * nums[1] + nums[0] * nums[1] * nums[2]
        
    return ribbonLength


def main():
    print ("The elves need this many square feet of paper:", paperFeetNeeded())
    print ("The elves need this many feet of ribbon length:", ribbonFeetNeeded())


if __name__ == "__main__":
    main()