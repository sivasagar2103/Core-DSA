'''
Problem:
Given two numbers N and M, find the Nth root of M. 
The Nth root of a number M is defined as a number X such that
 when X is raised to the power of N, it equals M. 
 If the Nth root is not an integer, return -1.

Approach:
- Binary Search for the Root - O(log base)
- Exponentiation by squaring - O(log index)


Time: O(log base * log index)
Space: O(1)

'''


def safe_root(base, index, limit):
    result = 1
    while index > 0:
        if index % 2 == 1:
            result *= base
            if result > limit:
                return limit + 1
        index //=2
        base *= base
        if base > limit and index > 0:
            return limit + 1
    return result



def find_root(base, index):
    low = 1
    high = base

    while low <= high:
        mid = (low+high)//2
        val = safe_root(mid, index, base)
        if val == base:
            return mid
        elif val < base:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1



base = 64
index = 3

res = find_root(base, index)
print(res)