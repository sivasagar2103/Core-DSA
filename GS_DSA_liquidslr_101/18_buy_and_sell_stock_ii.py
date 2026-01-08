'''
Problem Statement:
You are given an array prices, where prices[i] is the stock price on day i.
Rules:
You may buy and sell multiple times
You can hold at most one stock at any time
You may buy and sell on the same day
Goal: maximize total profit

Approach Used: Greedy Algorithm

Core Idea:
- multiple transactions are allowed --> Take profit from every upward price movement.
- Traverse the price array
- Whenever prices[i] > prices[i-1], add the difference to profit
- Ignore price drops (no transaction)

Time: O(n)
Space: O(1)

'''

def maxProfit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit

prices = [7,1,5,3,6,4]
result = maxProfit(prices)
print(result)
