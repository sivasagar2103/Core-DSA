'''
Problem:
Rotate matrix by 90 degrees

Approach:
1. Transpose of a matrix: converting columns into rows
2. Reverse each row in the matrix

Time Complexity:  O(N*N) + O(N*N) = O(N**2)
Space Complexity: O(1)

'''
def rotate_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])

    #Transpose of a matrix: converting columns into rows
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    #reverse the elements in each row
    for i in range(n):
        start = 0
        end = m-1
        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_matrix(matrix)
print(matrix)
#matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]