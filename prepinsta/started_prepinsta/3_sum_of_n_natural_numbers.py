num = int(input("enter a number: "))


#using for loop
res = 0

for i in range(num + 1):
    res += i

print(res)

#using formula
print((num*(num+1))//2)

#using recursion
'''
recursion "builds up a call stack" — each function call gets 
added to the stack  until it reaches the base case, and then 
they "pop" off as they return.

Intialize the stack based on the iteration calls of function
and pop the stack by executing the function.

'''
def recursion_sum(n):
    if n == 0:
        return n
    return n + recursion_sum(n - 1)


rec_result = recursion_sum(num)
print(rec_result)

