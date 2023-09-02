# Create fabric and list all claims
fabric = [[0 for i in range(1000)] for j in range(1000)]
claims = []
with open("2018/day03.txt") as inp:
    for line in inp:
        claim = line.split(" ")
        claim_id = int(claim[0][1:])
        claim_start = tuple(int(coord) for coord in claim[2][:-1].split(","))
        claim_size = tuple(int(dim) for dim in claim[3].split("x"))
        claims.append((claim_id, claim_start, claim_size))
        for i in range(claim_start[0], claim_start[0] + claim_size[0]):
            for j in range(claim_start[1], claim_start[1] + claim_size[1]):
                fabric[i][j] += 1

def part1():
    overlaps = 0
    for row in fabric:
        for inch in row:
            if inch > 1:
                overlaps += 1

    return overlaps

def part2():
    for claim in claims:
        flag = False
        for i in range(claim[1][0], claim[1][0] + claim[2][0]):
            for j in range(claim[1][1], claim[1][1] + claim[2][1]):
                if fabric[i][j] > 1:
                    flag = True
                    break
            if flag == True:
                break
        if not flag:
            ans = claim[0]
            break

    return ans

print (part1())
print (part2())