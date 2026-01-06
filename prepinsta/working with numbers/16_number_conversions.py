def binary_to_decimal(num):
    base = 1
    decimal_value = 0

    while num > 0:
        #rem should be zero or one
        rem = num % 10
        decimal_value += rem * base
        num //= 10
        base *= 2
    
    return decimal_value

binary_number = 1010
decimal_number = binary_to_decimal(binary_number)
print(decimal_number)

def octal_to_decimal(num):
    base = 1
    decimal_value = 0
    while num:
        #rem should be in range of 0 - 7
        rem = num % 10
        decimal_value += rem * base
        num //= 10
        base = base * 8
    
    return decimal_value

octal = 512
decimal_number = octal_to_decimal(octal)
print(decimal_number)

#hexadecimal number is string that contains in range of 0 - 9 and A - F
def hexadecimal_to_decimal(num):
    hexa_constants = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    n = len(num)
    decimal_value = 0
    pos = 0

    for i in range(n-1,-1, -1):
        if '0' <= num[i] <= '9':
            dig = int(num[i])
        elif num[i] in hexa_constants:
            dig = hexa_constants.get(num[i])

        decimal_value += dig * (16 ** pos)
        pos += 1
    
    return decimal_value

hexadecimal_num = "C9"
res = hexadecimal_to_decimal(hexadecimal_num)
print(res)


def decimal_to_binary(num):
    base = 1
    binary_value = 0

    while num:
        rem = num % 2
        binary_value += rem * base
        num //= 2
        base *= 10
    
    return binary_value

decimal_number = 21
res = decimal_to_binary(decimal_number)
print(res)

def decimal_to_octal(num):
    base_value = 1
    octal_number = 0

    while num:
        rem = num % 8
        octal_number += rem * base_value
        num //= 8
        base_value *= 10
    
    return octal_number

decimal_number = 33
res = decimal_to_octal(decimal_number)
print(res)


def decimal_to_hexadecimal(num):
    hex_map = '0123456789ABCDEF'
    res = ''

    while num:
        rem = num % 16
        res = hex_map[rem] + res
        num //=16
    
    return res

decimal_number = 2545
res = decimal_to_hexadecimal(decimal_number)
print(res)


'''
1 octal == 3 binary digits
from right to left
converting each chunk of 3 into octal

padding = (3 - len(binary) % 3) % 3
padding = 3 - 0 = 3   ❌ (We don’t need to pad 3 zeros when it's already a multiple of 3)
padding = (3 - 0) % 3 = 0 ✅
So the last % 3 ensures that when the length is already a multiple of 3, you don’t pad unnecessarily.

The ASCII code for '0' is 48.
chr(6 + 48) becomes chr(54) → '6'.
'''
def binary_to_octal(num):
    binary = str(num)

    #The last %3 to handle the multiples of three
    default_zeroes = (3 - len(binary) % 3) % 3
    binary = '0' * default_zeroes + binary

    result = ''
    i = 0

    while i < len(binary):
        #ord to get the ascii code
        b1 = ord(binary[i]) - 48
        b2 = ord(binary[i + 1]) - 48
        b3 = ord(binary[i + 2]) - 48

        value = b1 * 4 + b2 * 2 + b3 * 1
        #chr to get the base value
        result += chr(value + 48)

        i += 3
    
    return result

binary = 110110
print(binary_to_octal(binary))


def octal_to_binary(num):
    decimal_number = octal_to_decimal(num)
    binary_number = decimal_to_binary(decimal_number)
    return binary_number

octal = 66
print(octal_to_binary(octal))
