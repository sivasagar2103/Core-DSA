class WeightedGraphAdjacencyList:
    def __init__(self):
        self.graph = {}
    
    def add_u_v_weight(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v,weight))
        self.graph[v].append((u, weight))
    
    def display_graph(self):
        print(self.graph)
        for key, value in self.graph.items():
            print(f"{key} -- > {value}")


g = WeightedGraphAdjacencyList()
g.add_u_v_weight(1, 2, 10)
g.add_u_v_weight(1, 3, 5)
g.add_u_v_weight(2, 4, 7)
g.add_u_v_weight(3, 4, 3)
g.add_u_v_weight(4, 5, 1)

g.display_graph()