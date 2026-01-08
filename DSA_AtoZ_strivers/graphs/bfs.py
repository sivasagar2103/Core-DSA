from collections import defaultdict, deque

class BreadthFirstSearch:
    
    def __init__(self):
        self.graph_adj = defaultdict(list)
    

    def add_edge(self, u, v):
        self.graph_adj[u].append(v)
        self.graph_adj[v].append(u) #comment this if the graph is directed
    

    def bfs(self, start):
        visited = set()
        result = []
        queue_elements = deque([start])
        visited.add(start)

        while queue_elements:
            node = queue_elements.popleft()
            result.append(node)

            for neighbour in self.graph_adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue_elements.append(neighbour)
        return result

graph = BreadthFirstSearch()
graph.add_edge(0,1)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(0, 4)
res = graph.bfs(0)
print(res)

