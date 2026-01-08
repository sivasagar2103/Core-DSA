def maze_paths(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    diff_rows = [-1,0,1,0]
    diff_cols = [0,1,0,-1]
    directions = ['U', 'R', 'D', 'L']
    seen = [[False for _ in range(n_cols)] for _ in range(n_rows)]
    result = []


    '''
    Strings in Python are immutable. So when you do:
    new_path = path + 'R'
    it creates a new string instead of modifying path in place. This means:
    Each recursive call works with its own copy of the path string.
    Changes in one call don’t affect the value of path in the calling function.

    Say the current path is "D" and direction is "R".
    path + direction = "D" + "R" = "DR"
    This new string "DR" is passed to the next call
    The current call still has path = "D"
    So the two strings are separate.

    '''
    def backtrack(sr, sc, path):
        if sr == n_rows - 1 and sc == n_cols - 1:
            result.append(path)
            return
        
        seen[sr][sc] = True
        for i in range(4):
            nei_row = sr + diff_rows[i]
            nei_col = sc + diff_cols[i]
            if (0 <= nei_row < n_rows) and (
                0 <= nei_col < n_cols) and (
                matrix[nei_row][nei_col] == 1) and (not seen[nei_row][nei_col]
                ):
                backtrack(nei_row, nei_col, path + directions[i])
        
        seen[sr][sc] = False

    if matrix[0][0]:
        backtrack(0,0,'')
    
    #lexicographically sort -- based on the oxford dictionary order
    result.sort()
    return result


input_matrix = [[1,0,0,0], [1,1,0,1], [1,1,0,0], [0,1,1,1]]
result = maze_paths(input_matrix)
print(result)