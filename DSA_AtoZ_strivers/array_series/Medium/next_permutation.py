
'''
Algorithm (Next Permutation):
- First decreasing element from right - i 
 (Find pivot to create next greater permutation)
- Find First Greater Number from the right of i - j
- swap elements i and j
- Reverse the suffix part from i + 1 to end to get the next smallest arragement

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
