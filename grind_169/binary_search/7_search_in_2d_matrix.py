'''
Problem: Search a 2D Matrix where each row is sorted.

Intuition:
- The matrix behaves like one big sorted 1D array.
- Then, binary search will works.

Core Idea:
- m rows, n cols in 2D.
- m*n-1 elements in 1D array of 2D matrix.
- To convert 1D index into 2D matrix position or index
  row = index // n
  col = index % n
- This allows binary search without extra space.

Time: O(log(m*n))
Space: O(1) 

'''

def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    total = rows * cols
    low, high = 0, total-1

    while low <= high:
        mid = (low + high)//2
        row = mid // cols
        col = mid % cols

        val = matrix[row][col]

        if val == target:
            return True
        elif val < target:
            low = mid+1
        else:
            high = mid-1
    
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 11
#Output: false
res = search_matrix(matrix, target)
print(res)
