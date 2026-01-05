'''
Time: O(amount × n) where n = len(coins)

Space: O(amount)

'''

def coin_change_dp(coins, amount):
    # 1. Initialize
    dp = [amount + 1] * (amount + 1)   # "infinity"
    choice = [-1] * (amount + 1)       # which coin was last used
    dp[0] = 0                          # base case
    
    # 2. Build DP table
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                choice[i] = coin
    
    # 3. If impossible
    if dp[amount] == amount + 1:
        return -1, []
    
    # 4. Reconstruct path
    res_coins = []
    curr = amount
    while curr > 0:
        coin = choice[curr]
        res_coins.append(coin)
        curr -= coin
    
    return dp[amount], res_coins

coins = [1, 2, 5]
amount = 11
count, used_coins = coin_change_dp(coins, amount)
print("Count:", count)       # 3
print("Coins:", used_coins)  # [5, 5, 1] (order may vary)
