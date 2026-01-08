def combination_sum(k, n):
    nums_list = [i for i in range(1, 10)]
    result = []

    def backtrack(start, path, total):
        if len(path) == k and total == n:
            result.append(path[:])
            return
        
        if total > n or len(path) > k:
            return
        
        for i in range(start, len(nums_list)):
            if total + nums_list[i] > n:
                break
            path.append(nums_list[i])
            backtrack(i+1, path, total+nums_list[i])
            path.pop()
    
    backtrack(0, [], 0)
    return result

k = 3 #set length
n = 7 #target
result = combination_sum(k, n)
print(result)
