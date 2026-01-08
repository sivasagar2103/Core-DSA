def min_number_for_valid_paranthesis(word):
    depth = 0
    required = 0
    for ch in word:
        if ch == '(':
            depth += 1
        elif depth == ')':
            if depth > 0:
                depth -= 1
            else:
                required += 1
    
    return depth + required




s = "())"
res = min_number_for_valid_paranthesis(s)
print(res)