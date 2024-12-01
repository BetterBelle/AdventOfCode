class Node():
    def __init__(self, id : int) -> None:
        self._marked : bool = False 
        self._id : int = id

    def mark(self) -> None:
        self._marked = True

    def unmark(self) -> None:
        self._marked = False

    @property
    def id(self) -> int:
        return self._id

    @property
    def marked(self) -> bool:
        return self._marked

class Edge():
    def __init__(self, u : Node, v : Node) -> None:
        self._u : Node = u
        self._v : Node = v

    def get_end(self, u) -> Node:
        if self._u == u:
            return self._v
        elif self._v == u:
            return self._u

        raise Exception("That node isn't incident on this edge.")

class Graph():
    def __init__(self, n : int) -> None:
        self._nodes : list[Node] = [Node(i) for i in range(n)]
        self._adj_list : dict[Edge] = {node: [] for node in self._nodes}

    def insert_edge(self, u : Node, v : Node) -> None:
        temp = self.get_edge(u, v)

        if temp != None:
            raise Exception("This edge already exists in the graph.")

        new_edge = Edge(u, v)
        self._adj_list[u].append(new_edge)
        self._adj_list[v].append(new_edge)


    def get_node(self, id : int) -> Node:
        if id >= 0 and id < len(self._nodes):
            return self._nodes[id]

        raise Exception("A node with id {} does not exist in the graph.".format(id))

    def incident_edges(self, u : Node) -> list[Edge]:
        if u not in self._nodes:
            raise Exception("This node does not exist in the graph.")

        return self._adj_list[u]

    def get_edge(self, u : Node, v : Node):
        if u not in self._nodes or v not in self._nodes:
            raise Exception("One of the nodes is not in the graph.")

        edges = self._adj_list[u]
        for edge in edges:
            if edge.get_end(u) == v:
                return edge

        raise Exception("There is no edge connecting u to v")

    def are_adj(self, u : Node, v : Node):
        pass 

        
input = [line.strip() for line in open("2023/day10.txt")]

def part1(input):
    return None

def part2(input):
    return None

print(part1(input))
print(part2(input))
