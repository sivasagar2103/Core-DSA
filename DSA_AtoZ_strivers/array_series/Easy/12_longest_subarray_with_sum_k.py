
#using sliding window
'''
Why it fails with negative numbers:
When numbers can be negative, removing elements from the left 
might actually increase the total sum.
So, the logic:
while current_sum > k:
    current_sum -= arr[left]
    left += 1
is no longer valid, because current_sum can jump up or down 
unexpectedly depending on the values removed.

'''
def find_subarray(arr, k):
    start , end = 0, 0
    left = 0
    current_sum = 0
    max_length = 0
    n = len(arr)

    for right in range(n):
        current_sum += arr[right]

        while current_sum > k:
            current_sum -= arr[left]
            left += 1
        
        if current_sum == k:
            if right - left + 1 > max_length:
                max_length = right - left + 1
                start, end = left, right
    
    print(arr[start: end +1])

    return max_length

#using prefix-sum + hashmap
def find_subarray_include_negatives(arr, k):
    max_length = 0
    prefix_sum = 0
    n = len(arr)
    seen = {}
    start, end = 0, 0

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum == k:
            max_length = i + 1
            start, end = 0, i
        
        if prefix_sum - k in seen:
            stop = i - seen[prefix_sum - k]
            if stop > max_length:
                max_length = stop
                start, end = stop +1, i

        if prefix_sum not in seen:
            seen[prefix_sum] = i
    
    print(arr[start:end])
    return max_length


nums1 = [10, 5, 2, 7, 1, 9]
k1 = 15
res1 = find_subarray(nums1, k1)
print(res1) 
arr = [1, -1, 5, -2, 3]
k = 3
res = find_subarray_include_negatives(arr, k)
print(res)