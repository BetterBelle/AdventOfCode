def withRoboSanta():
    currentSLoc = [0,0]
    currentRLoc = [0,0]
    passedLocs = []
    passedLocs.append((0,0))
    
    turn = 0
    
    input = open("2015/inputs/day03.txt")
    directions = input.read()
    
    for d in directions:
        if turn % 2 == 0:
            if d == 'v':
                currentSLoc[1] = currentSLoc[1] - 1
            elif d == '^':
                currentSLoc[1] = currentSLoc[1] + 1
            elif d == '>':
                currentSLoc[0] = currentSLoc[0] + 1
            elif d == '<':
                currentSLoc[0] = currentSLoc[0] - 1
            
            if not foundLocation(currentSLoc, passedLocs):
                passedLocs.append((currentSLoc[0], currentSLoc[1]))
    
        else:
            if d == 'v':
                currentRLoc[1] = currentRLoc[1] - 1
            elif d == '^':
                currentRLoc[1] = currentRLoc[1] + 1
            elif d == '>':
                currentRLoc[0] = currentRLoc[0] + 1
            elif d == '<':
                currentRLoc[0] = currentRLoc[0] - 1
            
            
            if not foundLocation(currentRLoc, passedLocs):
                passedLocs.append((currentRLoc[0], currentRLoc[1]))
                    
        turn += 1

    return len(passedLocs)

def countHousesWithPresents():
    currentLoc = [0,0]
    passedLocs = []
    passedLocs.append((0,0))
    input = open("2015/inputs/day03.txt")
    directions = input.read()
    for d in directions:
        if d == 'v':
            currentLoc[1] = currentLoc[1] - 1
        elif d == '^':
            currentLoc[1] = currentLoc[1] + 1
        elif d == '>':
            currentLoc[0] = currentLoc[0] + 1
        elif d == '<':
            currentLoc[0] = currentLoc[0] - 1
        
        
        if not foundLocation(currentLoc, passedLocs):
            passedLocs.append((currentLoc[0], currentLoc[1]))

    return len(passedLocs)
    
def foundLocation(currentLoc, passedLocs):
    for loc in passedLocs:
        if currentLoc[0] == loc[0] and currentLoc[1] == loc[1]:
            return True
                    
    return False


def main():
    print("Santa has delivered presents to ", countHousesWithPresents(), " houses")
    print("With RoboSanta, they delivered presents to ", withRoboSanta(), " houses")
    
    
if __name__ == "__main__":
    main()
