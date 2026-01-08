

def find_large(arr):
    n = len(arr)
    if n == 0:
        return -1
    if n == 1:
        return arr[0]
    
    first = arr[0]
    first_neg = 0
    
    for i in range(1, n):
        if arr[i] > first:
            first = arr[i]
        if arr[i] < 0:
            if first_neg == 0:
                first_neg = arr[i]
            if first_neg < arr[i]:
                first_neg = arr[i]
    return first, first_neg

nums = [3, 3, 6, 1, 6, -1, -2, -3, 0]
pos, neg = find_large(nums)
print(pos)
print(neg)
