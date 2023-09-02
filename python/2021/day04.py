inp = open("2021/day04.txt")

class BingoBoard():
    def __init__(self):
        self.board = []
        self.complete = False

    def add_row(self, row):
        new_row = []
        for num in row:
            new_row.append([num, 0])

        self.board.append(new_row)

    def check_bingo(self):
        bingo = False
        checker = []

        for row in self.board:
            row_sum = 0
            for num in row:
                if num[1]:
                    row_sum += 1

            checker.append(row_sum)
                    
        for i in range(len(self.board)):
            col_sum = 0
            for j in range(len(self.board)):
                if self.board[j][i][1]:
                    col_sum += 1

            checker.append(col_sum)

        if 5 in checker:
            bingo = True
            self.complete = True
        return bingo
        
    def get_score(self):
        score = 0
        for row in self.board:
            for num in row:
                if not num[1]:
                    score += num[0]

        return score

    def dab_num(self, to_dab):
        for row in self.board:
            for num in row:
                if num[0] == to_dab:
                    num[1] += 1


draws = []
boards = []
next_board = BingoBoard()

for line in inp:
    if ',' in line:
        draws = [int(num) for num in line.split(',')]
        print (draws)
    elif line == '\n':
        if next_board.board:
            boards.append(next_board)
        next_board = BingoBoard()
    else:
        row = [int(num) for num in line.split(' ') if num]
        next_board.add_row(row)

boards.append(next_board)
board_scores = []
for draw in draws:
    for board in boards:
        if not board.complete:
            board.dab_num(draw)
            if board.check_bingo():
                board_scores.append(board.get_score() * draw)


def part1():
    return board_scores[0]


def part2():
    return board_scores[-1]

print(len(board_scores))
print (part1())
print (part2())