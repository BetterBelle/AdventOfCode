import re
input = [line.strip() for line in open("2023/day04.txt")]

class CardData:
    def __init__(self, card_num, winners, my_nums) -> None:
        self.card_num = card_num
        self.num_copies = 1
        self.winners = winners 
        self.my_nums = my_nums

    def calc_score(self):
        winning_numbers = self.num_winners()
        if winning_numbers == 0:
            return 0

        return 2 ** (winning_numbers - 1)
    
    def num_winners(self):
        winning_nums = 0
        for winner in self.winners:
            if winner in self.my_nums:
                winning_nums += 1

        return winning_nums
    
    def add_copy(self):
        self.num_copies += 1
    
    def add_copies(self, copies):
        self.num_copies += copies

cards : list[CardData] = []
for line in input:
    winners, my_nums = line.split("|")
    card_num = int(re.findall('[0-9]+', winners.split(":")[0])[0])
    winners = [int(num) for num in re.findall('[0-9]+', winners.split(":")[1])]
    my_nums = [int(num) for num in re.findall('[0-9]+', my_nums)]
    cards.append(CardData(card_num, winners, my_nums))

def part1():
    total = 0
    for card in cards:
        total += card.calc_score()

    return total

def part2():
    total = 0
    for i, card in enumerate(cards):
        winning_nums = card.num_winners()
        for j in range(1, winning_nums + 1):
            cards[i + j].add_copies(card.num_copies)

        total += card.num_copies

    return total

print(part1())
print(part2())
