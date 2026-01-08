

def sort_colors(arr):
    n = len(arr)
    left = 0 #pointer for 0
    mid = 0 #current pointer
    right = n - 1 #pointer for 2

    while mid <= right:
        if arr[mid] == 0:
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1

nums = [2,0,2,1,1,0]
sort_colors(nums)
print(nums)