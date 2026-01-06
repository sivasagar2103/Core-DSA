def occurence_of_digit(num, dig):
    res = 0

    while num > 0:
        if (num % 10) == dig:
            res += 1
        num //= 10

    return res 


number = 897982
find_num = 9
res = occurence_of_digit(number, find_num)
print(res)
