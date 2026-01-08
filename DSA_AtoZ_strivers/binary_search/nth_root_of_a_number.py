'''
Binary Search to find the root
A helper function safe_power() to compute mid**n without overflow.
Why Safe Power?
- It Uses binary exponentiation
- Exits early if mid value is greater than limit
- computing mid ** n is highly cost
- Runs in O(logN)

Exponentiation by Squaring is an algorithm.
#need to check in detail

'''

def safe_power(mid_value, power, limit):
    #The safe_power() function prevents overflow by checking early
    # if intermediate results exceed the base.
    #Time: O(log power)
    result = 1
    while power > 0:
        if power % 2 == 1:
            result *= mid_value
            if result > limit:
                return limit + 1
        power //= 2
        mid_value *= mid_value
        if mid_value > limit and power > 0:
            return limit + 1
    return result

def find_root(base, index):
    #O(log base)
    low = 1
    high = base
    while low <= high:
        mid = (low + high) // 2
        #val = mid ** index
        val = safe_power(mid, index, base)
        if val == base:
            return mid
        if val < base:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


index = 3
base = 27

res = find_root(base, index)
#Total time: O(log base. log index), Space: O(1)
print(res)