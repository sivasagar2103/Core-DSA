'''
Problem:
Given an integer n, there is a staircase with n steps, starting from the 0th step. 
Determine the number of unique ways to reach the nth step, given that each move 
can be either 1 or 2 steps at a time.

'''

def climbing_stairs_rec(n):

    def stairs(i):
        if i == 0 or i == 1:
            return 1
        
        return stairs(i-1) + stairs(i-2)
    
    return stairs(n)

def climbing_stairs_memo(n):
    dp = [-1] * (n+1)

    def stairs(i):
        if i == 0 or i == 1:
            return 1
        
        dp[i] = stairs(i-1) + stairs(i-2)
        return dp[i]
    
    return stairs(n)

def climbing_stairs_tab(n):
    if n == 0 or n == 1:
        return 1
     
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[-1]

#space
def climbing_stairs_space(n):
    prev1 = 2
    prev2 = 1

    for i in range(3, n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    
    return prev1


n = 3
res = climbing_stairs_rec(n)
print(res)
res1 = climbing_stairs_memo(n)
print(res1)
res2 = climbing_stairs_tab(n)
print(res2)
res3 = climbing_stairs_space(n)
print(res3)