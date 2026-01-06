'''

| Version          | Time  | Space | Notes                            |
| ---------------- | ----- | ----- | -------------------------------- |
| Iterative        | O(n)  | O(n)  | Simple & fastest                 |
| Recursive + Memo | O(n)  | O(n)  | Good for recursion/DP interviews |
| Plain Recursive  | O(2ⁿ) | O(n)  | ❌ Avoid                          |

'''


def fibonacci_n(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

def fibonacci_series(n):
    '''
    Time: O(n)
    Space: O(n)
    '''

    if n <= 0:
        return []
    if n == 1:
        return [0]

    result = [0, 1]

    for _ in range(2, n):
        result.append(result[-1] + result[-2])

    return result

def fibonacci_series_recursive_memo(n):
    """
    Time: O(n)
    Space: O(n)  (memo + recursion stack)
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    memo = {0: 0, 1: 1}

    def fib(k):
        if k in memo:
            return memo[k]

        memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]

    result = []
    for i in range(n):
        result.append(fib(i))

    return result

def fibonacci_series_recursive_memo2(n):
    '''
    Using list instead of dict for memoization

    '''

    if n <= 0:
        return []
    if n == 1:
        return [0]

    memo = [-1] * n
    memo[0], memo[1] = 0, 1

    def fib(k):
        if memo[k] != -1:
            return memo[k]
        memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]

    for i in range(2, n):
        fib(i)

    return memo


num = 8
res = fibonacci_series_recursive_memo2(num)
print(res)
