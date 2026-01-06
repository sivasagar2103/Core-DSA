#source == reverse ==> palindrome else not palindrome
def check_palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = (rev * 10) + dig
        num //= 10
    return True if temp == rev else False

def check_palindrome_string(num):
    str_num = str(num)
    n = len(str_num)

    for i  in range(n):
        if str_num[i] != str_num[n - i - 1]:
            return False
    return True

def check_palindrome_string_half(num):
    str_num = str(num)
    n = len(str_num)

    mid = n //2
    for i in range(mid):
        if str_num[i] != str_num[n - i - 1]:
            return False
    return True

def palidrome_without_reverse_num(num):
    if num < 0:
        return False
    temp = num
    digits = 0
    while temp>0:
        digits += 1
        temp //=10
    
    degree = 10 ** (digits - 1)

    while num:
        first = num // degree
        last = num % 10

        if first != last:
            return False
        
        num = (num % degree) // 10
        degree //= 100
    
    return True


#res = check_palindrome_string(12216)
num = 1221
result = palidrome_without_reverse_num(num)
print(result)

#print(res)

