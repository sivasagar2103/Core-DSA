'''
Problem:
Given an array of non-negative integers representation elevation of ground. 
Your task is to find the water that can be trapped after rain.

Approach:
Core Idea:
1. For each bar, the trapped water is limited by the shorter of these two bars minus
   the height of the current
2. To avoid precomputing maximums for each position, two pointers (l and r) 
   start at the leftmost and rightmost indices. Alongside, two variables, 
   leftMax and rightMax, keep track of the highest bars encountered from each end.

Steps: Two Pointer Approach
- Initialize pointers and variables:
  . Set two pointers, left at index 0 and right at index n-1.
  . Initialize leftMax and rightMax to 0, and a variable to store total trapped water.
- Iterate while left ≤ right:
  . If height[left] is less than or equal to height[right]:
    . If height[left] is greater than or equal to leftMax, update leftMax to height[left].
    . Else, add leftMax - height[left] to the result.
  . Move left pointer to the right (left++).
  . Else
    . If height[right] is greater than or equal to rightMax, update rightMax to height[right].
    . Else, add rightMax - height[right] to the result.
    . Move right pointer to the left (right--)

Time: O(N)
Space: O(1)

'''

def trap_water_units(arr):
    n = len(arr)
    left = 0
    right = n-1
    left_max, right_max = 0, 0
    res = 0
    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] > left_max:
                left_max = arr[left]
            else:
                res += left_max - arr[left]

            left += 1
        
        else:
            if arr[right] > right_max:
                right_max = arr[right]
            else:
                res += right_max - arr[right]

            right -= 1
    
    return res


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = trap_water_units(arr)
print(res)

