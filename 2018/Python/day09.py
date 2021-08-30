class Marble():
    def __init__(self, points):
        self.after = None
        self.before = None
        self.points = points

    def insert_after(self, marble):
        marble.after = self.after
        marble.before = self
        self.after = marble
        marble.after.before = marble

    def __repr__(self):
        return "Marble " + str(self.points)

def play(num_players, score):
    players = [0 for _ in range(num_players)]

    current = Marble(0)
    current.after = current
    current.before = current

    player_turn = 0

    for marble_worth in range(1, score):
        if marble_worth % 23 == 0:
            marble_remove = current.before.before.before.before.before.before.before
            before_remove = marble_remove.before

            current = current.before.before.before.before.before.before
            current.before = before_remove

            before_remove.after = current

            players[player_turn] = players[player_turn] + marble_remove.points + marble_worth
            marble_remove = None
        else:
            new_marble = Marble(marble_worth)
            current.after.insert_after(new_marble)
            current = new_marble

        player_turn = (player_turn + 1) % num_players
            

    return max(players)

num_players = int(open("2018/inputs/day09.txt").read().split(" ")[0])
max_points = int(open("2018/inputs/day09.txt").read().split(" ")[6]) + 1
print (play(num_players, max_points))
print (play(num_players, max_points * 100))