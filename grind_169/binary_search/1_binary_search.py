'''
Always the array is sorted in an ascending order

low, high, mid

Intuition:
- Binary search halves the search space each time.
- if mid is too small go right, if too big go left, if equal return.

Time: O(logn)
Sapce: O(1)

'''


def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid -1 
    return False


nums = [-1,0,3,5,9,12]
target = 9
res = binary_search(nums, target)
print(res)
