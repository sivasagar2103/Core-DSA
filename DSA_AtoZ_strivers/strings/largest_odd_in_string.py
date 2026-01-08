
def find_largest_odd(num):
    n = len(num)
    for i in range(n-1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[:i+1]
    return ""

num = "35427"
res = find_largest_odd(num)
print(res)