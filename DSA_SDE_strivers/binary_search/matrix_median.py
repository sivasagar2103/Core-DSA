'''
Problem:
Given a 2D array matrix that is row-wise sorted.
The task is to find the median of the given matrix.

Approach:
- Find Minimum and Maximum from the entire 2D matrix.
- Perform binary search between the minimum and maximum values found.
- For each mid-value, count how many elements in the matrix are less than
  or equal to mid. Since each row is sorted, you can use binary search per row 
  for this count.
- If the total count is less than the required median position search in the
  higher half; otherwise, search in the lower half.

Time:
Outer Binary Search: O(log(max-min))
For Count: O(N * (logM))
N: number of rows, M: number of columns
Space: O(1)

Note: This method is optimal for row-wise (and even column-wise) sorted matrices.
'''

def check_row(mid, row):
    left, right = 0, len(row)
    while left < right:
        row_mid = (left + right)//2
        if row[row_mid] <= mid:
            left = row_mid + 1
        else:
            right = row_mid
    return left

def find_median(matrix):
    low, high = matrix[0][0], matrix[0][-1]
    n, m = len(matrix), len(matrix[0])
    desired = (n * m + 1)//2

    for i in range(n):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][-1])
    
    while low < high:
        mid = (low + high)//2
        count = sum(check_row(mid, row) for row in matrix)
        if count < desired:
            low = mid + 1
        else:
            high = mid

    return low

matrix=[ [1, 4, 9, 10], [2, 5, 6, 11], [3, 7, 8, 12] ] 
res = find_median(matrix)
print(res)