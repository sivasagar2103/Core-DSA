
#using binary search
def is_perfect_square(num):
    if num < 0:
        return False
    
    if num == 0 or num == 1:
        return True

    low = 1
    high = num // 2

    while low <= high:
        mid = (low + high) // 2
        sq = mid * mid

        if sq == num:
            return True

        elif sq < num:
            low = mid + 1

        else:
            high = mid - 1

    return False

def is_perfect_square_basic(num):
    if num < 0:
        return False
    
    i = 1
    while i**2 <= num:
        if i**2 == num:
            return True
        i += 1

    return False

number = 25
res = is_perfect_square_basic(number)
print(res)
