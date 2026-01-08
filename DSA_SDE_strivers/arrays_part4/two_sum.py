'''
Problem:
Given an array of integers nums and an integer target. Return the indices(0 - indexed) 
of two elements in nums such that they add up to target.

Solution:
1. Hashing

Time: O(N)
Space: O(N)

2. Two Pointer:
- We can't get the indexes.
- We will check the target, is it possible or not.

Time: O(nlogn) + O(n)
Space: O(1)

'''

def two_sum(arr, target):
    n = len(arr)
    val_ind = {}

    for i in range(n):
        diff = target - arr[i]
        if diff in val_ind:
            return [val_ind[diff], i]
        else:
            val_ind[arr[i]] = i
    return - 1

def two_sum_pointers(arr, target):
    arr.sort()
    n = len(arr)
    left = 0
    right = n -1
    while left < right:
        sum_res = arr[left] + arr[right]
        if sum_res == target:
            return True
        elif sum_res < target:
            left += 1
        else:
            right -= 1
    return False


nums = [1, 6, 2, 10, 3]
target = 7
res = two_sum(nums, target)
print(res)