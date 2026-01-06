a = 3
b = 6

res = 0
#using brute-force
for i in range(a, b+1):
    res += i

print(res)

#using formula
#(b * (b + 1))/2 - (a * (a + 1))/2 + a
formula_result = (b * (b + 1) // 2) - (a * (a + 1) // 2) + a
print(formula_result)

#using recursion
def sum_recursion(x, y):
    if x > y:
        return 0
    return x + sum_recursion(x + 1, y)

rec_result = sum_recursion(a, b)

print(rec_result)
