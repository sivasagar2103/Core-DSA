def combinations_sum(nums_list, target):
    nums_list.sort()
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        
        for i in range(start, len(nums_list)):
            # # Prune the search space
            if (total + nums_list[i]) > target:
                break

            path.append(nums_list[i])
            backtrack(i, path, total+nums_list[i])
            path.pop()
    
    backtrack(0,[],0)
    return result


candidates = [2, 3, 5, 4]
target = 7
result = combinations_sum(candidates, target)
print(result)