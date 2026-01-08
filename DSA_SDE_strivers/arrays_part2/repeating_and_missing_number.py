'''
Problem: Find the repeating and missing number
Given an integer array nums of size n containing values from [1, n] 
and each value appears exactly once in the array, except for A, 
which appears twice and B which is missing.

Approach:
1. Brute Force

2. Mathematical Approach
Let, repeating num = A ; missing num = B
step1:
- n natural numbers sum -- S = n * (n+1)//2 
- sum of squares of n natural numbers -- P = n * (n+1) * (2*n+1) // 6
step2:
- sum of numbers in array -- sum_arr
- sum of squares of numbers in array -- sq_sum_arr
step3:
- sum_arr = S - B + A
- sq_sum_arr = P - B**2 + A**2
step4:
A - B = sum_arr - S --> X
A**2 - B**2 = sq_sum_arr - P --> Y
 
By solving the above equations,
A = X + (Y//X) // 2
B = A - X

Time : O(N)
Space: O(1)

'''

def find_rm_bf(arr):
    n = len(arr)
    r , m = -1, -1

    for i in range(1, n+1):
        cnt = 0
        for j in range(n):
            if i == arr[j]:
                cnt += 1
        
        if cnt == 2:
            r = i
        if cnt == 0:
            m = i
        
        if r != -1 and m != -1:
            break
    
    print([r,m])


def find_repeating_and_missing(arr):
    n = len(arr)

    n_sum = n * (n+1)//2
    n_square_sum = n * (n+1) * (2*n+1) // 6

    sum_arr = 0
    square_sum_arr = 0
    for num in arr:
        sum_arr += num
        square_sum_arr += num * num

    x = sum_arr - n_sum
    y = square_sum_arr - n_square_sum

    sum_ab = y//x

    a = (x + sum_ab) // 2
    b = a - x

    return [a, b]
    

nums = [3, 5, 4, 1, 1]
find_rm_bf(nums)
res = find_repeating_and_missing(nums)
print(res)