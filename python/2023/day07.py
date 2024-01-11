from enum import Enum

class Score(Enum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


class Hand():
    def __init__(self, hand: str, bet: str) -> None:
        self.hand = hand
        self.bet = int(bet)
        self.card_strengths = {
                '2': 0,
                '3': 1,
                '4': 2,
                '5': 3,
                '6': 4,
                '7': 5,
                '8': 6,
                '9': 7,
                'T': 8,
                'J': 9,
                'Q': 10,
                'K': 11,
                'A': 12,
                }

    def _one_pair(self) -> bool:
        # exactly one duplicate means pair
        if len(set(self.hand)) == 4:
            return True
        return False

    def _two_pair(self) -> bool:
        # count is three as there are 2 dupes
        if len(set(self.hand)) == 3:
            for char in set(self.hand):
                # if one of them is counted twice, there has to be a two pair
                if self.hand.count(char) == 2:
                    return True
        return False

    def _three_of_a_kind(self) -> bool:
        # count is three as there are 2 dupes
        if len(set(self.hand)) == 3:
            for char in set(self.hand):
                # if one of them is counted 3 times, it's a three of a kind
                if self.hand.count(char) == 3:
                    return True
        return False

    def _full_house(self) -> bool:
        if len(set(self.hand)) == 2:
            if self.hand.count(self.hand[0]) == 2 or self.hand.count(self.hand[0]) == 3:
                return True
        return False 

    def _four_of_a_kind(self) -> bool:
        if len(set(self.hand)) == 2:
            if self.hand.count(self.hand[0]) == 1 or self.hand.count(self.hand[0]) == 4:
                return True
        return False 

    def _five_of_a_kind(self) -> bool:
        if len(set(self.hand)) == 1:
            return True
        return False

    def score(self) -> Score:
        score = Score.HIGH_CARD
        if self._one_pair():
            score = Score.PAIR
        if self._two_pair():
            score = Score.TWO_PAIR
        if self._three_of_a_kind():
            score = Score.THREE_OF_A_KIND
        if self._full_house():
            score = Score.FULL_HOUSE
        if self._four_of_a_kind():
            score = Score.FOUR_OF_A_KIND
        if self._five_of_a_kind():
            score = Score.FIVE_OF_A_KIND
        return score

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Hand):
            return False
        if self.score() != __value.score():
            return False
        for own, other in zip(self.hand, __value.hand):
            if own != other:
                return False
        return True

    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Hand):
            raise NotImplementedError
        if self.score().value > __value.score().value:
            return False
        if self.score().value < __value.score().value:
            return True
        for own, other in zip(self.hand, __value.hand):
            if self.card_strengths[own] < self.card_strengths[other]:
                return True
            if self.card_strengths[own] > self.card_strengths[other]:
                return False
        
        return False

    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, Hand):
            raise NotImplementedError
        if self.score().value > __value.score().value:
            return True
        if self.score().value < __value.score().value:
            return False
        for own, other in zip(self.hand, __value.hand):
            if self.card_strengths[own] < self.card_strengths[other]:
                return False
            if self.card_strengths[own] > self.card_strengths[other]:
                return True
        
        return False
        
    def __str__(self):
        return "Hand: {}, Bet: {}".format(self.hand, self.bet) 

    def __repr__(self):
        return str(self)

class HandJoker(Hand):
    def __init__(self, hand: str, bet: str) -> None:
        super().__init__(hand, bet)
        self.card_strengths = {
                'J': 0,
                '2': 1,
                '3': 2,
                '4': 3,
                '5': 4,
                '6': 5,
                '7': 6,
                '8': 7,
                '9': 8,
                'T': 9,
                'Q': 10,
                'K': 11,
                'A': 12,
                }

    def score(self) -> Score:
        score = super().score()
        
        # high card, can only be one J which means pair
        if score == Score.HIGH_CARD:
            if self.hand.count('J') > 0:
                score = Score.PAIR
        # pair, if there are jacks, it's trips instead
        elif score == Score.PAIR:
            if self.hand.count('J') > 0:
                score = Score.THREE_OF_A_KIND
        # two pair, if there's one jack, it's a full house
        # if there are two jacks, it's quads
        elif score == Score.TWO_PAIR:
            if self.hand.count('J') == 1:
                score = Score.FULL_HOUSE
            if self.hand.count('J') > 1:
                score = Score.FOUR_OF_A_KIND
        # three of a kind, if there are any jacks, it's a four of a kind
        elif score == Score.THREE_OF_A_KIND:
            if self.hand.count('J') > 0:
                score = Score.FOUR_OF_A_KIND
        # if full house and jack, it's a fiver
        elif score == Score.FULL_HOUSE:
            if self.hand.count('J') > 0:
                score = Score.FIVE_OF_A_KIND
        # if it's quads, if there are jacks it's a fiver
        elif score == Score.FOUR_OF_A_KIND:
            if self.hand.count('J') > 0:
                score = Score.FIVE_OF_A_KIND

        return score

input = [(Hand(line.split(' ')[0], line.split(' ')[1]), HandJoker(line.split(' ')[0], line.split(' ')[1])) for line in open("2023/day07.txt")]
input_one = [hand[0] for hand in input]
input_two = [hand[1] for hand in input]

def part1(input: list[Hand]):
    solution = 0
    input.sort()
    for i, hand in enumerate(input):
        solution += (i + 1) * hand.bet

    return solution

def part2(input: list[HandJoker]):
    solution = 0
    input.sort()
    for i, hand in enumerate(input):
        solution += (i + 1) * hand.bet

    return solution

print(part1(input_one))
print(part2(input_two))
