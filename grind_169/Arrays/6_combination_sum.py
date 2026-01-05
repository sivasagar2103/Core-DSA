''''
Use-Cases & Intuition
1. Why Backtracking
  - We use backtracking because we are generating actual combinations,
  not just checking existence.
  - At each index:
    . Pick the number and stay at the same index (reuse allowed), or
    . Skip the number and move ahead.
2. Sorting + Duplicate Handling
  - Sorting helps in:
    . Early pruning (for positive numbers)
    . Skipping duplicates at the same recursion level
  - Duplicate skipping ensures unique combinations.
3. Reuse vs No Reuse
  - Reuse allowed --> recurse with index i
  - Reuse not allowed --> recurse with index i + 1
4. Impact of Negative Numbers
  - With positive numbers only, pruning works because the sum always increases.
  - With negative numbers, pruning breaks:
    . The sum can oscillate.
    . Recursion depth becomes unbounded.
  - We must cap recursion using DP (memoization).

Backtracking (Positive Numbers Only)
- Intuition
  . Each recursive call adds one element to the path.
  . Since all numbers are positive, the total strictly increases.
  . Recursion terminates naturally once the sum exceeds the target.
- Recursion Characteristics
  . Depth of recursion : Depth ≈ T / min(arr), where T is the target
  . Branching factor : Up to n choices at each level
- Time Complexity : O(n^(T / min(arr)))   // exponential
- Space Complexity : O(T / min(arr))      // recursion depth + path storage

Backtracking + DP (Negative Numbers Allowed)
- Why Backtracking Alone Fails
  . Negative numbers allow the sum to:
    . Increase
    . Decrease
  . This leads to:
    . Infinite or repeated recursion paths
    . Exponential blow-up
- Solution: Memoization
  . Store dead states as (index, current_sum)
  . Skip recursion if the state is already known to fail

State Space Analysis
Sum range ≈ [-n · maxAbs, +n · maxAbs]
Let S = O(n · maxAbs)
Total states = O(n · S)

- Time Complexity : O(n² · S)
- Space Complexity
  Memo table: O(n · S)
  Recursion depth: O(n)
  Path storage: O(n)
  Total: O(n · S)

Backtracking explodes in DEPTH
DP explodes in STATE SPACE

Positive numbers bound depth --> backtracking works.
Negative numbers break pruning --> DP is required.”

'''

def combination_sum(arr, target):
    arr.sort()
    res = []
    n = len(arr)

    def backtrack(start, total, path):
        if total == target:
            res.append(path[:])
            return
        
        if total > target:
            return
        
        for i in range(start, n):

            #early pruning - it works if the array is sorted.
            if arr[i] > target - total:
                break
    
            #to skip duplicates
            if i > start and arr[i-1] == arr[i]:
                continue

            path.append(arr[i])
            backtrack(i, total + arr[i], path) #i+1 if reuse of the same element is not allowed
            path.pop()

    backtrack(0, 0, [])
    return res

def combination_sum_with_negatives(arr, target):
    arr.sort()
    res = []
    n = len(arr)
    
    # memo[(start, total)] = False means "no solution from here"
    memo = set()

    def backtrack(start, total, path):
        # success
        if total == target:
            res.append(path[:])
            return True
        
        # out of bounds
        if start == n:
            return False
        
        # already visited dead state
        if (start, total) in memo:
            return False
        
        found = False
        
        for i in range(start, n):
            # skip duplicates
            if i > start and arr[i] == arr[i - 1]:
                continue
            
            path.append(arr[i])
            if backtrack(i + 1, total + arr[i], path):
                found = True
            path.pop()
        
        # mark as dead end if no solution found
        if not found:
            memo.add((start, total))
        
        return found

    backtrack(0, 0, [])
    return res


candidates = [2,3,6,7,2]
target = 7
res = combination_sum(candidates, target)
print(res)
#Output: [[2,2,3],[7]]
