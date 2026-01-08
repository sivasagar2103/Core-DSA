'''
Always sort when your problem involves:
Handling duplicates
Avoiding duplicate subsets/permutations/combinations

If it’s a duplicate, I only want to add it to the new subsets formed by the last number.
If it’s not a duplicate, I can freely add it to all existing subsets.

'''


def subsets(nums):
    nums.sort()
    result = [[]]
    start = 0
    end = 0

    for i in range(len(nums)):
        start = 0

        if i > 0 and nums[i] == nums[i-1]:
            start = end + 1
        
        end = len(result) - 1

        for j in range(start, len(result)):
            temp_list = result[j] + [nums[i]]
            result.append(temp_list)
    return result

def subsets_with_tuple(nums):
    nums.sort()
    result = [[]]
    seen = set()

    for num in nums:
        temp_res = []
        for ele in result:
            temp_list = ele + [num]
            temp_tuple = tuple(temp_list)
            if temp_tuple not in seen:
                seen.add(temp_tuple)
                temp_res.append(temp_list)
        result += temp_res
    
    return result


'''
if i > 0 and nums[i] == nums[i - 1]:
You will skip any duplicate as long as it’s not at index 0 — 
even if it’s in a different recursive branch.

if i > start and nums[i] == nums[i - 1]:

Only skip duplicates when you’re trying to add the
same number again at the same recursive depth.

'''
def subsets_with_backtracking(nums):
    nums.sort()
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue

            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    
    backtrack(0,[])
    return result


nums = [1,1,2]
result = subsets_with_backtracking(nums)
print(result)
