

def fractional_knapsack(val, wt, capacity):
    res = 0
    ratio_values = [(v/w, v, w) for v, w in zip(val, wt)]
    ratio_values.sort(reverse = True)

    for ratio, value, weight in ratio_values:
        if capacity == 0:
            break
        if weight <= capacity:
            res += value
            capacity -= weight
        else:
            res += ratio * capacity
            capacity = 0
    
    return res

val = [60,100,120]
wt = [10,20,30]
capacity = 50
res = fractional_knapsack(val, wt, capacity)
print(res)