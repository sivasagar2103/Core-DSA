
def find_leaders(arr):
    n = len(arr)

    max_from_right = arr[-1]
    temp = [0] * n
    count = 0
    temp[count] = max_from_right
    count += 1

    i = n -2
    while i >= 0:
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            temp[count] = max_from_right
            count += 1
        i -= 1
    
    print(temp)
    print(count)
    result = [0] * count
    for j in range(count):
        print(count - 1 - j)
        result[j] = temp[count - 1 - j]

    return result


nums = [1, 2, 5, 3, 1, 2]
res = find_leaders(nums)
print(res)