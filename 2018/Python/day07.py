class Step():
    def __init__(self, name):
        self.prev = []
        self.after = []
        self.complete = False
        self.name = name
        self.time = ord(self.name) - 4

    def ready(self):
        for step in self.prev:
            if not step.complete:
                return False

        return True

    def work_task(self):
        self.time -= 1

    def add_next_step(self, next_step):
        self.after.append(next_step)
        self.after.sort()

    def add_prev_step(self, prev):
        self.prev.append(prev)
        self.prev.sort()

    def __lt__(self, b):
        return self.name < b.name

    def __gt__(self, b):
        return self.name > b.name

    def __repr__(self):
        return "Step " + self.name


def setup_steps():
    steps = {}
    with open("2018/inputs/day07.txt") as inp:
        for line in inp:
            prev = line.split(" ")[1]
            after = line.split(" ")[7]
            if not prev in steps:
                steps[prev] = Step(prev)
            if not after in steps:
                steps[after] = Step(after)

            steps[prev].add_next_step(steps[after])
            steps[after].add_prev_step(steps[prev])

    return steps


def part1():
    steps = setup_steps()
    order = ''
    while True:
        ready_steps = []
        for step in steps.values():
            if step.ready() and not step.complete:
                ready_steps.append(step)
        ready_steps.sort()

        if len(ready_steps) == 0:
            break

        order += ready_steps[0].name
        ready_steps[0].complete = True

    return order


def part2():
    steps = setup_steps()
    time = 0
    workers = [None, None, None, None, None]

    while True:
        # Figure out work
        ready_steps = []
        for step in steps.values():
            if step.ready() and not step.complete and not step in workers:
                ready_steps.append(step)
        ready_steps.sort()

        # Figure out if work done
        no_work = True
        for i in range(len(workers)):
            if workers[i] != None:
                no_work = False
                break
        
        if no_work and len(ready_steps) == 0:
            break

        # Assign work
        for i in range(len(workers)):
            if workers[i] == None:
                if len(ready_steps) > 0:
                    workers[i] = ready_steps[0]
                    ready_steps = ready_steps[1:]

        # Work
        for i in range(len(workers)):
            if workers[i] != None:
                workers[i].work_task()

        # Remove Completed work
        for i in range(len(workers)):
            if workers[i] != None:
                if workers[i].time == 0:
                    workers[i].complete = True
                    workers[i] = None

        time += 1

    return time


print (part1())
print (part2())