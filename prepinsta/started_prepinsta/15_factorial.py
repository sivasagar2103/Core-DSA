
def factorial(n):
    res = 1
    for i in range(1,n + 1):
        res *= i

    return res

def factorial_by_recursion(n):
    if n == 1:
        return n
    return n * factorial_by_recursion(n - 1)
    

number = 5
res = factorial_by_recursion(number)
print(res)
