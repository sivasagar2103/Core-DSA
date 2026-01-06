def prime_numbers(n):
    result = [2]
    for i in range(3, n, 2):
        is_prime = True
        
        for j in range(3, int(pow(i, 0.5)) + 1, 2):
            if i % j == 0:
                is_prime = False
                break
        
        if is_prime:
            result.append(i)
    
    return result

print(prime_numbers(100))

