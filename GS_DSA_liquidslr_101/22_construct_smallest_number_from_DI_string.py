'''
Problem Statement
You are given a string pattern of length n consisting of:
'I' → increasing  ; 'D' → decreasing
You must construct a string num of length n + 1 such that:
Digits are from '1' to '9'
Each digit is used at most once
If pattern[i] == 'I' → num[i] < num[i+1]
If pattern[i] == 'D' → num[i] > num[i+1]
Return the lexicographically smallest valid num.

Approach Used: Greedy + Stack

Core Idea:
- Iterate from 1 to n+1
- Push each number onto a stack
- When you see:
  . 'I' → pop everything from the stack
  . end of pattern → pop everything
- This ensures:
  . Increasing segments stay increasing
  . Decreasing segments are reversed correctly
  . The smallest digits are used as early as possible

Time: O(n)
Space: O(n)

'''

def smallest_number(pattern):
    stack = []
    result = []
    n = len(pattern)

    for i in range(n+1):
        stack.append(i+1)

        if i == n or pattern[i] == 'I':
            while stack:
                result.append(str(stack.pop()))
    
    return ''.join(result)


pattern = "IIIDIDDD"
result = smallest_number(pattern)
print(result)
#"123549876"
