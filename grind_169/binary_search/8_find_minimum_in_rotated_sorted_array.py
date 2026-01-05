'''

'''

def find_minimum(arr):
    n = len(arr)

    low, high = 0, n-1

    while low < high:
        mid = (low + high)//2

        if nums[mid] > nums[high]:
            low = mid + 1 # # min is in right half
        else:
            high = mid

    return arr[low]


nums = [3,4,5,1,2]
#Output: 1
res = find_minimum(nums)
print(res)