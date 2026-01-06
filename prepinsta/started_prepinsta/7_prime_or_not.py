num = 130

def is_prime(n):
    flag = 0
    if n < 2:
        flag = 1
        return flag
    for i in range(2, n):
        if n % i == 0:
            flag = 1
            return flag

    return flag

if is_prime(num):
    print("not prime")
else:
    print("prime")
    
    

#check if the number input have any factors within the range of 2 to number/2.
#Any number has it’s lowest factor after 1 if any, in the range[2,number/2].
def is_prime_by_half(n):
    flag = 0
    if n < 2:
        flag = 1
        return flag
    for i in range(2, n //2 + 1):
        if n % i == 0:
            flag = 1
            return flag
    return flag

if is_prime_by_half(num):
    print("not prime")
else:
    print("prime")
    
    
    
'''
A number n can be written as a product of two factors:

n = a * b


If both a and b were greater than √n, their product would be greater than n,
which is a contradiction.

So, at least one of the factors must be ≤ √n.

'''

def is_prime_by_using_root(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(pow(0.5, 2))+1, 2):
        if n % i == 0:
            return False
    return True


if is_prime_by_using_root(num):
    print("prime")
else:
    print("not prime")


#by using recursion
def is_prime_using_recursion(n, num = 2):
    if n == num:
        return True
    if n < 2:
        return False
    if n % num == 0:
        return False
    return is_prime_using_recursion(n, num + 1)


if is_prime_using_recursion(num):
    print("prime")
else:
    print("not prime")
