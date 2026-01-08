
def rotate_array_by_one(arr):
    first = arr[0]
    n = len(arr)
    for i in range(1, n):
        arr[i-1] = arr[i]
        if i == n-1:
            arr[i] = first

nums = [1, 2, 3, 4, 5,7,8]
rotate_array_by_one(nums)
print(nums)