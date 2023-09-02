class Guard:
    def __init__(self, gid):
        self.minutes = [0 for i in range(60)]
        self.gid = gid

    def sleep(self, start, end):
        for i in range(start, end):
            self.minutes[i] += 1

    def time_asleep(self):
        total = 0
        for time in self.minutes:
            total += time
        return total
    
    def highest_minute(self):
        max_index = 0
        max_slept = 0
        for i in range(len(self.minutes)):
            if self.minutes[i] > max_slept:
                max_slept = self.minutes[i]
                max_index = i

        return max_index

    def __repr__(self):
        return "Guard #" + str(self.gid)

# Already sorted inputs, just gotta go through
# Setting up all the guards information into a dictionary
guards = {}
with open("2018/day04.txt") as inp:
    guard = None
    for line in inp:
        info = line.split(" ")
        if info[2] == "Guard":
            guard_id = int(info[3][1:])
            if int(info[3][1:]) in guards:
                guard = guards[guard_id]
                continue
            else:
                guards[guard_id] = Guard(guard_id)
                guard = guards[guard_id]
                continue

        if info[2] == "falls":
            start_sleep = int(info[1][3:5])
            continue

        if info[2] == "wakes":
            end_sleep = int(info[1][3:5])
            guard.sleep(start_sleep, end_sleep)
            continue


def part1():
    chosen_guard = Guard(-1)
    for guard in guards.values():
        if guard.time_asleep() > chosen_guard.time_asleep():
            chosen_guard = guard

    return chosen_guard.gid * chosen_guard.highest_minute()


def part2():
    chosen_guard = Guard(-1)
    for guard in guards.values():
        if guard.minutes[guard.highest_minute()] > chosen_guard.minutes[chosen_guard.highest_minute()]:
            chosen_guard = guard

    return chosen_guard.gid * chosen_guard.highest_minute()

print (part1())
print (part2())