'''
Note:
- DFS/BFS are best for static traversal problems.
- BFS is preferred when shortest path or distance matters.
- Union-Find works in dynamic connectivity scenarios 
  where relationships change over time.

Problem Statement
You are given an m * n grid of '1's (land) and '0's (water).
Your task is to count the number of islands.
An island is a group of '1's connected horizontally or vertically (not diagonally)
and surrounded by water.

Approach Used: DFS or BFS

Core Idea
- Treat each '1' cell as a node in a grid-graph.
- Adjacent (up/down/left/right) land cells belong to the same island.
- When you find an unvisited '1', that starts a new island.

Time: O(m * n)
Space: O(m * n) -- recursion stack

'''

def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(row, col):

        if (row < 0 or row >= rows or 
            col < 0 or col >= cols or 
            grid[row][col] == '0'):
            return
        
        grid[row][col] = '0' #To mark visited cells and avoid using extra space.

        #explore neighbours
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    
    return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
res = numIslands(grid)
print(res)
