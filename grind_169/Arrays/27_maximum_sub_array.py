'''
Kadane's Algorithm — Maximum Subarray Sum

Core Idea:
At every index, decide whether to:
- extend the previous subarray, or
- start a new subarray from the current element.
Keep track of the maximum sum seen so far.

Intuition
A subarray that has a negative running sum will only reduce future sums.
So at each index, we ask:
Is it better to:
    1)include this element in the previous subarray, or
    2) start fresh from this element?

Steps of Implementation
1. Initialize:
    current_sum = first element
    max_sum = first element
2. Traverse the array from index 1 onward:
    If arr[i] > current_sum + arr[i]:
    . Start a new subarray at i
    Else:
    . Extend the existing subarray
3. Update max_sum whenever a better sum is found.
4. Track indices to reconstruct the subarray (optional).
5. Return the maximum sum and the corresponding subarray.

Time: O(n)
Space: O(1)

'''
def maximum_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    n = len(arr)
    start, end, temp = 0, 0, 0

    for i in range(1, n):
        #If negative numbers available, Negative sum dropped and Fresh subarray started
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
