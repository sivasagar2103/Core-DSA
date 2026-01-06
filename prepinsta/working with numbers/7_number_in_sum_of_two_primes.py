
def list_of_prime_numbers(num):
    res = []

    if num < 2:
        return []
    if num == 2:
        res.append(num)
        return res
    
    for i in range(3, num, 2):
        is_prime = 1
        for j in range(3, int(pow(i, 0.5)) + 1, 2):
            if i % j == 0:
                is_prime = 0
                break
        
        if is_prime:
            res.append(i)

    return res

def is_sum_of_two_primes(prime_numbers, target):
    res = []
    for num in prime_numbers:
        diff = target - num
        if diff in prime_numbers and num <= diff:
            res.append((num, diff))
    return res

number = 30
res = list_of_prime_numbers(number)
print(res)
result = is_sum_of_two_primes(res, number)
print(result)
