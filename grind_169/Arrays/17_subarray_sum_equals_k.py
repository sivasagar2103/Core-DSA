'''
Subarray Sum Equals K

1. Sliding Window (Only Positive Numbers)

Intuition
- With only positive numbers, expanding the window increases the sum.
- Shrinking the window decreases the sum.
- This monotonic behavior allows a sliding window.

Steps of implementation:
1. Initialize:
    left pointer = 0
    current_sum = 0
    result counter = 0
2. Traverse the array using the right pointer:
    Add arr[right] to current_sum.
3. While current_sum > k:
    Subtract arr[left] from current_sum.
    Move left pointer forward.
4. If current_sum == k:
    Increment result counter.
5. Continue until all elements are processed.
6. Return the total count.

Time: O(n)
Space: O(1)

2. Prefix Sum + HashMap (Handles Negatives)

Intuition
- Use prefix sums to track cumulative sums.
- If prefix_sum - k has appeared before,
  all those occurrences form valid subarrays ending at the current index.

Steps of implementation:
1. Initialize:
    prefix_sum = 0
    hashmap = {0 : 1} (to handle subarrays starting at index 0)
2. Traverse the array:
    Add current element to prefix_sum.
3. Check if (prefix_sum − k) exists in the hashmap:
    Add its frequency to the result.
4. Record the current prefix_sum in the hashmap.
5. Return the total count.

Time: O(n)
Space: O(n)

'''

def subarray_equals_k(arr, k):
    #return the total number of subarrays whose sum equals to k.
    left = 0
    n = len(arr)
    current = 0
    res = 0

    for right in range(n):
        current += arr[right]

        while current > k:
            current -= arr[left]
            left += 1
        
        if current == k:
            res += 1

    return res


def subarray_equals_k_two(arr, k):
    #return the total number of subarrays whose sum equals to k.
    prefix_sum = 0
    prefix_count = {0:1} # prefix_sum : count of occurrences
    res = 0

    n = len(arr)

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum - k in prefix_count:
            res += prefix_count[prefix_sum - k]
        
        if prefix_sum not in prefix_count:
            prefix_count[prefix_sum] = 0

        prefix_count[prefix_sum] += 1
    
    return res



nums = [1,1,1]
k = 2
res = subarray_equals_k(nums, k)
print(res)

res2 = subarray_equals_k_two(nums, k)
print(res2)
