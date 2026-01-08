'''
Problem:
Given an integer array nums, find the subarray with the largest sum 
and return the sum of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.

Approach:
Kadane's Algorithm is an efficient method to solve the Maximum Subarray Problem — i.e., 
find the contiguous subarray within a 1D array of numbers that has the largest sum.
Traverse the array while maintaining:
- max_current: the maximum subarray sum ending at current index
- max_global: the overall maximum subarray sum so far
At each step:
- Either extend the current subarray (max_current + arr[i]) or start a new one at arr[i].
- Update max_global if max_current exceeds it.

Time Complexity: O(n)
Space Complexity: O(1)

'''

def max_subarray(arr):
    n = len(arr)
    current = arr[0]
    maxi = arr[0]
    start = 0
    end = 0

    for i in range(1, n):
        if arr[i] > current + arr[i]:
            current = arr[i]
            start = i
        else:
            current += arr[i]
        
        if current > maxi:
            maxi = current
            start, end = start, i
    
    return maxi,arr[start:end+1]


nums = [2, 3, 5, -2, 7, -4]
total, sub = max_subarray(nums)
print(total)
print(sub)
