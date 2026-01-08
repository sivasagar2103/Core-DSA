'''
Problem:
Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
The sorting must be done in-place, without making a copy of the original array.
Approach:
This algorithm contains 3 pointers i.e. low, mid, and high, and 3 main rules.
The rules are the following:
arr[0….low-1] contains 0. [Extreme left part]
arr[low….mid-1] contains 1.
arr[high+1….n-1] contains 2. [Extreme right part], n = size of the array


Time Complexity: O(N)
Space Complexity: O(1)

'''

def sort_array(arr):
    n = len(arr)
    low = 0
    mid = 0
    high = n-1

    while mid <= high:
        #o to low-1 -- 0's
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        #low to mid-1 -- 1's
        elif arr[mid] == 1:
            mid += 1
        #high+1 to n-1 -- 2's
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

nums = [1, 0, 2, 1, 0]
sort_array(nums)
print(nums)