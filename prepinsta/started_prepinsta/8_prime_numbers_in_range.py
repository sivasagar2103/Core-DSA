#using normal two for loops
#time complexity: O(n^2)
def prime_numbers(low, high):
    result = []

    for num in range(low, high + 1):
        flag = 0
        if num == 2:
            result.append(2)
            continue
        if num < 2:
            continue

        for i in range(2, num):
            if num %i == 0:
                flag = 1
                break
        
        if not flag:
            result.append(num)
    
    return result

low = 2
high = 20

res = prime_numbers(2, 20)
print("normal two loops program:",res)

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(pow(num, 0.5))+1, 2):
        if num % i == 0:
            return False
    return True

#time complexity: O(n(n)^1/2) - n root n
def prime_numbers_in_sqrt_iterations(low, high):
    result = []
    for num in range(low, high + 1):
        if is_prime(num):
            result.append(num)

    return result


low = 2
high = 20

res = prime_numbers_in_sqrt_iterations(2, 20)
print("prime_numbers_in_sqrt_iterations program:",res)