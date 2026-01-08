def combinations_sum(nums_list, target):
    result = []
    nums_list.sort()
    #seen = [False] * len(nums_list)

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        
        for i in range(start, len(nums_list)):
            if total + nums_list[i] > target:
                break

            if i > start and nums_list[i] == nums_list[i-1]:
                continue

            path.append(nums_list[i])
            backtrack(i+1, path, total+nums_list[i])
            path.pop()

    backtrack(0, [], 0)
    return result

candidates = [10,1,2,7,6,1,5]
target = 8
res = combinations_sum(candidates, target)
print(res)