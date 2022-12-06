inp = [line.strip() for line in open("2022/inputs/day06.txt")][0]

def solution(check_chars):
    answer = 0
    for i in range(len(inp) - check_chars - 1):
        current = inp[i:i+check_chars]
        if len(set(current)) == len(current) and answer == 0:
            answer = i + check_chars

    return answer

print(solution(4))
print(solution(14))