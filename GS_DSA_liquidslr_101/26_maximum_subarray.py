'''
Problem Statement:
Given an integer array arr, find the contiguous subarray
(which contains at least one number) that has the largest sum
and return its sum.
Additionally, print the subarray that produces this maximum sum.

Approach Used: Kadane's Algorithm (Greedy + Dynamic Programming)

Core Idea:
- A subarray ending at index i is optimal if:
    max(arr[i], current_sum + arr[i])
- If extending the previous subarray makes the sum worse,
  start a new subarray from the current index.
- Keep updating the global maximum whenever a better sum is found.
- Track indices using:
  - temp → potential start index
  - start, end → final best subarray boundaries

Time: O(n)
Space: O(1)

'''

def maximum_subarray(arr):
    current = arr[0]
    maxi = arr[0]
    n = len(arr)
    start, end, temp = 0, 0, 0

    for i in range(1, n):
        if arr[i] > current + arr[i]:
            current = arr[i]
            temp = i
        else:
            current += arr[i]
        
        if current > maxi:
            maxi = current
            start = temp
            end = i
    
    print(arr[start: end+1])
    return maxi
        

nums = [2, 3, 5, -2, 7, -4]
maxi = maximum_subarray(nums)
print(maxi)
