
def factors(n):
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res.append(i)
    return res

'''
Example: n = 36
Factors of 36:
- 1 * 36
- 2 * 18
- 4 * 9
- 6 * 6

left side were i [1,2,4,6]
right side were n//i -- [36, 18, 9, 6]

we can add unique and all based on the use cases of the program.

'''

#to reduce the number of iterations but the result will be unsorted
def factors_using_root(n):
    res = []
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            res.append(n // i)
            #to avoid duplicate entry of factors for a number like 6, 144
            #when n is a parfect square
            if i not in res:
                res.append(i)
    return res


number = 36
res = factors_using_root(number)
print(res)


