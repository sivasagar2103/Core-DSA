'''
Pascal's Triangle is a triangle of numbers where:
1. The first and last element of every row is 1.
2. Every inner element is the sum of the two numbers from the row directly above it:
  - row[i][j] = row[i-1][j-1] + row[i-1][j]

Row 0:       [1]
Row 1:      [1, 1]
Row 2:     [1, 2, 1]     ← 2 = 1 + 1
Row 3:   [1, 3, 3, 1]    ← 3 = 1+2 and 3=2+1

Time Complexity: O(n²)
Space Complexity: O(n²)

'''

def pascal_triangle(n):
    result = []

    for i in range(n):
        row = [1] * (i+1)
        for j in range(1, i):
            row[j] = result[i-1][j-1] + result[i-1][j]
        result.append(row)

    return result

'''
Approach:
- For each level from 2 to k, it updates elements from right to left.
- The update rule is row[j] = row[j] + row[j-1], which corresponds to the
sum of two numbers from the previous row.

Time: O(k²)
Space: O(k)

'''

def get_kth_level(k):
    row = [1] * (k+1)
    for i in range(2, k+1):
        for j in range(i-1, 0, -1):
            row[j] = row[j] + row[j-1]
    return row

n = 5
res = pascal_triangle(n)
print(res)
level = 3
result = get_kth_level(level)
print(result)