'''
Note:
- Arrays care about positions.
- Graphs care about connections. [keywords: Reorder, Pairs, End matches start]
- We want a path that:
  . Uses every edge exactly once
  . Respects direction
- This is called Eulerian Path.
- An Eulerian Path is, a path in a graph that uses every edge exactly once.
- Rules:
  . outdegree(node) = how many edges go out
  . indegree(node) = how many edges come in
- At most one node can have: outdegree = indegree + 1 (start node)
- At most one node can have: indegree = outdegree + 1 (end node)
- All other nodes must have: indegree == outdegree (middle nodes)

Problem Statement:
You are given pairs [start, end].
You must reorder them so that:
. Every pair must be used exactly once
. A valid arrangement is guaranteed to exist
. You may return any valid arrangement

Approach Used: Graph + Eulerian Path

Core Idea: [Graph problem]
- Convert array into a graph or adjacency list(directed graph).
- store indegree & outdegree
- Find start node
- Use Hierholzer's Algorithm (the standard algorithm to find Eulerian Path.)
  . Start from start node
  . Keep walking edges
  . Remove edges as you go (Each edge is used only once and We don't loop forever)
  . If stuck, backtrack
  . Reverse final path
- We reverse because we add nodes to the path only after finishing all outgoing edges.
- This is called post-order
- It means:
  . You go forward as much as possible
  . Only when stuck, you add nodes to the path
  . So the path is collected from end → start
- In Eulerian Path algorithms, nodes are added after edge exhaustion.
  Therefore, the path is collected in reverse.

Time: O(n) (each edge visited once)
Space: O(n) (graph + recursion stack)

'''

from collections import defaultdict

def valid_arrangement(pairs):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    outdegree = defaultdict(int)

    # Build graph and degrees
    for u, v in pairs:
        graph[u].append(v)
        outdegree[u] += 1
        indegree[v] += 1
    
    start = pairs[0][0]
    for node in graph:
        if outdegree[node] == indegree[node] + 1:
            start = node
            break
    
    path = []

    def dfs(node):
        while graph[node]:
            next_node = graph[node].pop()
            dfs(next_node)
        path.append(node)

    dfs(start)
    path.reverse()

    result = []
    for i in range(len(path) - 1):
        result.append([path[i], path[i+1]])
    
    return result


pairs = [[5,1],[4,5],[11,9],[9,4]]
result = valid_arrangement(pairs)
print(result)
