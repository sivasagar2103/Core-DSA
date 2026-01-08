'''
Problem Statement:
Given an integer n, determine whether it is a power of three.

Approach Used: Iterative Division

Core Idea:
Keep dividing n by 3 as long as it is divisible by 3
If we end at 1, then it is a power of three

Time: O(log3 ** n)
Space: O(1)

'''

def is_power(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    
    return n == 1

def isPowerOfK(n: int, k: int) -> bool:
    if n <= 0 or k <= 1:
        return False

    while n % k == 0:
        n //= k

    return n == 1

num = 27
res = is_power(num)
print(res)
