'''
An abundant number is a number where the sum of its proper divisors 
is greater than the number itself.

12 → divisors: 1, 2, 3, 4, 6 → sum = 16 → ✅ abundant

28 → sum = 28 → ❌ not abundant

18 → sum = 1+2+3+6+9 = 21 → ✅

'''

def is_abundant_number(num):
    res_sum = 1
    print(int(pow(num, 0.5)+1))
    for i in range(2, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            quo = num // i
            if i == quo:
                res_sum += i
            else:
                res_sum += i + quo
    
    return res_sum > num

number = 12
res = is_abundant_number(number)
print(res)