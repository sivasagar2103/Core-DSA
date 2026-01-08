

def str_to_int(sen):
    i = 0
    n = len(sen)
    result = 0
    sign = 1

    MIN_INT = -2**31  
    MAX_INT = 2**31 - 1 

    while i < n and sen[i] == ' ':
        i += 1
    
    if i < n and (sen[i] == '-' or sen[i] == '+'):
        if sen[i] == '-':
            sign = -1
        i += 1
    
    while i < n:
        ch = sen[i]
        if ch >= '0' and ch <= '9':
            dig = ord(ch) - ord('0')
            if result > (MAX_INT - dig) //10:
                return MAX_INT if sign == 1 else MIN_INT
            result = result * 10 + dig
            i += 1
        else:
            break

    return sign * result 

s = " -0420456abc"
res = str_to_int(s)
print(res)