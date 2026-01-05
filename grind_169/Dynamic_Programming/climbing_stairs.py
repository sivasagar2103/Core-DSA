'''
Either climb 1 or 2 steps at a time

'''

#Time: O(n) ; Space: O(n)

def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

#Time: O(n) ; Space: O(1)
def climb_stairs_optimized(n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    return b if n > 1 else a

n = 5

#Output: 2

