'''
If the array is sorted, then you can use the 
Two Pointers technique in a single pass.

'''

def two_sum_sorted(arr, target):
    n = len(arr)
    i = 0
    j = n - 1

    while i < j:
        current = arr[i] + arr[j]
        if current == target:
            return [i, j]
        elif current < target:
            i += 1
        else:
            j -= 1
    
    return []

def two_sum_unsorted(arr, target):
    map = {}
    n = len(arr)

    for i in range(n):
        complement = target - arr[i]
        if complement in map:
            return [map[complement], i]
        map[arr[i]] = i

    return []


nums = [2,7,11,15]
target = 9
res = two_sum_unsorted(nums, target)
print(res)

nums1 = [1,2,3,4,5]
target1 = 7
res1 = two_sum_sorted(nums1, target1)
print(res1)
