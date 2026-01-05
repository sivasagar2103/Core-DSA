'''

Transpose + reverse each row

'''

def rotate_image(matrix):

    #transpose a matrix
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    #reverse each row
    for i in range(rows):
        left = 0
        right = cols-1

        while left <= right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
    

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate_image(matrix)
print(matrix)
