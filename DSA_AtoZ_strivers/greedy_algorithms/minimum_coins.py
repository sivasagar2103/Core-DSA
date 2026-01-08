
'''
The greedy approach only works when the coin denominations are canonical,
meaning the greedy choice always leads to an optimal solution.
For example:
US coin system: [1, 5, 10, 25, 50] -- greedy works
Custom set like [1, 3, 4] -- greedy may fail!

'''


def minimum_coins(coins, amt):
    coins.sort(reverse = True)
    count = 0
    for coin in coins:
        if amt == 0:
            break
        take = amt // coin
        count += take
        amt = amt - coin * take
    return count if amt == 0 else -1

# def minimum_coins_dp(coins, amt):
#     max_val = amt + 1
#     dp = [max_val] * len(coins)




coins = [1, 2, 5]
amount = 11
res = minimum_coins(coins, amount)
print(res)