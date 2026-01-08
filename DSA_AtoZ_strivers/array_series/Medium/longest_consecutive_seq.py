

def longest_sequence(arr):
    arr_set = set(arr)
    longest = 0
    for num in arr_set:
        if num - 1 not in arr_set:
            length = 1
            while num + length in arr_set:
                length += 1
            longest = max(longest, length)
    
    return longest


nums = [100,4,200,1,3,2, 5]
res = longest_sequence(nums)
print(res)