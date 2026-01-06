a = 10
b = 20
c = 30

if a > b and a > c:
    print(a)
elif b > c and b > a:
    print(b)
else:
    print(c)


#second highest number
if (a > b and a < c) or (a > c and a < b):
    print("second highest:",a)
elif (b > c and b < a) or (b > a and b < c):
    print("second highest", b)
else:
    print("second highest", c) 


#using ternary operator
maxi = a if a > b else b
maxi = c if c > maxi else maxi
print(maxi)
