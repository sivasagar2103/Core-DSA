'''
Maximum Subarray Sum with Length k and Distinct Elements

Core Idea:
Use a fixed-size sliding window of length k.
Maintain a frequency map to ensure all elements in the window are distinct.
Track the window sum and update the maximum when the window is valid.

Intuition:
The subarray length must be exactly k --> fixed-size window.
All elements must be distinct --> use a frequency map.
Sliding window lets us:
    Add one element from the right,
    Remove one element from the left,
    Maintain the sum in O(1) time.

Steps of Implementation
1. Initialize:
    . left = 0
    . window_sum = 0
    . max_sum = 0
    . frequency_map to track element counts
2. Traverse the array using right pointer:
    Add arr[right] to window_sum
    Increment its count in frequency_map
3. If a duplicate is introduced:
    Shrink the window from the left until all elements are unique.
4. When window size becomes exactly k:
    Update max_sum
    Slide the window forward by removing arr[left]
5. Continue until the array ends.
6. Return max_sum.

Time: O(n)
Space: O(k)   // at most k distinct elements in the window

Fixed-size sliding window + frequency map to enforce uniqueness.

'''

def maximumSubarraySum(arr, k):
    n = len(arr)

    frequency_map = {}
    window_sum = 0
    maxi_sum = 0
    left = 0

    for right in range(n):
        window_sum += arr[right]

        if arr[right] not in frequency_map:
            frequency_map[arr[right]] = 0
        frequency_map[arr[right]] += 1

        #shrinking the window
        while frequency_map[arr[right]] > 1:
            frequency_map[arr[left]] -= 1
            window_sum -= arr[left]
            left += 1

        if right - left + 1 == k:
            maxi_sum = max(maxi_sum, window_sum)
            frequency_map[arr[left]] -= 1
            window_sum -= arr[left]
            left += 1

    return maxi_sum


nums = [1,5,4,2,9,9,9]
#nums = [4,4,4]
k = 3
res = maximumSubarraySum(nums, k)
print(res)
