from collections import deque

class Solution:
    def findCircleNum_dfs(self, isConnected):
        visited = set()
        n = len(isConnected)
        provinces = 0

        def dfs_helper(city):
            for neighbour in range(n):
                if isConnected[city][neighbour] == 1 and neighbour not in visited:
                    visited.add(neighbour)
                    dfs_helper(neighbour)

        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs_helper(city)
                provinces += 1
        
        return provinces
    
    def findCircleNum_bfs(self, isConnected):
        n = len(isConnected)
        provinces = 0
        visited = set()

        for city in range(n):
            if city not in visited:
                queue_elements = deque([city])
                while queue_elements:
                    node = queue_elements.popleft()
                    visited.add(node)
                    for neighbour in range(n):
                        if isConnected[node][neighbour] == 1 and neighbour not in visited:
                            queue_elements.append(neighbour)
                provinces +=1
        
        return provinces



isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected2 = [[1,0,0],[0,1,0],[0,0,1]]
sol = Solution()
res = sol.findCircleNum_dfs(isConnected)
res2 = sol.findCircleNum_dfs(isConnected2)
res_bfs = sol.findCircleNum_bfs(isConnected)
res_bfs2 = sol.findCircleNum_bfs(isConnected2)
print(res)
print(res2)
print(res_bfs)
print(res_bfs2)
