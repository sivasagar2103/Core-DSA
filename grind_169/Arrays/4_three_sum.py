'''
Core Idea:
Fix one number and use two pointers to find pairs that sum 
to the remaining target (0 - fixed number),
while skipping duplicates to avoid repeated triplets.

Steps of implementation:
1. Sort the input array to enable two-pointer traversal and easy duplicate handling.
2. Iterate through the array with index i:
   - Skip the iteration if the current number is the same 
   as the previous one (to avoid duplicates).
3. For each fixed nums[i]:
   - Initialize two pointers:
     . left = i + 1
     . right = n - 1
4. While left < right:
   - Compute the sum of nums[i] + nums[left] + nums[right].
   - If the sum is 0:
     . Add the triplet to the result list.
     . Move both pointers inward.
     . Skip duplicate values for left and right.
   - If the sum is less than 0:
     . Move the left pointer to the right (increase sum).
   - If the sum is greater than 0:
     . Move the right pointer to the left (decrease sum).
5. Continue until all valid triplets are found.
6. Return the result list.

Time: O(n²)
Space: O(1)  (excluding the output list and sort space)

Sort --> fix one --> two pointers --> skip duplicates.

'''

def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n):

        #to skip duplicates
        if i>0 and nums[i-1] == nums[i]:
            continue

        left = i+1
        right = n-1

        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -=1 
                
            elif s < 0:
                left += 1
            else:
                right -= 1
    
    return res

nums = [-1,0,1,2,-1,-4]
res = three_sum(nums)
print(res)
