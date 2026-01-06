
def check_armstrong_number(number, n, sum = 0):
    if number == 0:
        return sum
    
    dig = number % 10
    return check_armstrong_number(number // 10, n, sum + (dig ** n))


def armstrong_numbers_in_range(a, b):
    res = []
    for num in range(a, b):
        n = len(str(num))
        if num == check_armstrong_number(num, n):
            res.append(num)
    return res

low = 150
high = 160
result = armstrong_numbers_in_range(low, high)
print(result)

