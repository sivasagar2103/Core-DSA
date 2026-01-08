'''
Note:
Patience Sorting is also DP, just:
    . Optimized
    . Greedy
    . Uses binary search
- When we add:
    prev[] → previous index
    tails_idx[] → index of tails
* It becomes a full DP solution with backtracking

Problem Statement
Given an integer array nums, return the length of the longest strictly 
increasing subsequence.
Subsequence means:
- You can skip elements
- Order must stay the same

Approach Used: Sorting + Manual Binary Search (Patience Sorting for LIS))
* Patience Sorting = Optimized DP

what is tails array?
- tails[i] = smallest possible ending value of an increasing 
  subsequence of length i + 1
- We do not try to build the actual subsequence.
- tails only stores candidate ending values, 
and these values may come from different positions in the array.

Why Binary Search?
- Because tails is always sorted
- We need to find the first value ≥ num

Core Idea:
- Smaller ending value = more chance to extend later.
- For each number:
  . Find the leftmost position in tails where it can replace a value ≥ itself
  . Replace to keep tails minimal
- The length of tails is the LIS length

Time: O(nlogn)
Space: O(n)

Why This Is Still DP?

| Classic DP                        | Patience Sorting                 |
| --------------------------------- | -------------------------------- |
| `dp[i]` = LIS ending at index `i` | `dp[len]` = best tail for length |
| O(n²) transitions                 | O(log n) transitions             |
| Stores full state                 | Stores compressed state          |

Why Replacing Does NOT Break LIS Length?
- We only replace with a smaller or equal value
- The length of LIS never decreases

--------------------------------------------------------

* Finding LIS
- We combine 3 ideas
  . Greedy: to get the best possible endings
  . Binary Search: find the position of the current number
  . Backtracking: recover the actual sequence
- We have 3 key arrays
  . tails = [] --> tails[i] = smallest possible ending value of increasing sequence
                              of length i + 1
  . tails_idx = [] --> Index in arr of the value stored in tails
  . prev = [] --> index of the previous element in the LIS ending at arr[i] (parent pointer)

Time: O(nlogn)
Space: O(n)

'''

def find_lis_length(arr):
    tails = []

    for num in arr:
        left, right = 0, len(tails) - 1
        idx = len(tails)  # default position (append)

        while left <= right:
            mid = (left + right) // 2

            if tails[mid] >= num:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if len(tails) == idx:
            tails.append(num)
        else:
            tails[idx] = num
    
    return len(tails)

def find_lis(nums):
    n = len(nums)
    tails = []
    tails_idx = []
    prev_arr = [-1] * n

    for i in range(n):
        num = nums[i]

        left, right = 0, len(tails)-1
        idx = len(tails)

        while left <= right:
            mid = (left + right)//2

            if tails[mid] >= num:
                idx = mid
                right = mid -1 
            else:
                left = mid + 1
        
        if idx == len(tails):
            tails.append(num)
            tails_idx.append(i)
        else:
            tails[idx] = num
            tails_idx[idx] = i
        
        if idx > 0:
            prev_arr[i] = tails_idx[idx - 1]
    
    res = []
    res_idx = tails_idx[-1]

    while res_idx != -1:
        res.append(nums[res_idx])
        res_idx = prev_arr[res_idx]
    
    res.reverse()

    return res

nums = [10, 9, 2, 5, 3, 7, 101, 18]
result = find_lis_length(nums)
print(result)
r = find_lis(nums)
print(r)
