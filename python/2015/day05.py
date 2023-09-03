import re

inputFile = open('2015/day05.txt')
part1 = 0
part2 = 0
for line in inputFile.read().split('\n'):
	doubles = len(re.findall(r"(.)\1", line)) >= 1
	vowels = len(re.findall(r"a|e|i|o|u", line)) >= 3
	forbidden = len(re.findall(r"ab|cd|pq|xy", line)) == 0
	squeeze = len(re.findall(r"(.)(?!\1).\1", line)) >= 1
	repeat_pair = len(re.findall(r"(..).*\1", line)) >= 1

	if doubles and vowels and forbidden:
		part1 += 1
	if squeeze and repeat_pair:
		part2 += 1


print(part1)
print(part2)