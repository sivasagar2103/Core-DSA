'''
A number whose square ends with the same number is known as an Automorphic number.

5² = 25
76² = 5776
6² = 36

'''

def is_automorphic(num):
    source = num
    return (source ** 2) % (10 ** len(str(source))) == num


number = 76
res = is_automorphic(number)
print(res)  