from collections import defaultdict

class DepthFirstSearch:

    def __init__(self):
        self.graph_adj = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph_adj[u].append(v)
        self.graph_adj[v].append(u) #comment this if the graph is directed

    def dfs(self, start):
        result = []
        visited = set()

        def dfs_helper(node):
            visited.add(node)
            result.append(node)
            for neighbour in self.graph_adj[node]:
                if neighbour not in visited:
                    dfs_helper(neighbour)
        
        dfs_helper(0)
        return result
    
    def dfs_using_stack(self, start):
        result = []
        stack = [start]
        visited = set()

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
            
                for neighbour in reversed(self.graph_adj[node]):
                    if neighbour not in stack:
                        stack.append(neighbour)
        
        return result

graph = DepthFirstSearch()
graph.add_edge(0,1)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(0, 4)
res = graph.dfs(0)
res1 = graph.dfs_using_stack(0)
print(res)
print(res1)