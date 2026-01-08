'''
Problem Statement

Given two integers numerator and denominator, return the fraction as a string.

Rules:
- If the decimal part is repeating, enclose the repeating part in parentheses.

Core Idea:
- long division method
- A decimal starts repeating when the same remainder appears again.
- Track remainders using a hashmap
- When a remainder repeats, we have found a cycle

Time: O(n)
Space: O(n)

'''

def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"
    
    result = []

    if (numerator < 0) or (denominator < 0):
        result.append("-")
        numerator, denominator = abs(numerator), abs(denominator)

    quot = numerator // denominator
    remainder = numerator % denominator
    result.append(str(quot))

    if remainder == 0:
        return ''.join(result)
    
    result.append('.')

    seen = {}

    while remainder != 0:
        if remainder in seen:
            idx = seen[remainder]
            result.insert(idx, '(')
            result.append(')')
            break

        seen[remainder] = len(result) #bracket starting
        remainder *= 10
        q = remainder // denominator
        result.append(str(q))
        remainder %= denominator
    
    return ''.join(result)

numerator = 1
denominator = 2
res = fractionToDecimal(numerator, denominator)
print(res)
