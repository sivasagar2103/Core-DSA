'''
Problem:
Implement the power function pow(x, n) , which calculates the x raised to n.

Approach:
Binary Exponentiation

Time: O(log n)
Space: O(1)

'''

def power_of_x(x, n):
    result = 1.0
    index = n
    if index < 0:
        index = -1 * index
    while index:
        if index % 2 == 1:
            result = result * x
            index -= 1
        else:
            x *= x
            index //= 2
    
    if n < 0:
        return 1/result
    return result


x = 2.0000
n = -2
res = power_of_x(x, n)
print(res)