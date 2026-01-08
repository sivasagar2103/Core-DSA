#Brute Force Algorithm
'''
Brute Force Algorithm
Iterative
Time : O(N * 2^N)	
Space : O(N * 2^N)	
Simple, elegant
'''
def subsets(nums):
    result = [[]]
    for num in nums:
        temp_result = []
        for element in result:
            temp = element + [num]
            temp_result.append(temp)
        result += temp_result
    return result

#Backtracking technique
'''
Backtracking
Time : O(N * 2^N)	
Space : O(N * 2^N)	
Flexible for constraints (e.g., subset size)
'''
def subsets_backtracking(nums):
    result = []
    n = len(nums)
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, n):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result

#Bitmasking approach
'''
'''
def subsets_bitmasking(nums):
    #TODO
    pass


nums = [1,2, 3]
result = subsets(nums)
print(result)