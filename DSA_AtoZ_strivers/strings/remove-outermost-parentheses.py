
def remove_outermost_parantheses(sentence):
    res = ""
    depth = 0
    for char in sentence:
        if char == '(':
            if depth > 0:
                res += char
            depth += 1
        elif char == ')':
            depth -= 1
            if depth > 0:
                res += char
    return res


sentence = "(()())(())"
res = remove_outermost_parantheses(sentence)
print(res)