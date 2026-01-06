'''
Example of prime factors:

36 -- 2 * 2 * 3 * 3 [LCM]

'''


def distinct_prime_factors(n):
    prime_factors = []
    #skipping even numbers
    if n % 2 == 0:
        prime_factors.append(2)

    while n % 2 == 0:
        n = n // 2

    i = 3
    while i**2 <= n:
        if n % i == 0:
            prime_factors.append(i)
            while n % i == 0:
                n = n // i
        i = i + 2

    # If n is still > 2, then it's a prime
    if n > 2:
        prime_factors.append(n)
    
    return prime_factors


def all_prime_factors(n):
    prime_factors = []

    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            prime_factors.append(i)
            n //= i
        i += 2 #move to next odd number

    if n > 2:
        prime_factors.append(n)
    
    return prime_factors

number = 36
res = all_prime_factors(number)
print(res)
