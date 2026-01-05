'''
1. Using extra arrays
- Mark rows & columns using two helper arrays

Time: O(m*n)
Space: O(m+n)

2. without using extra arrays
- Use first row/column as markers + a flag

Time: O(m*n)
Space: O(1)

123
456
789

[[1,2,3], [4,5,6], [7,8,9]]
outside: i
inside: j
'''

def set_matrix_zeroes_two(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    row_mark = [0] * rows
    col_mark = [0] * cols

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_mark[i] = 1
                col_mark[j] = 1
    
    for i in range(rows):
        for j in range(cols):
            if row_mark[i] == 1 or col_mark[j] == 1:
                matrix[i][j] = 0
    

def set_matrix_zeroes(matrix):
    #conidered first col -- i changes, j constant - 0
    #considered first row -- i constnat - 0, j changes
    rows = len(matrix)
    cols = len(matrix[0])

    col0 = 1

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 1:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    
    if matrix[0][0] == 0:
        for j in range(cols):
            matrix[0][j] = 0
    
    if col0 == 0:
        for i in range(rows):
            matrix[i][0] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
set_matrix_zeroes(matrix)
#set_matrix_zeroes_two(matrix)
print(matrix)
