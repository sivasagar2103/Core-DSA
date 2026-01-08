'''
Iterative approach
nums = [1,2,3]
i = 2
nums[i:] = [3] -- start and include ith(2nd) index value.
nums[:i] = [1,2] -- start and exclude ith(2nd) index value

'''

def permutations(nums):
    result = [[]]
    for num in nums:
        temp_result = []
        for comb in result:
            for i in range(len(comb) + 1):
                temp = comb[:i] + [num] + comb[i:]
                temp_result.append(temp)
        result = temp_result
    return result

'''
Backtracking technique:

When storing intermediate results in backtracking, always copy mutable structures
like lists or dictionaries.
Note: with and without slicing operator
nums[:] creates a shallow copy of the list — a new list with the current content.
without slicing opearator
nums = [1, 2, 3]
a = []
a.append(nums)
nums[0] = 99
print(a)  # [[99, 2, 3]]

with slicing operator
nums = [1, 2, 3]
a = []
a.append(nums[:])
nums[0] = 99
print(a)  # [[1, 2, 3]]

'''

def permutations_backtracking(nums):
    result = []
    n = len(nums)

    def back_track(start):
        if start == n:
            #to capture the current state of the list
            result.append(nums[:])
            return
        for i in range(start, n):
            nums[start], nums[i] = nums[i], nums[start]
            back_track(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    back_track(0)
    return result

nums = [1,2,3]
res = permutations(nums)
result = permutations_backtracking(nums)
print(res)
print("************")
print(result)