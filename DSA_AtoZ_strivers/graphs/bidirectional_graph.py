class GraphAdjacencyList:
    def __init__(self):
        self.graph = {}
    
    def add_u_v(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def display_graph(self):
        print(self.graph)
        for key, value in self.graph.items():
            print(f" {key} -- > {value}")

g = GraphAdjacencyList()
# g.add_u_v("A", "B")
# g.add_u_v("A", "C")
# g.add_u_v("B", "D")
g.add_u_v(1, 2)
g.add_u_v(1, 3)
g.add_u_v(2,4)
g.add_u_v(3,4)
g.add_u_v(3,5)
g.add_u_v(4,5)

g.display_graph()