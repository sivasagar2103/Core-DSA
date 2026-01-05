'''
Core Idea:
Use two pointers starting at both ends.
The water area is limited by the shorter height, so always move the pointer
with the smaller height to possibly find a larger container.

Steps of implementation:
1. Initialize two pointers:
   - left at the start of the array
   - right at the end of the array
2. Initialize max_area as 0.
3. While left < right:
   - Calculate height = min(arr[left], arr[right]).
   - Calculate width = right - left.
   - Update max_area = max(max_area, height * width).
4. Move the pointer pointing to the smaller height:
   - If arr[left] < arr[right]:
     . Move left pointer to the right.
   - Else:
     . Move right pointer to the left.
5. Continue until the pointers meet.
6. Return max_area.

Time: O(n)
Space: O(1)

Area is limited by the shorter wall — move the smaller pointer.

'''

def container_with_most_water(arr):
    n = len(arr)
    left = 0
    right = n-1
    res = 0

    while left < right:
        height = min(arr[left], arr[right])
        width = right - left
        res = max(res, height * width)
    
        # move the pointer at the smaller height
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return res


height = [1,8,6,2,5,4,8,3,7]
res = container_with_most_water(height)
print(res)
