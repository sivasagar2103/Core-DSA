'''
Core Idea:
For each index, compute the product of all elements 
to the left and all elements to the right,
without using division.

Steps of implementation:
1. Initialize a result array res of size n with all values as 1.
2. Traverse from left to right to compute prefix products:
   - Maintain a variable prefix initialized to 1.
   - At each index i:
     . Set res[i] = prefix (product of all elements before i)
     . Update prefix *= nums[i]
3. Traverse from right to left to compute suffix products:
   - Maintain a variable suffix initialized to 1.
   - At each index j:
     . Multiply res[j] by suffix (product of all elements after j)
     . Update suffix *= nums[j]
4. After both passes, res contains the product of array except self for each index.
5. Return the result array.

Time: O(n)
Space: O(1)  (excluding the output array)

Prefix pass * Suffix pass = product except self.

'''

def product_array(nums):
    n = len(nums)
    res = [1] * n
    
    prefix = 1
    for i in range(n):
        res[i] = prefix 
        prefix *= nums[i]
    
    suffix = 1
    for j in range(n-1, -1, -1):
        res[j] *= suffix
        suffix *= nums[j]

    return res


nums = [1,2,3,4]
res = product_array(nums)
print(res)
#Output: [24,12,8,6]
