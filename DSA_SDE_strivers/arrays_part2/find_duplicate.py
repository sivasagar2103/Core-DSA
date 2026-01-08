'''
Problem:
Find the Duplicate Number.
Given an array of integers nums containing n + 1 integers
where each integer is in the range [1, n] inclusive, 
there is only one repeated number in nums, return this duplicate number.

Approach:
Floyd's Tortoise and Hare (Cycle Detection)

Note: Works if array contains n+1 integers where each integer is in [1, n],
and only one duplicate is guaranteed.

1. Treat array values as pointers to next index.
2. Two pointers (slow moves 1 step, fast moves 2 steps) 
will meet inside the cycle (duplicate).
3. Reset one pointer to start and move both at same speed;
they meet at duplicate number.
4. This approach assumes exactly one duplicate.

Time: O(n)
Space: O(1)

'''

def find_duplicate(arr):
    slow = arr[0]
    fast = arr[0]

    #find intersection point
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]

        if slow == fast:
            break
    
    #find the starting point
    slow = nums[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow


nums = [1,3,4,2,2]
res = find_duplicate(nums)
print(res)