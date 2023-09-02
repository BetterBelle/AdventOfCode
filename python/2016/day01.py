def distance():
    card = 0
    endLoc = [0, 0]
    input = open("2016/day01.txt")
    directions = input.read().split(", ")
    for d in directions:
        dist = int(d[1:])
        if d[0] == 'L':
            card = (card - 1) % 4
        else:
            card = (card + 1) % 4
        
        if card == 0:
            endLoc[1] += dist
        if card == 1:
            endLoc[0] += dist
        if card == 2:
            endLoc[1] -= dist
        if card == 3:
            endLoc[0] -= dist
            
    return abs(endLoc[0]) + abs(endLoc[1])
    
def firstDouble():
	card = 0
	endLoc = [0,0]
	storage = []
	input = open("2016/day01.txt")
	directions = input.read().split(", ")
	for d in directions:
		dist = int(d[1:])
		if d[0] == 'L':
			card = (card - 1) % 4
		else:
			card = (card + 1) % 4

		if card == 0:
			for i in range(dist):
				endLoc[1] += 1
				if find(storage,(endLoc[0],endLoc[1])):
					return abs(endLoc[0]) + abs(endLoc[1])
				else:
					storage.append((endLoc[0],endLoc[1]))
		elif card == 1:
			for i in range(dist):
				endLoc[0] += 1
				if find(storage,(endLoc[0],endLoc[1])):
					return abs(endLoc[0]) + abs(endLoc[1])
				else:
					storage.append((endLoc[0],endLoc[1]))
		elif card == 2:
			for i in range(dist):
				endLoc[1] -= 1
				if find(storage,(endLoc[0],endLoc[1])):
					return abs(endLoc[0]) + abs(endLoc[1])
				else:
					storage.append((endLoc[0],endLoc[1]))
		elif card == 3:
			for i in range(dist):
				endLoc[0] -= 1
				if find(storage,(endLoc[0],endLoc[1])):
					return abs(endLoc[0]) + abs(endLoc[1])
				else:
					storage.append((endLoc[0],endLoc[1]))

def find(arr, val):
	for item in arr:
		if val == item:
			return True

	return False
		
    
def main():
    print (distance())
    print (firstDouble())
    

if __name__ == "__main__":
    main()
