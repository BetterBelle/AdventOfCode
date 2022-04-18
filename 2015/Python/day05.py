inputFile = open('2015/inputs/day05.txt')
input = inputFile.read().split('\n')
niceStrings = 0

#part 1
for line in input:
	double = False
	vowels = 0
	prevChar = ''
	if not ("ab" in line or "cd" in line or "pq" in line or "xy" in line):
		for c in line:
			if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
				vowels += 1
			if prevChar == c:
				double = True
				
			prevChar = c
			
		if vowels >= 3 and double == True:
			niceStrings += 1
			
print (niceStrings)

#part 2
inputFile = open('2015/inputs/day05.txt')
input = inputFile.read().split('\n')
niceStrings = 0
