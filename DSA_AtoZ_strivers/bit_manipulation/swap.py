
a , b = 5, 10

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

a = a + b
b = a - b
a = a - b

print(a, b)