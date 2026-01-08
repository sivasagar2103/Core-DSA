'''
Problem:
You are given: an array nums ; a number original
As long as original exists in nums:
replace original with original * 2
The moment original is not found, stop.
Return the final value of original.

Approach Used: Hashset

'''

def find_value(nums, original):
    nums_set = set(nums)   # O(1) lookup

    while original in nums_set:
        original *= 2

    return original

nums = [5,3,6,1,12]
original = 3
res = find_value(nums, original)
print(res)
#Output: 24
