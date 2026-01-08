
def bad_version(n, bad):
    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2
        if mid < bad:
            low = mid + 1
        else:
            high = mid -1
    return low

n = 5
bad = 4
res = bad_version(n, bad)
print(res)