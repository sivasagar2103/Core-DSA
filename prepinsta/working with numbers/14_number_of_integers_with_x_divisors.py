
def find_divisors(num):
    count = 0
    for i in range(1, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            factors = (i, num // i)
            count += 2 if i != num // i else 1
    return count

def divisor_count(number, divisors):
    div_count = [0] * (number + 1)

    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            div_count[j] += 1
    
    result = [x for x in range(1, number + 1) if div_count[x] == divisors]

    return result, div_count

number = 7
divisors = 2
res = 0
for i in range(1, number + 1):
    if find_divisors(i) == divisors:
        res += 1

print(res)

print(divisor_count(number, divisors))
