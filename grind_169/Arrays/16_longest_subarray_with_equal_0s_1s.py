'''
Longest Subarray with Equal 0s and 1s

Core Idea:
To find equal numbers of 0s and 1s, transform the problem into finding
the longest subarray with sum = 0 using prefix sums.

Intuition:
- We want the longest subarray with equal number of 0s and 1s.
- To make counting easy:
  . Treat 0 as -1,
  . Treat 1 as +1.
- keep a running sum(prefix sum), and track the earliest index of each prefix sum.
- Whenever we see the same prefix sum again in hashmap(prefix index),
  we found a balanced subarray.

Time: O(n)
Space: O(n)

Note:
If the condition is “at most / at least” → Sliding Window
If the condition is “exactly / equal” → Prefix Sum

Bounded problems --> sliding window
Equality problems --> prefix sums

'''

def find_max_length(arr):
    prefix_sum = 0
    prefix_index = {0:-1}
    n = len(arr)
    res = 0
    start = 0
    end = 0

    for i in range(n):
        prefix_sum += (1 if arr[i] == 1 else -1)

        if prefix_sum in prefix_index:
            diff = i - prefix_index[prefix_sum]
            if diff > res:
                start = prefix_index[prefix_sum]
                end = i
                res = diff
        else:
            prefix_index[prefix_sum] = i
    
    print(arr[start : end + 1])

    return res


nums = [0,1,1,1,1,1,0,0,0]
res = find_max_length(nums)
print(res)
