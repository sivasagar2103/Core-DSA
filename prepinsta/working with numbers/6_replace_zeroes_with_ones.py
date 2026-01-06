
def replace_with_ones(num):
    res = 0
    place = 1

    while num > 0:
        dig = num % 10
        dig = 1 if dig == 0 else dig
        res = res + (dig * place)
        place *= 10
        num //= 10
    
    return res


number = 12090
res = replace_with_ones(number)
print(res)
