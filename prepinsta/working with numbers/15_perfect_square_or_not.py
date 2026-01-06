def is_perfect_square(n):
    if n == 0 or n == 1:
        return True
    
    i = 2
    while i < n:
        if i * i == n:
            return True
        i += 1
    return False

def is_square(n):
    if n == 0 or n == 1:
        return True
    
    low = 2
    high = n // 2

    while low <= high:
        mid = (low + high)//2
        temp = mid * mid

        if temp == n:
            return True
        
        if temp < n:
            low = mid + 1
        if temp > n:
            high = mid - 1
    
    return False


n = 17
res = is_perfect_square(n)
r = is_square(n)
print(res)
print(r)
