#BFS

from collections import deque


class Solution:

    def floodFill(self, image, sr, sc, color):
        current_color = image[sr][sc]
        color_indexes = deque()
        rows, cols = len(image), len(image[0])

        for i in range(rows):
            for j in range(cols):
                if image[i][j] == current_color:
                    color_indexes.append((i, j))
        
        diff_row = [-1,0,1,0]
        diff_col = [0,1,0,-1]

        while color_indexes:
            for _ in range(len(color_indexes)):
                x, y = color_indexes.popleft()
                for i,  j in zip(diff_row, diff_col):
                    dx, dy = x + i, y + j
                    if 0 <= dx < rows and 0 <= dy < cols and image[dx][dy] == current_color:
                        image[dx][dy] = color

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

sol = Solution()
res = sol.floodFill(image, sr, sc, color)
print(image)