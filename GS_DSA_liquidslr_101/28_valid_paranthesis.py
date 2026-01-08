'''
close is the key
open is the value

at the end stack should be empty

'''


def valid_paranthesis(sen):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in sen:
        if ch in mapping.values():  # opening
            stack.append(ch)
        elif ch in mapping:         # closing
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            return False  # invalid character

    return not stack


# Tests
s1 = "()"
print(valid_paranthesis(s1))  # True

s2 = "()[]{}"
print(valid_paranthesis(s2))  # True

s3 = "(]"
print(valid_paranthesis(s3))  # False

s4 = "([{}])"
print(valid_paranthesis(s4))  # True
