'''
Core Idea:
For every number: check if its partner already exists — if not, remember it.

Steps of implementation:
1. Create an empty dictionary (comp_map) to remember numbers that are already seen.
2. For each number x in nums:
   - Compute its complement: target - x
   - If the complement is already in the dictionary:
     . Found the pair --> return it immediately
   - Otherwise:
     . Store the current number in the dictionary 

Time: O(n)
Space: O(n)

'''

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
