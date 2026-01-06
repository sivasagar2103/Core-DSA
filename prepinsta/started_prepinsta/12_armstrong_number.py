

def armstrong_number(number):
    source = number
    res = 0
    n = len(str(number))
    while source > 0:
        dig = source % 10
        res += (dig ** n)
        source //= 10

    return True if number == res else False


def armstrong_number_recursion(number, n, sum = 0):
    if number == 0:
        return sum
    dig = number % 10
    return armstrong_number_recursion(number // 10, n, sum = sum + dig ** n )



number = 371
res = armstrong_number(number)
print(res)

rec_num = 371
n = len(str(rec_num))
res_rec = armstrong_number_recursion(rec_num, n)
print(True) if res_rec == rec_num else print(False)
