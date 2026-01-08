
def two_sum(nums, target):
    comp_map = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in comp_map:
            return [comp, nums[i]]
        comp_map[nums[i]] = i

nums = [2,7,11,15]
target = 9
res = two_sum(nums, target)
print(res)
