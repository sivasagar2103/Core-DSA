'''
Core Idea:
Generate the next lexicographically greater permutation of the array.
If no such permutation exists, rearrange it into the smallest possible order.

Intuition
The next permutation is the smallest arrangement that is strictly greater
than the current one.
To achieve this with minimal change:
    Modify the array as far right as possible.
    Keep the prefix unchanged and reorder only the suffix.

Steps:
1. Find the Pivot (First Decreasing Element from the Right)
    Traverse from right to left.
    Find the first index i such that: nums[i] < nums[i + 1]
    This index is where the next permutation can be formed.
2. Find the Next Greater Element
    From the right side of the array, find the smallest element greater than nums[i].
    Let its index be j.
3. Swap Pivot and Next Greater Element. Swap nums[i] and nums[j].
4. Swap nums[i] and nums[j].
    Reverse the portion of the array from i + 1 to the end.
    This ensures the suffix is in the smallest possible order.

Time: O(n)
Space: O(1)

Find pivot --> swap with next greater --> reverse the suffix.

'''

def next_permutation(nums):
    n = len(nums)
    i = n - 2

    #Find first decreasing element from right
    while i >= 0 and nums[i] > nums[i+1]:
        i -= 1
    
    #Find greatest number from right of i
    if i >= 0:
        j = n -1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    
    #reverse the right part
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

nums = [1,2,3]
next_permutation(nums)
print(nums)
