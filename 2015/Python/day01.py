def finalFloor():
    floor = 0
    input = open("2015/inputs/day01.txt")
    str = input.read()
    for c in str:
        if c == ')':
            floor -= 1
        if c == '(':
            floor += 1
            
    return floor
    
def positionAtBasement():
    position = 0
    floor = 0
    input = open("2015/inputs/day01.txt")
    str = input.read()
    for c in str:
        if c == ')':
            floor -= 1
        if c == '(':
            floor += 1
            
        position += 1
        
        if floor == -1:
            break
            
    return position
    
def main():
    print ("Santa must finish on floor:", finalFloor())
    print ("Santa will first reach the basement on instruction:", positionAtBasement())
    return
    
if __name__ == "__main__":
    main()