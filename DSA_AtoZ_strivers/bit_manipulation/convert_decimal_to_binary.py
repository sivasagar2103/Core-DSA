
def convert_dec_to_bin(num):
    '''
    
    '''
    res = []
    temp = num

    while temp > 0:
        res.append(temp % 2)
        temp //= 2

    print(res)
    last = len(res) - 1
    return ''.join(str(x) for x in res[::-1])

def convert_bin_to_decimal(bina):
    n = len(bina)
    res = 0

    for ch in bina:
        res += int(ch) * (2**(n-1))
        n -= 1
    
    return res


num = 13
res = convert_dec_to_bin(num)
print(res)

bina = '1101'
dec = convert_bin_to_decimal(bina)
print(dec)