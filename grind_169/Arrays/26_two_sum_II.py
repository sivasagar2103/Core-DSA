'''
Problem:
A 1-indexed, sorted array numbers and a target.
Find two numbers such that they sum to the target.

Intuition:
- Since the array is sorted, use two pointers from both ends.
- Move inward depending on whether the sum is too small or too big.

Time: O(n)
Space: O(1)

'''

def two_sum(arr, target):
    n = len(arr)
    left, right = 0, n-1

    while left < right:
        s = arr[left] + arr[right]

        if s == target:
            return [left+1, right+1] #as per the problem consider 1-indexed array 
        elif s < target:
            left += 1
        else:
            right -=1
    return None

numbers = [2, 7, 11, 15]
target = 9
res = two_sum(numbers, target)
print(res)
