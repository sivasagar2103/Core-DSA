
def valid_paranthesis(st):
    low = high = 0

    for ch in st:
        if ch == '(':
            low += 1
            high += 1
        elif ch == ')':
            low -= 1
            high -= 1
        else:
            low -= 1
            high += 1
        
        if high < 0:
            return False
        if low < 0:
            low = 0
    
    return low == 0

        

s = "(*))"
res = valid_paranthesis(s)
print(res)