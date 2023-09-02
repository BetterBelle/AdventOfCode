inp_file = open('2020/day10.txt')
adapters = []
for line in inp_file:
    adapters.append(int(line))

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1] + 3)


class Graph:
    def __init__(self):
        self.adj_list = []

    def add_edge(self, from_vertex, to_vertex):
        self.adj_list[from_vertex].append(to_vertex)
    
    def add_vertex(self, vertex):
        self.adj_list.append(vertex)

    def __repr__(self):
        return str(self.adj_list)

    def __str__(self):
        return str(self.adj_list)


def part1():
    diffs = [0, 0, 0]

    for i in range(1, len(adapters)):
        diffs[adapters[i] - adapters[i-1] - 1] += 1

    return diffs[0] * diffs[2]



def part2():
    graph = Graph()
    current_vertex = 0
    for i in range(len(adapters)):
        new_edges = []
        for j in range(1,4):
            if i+j < len(adapters) and adapters[i+j] - adapters[i] <= 3:
                new_edges.append(current_vertex+j)

        if len(new_edges) == 1 and (len(graph.adj_list) == 0 or len(graph.adj_list[-1]) == 1):
            continue
        else:
            graph.add_vertex(new_edges)
            current_vertex += 1

    # Get the number of edges at each vertex
    num_of_edges = [len(graph.adj_list[i]) for i in range(len(graph.adj_list))]

    # Start from the second to last edge
    for i in range(len(graph.adj_list)-2, 0, -1):
        for j in range(1, 4):
            # If the current vertex is in a previous vertex
            if i-j >= 0 and i in graph.adj_list[i-j]:
                # Increase the number of edges in the previous vertex
                num_of_edges[i-j] += num_of_edges[i]
                # Remove an edge (because we're essentially doing a substitution)
                num_of_edges[i-j] -= 1
                

    return num_of_edges[0]


print (part1())
print (part2())