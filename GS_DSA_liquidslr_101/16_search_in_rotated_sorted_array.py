'''
Problem Statement

Given a rotated sorted array arr (with distinct elements) and a target value,
determine whether the target exists in the array.

Approach Used: Modified Binary Search

Core Idea:
- At each step:
  . Check if arr[mid] equals the target
  . Identify which half (left → mid or mid → right) is sorted
  . Decide whether the target lies in the sorted half
  . Narrow the search space accordingly

Time: O(logn)
Space: O(1) 

'''

def search_array(arr, target):
    n = len(arr)
    low, high = 0, n-1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == target:
            return True
        
        elif arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return False


nums = [4,5,6,7,0,1,2]
target = 0
res = search_array(nums, target)
print(res)
