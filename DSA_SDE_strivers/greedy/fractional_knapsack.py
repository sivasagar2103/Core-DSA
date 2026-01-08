'''
Problem:
The weight of N items and their corresponding values are given. 
We have to put these items in a knapsack of weight W such that the total value 
obtained is maximized.

Approach:
Greedy Approach
- Calculate the value-to-weight ratio for each item.
- Sort items in decreasing order based on this ratio.
- Iterate through the sorted items:
  . If the item can fit entirely in the knapsack, add its full value.
  . If only a part of the item can fit, add value proportional to the remaining capacity
    and break out of the loop, as the knapsack will be full.
- 

Time: O(nlogn + n) #sorting and looping
Space: O(n)

'''

def fractional(wt, val, cap):
    ratio_values = [(v/w, v, w) for v, w in zip(val, wt)]
    ratio_values.sort(reverse=True)
    res = 0

    for ratio_val, value, weight in ratio_values:
        if cap == 0:
            break
        if weight < cap:
            res += value
            cap -= weight
        else:
            res += ratio_val * cap
            cap = 0
    return res

n = 3
max_weight = 50
values = [100,60,120]
weight = [20,10,30]
res = fractional(weight, values, max_weight)
print(res)
