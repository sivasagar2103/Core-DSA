def permutations_iterative(nums):
    result = [[]]

    for num in nums:
        temp_result = []
        seen = set()
        for res in result:
            for i in range(len(res) + 1):
                temp = res[:i] + [num] + res[i:]
                tuple_temp = tuple(temp)
                if tuple_temp not in seen:
                    seen.add(tuple_temp)
                    temp_result.append(temp)
        result = temp_result
    
    return result

def permutations_backtracking(nums):
    result = []
    nums.sort()
    seen = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if seen[i]:
                continue
            
            if i > 0 and nums[i] == nums[i-1] and not seen[i-1]:
                continue

            seen[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            seen[i] = False

    backtrack([])
    return result


nums = [1,1,2]
res = permutations_backtracking(nums)
print(res)