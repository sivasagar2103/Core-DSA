'''
Friendly Pair Numbers
The numbers whose ( sum of divisors ) / number ratio is same 
are known as Friendly Pair Numbers.
Let's try and understand it better using an example

Example
Input : 6 28
Output : Yes, they are a friendly pair
Explanation : The factors of 6 and 28 except the numbers themselves 
are 1, 2, 3 and 1, 2, 4, 7, 14 respectively.
Now the sum of factors of both the numbers are 6 and 28 respectively. 
When we divide the sums with the numbers we get 1 and 1 respectively. 
As the ratio of both the number match, they are considered as a friendly pair.

'''

def number_quo(n):
    sum_res = 1
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            quo = n // i
            if quo == i:
                sum_res += i
            else:
                sum_res += i + quo

    return sum_res // n

num1 = 6
num2 = 28
res = number_quo(num1) == number_quo(num2)
print(res)
