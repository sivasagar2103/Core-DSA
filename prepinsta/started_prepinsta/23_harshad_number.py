'''
Harshad Number
A Number that is divisible by the sum of it's digits is known as a Harshad number.

'''

def is_harshad_number(n):
    sum_digits = 0
    source = n
    while source > 0:
        dig = source % 10
        sum_digits += dig
        source //= 10

    return n % sum_digits == 0


def is_harshad_number(n):
    if n <= 0:
        return False
    sum_digits = sum(map(int, str(n)))
    return n % sum_digits == 0

number = 12
res = is_harshad_number(number)
print(res)