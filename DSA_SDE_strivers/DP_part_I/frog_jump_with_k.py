'''
Tabulation Approach:
- 
- For each jump, calculate the cost as dp[j] + abs(heights[i] - heights[j])
- Update dp[i] with the minimum cost found.
- After filling dp, return dp[n-1] as the minimum cost to reach the last stone.

Time: O(n*k)
Space: O(n)

Space Optimised:

- Maintain a sliding window dp list that only keeps the last k+1 dp values
  needed for calculations.
- Use window_idx to track the actual index corresponding to dp in the global stone sequence.
-  iterate over just the necessary indices j in [max(window_idx, i-k), i-1].

Time: O(n*k)
Space: O(k)

'''

def frog_jump_with_k_tab(heights, k):
    n = len(heights)
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(max(0, i-k), i):
            cost = dp[j] + abs(heights[i] - heights[j])
            if cost < dp[i]:
                dp[i] = cost
    
    return dp[-1]

#space
def frog_jump_with_k_space(heights, k):
    dp = [0]
    window_idx = 0
    n = len(heights)

    for i in range(1, n):
        min_cost = float('inf')
        start_j = max(window_idx, i-k)
        for j in range(start_j, i):
            cost = dp[j - window_idx] + abs(heights[i] - heights[j])
            if cost < min_cost:
                min_cost = cost
        dp.append(min_cost)

        #deleting the old element
        if len(dp) > k+1:
            dp.pop(0)
            window_idx += 1
    
    return dp[-1]


heights = [10, 5, 20, 0, 15]
k = 2
res = frog_jump_with_k_tab(heights, k)
print(res)
res2 = frog_jump_with_k_space(heights, k)
print(res2)