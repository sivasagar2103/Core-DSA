'''
Problem Statement
Given a rotated sorted array with no duplicate elements, 
find the minimum element in the array.

Approach Used: Binary Search

Core Idea
- Compare the middle element with the rightmost element:
  . If arr[mid] > arr[high], the minimum must lie to the right of mid
  . Otherwise, the minimum lies at mid or to the left
- Narrow the search space until low == high
- That index points to the minimum element

Time: O(logn)
Space: O(1)

'''

def find_minimum(arr):
    n = len(arr)
    low, high = 0, n-1

    while low < high:
        mid = (low + high)//2

        if arr[mid] > arr[high]:
            low = mid + 1
        elif arr[mid] < arr[high]:
            high = mid
        else:
            high -= 1   # to handle duplicates
    
    return arr[low]

nums = [3,4,5,1,2]
#Output: 1
res = find_minimum(nums)
print(res)
