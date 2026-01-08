'''
Problem:
A frog wants to climb a staircase with n steps. Given an integer array heights,
where heights[i] contains the height of the ith step.

To jump from the ith step to the jth step, the frog requires abs(heights[i] - heights[j]) energy,
where abs() denotes the absolute difference.
The frog can jump from any step either one or two steps, provided it exists.
Return the minimum amount of energy required by the frog to go from the 
0th step to the (n-1)th step.

Why Greedy does not works?
The frog can jump from any step either one or two steps, provided it exists.
Return the minimum amount of energy required by the frog to go from the 0th step 
to the (n-1)th step.
If the frog just takes the cheapest path in every stage it can happen that 
it eventually takes a costlier path after a certain number of jumps.

Ex: 30 10 60 10 60 50

Approach:
Recursion --> Try all possible ways --> find minimal energy
Steps:
1. Express the problem in terms of index
2. Do all the stuff on index
3. Find minimal from all the stuffs.

'''

def find_miminal_energy_rec(arr):
    n = len(arr)

    def energy(end):
        if end == 0:
            return 0
        
        first = energy(end-1) + abs(arr[end] - arr[end-1] )
        if end > 1:
            second = energy(end - 2) + abs(arr[end] - arr[end-2])
        else:
            second = float('inf')

        return min(first, second)


    return energy(n-1)

def find_miminal_energy_memo(arr):
    n = len(arr)
    dp = [-1] * (n+1)

    def energy(i):
        if i == 0:
            return 0
        
        if dp[i] != -1:
            return dp[i]
        
        jump1 = energy(i-1) + abs(arr[i] - arr[i-1])
        if i > 1:
            jump2 = energy(i-2) + abs(arr[i] - arr[i-2])
        else:
            jump2 = float('inf')
        
        dp[i] = min(jump1, jump2)
        return dp[i]
    
    return energy(n-1)

def find_miminal_energy_tab(heights):
    #Tabulation
    n = len(heights)
    dp = [-1] * (n)
    dp[0] = 0

    for i in range(1, n):
        jump1 = dp[i-1] + abs(heights[i] - heights[i-1])
        if i > 1:
            jump2 = dp[i-2] + abs(heights[i] - heights[i-2])
        else:
            jump2 = float('inf')
        
        dp[i] = min(jump1, jump2)

    return dp[n-1]

def find_miminal_energy_space(heights):
    #Space Optimization
    n = len(heights)
    prev1 = 0
    prev2 = 0

    for i in range(1, n):
        jump1 = prev1 + abs(heights[i] - heights[i-1])
        if i > 1:
            jump2 = prev2 +abs(heights[i] - heights[i-2])
        else:
            jump2 = float('inf')
        
        curr = min(jump1, jump2)
        prev2 = prev1
        prev1 = curr
    
    return prev1
   
heights = [2,1,3,5,4]
res = find_miminal_energy_rec(heights)
print(res)
res1 = find_miminal_energy_memo(heights)
print(res1)
res2 = find_miminal_energy_tab(heights)
print(res2)
res3 = find_miminal_energy_space(heights)
print(res3)
