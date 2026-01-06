
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def is_power_number(num):
    source = num
    sum_result = 0
    while source > 0:
        dig = source % 10
        fact = factorial(dig)
        sum_result += fact
        source //=10

    return True if sum_result == num else False

number = 145

res = is_power_number(number)

print(res)
