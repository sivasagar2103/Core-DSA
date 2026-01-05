'''
Dutch National Flag Problem

- Use Three Pointers 

Intuition:
- Move 0's to the left, 2's to the right; leave 1's in the middle.

- Time: O(n)
- Space: O(1)

'''


def sort_colors(arr):
    n = len(arr)
    low = 0
    mid = 0
    high = n-1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        
        elif arr[mid] == 1:
            mid += 1
        
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

nums = [2,0,2,1,1,0]
sort_colors(nums)
print(nums)
