'''

'''

def spiral_matrix(matrix):
    #first index: row
    #second index: col
    rows = len(matrix)
    cols = len(matrix[0])

    top, bottom = 0, rows-1
    left, right = 0, cols-1

    result = []

    while top <= bottom and left <= right:

        #traverse left to right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1

        #traverse top to bottom
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            #traverse right to left
            for j in range(right, left-1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        
        if left <= right:
            #traverse bottom to top
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result


matrix = [[1,2,3],[4,5,6],[7,8,9]]
res = spiral_matrix(matrix)
print(res)
