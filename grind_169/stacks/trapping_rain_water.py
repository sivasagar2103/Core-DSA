'''

Problem Statement:
Given an array height where each element represents the height of a bar and 
the width of each bar is 1, the task is to compute how much rainwater can be 
trapped between the bars after raining.

Core Idea
The amount of water trapped at any index = 

min(max height to the left, max height to the right) - current height

- Instead of precomputing left and right maximums for every index, 
this solution uses two pointers to compute the result in a single pass 
with constant extra space.


'''

def trapping_rain_water(height):
    n = len(height)
    left, right = 0, n-1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] <= height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1

        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water


height = [0,1,0,2,1,0,1,3,2,1,2,1]
res = trapping_rain_water(height)
print(res)
