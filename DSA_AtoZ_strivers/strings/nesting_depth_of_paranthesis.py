
def max_depth(sen):
    current_depth = 0
    max_depth = 0

    for ch in sen:
        if ch == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif ch == ')':
            current_depth -= 1
    return max_depth    

s = "(1+(2*3)+((8)/4))+1"
res = max_depth(s)
print(res)