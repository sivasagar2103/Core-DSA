'''
Approach:
1. Brute Force

2. Observation Way
Core Idea:
- If the given array only contains positive numbers: product of all
- If the given array contains even number of negative numbers: product of all
- If the given array contains odd number of negative numbers: Removal of one negative number
- That means, negative number divides the array in two parts, one is prefix and other suffix
- The answer will either be the prefix or the suffix of that negative number.
- If the array contains zero, we need to start form the next position.

Steps:
- prefix --> stores the product of the prefix subarray
- suffix --> stores the product of the suffix subarray
- If prefix == 0, prod = 1 --> consider the current element as a part of the new subarray.
- If suffix == 0, prod = 1 --> consider the current element as a part of the new subarray.
- return the maximum of result, prefix, suffix

Time: O(n)
Space: O(1)

'''

def max_product_subarray(arr):
    '''
    Time: O(n**2)
    Space: O(1)
    
    '''
    res = arr[0]
    n = len(arr)

    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= arr[j]
            res = max(res, prod)

    return res


def max_product_subarray_opt(arr):
    prefix = 1
    suffix = 1
    result = float('-inf')
    n = len(arr)

    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1  
        prefix *= arr[i]
        suffix *= arr[n-i-1]
        result = max(result, max(prefix, suffix))
    
    return result


nums = [1, 2, -3, 0, -4, -5]
res = max_product_subarray_opt(nums)
print(res)