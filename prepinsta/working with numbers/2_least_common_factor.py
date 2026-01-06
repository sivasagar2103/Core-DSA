# a * b = LCM(a, b) * HCF(a,b)

def find_hcf(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def find_lcm(a,b):
    return (a*b) // find_hcf(a, b)


num1 = 12
num2 = 18
res = find_lcm(num1, num2)
print(res)

#three numbers
x, y, z = 4, 5, 6
r = find_lcm(find_lcm(x,y), z)
print(r)