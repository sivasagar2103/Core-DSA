'''
Problem:
Given an array nums of size n and an integer k, find the length of the longest 
sub-array that sums to k. If no such sub-array exists, return 0.

Approach:
1. Sliding Window : supports only for positive values in the array
- Initialize pointers and variables: start=0, current_sum=0, max_length=0, left,right =0,0
- Expand the window using end pointer: iterate end from 0 to n-1. add nums[end] to current_sum.
- shrink the window: if current_sum > target or k. subtract nums[start] and increment start+=1
- Check if current sum equals k: if current_sum == k, update max_length and 
  record current start and end to left and right
- return the max_length

Time: O(n)
Space: O(1)

2. Prefix Sum + hash map: supports for both positive and negative
- Initialize variables: prefix_sum = 0, max_lenth = 0, prefix_sums = {0:-1}
- Iterate over the array: 
  . Add nums[i] to prefix_sum (this is the sum of all elements from the start up to index i).
  . Calculate needed_sum = prefix_sum - k.
  . If needed_sum has been seen before (i.e., it is in sum_indices):
    There is a subarray whose sum is k from index sum_indices[needed_sum] + 1 to i.
    Compute its length and, if it's the longest so far, update max_length.
  . If prefix_sum is not already in sum_indices, record the current index i 
    as the first place it appears.
- return the result

Time: O(n)
Space: O(n)

'''

def longest_subarray_sw(nums, k):
    n = len(nums)
    start = 0
    current_sum = 0
    max_length = 0
    left , right = 0,0

    for end in range(n):
        temp_start = start
        current_sum += nums[end]

        while current_sum > k:
            current_sum -= nums[start]
            start += 1
        
        if current_sum == k:
            left, right = temp_start, end
            max_length = max(max_length, end-start+1)
    
    return max_length, nums[left:right + 1]


def longest_subarray_ps(nums, k):
    prefix_sum = 0
    max_length = 0
    sum_indices = {0:-1}
    n = len(nums)
    left, right = 0, -1

    for i in range(n):
        prefix_sum += nums[i]

        if prefix_sum - k in sum_indices:
            gap = i - sum_indices[prefix_sum - k]
            if gap > max_length:
                left, right = sum_indices[prefix_sum - k] + 1, i
                max_length = gap

        if prefix_sum not in sum_indices:
            sum_indices[prefix_sum] = i
    
    if right == -1:
        return 0, []
    
    return max_length, nums[left:right+1]




nums = [10, 5, 2, 7, 1, 9]
k=15
maxi, sub = longest_subarray_sw(nums, k)
print(maxi)
print(sub)

maxima, sub_arr = longest_subarray_ps(nums, k)
print(maxima)
print(sub_arr)
