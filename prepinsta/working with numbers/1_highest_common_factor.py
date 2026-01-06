#basic method
def find_hcf(a, b):
    hcf = 1
    for i in range(1, min(a,b)):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf

#Euclidean algorithm
#HCF(a, b) = HCF(b, a % b)
def find_hcf_by_euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_hcf_by_euclidean_recursion(a, b):
    return a if b == 0 else find_hcf_by_euclidean_recursion(b, a % b)

num1 = 20
num2 = 8
res = find_hcf_by_euclidean_recursion(num1, num2)
print(res)

#for three numbers
x, y, z = 12, 15, 21
res = find_hcf_by_euclidean(find_hcf_by_euclidean(x,y), z)
print(res)