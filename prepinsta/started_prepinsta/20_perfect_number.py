'''
What is a Perfect Number?
- A number n is perfect if:
    Sum of its proper divisors (excluding itself) = n

- Divisors of 28: 1, 2, 4, 7, 14   (exclude 28)


'''

def is_perfect_number(n):
    source = n 
    res_sum = 1

    for i in range(2, int(pow(source, 0.5))+ 1):
        if source % i == 0:
            factor = source // i
            if i == factor:
                res_sum += i
            else:
                res_sum = res_sum + i + factor
    return res_sum == n

number = 28
res = is_perfect_number(number)
print(res)

