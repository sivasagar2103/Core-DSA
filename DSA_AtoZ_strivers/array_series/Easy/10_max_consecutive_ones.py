
def max_ones(arr):
    n = len(arr)
    current = 0
    max_count = 0
    for i in range(n):
        if arr[i] == 1:
            current += 1
            max_count = max(current, max_count)
        else:
            current = 0
    return max_count
        
nums = [1,1,0,1,1,1]
res = max_ones(nums)
print(res)