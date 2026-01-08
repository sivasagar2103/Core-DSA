'''
Problem:
Given two integers m and n, representing the number of rows and columns of a 2d array
named matrix. Return the number of unique ways to go from the top-left cell 
(matrix[0][0]) to the bottom-right cell (matrix[m-1][n-1]).

Approach:
1. Recursion:
- Start at the top-left cell (0,0).
- At each step, you have two choices:
  a. Move down by increasing the row.
  b. Move right by increasing the column.
- Keep moving recursively down or right until you reach the bottom-right cell (m-1, n-1).
- If you reach the bottom-right cell, return 1 (one valid path found).
- If you go out of bounds (beyond the grid), return 0 (invalid path).
- Sum the paths from the two choices to get the total paths from the current cell.

Time: Exponential recursion tree -- O(2**(rows+cols))
Space: Max recursion depth -- O(rows+cols)

2. Optimise by Memoization [DP]
- When the value dp[r][c] is not computed yet (-1),
  you calculate it recursively and store the result.
- The top-level call count_paths(0, 0) returns the total number
  of unique paths from the top-left corner to the bottom-right corner.
- Memoization ensures each subproblem is solved once, improving
  time complexity from exponential to O(rows * cols).
- Space complexity is O(rows * cols) due to the dp table and recursion call stack.

Time: O(rows * cols)
Space: O(rows * cols)

'''
def find_paths_rec(rows, cols):
    
    def count_paths(start_row, start_col):
        if start_row == rows - 1 and start_col == cols - 1:
            return 1
        elif start_row >= rows or start_col >= cols:
            return 0
        else:
            return count_paths(start_row+1, start_col) + count_paths(start_row, start_col+1)
    
    return count_paths(0,0)


def find_paths_dp(rows, cols):
    #top-down approach

    dp = [[-1] * cols for _ in range(rows)]

    def count_paths(start_row, end_col):
        if start_row >= rows or end_col >= cols:
            return 0
        elif start_row == rows - 1 and end_col == cols - 1:
            return 1
        elif dp[start_row][end_col] != -1:
            return dp[start_row][end_col]
        dp[start_row][end_col] = count_paths(start_row + 1, end_col) + count_paths(start_row, end_col+1)
        return dp[start_row][end_col]
    
    return count_paths(0,0)

def find_paths_ncr(rows, cols):
    pass
    

m = 3
n = 7
res = find_paths_rec(m, n)
print(res)
#The total number of Unique Paths are 28
result = find_paths_dp(m, n)
print(result)







