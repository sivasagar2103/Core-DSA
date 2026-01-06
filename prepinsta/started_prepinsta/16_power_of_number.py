'''
Any power can be broken using these identities:
If b is even: a^b = a^((b/2))^2
If b is odd: a^b = a * (a^(b-1))


Normal multiplication:
2^10 → multiply 2 ten times

Optimal Approach
10 → 5 → 2 → 1 → 0  (log₂ steps)

b % 2 checks the lowest binary bit
b //= 2 is equivalent to right shift
a *= a moves from a¹ → a² → a⁴ → a⁸ ...

'''

def power(a, b):
    """
    Time: O(b)
    Space: O(1)

    """
    result = 1
    for _ in range(b):
        result *= a
    return result

print(power(2, 3))

def power(a, b):
    """
    Time: O(log b)
    Space: O(1)

    """
    result = 1

    while b > 0:
        if b % 2 == 1:      # if b is odd
            result *= a
        a *= a              # square base
        b //= 2             # halve exponent

    return result

print(power(2, 10))  # 1024

def power(a, b):
    if b < 0:
        a = 1 / a
        b = -b

    result = 1
    while b > 0:
        if b & 1: #checking last bit is set or not == odd or even
            result *= a
        a *= a
        b >>= 1 #making half as exponent

    return result

