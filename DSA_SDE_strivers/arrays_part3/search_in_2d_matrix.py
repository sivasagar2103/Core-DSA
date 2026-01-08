'''
Problem: 
Given a 2-D array mat where the elements of each row are sorted in non-decreasing order,
and the first element of a row is greater than the last element of the previous row 
(if it exists), and an integer target, determine if the target exists in the given mat or not.

Approach:
1. Flatten the given 2D matrix to a 1D array, the 1D array will also be sorted.
2. Utilizing binary search on this sorted 1D array to locate the 'target' element
3. Instead of flattening and saving the 1D array, we use the pointers in range of (n*m) and search the
target in 2D array by the following formula:
- If index = i, and no. of columns in the matrix = m, the index i corresponds to the cell with
row = i / m and col = i % m.

Time: O(log(NxM))
Space: O(1)

'''

def search(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    low = 0
    high = n * m -1

    while low <= high:
        mid = (low + high)//2
        row = mid // m
        col = mid % m
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
target = 8
res = search(mat, target)
print(res)

