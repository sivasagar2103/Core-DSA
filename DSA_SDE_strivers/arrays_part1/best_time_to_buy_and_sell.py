'''
Problem:
Given an array arr of n integers, where arr[i] represents price of the stock on the ith day.
Determine the  maximum profit achievable by buying and selling the stock at most once. 
The stock should be purchased before selling it, and both actions cannot occur on the same day.

Approach:
Create a variable profit and store 0 initially.
Create a variable min_price and store the first value of array.
Run a for loop from 0 to n.
Update the min_price if the current element of the array is lesser than the min_price.
Take the difference of the min_price with the current element of the array 
and compare and maintain it in profit.
return the profit

Time Complexity: O(n)
Space Complexity: O(1)

'''

def maximum_profit(arr):
    min_price = arr[0]
    n = len(arr)
    profit = 0

    for i in range(1, n):
        if arr[i] < min_price:
            min_price = arr[i]
        diff = arr[i] - min_price
        if diff > profit:
            profit = diff
    
    return profit

arr = [10, 7, 5, 8, 11, 9]
res = maximum_profit(arr)
print(res) 
#Explanation: Buy on day 3 (price = 5) and sell on day 5 (price = 11), profit = 11 - 5 = 6.