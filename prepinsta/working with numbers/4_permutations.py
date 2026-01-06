'''
ncr = n! // (n-r)!

'''

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

n = 5
r = 2
res = factorial(n) // factorial(n - r)
print(res)
