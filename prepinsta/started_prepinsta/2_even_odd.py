num = int(input("enter a number:"))

#brute - force
if num % 2 == 0:
    print("even")
else:
    print("odd")

#ternary operator
print("even" if num % 2 == 0 else "odd")

#bit wise operator
bit_wise = num & 1 #for even it returns 0 i.e., False and odd it returns 1 i.e., True
if bit_wise:
    print("odd")
else:
    print("even")
