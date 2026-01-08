'''
Approach:

1. Using Recursion
- On every index, we have two options either to select the element to add it to your subset(pick)
  or not select the element at that index and move to the next index(not pick)


'''
def subset_sums(arr):
    '''
    - enumerates all possible subsets and appends their sums to result.
    - For each element two recursive calls
      . Pick the element (include in sum)
      . Not pick the element (exclude from sum)
    - Time : O(2**n) [Exactly 2**n subsets of n elements array.]
    - Space : 
      . Recursion stack: O(n)
      . result space: O(2**n)
      . Total : O(2**n)

    '''
    result = []
    n = len(arr)

    def subset_sum(i, sub_sum):
        if i >= n:
            result.append(sub_sum)
            return
        
        subset_sum(i+1, sub_sum + arr[i])
        subset_sum(i+1, sub_sum)

    subset_sum(0, 0)
    return result

def subset_sum_target(arr, target):
    '''
    - tries to find if any subset sums to target.
    - Recursion explores all subsets until a subset sum equal to the target is found.
    - Time: O(2**n)
    - Space: 
       . Recursion stack
       . O(n)

    '''
    n = len(arr)

    def find_target(i, sub_sum):
        if sub_sum == target:
            return True
        if i == n:
            return False
        
        not_pick = find_target(i+1, sub_sum)
        pick = find_target(i+1, sub_sum + arr[i])
        return not_pick or pick

    return find_target(0,0)

def subset_sum_target_elements(arr, target):
    '''
    - keeps track of the elements forming the solution subset.
    - Time:
      . O(2**n)  -- exploring all subset combinations
    - Space:
      . Recursion stack: O(n)
      . path list per recusrion: O(n)
      . Total: O(n**2)
    
    '''
    n = len(arr)

    def subset_elements(i, sub_sum, path):
        if sub_sum == target:
            return True, path.copy()
        if i == n or sub_sum > target:
            return False, []
        
        pick, elements = subset_elements(i+1, sub_sum+arr[i], path + [arr[i]])
        if pick:
            return pick, elements
        not_pick, elements = subset_elements(i+1, sub_sum, path)
        if not_pick:
            return not_pick, elements

    return subset_elements(0, 0, [])


def subset_sum_memoization(arr, target):
    '''
    - Memoization (Top-Down Dynamic Programming)
      . stores the results of subproblems in a cache (usually a dict) so that
        unique state is computed only once.
      . Before recursing, check if you have already solved that subproblem 
        and return the cached value.
      . Each (i, sum) computed at most once
    - Time: O(n * target)
    - Space: O(n*target)
    
    '''

    n = len(arr)
    memo = {}

    def find_target(i, sub_sum):
        if sub_sum == target:
            return True
        if i == n:
            return False
        if (i, sub_sum) in memo:
            return memo[(i,sub_sum)]
        pick = find_target(i+1, sub_sum + arr[i])
        not_pick = find_target(i+1, sub_sum)
        memo[(i, sub_sum)] = pick or not_pick
        return memo[(i, sub_sum)]

    return find_target(0, 0)

def subset_sum_tabulation(arr, target):
    '''
    - Tabulation (Bottom-Up Dynamic Programming)
       . Iteratively build up a table (a 2D list) where dp[i][j] is True
         when sum j can be formed using the first i elements.
       . Avoids recursion stack, every subproblem is solved no more than once, 
         using nested loops. 
    
    '''

    n = len(arr)
    dp_table = [[False] * (target + 1) for _ in range(n+1)]
    pass


arr = [1, 2, 7, 3]
target = 6
res = subset_sums(arr)
print(res)
is_exists = subset_sum_target(arr, target)
print(is_exists)
elements = subset_sum_target_elements(arr, target)
print(elements)
td_approach = subset_sum_memoization(arr, target)
print(td_approach)
bu_approach = subset_sum_tabulation(arr, target)
print(bu_approach)