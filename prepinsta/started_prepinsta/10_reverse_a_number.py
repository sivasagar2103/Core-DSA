
def reverse_a_number(num):
    res = 0
    while num > 0:
        dig = num % 10
        res = (res * 10) + dig
        num = num // 10

    return res

def reverse_by_recusrsion(num, res = 0):
    if num == 0:
        return res
    dig = num % 10
    return reverse_by_recusrsion(num // 10, res = ((res * 10) + dig))
    

re = reverse_by_recusrsion(123)
print(re)