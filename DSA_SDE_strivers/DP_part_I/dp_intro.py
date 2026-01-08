'''
Introduction points avaialble in personal book.

'''

#recursive approach
def find_fibo_recursive(n):
    '''
    T : O(2**n)
    S: O(n)

    '''

    def fibo(i):
        if i <= 1:
            return i
        
        return fibo(i-1) + fibo(i-2)

    return fibo(n)


#memoization
def find_fibo_memoization(n):
    '''
    T: O(n)
    S: O(n)
    
    '''
    #main to base case
    dp = [-1] * (n+1)

    def fibo(i):
        if i <= 1:
            return i
        
        if dp[i] != -1:
            return dp[i]

        dp[i] = fibo(i-1) + fibo(i-2)
        return dp[i]
    
    return fibo(n)

#tabulation
def find_fibo_tabulation(n):
    '''
    T : O(n)
    S : O(n)

    '''
    #base to desired case
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[-1]

#space optimization
def find_fibo_space(n):
    '''
    T: O(n)
    S: O(1)
    
    '''
    prev2 = 0
    prev1 = 1

    for i in range(2, n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    
    return prev1




n = 8
res1 = find_fibo_recursive(n)
print(res1)
res2 = find_fibo_memoization(n)
print(res2)
res3 = find_fibo_tabulation(n)
print(res3)
res4 = find_fibo_space(n)
print(res4)

