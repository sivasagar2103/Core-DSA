import math

def number_of_digits(num):
    res = 0
    while num > 0:
        res += 1
        num //= 10
    
    return res

n = 78673
digit = math.floor(math.log10(n)+1)
print(digit)

print(number_of_digits(123))