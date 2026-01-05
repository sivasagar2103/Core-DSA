'''

'''

def is_bad_version(version, bad):
    return version >= bad


def first_bad_version(n, bad):
    low = 1
    high = n

    while low < high:
        mid = (low + high)//2
        if is_bad_version(mid, bad):
            high = mid
        else:
            low = mid + 1
    
    return low

n = 5
bad = 4
res = first_bad_version(n, bad)
print(res)
