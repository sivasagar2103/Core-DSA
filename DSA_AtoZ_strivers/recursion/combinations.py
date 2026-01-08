def combinations(n, k):
    result = [[i] for i in range(1, n +1)]

    for i in range(1,k):
        new_res = []
        for res_list in result:
            last_ele = res_list[-1]#1
            for j in range(last_ele+1, n+1):
                new_res.append(res_list + [j])
        result = new_res

    return result

def combinations_backtracking(n, k):
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, n+1):
            path.append(i)
            backtrack(i+1, path)
            path.pop()
    
    backtrack(1, [])
    return result


n = 4
k = 2
res = combinations_backtracking(n,k)
print(res)