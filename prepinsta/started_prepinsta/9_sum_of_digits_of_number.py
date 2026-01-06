
def sum_of_digits(num):
    res = 0
    while num > 0:
        digit = num % 10
        res += digit
        num = num //10
    return res

res = sum_of_digits(123)
print("normal while loop", res)

def sod_using_recursion(num):
    if num == 0:
        return num
    digit = num % 10
    return digit + sod_using_recursion(num //10)

res = sod_using_recursion(123)
print("sod_using_recursion", res)
