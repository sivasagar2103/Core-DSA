
'''
Kadane's Algorithm — The Intuition
The idea is simple:
At every index, decide whether to:
Extend the previous subarray, or
Start a new subarray starting at the current element
Track the maximum sum seen so far

problems like:
Maximum Subarray Sum (Leetcode 53)
Finding profitability or best gain/loss streaks
Weather/stock trends, etc.
'''
def maximum_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    n = len(arr)
    start, end, temp = 0, 0, 0

    for i in range(1, n):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp = i
        else:
            current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp
            end = i
    
    return max_sum, arr[start:end+1]


nums = [2, 3, 5, -2, 7, -4]
maxi, sub = maximum_subarray(nums)
print(maxi)
print(sub)