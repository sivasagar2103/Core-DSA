
def max_profit(arr):
    mini = arr[0]
    maxi = 0
    n = len(arr)

    for i in range(1, n):
        profit = arr[i] - mini
        mini = min(arr[i], mini)
        maxi = max(maxi, profit)
    
    return maxi


prices = [7,1,5,3,6,4]
res = max_profit(prices)
print(res)