'''
Problem Statement

Given an array prices where prices[i] is the stock price on day i,
find the maximum profit you can achieve by buying once and selling once.

Approach Used: Single Pass (Greedy)

Core Idea:
- Always buy at the lowest price seen so far
- At each day, compute the profit if you sell on that day
- Track the maximum profit

Time: O(n)
Space: O(1)

'''


def best_time(prices):
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


