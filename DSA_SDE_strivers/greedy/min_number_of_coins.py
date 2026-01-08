'''
Problem:
Given a value V, if we want to make a change for V Rs, and we have an infinite supply 
of each of the denominations in Indian currency, i.e., we have an infinite supply 
of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, 
what is the minimum number of coins and/or notes needed to make the change.

Approach:
- Start with the highest denomination less than or equal to the current value (V).
- For each denomination, use as many of that coin/note as possible, subtracting 
  its value from V each time, until V becomes less than the denomination.
- Repeat with the next lower denomination.
- Continue until V reaches zero. Collect all coins/notes used.

Time: O(N)
Space: O(1)

'''

def min_number_of_coins(deno, value):
    n = len(deno)
    i = n - 1
    res = 0
    while i >= 0:
        if value >= deno[i]:
            res += 1
            value -= deno[i]
        else:
            i -= 1
    return res

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
value = 49
res = min_number_of_coins(denominations, value)
print(res)