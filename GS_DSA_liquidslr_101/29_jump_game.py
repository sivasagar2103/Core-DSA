'''

Problem Statement
You are given an integer array nums.
You start at index 0
nums[i] represents the maximum jump length from index i
Determine whether you can reach the last index
Return True if reachable, otherwise False.

Approach Used: Greedy

Core Idea:
Instead of thinking “where can I jump next?”, think:
    . What is the farthest index I can reach so far?
- Maintain a variable max_reach
- Iterate through the array
- At each index:
  . If the index is beyond maxReach, you are stuck → return False
  . Otherwise, update maxReach
- If at any point maxReach ≥ last index, you can finish.

Time: O(n)
Space: O(1)

'''

def canJump(nums):
    maxReach = 0
    n = len(nums)

    for i in range(n):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + nums[i])

    return True

nums = [3,2,1,0,4]
res = canJump(nums)
print(res)
