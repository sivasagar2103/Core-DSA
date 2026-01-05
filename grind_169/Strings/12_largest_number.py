'''

'''

def largest_number(nums):
    nums = list(map(str, nums))

    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] < nums[j] + nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    
    print(nums)
    return ''.join(nums)


nums = [3,30,34,5,9]
res = largest_number(nums)
print(res)
