#BFS

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        ro_indexes = deque()
        fresh_oranges = 0
        minutes = -1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    ro_indexes.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1
        
        if not fresh_oranges:
            return 0
        
        diff_row = [-1,0,1,0]
        diff_col = [0,1,0,-1]
        
        while ro_indexes:
            for _ in range(len(ro_indexes)):
                x, y = ro_indexes.popleft()
                for i, j in zip(diff_row, diff_col):
                    dx , dy = x + i, y + j
                    if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                        grid[dx][dy] = 2
                        fresh_oranges -= 1
                        ro_indexes.append((dx, dy))
            minutes += 1
        
        return minutes if not fresh_oranges else -1


grid = [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[2,1,1],[0,1,1],[1,0,1]]
sol = Solution()
res = sol.orangesRotting(grid2)
print(res)