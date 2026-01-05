'''
Core Idea:
Track the lowest price so far and compute profit if sold today.
Update the maximum profit whenever a better selling opportunity appears.

Steps of implementation:
1. Initialize:
   - cp (current minimum price) as the first day's price
   - max_profit as 0
2. Traverse the prices array from day 1 onward:
   - Calculate profit = prices[i] - cp
   - If profit is greater than max_profit:
     . Update max_profit
   - If prices[i] is less than cp:
     . Update cp to the new lower price (better buying day)
3. After traversal, return max_profit

Time: O(n)
Space: O(1)

Buy at the lowest price so far, sell today if it gives more profit.

'''

def best_time(prices):
    #only one possibility need to check

    cp = prices[0]
    max_profit = 0
    n = len(prices)

    for i in range(1, n):
        profit = prices[i] - cp
        if profit > max_profit:
            max_profit = profit
        if prices[i] < cp:
            cp = prices[i]

    return max_profit

prices = [7,1,5,3,6,4]
result = best_time(prices)
print(result)
