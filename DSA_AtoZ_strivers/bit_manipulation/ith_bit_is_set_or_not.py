
def check_ith_bit(n, i):
    return n & (n << i) != 0


n = 5
i = 0
res = check_ith_bit(n, i)
print(res)