
def move_zeroes(arr):
    n = len(arr)
    pos = 0

    for i in range(n):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    
    for i in range(pos, n):
        arr[i] = 0


nums = [0,1,0,3,12]
move_zeroes(nums)
print(nums)