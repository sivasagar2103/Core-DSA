'''
Problem:
Given an array that contains only 1 and 0 return the count of 
maximum consecutive ones in the array.

Approach:


Time:
Space:

'''


def count_max_ones(arr):
    cnt = 0
    max_cnt = 0
    n = len(arr)

    for num in arr:
        if num == 1:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 0
    
    return max_cnt






prices = [1, 1, 0, 1, 1, 1]
res = count_max_ones(prices)
print(res)