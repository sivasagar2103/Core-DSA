'''
Problem Statement:
Given an array height where each element represents the height of a vertical line
at that index, find two lines that together with the x-axis form a container 
such that the container holds the maximum amount of water.

Approach Used: Two Pointer

Core Idea:
- area = min(height[left], height[right]) * (right - left)
- Keeping the taller line and moving the shorter one is the 
  way to potentially increase the area, since width always decreases.
Time: O(n)
Space: O(1)

'''

def container_with_most_water(arr):
    n = len(arr)
    left, right = 0, n-1
    res = 0

    while left < right:
        height = min(arr[left], arr[right])
        width = right - left
        area = height * width
        res = max(res, area)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    
    return res


height = [1,8,6,2,5,4,8,3,7]
res = container_with_most_water(height)
print(res)
