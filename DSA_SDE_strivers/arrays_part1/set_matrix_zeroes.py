
'''
Approach (Using two extra arrays):
using two separate arrays (like row[] and col[]) to remember
which row and column should be zeroed.

Time Complexity: O(2*(N*M))
Space Complexity: O(N) + O(M)

'''
def set_zeros(matrix):
    n = len(matrix) #row
    m = len(matrix[0]) #column

    row = [0] * n
    col = [0] * m

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0


'''
Instead of using two separate arrays (like row[] and col[]) to remember
which row and column should be zeroed, this solution smartly reuses the matrix itself.
It does this by:
1. Using the first row and first column in the matrix as markers (flags).
2. Keeping one extra variable (col0) to safely track the first column (
since the top-left cell matrix is shared by both first row and column)
Steps:
1. Mark rows and columns that have a 0.
- If you find a zero at any cell [i][j], you mark:
    matrix[i] = 0 → This row should become zero
    matrix[j] = 0 → This column should become zero
- But if it's in the first column (j == 0), you can't use matrix because it's shared by 
  both first row and column. So use a separate variable col0 to track it.
2. Zero out cells (excluding first row & column)
- Go from cell (1,1) to bottom-right.
- If the “marker” for the current row/column is 0, set matrix[i][j] = 0
- This uses the markers you created in Step 1.
3. At the end, you deal with row 0 and column 0 separately because:
- They were used as markers, so modifying them earlier might have corrupted information.
- Now it's safe to zero them if needed, using matrix and col0.

Time Complexity: O(2*(N*M))
Space Complexity: O(1) as we are not using any extra space.

'''

def set_zeros_optimal(matrix):
    n = len(matrix) #rows
    m = len(matrix[0]) #cols

    col0 = 1

    #step1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j!=0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    
    #step 2
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 1:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    #step 3
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
set_zeros_optimal(matrix)
print(matrix)