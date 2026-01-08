
def find_single_number(nums):
    result = 0
    for num in nums:
        result = result ^ num
    return result


nums = [4,1,2,1,2]
res = find_single_number(nums)
print(res)