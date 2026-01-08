def flood_fill(image, sr, sc, new_color):
    n = len(image)
    diff_row = [-1,0,1,0]
    diff_col = [0,1,0,-1]
    current_color = image[sr][sc]
    nrows = len(image)
    ncolumns = len(image[0])

    def dfs(row, col, color):
        if 0 <= row < nrows and 0 <= col < ncolumns:
            if image[row][col] == current_color and not image[row][col] == color:
                image[row][col] = color
                for i in range(4):
                    neighbour_row = row + diff_row[i]
                    neighbour_column = col + diff_col[i]
                    dfs(neighbour_row, neighbour_column, color)

    dfs(sr, sc, new_color)

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
new_color = 2
res = flood_fill(image, sr, sc, new_color)
print(image)