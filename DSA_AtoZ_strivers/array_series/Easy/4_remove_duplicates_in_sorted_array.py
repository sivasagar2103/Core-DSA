
def remove_duplicates(arr):
    start = 1
    n = len(arr)

    for i in range(1, n):
        if arr[i] != arr[i-1]:
            arr[start] = arr[i]
            start += 1
    
    print(arr)
    return start


nums = nums = [1,1,2]
count = remove_duplicates(nums)
print(count)
